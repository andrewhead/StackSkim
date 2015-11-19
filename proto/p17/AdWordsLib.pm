  package AdWordsLib;
 
  use strict;
  #use warnings;

  use Google::Ads::AdWords::Client;
  use Google::Ads::AdWords::Logging;
  use Google::Ads::AdWords::v201008::Keyword;
  use Google::Ads::AdWords::v201008::CountryTarget;
  use Google::Ads::AdWords::v201008::LanguageTarget;
  use Google::Ads::AdWords::v201008::CountryTargetSearchParameter;
  use Google::Ads::AdWords::v201008::LanguageTargetSearchParameter;
  use Google::Ads::AdWords::v201008::KeywordMatchTypeSearchParameter;
  use Google::Ads::AdWords::v201008::Paging;
  use Google::Ads::AdWords::v201008::RelatedToKeywordSearchParameter;
  use Google::Ads::AdWords::v201008::TargetingIdeaSelector;
  use Google::Ads::Common::MapUtils;
 
  use vars qw($VERSION @ISA @EXPORT);

  $VERSION = '1.00';
  @ISA     = qw(Exporter);
  @EXPORT  = qw(query_adwords);
 
  #####

  my $client = undef;

sub query_adwords {

  # Get the searches
  my $phrases_ref = shift(@_);

  my $countryCode = '';
  if (scalar(@_)) {
    $countryCode = shift(@_);
  }

  my $languageCode = '';
  if (scalar(@_)) {
    $languageCode = shift(@_);
  }

  my $localeCode = '';
  if (scalar(@_)) {
    $localeCode = shift(@_);
  }

  my @phrases = @$phrases_ref;

  # Get AdWords Client, credentials will be read from ~/adwords.properties.
  unless (defined($client)) {
    $client = Google::Ads::AdWords::Client->new({version => "v201008"});
  }

  # By default examples are set to die on any server returned fault.
  $client->set_die_on_faults(1);

  my @keywords = ();

  # Create an array of keywords
  foreach my $p(@phrases) {
    my $keyword = Google::Ads::AdWords::v201008::Keyword->new({
      text => $p,
      matchType => "EXACT"
    });
    push @keywords, $keyword;
  }

  # Create selector.
  my $selector;
  if ($localeCode eq '') {
    $selector  = Google::Ads::AdWords::v201008::TargetingIdeaSelector->new({
      requestType => "STATS",
      ideaType => "KEYWORD",
      requestedAttributeTypes => ["KEYWORD",
    				  "AVERAGE_TARGETED_MONTHLY_SEARCHES",
                                  "TARGETED_MONTHLY_SEARCHES"],
    });
  }
  else {
    $selector  = Google::Ads::AdWords::v201008::TargetingIdeaSelector->new({
      requestType => "STATS",
      ideaType => "KEYWORD",
      localeCode => $localeCode,
      requestedAttributeTypes => ["KEYWORD",
    				  "AVERAGE_TARGETED_MONTHLY_SEARCHES",
                                  "TARGETED_MONTHLY_SEARCHES"],
    });
  }

  # Set selector paging (required for targeting idea service).
  my $paging = Google::Ads::AdWords::v201008::Paging->new({
    startIndex => 0,
    numberResults => scalar(@phrases)
  });
  $selector->set_paging($paging);


  my @params = ();

  # Create related to keyword search parameter.
  my $keyword_search_parameter =
    Google::Ads::AdWords::v201008::RelatedToKeywordSearchParameter->new({
      keywords => \@keywords 
    });

  # Create keyword match type search parameter to ensure unique results.
  my $keyword_match_type =
    Google::Ads::AdWords::v201008::KeywordMatchTypeSearchParameter->new({
      keywordMatchTypes => ["EXACT"]
    });

  push(@params, $keyword_search_parameter);
  push(@params, $keyword_match_type);

  if ($countryCode ne '') {
    my $target = Google::Ads::AdWords::v201008::CountryTarget->new({
        countryCode => $countryCode
    });

    my $country_target_search_parameter = Google::Ads::AdWords::v201008::CountryTargetSearchParameter->new({
	countryTargets => [$target]
    });

    push(@params, $country_target_search_parameter);
  }

  if ($languageCode ne '') {
    my $target = Google::Ads::AdWords::v201008::LanguageTarget->new({
        languageCode => $languageCode
    });

    my $language_target_search_parameter = Google::Ads::AdWords::v201008::LanguageTargetSearchParameter->new({
	languageTargets => [$target]
    });

    push(@params, $language_target_search_parameter);
  }

  $selector->set_searchParameters(\@params);

  # Get related keywords.
  my $page = $client->TargetingIdeaService()->get({selector => $selector});


  my %results = ();

  # Display related keywords.
  if ($page->get_entries()) {
    foreach my $targeting_idea (@{$page->get_entries()}) {
      my $data = Google::Ads::Common::MapUtils::get_map($targeting_idea->get_data());

      my $phrase  = $data->{"KEYWORD"}->get_value()->get_text();
      my $avg     = $data->{"AVERAGE_TARGETED_MONTHLY_SEARCHES"}->get_value();
      my $monthly = $data->{"TARGETED_MONTHLY_SEARCHES"}->get_value();

      my %record = ();
      my @months = ();
      $record{'avg'} = $avg;
      $record{'raw'} = $targeting_idea;

      my @monthly_arr = @$monthly;
      foreach(@monthly_arr) {
        my $count .= $_->get_count() ? $_->get_count() : 0;
        push @months, {'year' => $_->get_year(), 'month' => $_->get_month(), 'count' => $count }; 
      }    

      $record{'monthly'} = \@months;
      $results{$phrase} = \%record;
    }
  } 

  return \%results;
}
 
1;
