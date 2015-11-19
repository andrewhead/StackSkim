#!/usr/bin/perl -w

use strict;


my $fname = $ARGV[0];
open(FH, "<raw/$fname") or die("$!\n");
my @lines = ();
while (<FH>) {
  push @lines, $_;
}
close(FH);

my %h = ();
foreach (@lines) {
  # Read the next line
  my $line = $_;
  chomp($line);
  $line = &trim($line);
  
  # Skip comments
  next if ($line =~ m/^#/);

  # Get fields
  my @fields = split(/,\s?/, $line);
  my ($level, $query, $cp, $rank, $suggestion, $num_pages) = @fields;

  if (exists $h{$suggestion}) {
    my $q = $h{$suggestion};
    if (length($query) < length($q)) {
      $h{$suggestion} = $query;
    }
  }
  else {
    $h{$suggestion} = $query;
  }
}

die("Bad filename unless") unless($fname =~ /^(.*?)__(\d\d)-(\d\d)-(\d\d\d\d)_(\d\d)(\d\d)(\d\d)\.full\.csv$/);

my $topic = $1;
my $day   = $2;
my $month = $3;
my $year  = $4;
my $hour  = $5;
my $min   = $6;
my $sec   = $7;

$topic =~ s/_/ /g;

print "\\set ON_ERROR_STOP\n";
print "BEGIN;\n";

print<<SQL;
INSERT INTO full_sets (
  topic, 
  dts,
  proxy,
  file_name)
VALUES (
  '@{[ &sql_str_encode($topic) ]}',
  '$year-$month-$day $hour:$min:$sec -5:00',
  NULL,
  '@{[ &sql_str_encode($fname) ]}'
);
SQL

my $line_n = 0;
foreach (@lines) {
  $line_n++;
  
  # Read the next line
  my $line = $_;
  chomp($line);
  $line = &trim($line);
  
  # Skip comments
  next if ($line =~ m/^#/);

  # Get fields
  my @fields = split(/,\s?/, $line);
  my ($level, $query, $cp, $rank, $suggestion, $num_pages) = @fields;

  if ($cp < 0) {
    $cp = length($query);
  }

  unless(defined($num_pages) && ($num_pages + 0 > 0)) {
    $num_pages = 'NULL';
  }

  my $first_observation = 'false';
  if (length($query) == length($h{$suggestion})) {
    $first_observation = 'true';
  }

  print<<SQL;
INSERT INTO full_suggestions (
  set_id, 
  query,
  caret_position,
  rank,
  suggestion,
  num_results,
  level, 
  first_observation)
VALUES (
  (SELECT id FROM full_sets WHERE file_name = '@{[ &sql_str_encode($fname) ]}'),
  '@{[ &sql_str_encode($query) ]}',
  $cp,
  $rank,
  '@{[ &sql_str_encode($suggestion) ]}',
  $num_pages,
  $level,
  $first_observation
);
SQL
}


print "COMMIT;\n";

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

