#!/usr/bin/perl -w

use lib '/home/afourney/lib/perl5';
use strict;
use XML::Simple;
use Encode;
use Data::Dumper;

binmode(STDOUT, ":utf8");
binmode(STDERR, ":utf8");

# http://www.xroxy.com/proxylist.php
my @proxies = (
  '',                    # NONE
  '74.115.1.10:80',      # US
);
my $proxy = $proxies[0];

my @alphabet = split(//, " abcdefghijklmnopqrstuvwxyz0123456789.'-_");

my $errors = 0;

my @seeds = ();
&main();

sub main() {
  print "#Proxy: $proxy\n";
  print "#Level, Query, CharacterPosition, Rank, Suggestion, NumPages\n";

  @seeds = (); 
  push @seeds, $ARGV[0];

  while ($#seeds > -1) {
    my $seed = shift(@seeds);

    ######
    my @results = &google_suggest($seed);

    print STDERR "'$seed': " . ($#results + 1) . " results\n";

    my $valid_results = 0;
    foreach my $result (@results) {
      my %r = %$result;

      next unless (index($r{'result'}, $seed) == 0);
      $valid_results++;

      print length($r{'query'}) - length($ARGV[0]) . ', ' .
            $r{'query'} . ', '.
                     -1 . ', '.
             $r{'rank'} . ', '.
           $r{'result'} . ', '.
        $r{'num_pages'} . "\n";
    } 

    sleep(rand(2) + 1) if (rand(10) > 7);

    ####
    if ($#results >= 9 && $valid_results > 0) { # A full set of results
      foreach my $c(@alphabet) {

	next if ($c eq ' ' && $seed =~ m/ $/); # No 2 spaces in a row
	next if ($c ne ' ' && $seed eq $ARGV[0]); # Enforce spaces after the initial seed

        push @seeds, "$seed$c";
      }
    } 
  }
}

sub google_suggest() {
  my $q = shift(@_);
  #$q =~ s/\s+/ /g;
  #$q = &trim($q);

  my $cp = -1;
  $cp = shift(@_) if (scalar(@_));

  my $convert_to_utf8 = 0;
  $convert_to_utf8 = shift(@_) if (scalar(@_));

  my $url_q = &url_encode($q);
  my $url_cp = $cp > -1 ? "&cp=$cp" : "";

  # Fetch the suggestions
  my @lines = ();
  if ($proxy ne '') {
    open(my $cmdin, "-|:raw", "/usr/bin/curl", "--silent", "-x", $proxy, "-w", '\n%{content_type}', "http://google.com/complete/search?output=toolbar&q=$url_q$url_cp");
    @lines = <$cmdin>;
    close($cmdin);
  } 
  else {
    open(my $cmdin, "-|:raw", "/usr/bin/curl", "--silent", "-w", '\n%{content_type}', "http://google.com/complete/search?output=toolbar&q=$url_q$url_cp");
    @lines = <$cmdin>;
    close($cmdin);
  }

  my $content_type = lc(pop(@lines));
  my $data = join('', @lines);

  # Read the charset, and convert to UTF-8
  my $charset = 'iso-8859-1'; # Google suggest seems to default to ISO-8859-1 in North America
  if ($content_type =~ /charset=(.*?)\s*$/) {
    $charset = $1;
  }
  $data = decode($charset, $data);

  # This is broken, but it should never happen....
  # In any case, it keeps things from crashing
  #
  if ($convert_to_utf8) {
    print STDERR "Converting to UTF-8\n";
    $data = encode_utf8($data);
  }

  my $toplevel = "";
  eval { $toplevel = XMLin($data, forcearray => 1) };

  if ($@) {
    my $err = "$@";

    print STDERR "$err\n$data\n";
    $errors++;

    if ($errors > 8) {
      print STDERR "Skipping '$q'\n";
      return ();
    }

    if (index($err, 'Input is not proper UTF-8') >= 0) {
      $convert_to_utf8 = 1;
    }

    sleep(15 + (2 ** $errors > 5*60 ? 5*60 : 2**$errors));
    return &google_suggest($q, $cp, $convert_to_utf8);
  }

  $errors = 0;

  my @results = ();

  if ( exists($toplevel->{CompleteSuggestion})) {
    my @cs = @{$toplevel->{CompleteSuggestion}}; 

    my $rank = 0;
    foreach my $s(@cs) {
      my $num_pages = $s->{num_queries}->[0]->{'int'}; 
      my $data = $s->{suggestion}->[0]->{'data'}; 

      if (!(defined $num_pages) || $num_pages eq '') {
        $num_pages = '';
      }

      my %r = ( 'query'       => $q,
                'result'      => $data,
                'rank'        => $rank,
                'num_pages'   => $num_pages );
	
      push @results, \%r;
      $rank++;
    }
  }

  return @results;
}

sub trim() {
  my $string = shift;
  $string =~ s/^\s+//;
  $string =~ s/\s+$//;
  return $string;
}

sub url_decode() {
  my $str = shift(@_);
  $str =~ s/\%([A-Fa-f0-9]{2})/pack('C', hex($1))/seg;
  return $str;
}

sub url_encode() {
  my $str = shift(@_);
  $str =~ s/([^A-Za-z0-9])/sprintf("%%%02X", ord($1))/seg;
  return $str;
}
