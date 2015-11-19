# Prototype

## Overview

### Purpose

We attempt to get a cross-section of typical programmer queries for tutorials.
For this purpose, we use Adam Fourney's implementation of CUTS!

### Summary

## Procedure

### The tool

Adam Fourney sent us the following code, with these instructions:
These are the two scripts that will get me started.

    ./google_suggest_bfs.pl "firefox" > raw/firefox.txt
    ./google_suggest_bfs_pre.pl "firefox" >> raw/firefox.txt

It should be okay that the NumPages field is always blank.

There's also a script that inserts these text files into a Postgresql database.
Adam writes that he used the database for three reasons:

1. It support concurrency out of the box (so, you could run multiple jobs in parallel to process data)
2. Transactions help keep the database consistent in case mutations were interrupted
3. Tasks could be easily interrupted and resumed

So, here's the expected division of content based on the scripts:
* the `google_suggest_*.pl` scripts are the ones that query the Google Suggest API for common queries.
* `adwords.pl`: all of the ideas (including the database access) come together here.  This one depends on the AdWordsLib, which depends on the Adwords Perl SDK downloaded from Google in 2010.
* `AdWordsLib.pm`: (presumably a wrapper for the Google AdWords API, which may be able to reveal common keywords)

#### More details

Additional files Adam once used included Javascript experiments, which enable real-time exploration of the data.
However, he'll have to track these down independently.

Other code Adam had written computed tree properties for prefixes and various forms of clustering.
The best clustering was achieved by pulling the search engine results pages (SERPs) for each query and then doing a K-means on the pages.

### Use case

Adam 

### Construction

### Expected Outcome


## Notes

### Observations

### Technical Improvements

### Research Ideas
 
