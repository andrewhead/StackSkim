# Evaluation 49: CSS Selector Parsing accuracy

## Overview

### Purpose

In past evaluations and prototypes, we have built a custom parser that's capable of parsing many simple CSS selectors into a parse tree from which we can generate explanations.  To show that the parsers that we can generate are capable of reliably parsing code snippets found on the web, we compute the success rate of our CSS selector parser parsing CSS selectors found in online tutorials.

### Summary

On a sample of 343 jQuery selectors, our CSS parser parses 330 (96.21%) of them successfully.  Furthermore, the parser successfully parses 340 / 343 (99.13%) when we exclude text snippets that include invalid characters or jQuery specific pseudo-classes.  For a sample of 50 of the selectors that successfully parse, all are parsed into the expected parse tree, verified through visual inspection of the resulting trees.

## Procedure

In E45, I extracted jQuery selectors from around 44 online tutorials.  From the data file from E45 of explainable region locations (jquery_validation\_44.txt), I extract all selectors (selectors.txt) using a script that scans the pages for the locations scraped (fetchselectors.py).  Then I clean the ones that appear obviously wrong / slightly offset, for example `"a.fancybox"` shouldn't have quotes surrounding, and ` #contact_form textarea[required=true` has a leading space and missing a trailing bracket.

From server revision `2f1fdc1`, I grab the ANTLR4 grammar 'Css.g4'.  I generate the parser from this, run it against each of the extracted selectors, and report the percentage of correct parses and failed parses.

For each of the parse failures, I classify whether the issue with the parse is with the selector itself (is it valid CSS selector syntax) or whether the problem is with our parser -- does it not accept the syntax shown.  For any parse failures caused by our system, I note what needs to be changed about our system to accept the selector.

Finally, for a sample of 42 of all correctly parsed selectors (with all those that failed to parse removed — see file `data/selectors_with_urls_pruned.txt`), I determine what I expect them to appear like when parsed, given our syntax.  I randomly sample 1 selector from each of the pages where a selector was correctly parsed, as some pages may have more simpler or more complex selectors, and have a larger share of the total number of correctly parsed selectors.  These selectors are stored in `data/selectors_to_inspect.txt`.

For each selector in this sample, I produce a string representation of the parse tree in the format that ANTLR writes with the `tree.toStringTree(parser)` method (`data/expected_trees.txt`).  I compare the parse trees I write to the ones produced by our parser (`data/generated_trees.txt`) using `diff` and report on the number that are parsed in an incorrect format.

#### Iterations on Data set

We increased the number of selectors in the ground truth to 466 after viewing the false negatives from rounds 3-6 of [Evaluation 45](../eval/eval45).  I update the overall parser accuracy based on this updated data set.

### Expected Outcome

We find that our system fails on 10% of examples.  We also find that there is only 1% of examples that are malformed CSS selectors to begin with.  We discover that our system does not support pseudo-selectors.

With the sample of 50 correctly parsed selectors, we find that there are none that are parsed into an incorrect parse tree.

## Notes

### Parser Completion Rate (Round 2)

Overall, we successfully parse 94.42% (440/466) selectors.  We find that the following strings fail to parse:

    div[data-role="page"]
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
    #contact_form input,#contact_form select
    #contact_form input,#contact_form select
    #contact_form select,#contact_form input
    :jqmData(role='page')
    :jqmData(role='content')
    :jqmData(role='foo')
    #filter a:contains("Bing")
    #filter a:nth-child(5)
    #filter a:contains("Bing")
    #filter a:nth-child(5)
    #filter a:contains("Contact")
    #username, #fullname
    #username, #fullname

The first 13 above are the same as before (3 that should have parsed, and 10 that should not).  Then the next 13 include 10 that should have parsed, and 3 that should not.  The 3 that should not are the selectors including ':jqmData'.  Those that should failed to parse due to the function construct or commas.

This leaves us at 440/453 (97.13%) of 'proper' selectors from our online corpus as correctly parsing.

### Parser Completion Rate

On our first run, 330 out of 343 selectors (96.21%) succeed at parsing.  If we consider selectors that failed to parse that should be parsed by a functional CSS selector parser, then we have a success rate of 340 out of 343 selectors (99.1%).

These are the strings that failed to parse:

    div[data-role="page"]
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


We can divide these into 3 strings (.88%) that *should have* parsed and 10 strings (2.92%) that were incorrectly specified online / had invalid syntax to begin with.

#### Strings that should have passed

Our system should, by initial appearances, be able to parse the following selectors:

    div[data-role="page"]
    input[name*="_r"]
    input[name*="_r"]
    #contact_form  input[required=true]
    #contact_form  input[required=true]

After inspection, we find that we fail to parse the following as our current grammar doesn't allow us to contain attribute values in double quotation marks.

    div[data-role="page"]
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

### Parse success rate

All 42 selectors (100%) in our sample were parsed into the expected tree.

### Errata

### Technical Improvements

By inspecting the [CSS3 selectors grammar](http://www.w3.org/TR/css3-selectors/#w3cselgrammar) I discover that our current parser doesn't handle the following aspects of the grammar:

* Multiple hashes, classes, pseudoclasses and attributes allowed for each sequence of simple selectors
* Groups of selectors
* Plus, greater, and tilde combinators
* Enforcing only one pseudo-element as part of the last sequence of simple selectors

### Research Ideas
 

