# Evaluation 49: CSS Selector Parsing accuracy

## Overview

### Purpose

In past evaluations and prototypes, we have built a custom parser that's capable of parsing many simple CSS selectors into a parse tree from which we can generate explanations.  To show that the parsers that we can generate are capable of reliably parsing code snippets found on the web, we compute the success rate of our CSS selector parser parsing CSS selectors found in online tutorials.

### Summary

## Procedure

In E45, I extracted jQuery selectors from around 44 online tutorials.  From the data file from E45 of explainable region locations (jquery_validation\_44.txt), I extract all selectors (selectors.txt) using a script that scans the pages for the locations scraped (fetchselectors.py).  Then I clean the ones that appear obviously wrong / slightly offset, for example "a.fancybox" shouldn't have quotes surrounding, and " #contact\_form textarea[required=true" has a leading space and missing a trailing bracket.

From server revision 2f1fdc1, I grab the ANTLR4 grammar 'Css.g4'.  I generate the parser from this, run it against each of the extracted selectors, and report the percentage of correct parses and failed parses.

For each of the parse failures, I classify whether the issue with the parse is with the selector itself (is it valid CSS selector syntax) or whether the problem is with our parser -- does it not accept the syntax shown.  For any parse failures caused by our system, I note what needs to be changed about our system to accept the selector.

Finally, for a sample of 30 correctly parsed selectors, I plot by hand what I expect them to appear like when parsed, given our syntax.  Then I verify by viewing the PNG output of the ANTLR parse tree that for each of these selectors, the parse tree is correct.

### Expected Outcome

We find that our system fails on 10% of examples.  We also find that there is only 1% of examples that are malformed CSS selectors to begin with.  We discover that our system does not support pseudo-selectors.

## Notes

### Observations

On our first run, 322 out of 334 selectors (96.41%) succeed at parsing.  If we consider selectors that failed to parse that should be parsed by a functional CSS selector parser, then we have a success rate of 332 out of 334 selectors (99.4%).

These are the strings that failed to parse:

    div[data-role=”page”]
    div[data-role=”page”]
    div[data-role=”dialog”]
    div[data-role=”page”]
    div[data-role=”page”]
    input[name*="_r"]
    input[name*="_r"]
    :jqmData(role='foo')
    :jqmData(role='page')
    :jqmData(role='content')
    #contact_form  input[required=true]
    #contact_form  input[required=true]

We can divide these into 2 strings (.60%) that *should have* parsed and 10 strings (2.99%) that were incorrectly specified online / had invalid syntax to begin with.

#### Strings that should have passed

Our system should, by initial appearances, be able to parse the following selectors:

    input[name*="_r"]
    input[name*="_r"]
    #contact_form  input[required=true]
    #contact_form  input[required=true]

After inspection, we find that we fail to parse the following as our current grammar doesn't allow us to contain attribute values in double quotation marks.

    input[name*="_r"]
    input[name*="_r"]

We also find that it's quite reasonable that the last 2 selectors didn't parse, and that our parser shouldn't necessarily support parsing of these selectors.  See the section below for clarification.

#### Strings that rightly failed

The last two selectors from the above group fail to parse because the two spaces are not both normal spaces.  While the first space is ASCII character 32, the second space is ASCII character 160, which according to [this reference](http://www.ascii.cl/htmlcodes.htm), is a non-breaking space.  This is a formatting problem that is a formatting failure on the part of the blog poster.

    #contact_form  input[required=true]
    #contact_form  input[required=true]

This group of strings have curly quotes instead of ASCII double quotes:

    div[data-role=”page”]
    div[data-role=”page”]
    div[data-role=”dialog”]
    div[data-role=”page”]
    div[data-role=”page”]

These selectors are actually valid jQuery selectors (using the jQuery-specific pseudoclass jqmData), but are not valid CSS selectors:

    :jqmData(role='foo')
    :jqmData(role='page')
    :jqmData(role='content')

### Errata

### Technical Improvements

### Research Ideas
 
