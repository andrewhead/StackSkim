# Prototype 18: A Repository of NPM README Files

## Overview

### Purpose

I want to do text processing on existing READMEs online.
I'm interested in determining the relationship of these features of READMEs to package popularity:
the presence of concrete tasks, code examples, and a large amount of descriptive text.

### Summary

## Procedure

I use the [Libraries.IO API](https://libraries.io/api#project-search) to perform a search for packages on npmjs.
I save these to a local database.
For each one, I save whether it has a README.
For the top 1,000 packages, I fetch their README by using a `requests` call to Github.

For each of these READMEs, I use `Python-Markdown` and BeautifulSoup to count the number of preformatted code blocks.
I also use Treude et al.'s (2015) criteria for determining what language describes programming tasks.
I count the number of words in each text.
I count the number of links.
Using the Libraries.IO API, I collect the download count and star count.

The questions I will ask about the following single statistics:
For the top 1,000 Node packages:
* About how many words are in a README?
* About how many code blocks are in them?
* How many forks does each one have?
* How many contributors does each one have?

Then, regarding interactions between statistics:
* Is there a relationship between the number of words and the number of contributors?
* Is there a relationship between the number of code blocks and the number of contributors?
* Same questions, for the following pairs: (words, forks), (code blocks, forks) (words, stars), (code blocks, stars)
I answer each question in the space below

### Expected Outcome

There appears to be a linear relationship between the number of words in a README and a package's downloads.
There also appears to be a linear relationship between the number of code blocks in a README and the package's downloads.

## Notes

### Observations

#### Single Statistics

* Code blocks: There is a median of 0 code blocks in READMEs (mean=1.93, min=0, max=45)
* Words: There is a median of 599 words per README (mean=940, min=15, max=13,395)
* Forks: There is a median of 163 forks per package (mean=744, min=4, max=38,180)
* Contributions: There is a median of 42 contributions per package (mean=94, min=1, max=2,583)
* Stars: there is a median of 1,083 stars per package (mean=4,227, min=2, max=90,207)
* Open Issues: there is a median of 22 open issues per pacakge (mean=38, min=0, max=3,219)

At a glance, most of the measures occur according to a power distribution.
There does not seem to be strong relationships between the amount of code or words in a README and the stars or contributions for that project.
The only one that seems like it might have some relationship is stars vs. word count.
However, this might not be the case once we query all 200,000 projects and look at the long tail of unpopular projects.

### Errata

Some of these values are wrong.
When I visited the page for `mongoid`, I found that it has over 3,000 stars.
But the data that I'm exploring only has two stars for it.

### Technical Improvements

Additional data I should scrape includes:
* download count
* temporal data on contributors, forks, and downloads
* programming tasks in READMEs
* programming entities in READMEs
* the number of sections in a README
* the number of links in a README
* number of search results on that package in the top page of Google search results for that package name

### Research Ideas
 
Some cool questions that we can follow up on this with include:
How do the blocks and words of a README change over time?
What is the connection between words and followers / contributors over time?
