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
 
# Evaluation 46: Regex detection accuracy

## Overview

### Purpose

We determine the correctnes (precision) of our regular expression detection for web tutorials to show how feasible it is to detect regular expressions that need to be explained in web tutorials.

### Summary

## Theory

We can think of how a language is used on a page through both the purpose of using the language in the first place, and by the ways the language is used.  We can start by categorizing pages by its purpose for a language:
* a __targeted end use__ help page produces code to perform a specific programming tasks (e.g, setting up a server, or validating form data) or teaches another language while making use of the target language
* a __miscellany end use__ help page is one provides a reference of useful snippets or patterns that can be applied to tasks in many domains.
* a __pedagogical page__ provides an introduction to what the language can do and how to construct code from language primitives

A language can be used in many ways.  These ways include:

* __end use example__: `example` written to perform a programming task (or to demonstrate a concept of another language?).  While these examples may require the reader to modify them with their own parameter values, this code is there to be used in close to its current form
* __conceptual example__: example written to demonstrate the reference or the capabilities of language in the abstract
* __breakdown__: description of syntactical elements used in an example
* __conceptual introduction__: description of what the language is used for
* __reference__: description of possibly useful syntactic elements, without the main purpose of applying them to concrete scenarios

With tutorons, we are interested in explaining end use examples on targeted end use pages (and to a lesser degree, miscellany end use pages).  During this evaluation, I ignore all regular expressions that are used as part of conceptual examples or reference material for the sake of expediency in finishing this study.

## Procedure

### Use case

I report the recall of our system for detecting end use examples on end use pages.  I also informally analyze false detections, taking a sample of false detections and reporting the proportion that are conceptual examples or reference syntax (i.e. have not been manually labeled in our ground truth set), and the number that are not regular expressions at all and shouldn't have been detected.

### Construction

#### Dataset

I inspect all pages from E39 that:

1. were fetched for with the 'regex' tag
2. include a code example.

For each page, I mark the high-level purpose of using the language on that page.  Even if a pedagogical page has end-use examples, I ignore these examples as I assume that no one will arrive at that page for that specific end use.  For our current labeling, the pedagogical class is our catch-all for non-end use pages, including library reference pages, cheatsheets, and regular expression building and validation tools.

In my first pass, the following are the IDs used for validation:

    [1723, 1938, 1875, 1690, 1936, 1939, 1683, 1837, 1598, 1755, 1870, 1858, 2030, 1784, 1869, 1819, 1793, 2067, 1791, 1742, 1907, 1839, 1912, 1717, 1999, 1853, 2004, 1534, 1860, 1984, 2042, 1935, 1779, 1538, 1914, 2053, 1946, 1797, 1995, 2023, 1572, 1753, 1788, 1655, 1932, 1985, 1712, 1908, 1796, 1769]

And the following are the IDs used for testing:

    [1540, 2056, 2007, 1804, 1877, 1953, 1986, 1904, 1906, 1910, 1760, 1794, 1989, 1893, 1532, 1903, 1836, 2001, 1714, 1800, 1983, 1851, 1568, 1897, 1937, 1589, 1838, 1834, 2026, 1958, 1639, 1959, 1539, 1856, 1789, 1855, 2074, 1902, 1934, 1682, 2009, 1919, 2077, 1754, 1997, 1767, 2002, 2003, 1715, 1840]

#### Flavor of regular expressions

As regular expressions detected can belong do different flavors, we rely on the fact that if we can explain something with PCRE, in general those explanations should apply to Python or Javascript, as PCR is more fully featured [(reference)](https://web.archive.org/web/20120119201049/http://www.regular-expressions.info/refflavors.html).

#### Detecting regex in grep commands

To detect patterns in grep, we refer to the grep man page to find that patterns may be specified as a positional required argument, or within an optional argument.  We then check out this commit of the grep source code (corresponding to v2.21).  We invoke the three commands specified by the `README-hacking`: `./bootstrap`, `./configure`, and `make`.  Then we modify the code!

#### Detecting regex in sed commands

For sed, we'll want to handle regexp-style addresses AND arguments to commands
Some commands accept addresses, and some don't (I think)
To install, I first fork from the Savannah GNU sed repository v4.2.2.  Then I install the dependency md5sha1sum, `./bootstrap`, `./configure`, `make`.

### Expected Outcome

## Notes

### Observations

In the first iteration of regular expression detection quality (server version `2f1fdc1`), we found the following reasons for the first 40 failed detections where the regexp could not be found:
We cannot find regular expressions in the following languages:
* tcl
* strings outside a programming block
* PHP strings
* perl
* awk, gawk
* Apache config (`FilesMatch`)
* Java strings
We also can't find them when they're not in a code or pre block

Then we also recognized these errors for the first 40 false detections where a regexp was found where it should have been.  The most frequent cause (accounting for ~75% of false detections) is finding Javascript regular expressions where they aren't by interpreting '/' in other languages as delimiters for regular expressions.

### Errata

### Technical Improvements

### Research Ideas
 
