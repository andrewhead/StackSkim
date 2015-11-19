#!/usr/bin/perl
use strict;

use DBI;

use FindBin;
use lib $FindBin::Bin . '/lib';

use AdWordsLib;

my %history = ();
my $set_id = 26;
my $country_code = 'US';
my $language_code = 'en';
my $locale_code = 'en_US';

my $dbh;
$dbh = DBI->connect('DBI:Pg:dbname=suggest_db;host=localhost;port=5432', 'postgres', '<PASSWORD>', {'RaiseError' => 1});
if ($dbh) {

while(1) {

  print STDERR "Making DB Request\n";

  my $res = $dbh->selectall_arrayref( "SELECT suggestion FROM full_suggestions WHERE suggestion NOT IN (SELECT a.suggestion FROM adword_data a WHERE a.set_id=$set_id AND a.country_code='". &sql_str_encode($country_code) ."' AND a.language_code='". &sql_str_encode($language_code) . "' AND a.locale_code='". &sql_str_encode($locale_code) ."') AND first_observation=true AND set_id=$set_id ORDER BY level ASC LIMIT 750;", { Slice => {} } );

  if (scalar(@$res) == 0) {
    print STDERR "Nothing to do.\n";
    exit(0);
  }

  my @phrases = ();

  foreach my $row( @$res ) {
    my $suggestion = $row->{'suggestion'};

    next if exists($history{$suggestion});
    $history{$suggestion} = 1;

    push @phrases, $suggestion;
#    print STDERR "$suggestion\n";
  }

  print STDERR "Making API Request\n";

  my $hr = &query_adwords(\@phrases, $country_code, $language_code, $locale_code);
  my %h = %$hr;

  foreach my $p(@phrases) {

    if (exists $h{$p}) {
      print STDERR "OK: '$p'\n";

      my $rec_r = $h{$p};
      my %rec = %$rec_r;

      my @monthly = @{$rec{'monthly'}};
      my $last_month = "NULL";
      my $last_year  = "NULL";
      my $last_count = "NULL";

      for (my $i=0; $i<scalar(@monthly); $i++) {
        if ($monthly[$i]->{'count'} > 0) {
          $last_month = $monthly[$i]->{'month'};
          $last_year  = $monthly[$i]->{'year'};
          $last_count = $monthly[$i]->{'count'};
          last;
        }        
      }

      my $total = 0;
      foreach my $m(@monthly) {
        $total += $m->{'count'};
      }

      my $avg = $rec{'avg'} == 0 ? 'NULL' : $rec{'avg'};
      my $raw = $rec{'raw'} eq "" ? 'NULL' : "'" . &sql_str_encode($rec{'raw'}) . "'";

      my $sql = "INSERT INTO adword_data ( ".
                "  set_id, ".
		"  suggestion, ".
		"  raw, ".
    		"  reported_monthly_average, ".
    		"  year_total, ".
		"  country_code, ".
		"  language_code, ".
		"  locale_code ) VALUES (".
                "$set_id, ".
		"'". &sql_str_encode($p) . "', ".
		"$raw, ".
		"$avg, ".
		"$total, ".
		"'" . &sql_str_encode($country_code) . "', ".
		"'" . &sql_str_encode($language_code) . "', ".
		"'" . &sql_str_encode($locale_code) . "');"; 
      print "$sql\n";
      $dbh->do($sql);

      foreach my $m(@monthly) {
        my $m_month = $m->{'month'};
        my $m_year  = $m->{'year'};
        my $m_count = $m->{'count'};

        if ($m_count == 0) {
          $m_count = 'NULL';
        }

        my $sql = "INSERT INTO adword_month_data ( adword_id, suggestion, count, month, year, country_code, language_code, locale_code ) VALUES ( ".
                  " (SELECT id FROM adword_data WHERE suggestion='". &sql_str_encode($p) ."' ORDER BY dts DESC LIMIT 1), ".
		  "'". &sql_str_encode($p) ."', ".
		  $m_count . ", " .
                  $m_month . ", " .
                  $m_year  . ", ".
		  "'" . &sql_str_encode($country_code) . "', ".
		  "'" . &sql_str_encode($language_code) . "', ".
		  "'" . &sql_str_encode($locale_code) . "');"; 

        print "$sql\n";
        $dbh->do($sql);
      }
    }
    else {
      print STDERR "Nothing for: '$p'\n";
      my $sql = "INSERT INTO adword_data (set_id, suggestion, country_code, language_code, locale_code) VALUES ($set_id, '" . &sql_str_encode($p) . "', ".
		  "'" . &sql_str_encode($country_code) . "', ".
		  "'" . &sql_str_encode($language_code) . "', ".
		  "'" . &sql_str_encode($locale_code) . "');"; 
      print "$sql\n";
      $dbh->do($sql);
    }
  }
}

  $dbh->disconnect();
}

sub trim() {
  my $string = shift;
  $string =~ s/^\s+//;
  $string =~ s/\s+$//;
  return $string;
}

sub sql_str_encode() {
  my $str = shift(@_);
  $str =~ s/'/''/sg;
  $str =~ s/[^[:ascii:]]+//sg;  # get rid of non-ASCII characters
  return $str;
}

