# Evaluation 45: CSS detection accuracy

## Overview

### Purpose

Determine the precision and recall of our CSS tutoron for detecting examples of CSS selectors that are used as code examples on webpages.

We develop our CSS selector extractor we actually focus on jQuery selectors.  So, selectors very similar to CSS selectors that:
1. Are more complex than just the name of a tag
2. If pseudo-selectors, are attached to the name of an element

### Summary


## Procedure

### Dataset

We fetch a corpus of about 300 HTML documents that come up on Google as results for tri-grams of tags related to jQuery (see the procedure of this step in E39).  When choosing what pages to examine, we exclude all pages where the only selectors on the page have already been explained in comments (textual or otherwise) that are directly adjacent to where the selector is written.  We also ignore jQuery selectors that are displayed as part of a cheatsheets format or intention.  In other words, if the selector is shown in some list or table of what selectors can be used in general instead of what selector(s) should be used for a specific task, we do not include these pages in our corpus because (a) extraction will take too long (b) the purpose of tutorons are to explain unexplained code on webpages.

We compute precision and recall similarly to how we do it in [Evaluation 39](../eval/eval39)

### Notes on extraction sources

When looking for pages that have code as the first step, we skip the following:
* Unresponsive script: 46
* Tutorial compilation pages: 57,97,104,105,106,107,109,122,123,130,131,132,133,144,148,149,218
* The only selectors shown are also explained in-place: 118

We also note that for page 69, there are characters that are part of the selector that are not displayed in the correct encoding.

When taking a pass through the 50 randomly selected tutorials, I intentionally omit:
* Code examples from comments: Validation 4, 13, 15, 20, 41.  For each of these pages, nothing happened when I selected using my plugin
* Full pages that failed to load. Fore example, for Validation 32, the page went blank part way through load
* Some pages had weird formatting that prohibited extraction: Validation 35
* On page Validation 37, there's the weird encoding

### Iteration on the dataset

In preparation for round 3, I go back through the tutorials, and look for all examples of jQuery selectors that are actually simple (only the tag name), and add for a second time any selectors that I thought were obscure enough to be missed on the first pass-through.  I also find both simple (purely tag-name) and complex selectors in Validation 45-49.

## Notes

### Results

Round 2: Precision 68.91% (164/238), Recall 47.81% (164/343)
Rounds 3,4,5: Precision 80.25% (191/238), Recall 45.26% (191/422)

### Errata

### Technical Improvements

### Research Ideas
 
