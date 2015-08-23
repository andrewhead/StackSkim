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
 
