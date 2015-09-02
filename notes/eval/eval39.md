# Evaluation 39: Quality of wget region detection

## Overview

### Purpose

We report how well our `wget` tutoron can detect code examples from real web pages.

### Summary


## Procedure

### Dataset

Although this evaluation concentrates on `wget`, this same procedure applies to our building datasets for CSS selectors (see [Evaluation 45](../eval/eval45)) and regular expressions (see [Evaluation 46](../eval/eval46)).

Scraping parameters:
T: count of top tag 3-grams (20)
S: number of search results to consider for each tag (10)
-: number of tutorials queried for a language (300)
N: number of random tutorials to pick from those found in each condition (100)
R: intended number of explainable regions for each micro-language (200)

We build a corpus of programming tutorials that have a code example containing a target micro-language topic, but which uses any number of additional tools or languages.  We want to get a good coverage of the primary (non-target) tools and languages to avoid overfitting our detection method to the tutorial convention of any one programmer community, if such conventions exist.

To find related languages and tools, we use the crowd-provided tags on StackOverflow to determine what other languages or topics are used with a language.  Our search process includes:

1. Collect the top T tag 3-grams that related to the micro-language
2. Search for `<tag1> <tag2> <tag3> tutorial` via Google, saving the full first page of search results, where we consider S search results
3. Continue with bigrams in order of frequency in SO posts (highest to lowest) until we have fetched N distinct pages.  Manually inspect each of result, asking: Does this page contain a code example?  We exclude all pages that do not.

In the above, a **code example** is one or more lines of source code in a programming language that demonstrates how to do something with code

We divide the remaining documents in half into a cross-validation and test set by random assignment.  Both consist of ~N tutorials per micro-language and, we hope, >R expected explainable regions total.  We separate the cross-validation and test sets so that we can improve our algorithm's performance on the cross-validation set, running the test set once the cross-validation set has been satisfied so that we don't overfit the test data.

**Note**: given time constraints, we have not gone beyond testing against a validation set of ~50 tutorials.  The numbers reported below are for this validation set.

To find expected explainable regions, we scan the full body of the page (both text and code elements). 

#### Why choose tutorials from only the top 10 search results?

Several studies suggest that web searchers expect the best answer to be among the top one or two hits in the results listing (Hearst 5.15).  Studies and query logs show that searchers rarely look beyond the first page of search results (Hearst 5.15).

In the domain of coding search (albeit with code examples and not looking at tutorials) we see this behavior:
  * Most of the users do not look beyond the first result page in Koders (Bajracharya & Lopes 431)
  * About 85% of all downloads that followed a search activity were made after only one page view (Bajracharya & Lopes 431)

#### Heuristics for finding explainable regions including wget.  What do we pick, and what do we skip?

**Note**: I need to review this to make sure that it was accurate throughout the entirety of sample extraction.

To find wget, we look for:
* strings that can be run in bash that will invoke wget
  * including those that have been found in output, for example of the process command
* it can have variables, or placeholders (e.g., <http://site.html> instead of a real site)
* capitals for WGET is also okay
* we cut off before the space before a pipe symbol or a "2>&1", and ignore the sudo that could precede it. 
* Include all instances where wget is preceded by xargs, and start the region at the "wget" command name
* It's okay if the command is in a reference comment in some other code, because the intent is to show a wget command that can be run
* Skipping
  * All instances of wget where no concrete or template args are provided, but just a very generic body (e.g., "wget someArgs").
  * Commands that wouldn't run in bash because of invalid syntax (e.g., unmatched quotes)

### Measurements

To compute precision and recall of our detection technique, we modify our detection algorithm to surround all detected explainable regions with a bright red box.  Then one of us went through all expected and detected explainable regions, viewing the documents side by side.  A mismatch occurs if one or the other documents has an explainable region whose bounds and parent container do not exactly match that of any explainable region in the other document.

## Technical Improvements

We were able to drastically improve detection accuracy on our validation set by iterating on our detection procedure.

### Round 5 Improvements

In the round of improvements at Tutorons server commit `fc51aac`, we began to parse each page using the `html5lib` library, which better preserves the whitespace to match how the examples were originally extracted in our ground truth data by Javascript.

### Round 8/9 Improvements

To ease debugging, `514640d` introduced finding a region once and not multiple times.  However, the initial version of this had a bug where the wrong node was reported for each region found.  So, we report the accuracy of both this initial 'bugged' version and the improved version.

### Round 10 Improvements

We examined all of the false detections (causes of poor precision) from round 9.  For the ones which were indeed valid `wget` commands, we added these to our list of 'ground truth' examples.  Then we re-ran our precision calculation.  This increased both the precision (because we identified the false negatives) and the recall (it added to the ratio of correct detections found).

## Notes

### Accuracy

Version `fc51aac`: Precision 82.63%, Recall 61.70%

Version `514640d` (with bugs): Precision 22.79%, Recall 16.49%

Version `514640d`: Precision 83.82%, Recall 60.64%

Version `514640d` (false negatives added to ground truth): Precision 94.85% (129/136), Recall 63.55% (129/203)

#### Version `514650d` false negatives

For each of the false negatives, we store it into our list of ground truths sot that we can re-run the tests with an updated version of the test dataset.

### Errata

