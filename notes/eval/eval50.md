# Evaluation 50: Using requests for automatic testing

## Overview

### Purpose

During iteration 7 of `wget` detection testing, we found that our precision decreases when fetching code examples using the `requests` package instead of loading them through the browser.  This evaluation looks to see whether there is a spacing difference between pages downloaded through requests and those loaded through the browser.

### Summary

See the `Observations` section.

## Procedure

To find out the additional misdetections that we find in iteration 7, I compare two files:

* `false_detections-7-20150824-22:04:19.tsv`
* `false_detections-5-20150824-16:41:15.tsv`

I find that there are roughly 100 additional misdetections for iteration 7, almost all of them occurring for the drupal.org page.  This page has caused problems in the past in that code examples may be found at a character offset of 10000 or more, which makes the positioning highly sensitive to whitespace that comes before the code example within the same HTML node.

To see how the two files differ, I start up the local file server of files from [Evaluation 39](../eval/eval39) and download the same file through the Firefox browser and through `requests.get`.  I query for this file:

    http://127.0.0.1:8000/pages/wget/curl%20php%20wget%20tutorial/8/www.drupal.org/node/23714.html

The versions of this file that I download are:

* `requests.html`: downloaded through `requests`
* `browser_source.html`: the saved version of the file as fetched through the "View Source" option in the browser
* `browser_saveas_html.html`: the browser page saved as "HTML only"
* `browser_innerhtml.html`: the contents of the page saved from `document.body.innerHTML` after opening it in the browser

I then use `meld` to report whether or not there are whitespace differences between these files, and what whitespace seems to get omitted by one copy of the file vs. the other.  I also report if there are any substantial non-whitespace differences.

### Expected Outcome

There are some newlines omitted.

## Notes

### Observations

There were no perceivable differences between `requests.html`, `browser_source.html`, and `browser_saveas_html.html`.

When comparing `requests.html` to `browser_innerhtml.html`, however, there are *many* differences.  The attributes of nodes are in a different order.  There are `&nbsp;` in place of spaces (at least a dozen times).  And one apostraphe is written as an apostrophe in `browser_innerhtml.html`, but is in numeric format (preceded with a `#`) in the `requests.html` file.  This suggests that the way that by the time that the HTML is accessible by Javascript, it has changed in some way from the original source.

### Errata

### Technical Improvements

### Research Ideas
 
