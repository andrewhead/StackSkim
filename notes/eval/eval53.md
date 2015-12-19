# Evaluation 53: Best features for clustering examples of programming primitives

## Overview

### Purpose

It may be possible to translate primitives from a source language to a target language by comparing semantically related code snippets from introductory documentation on the two languages.
See the vision in [Prototype 16](../proto/proto16).
I assume that code snippets from these documents may need to be reduced to the simplest possible formulation before being converted.
**What are the features that we can use to relate similar snippets to each other, so that we can perform these reductions?**

### Summary

## Procedure

### Fetching the corpus

First, we grab all code snippets for 10 beginner tutorial sites for Python.
We select the following tutorials.
These were feteched on Oct. 22, 2015 as the first 10 viable tutorials:
1. [A Beginner's Python Tutorial](http://sthurlow.com/python/)
2. [The Python Tutorial](https://docs.python.org/2/tutorial/index.html)
3. [Learn Python](http://www.learnpython.org/)
4. [Python tutorial](http://www.tutorialspoint.com/python/) ("Python Basic Tutorial" links)
5. [Learn Python the Hard Way](http://learnpythonthehardway.org/book/index.html)
6. [Hands-On Python Tutorial](http://anh.cs.luc.edu/python/hands-on/index26.html)
7. [How to Start Programming in Python](http://www.wikihow.com/Start-Programming-in-Python)
8. [Learn Python in 10 minutes](http://www.stavros.io/tutorials/python/)
9. [Programming for Teens: Beginning Python Tutorial](http://www.raywenderlich.com/62094/teens-python-tutorial)
10. [Introduction to Programming with Python](https://opentechschool.github.io/python-beginners/en/)

We use the following guidelines for selecting tutorials:
First, we pick only text tutorials (no video or Codecademy-style tutorials).
Second, we choose them from a Google search for "beginner python tutorial".
Third, we skip tutorials that look like duplicates (e.g., [this one](https://en.wikibooks.org/wiki/A_Beginner's_Python_Tutorial/Importing_Modules) after viewing the first one on the list above).
Fourth, we skip any tutorial that is explicitly designed to teach Python 3.

We automate this by doing the following:
* For each introduction site, we collect the URLs of all pages in the introductory tutorial
* Through manual inspection, we determine how to extract all formatted code snippets
* Using requests, we fetch each of these pages
* For each code snippet found, we save the following information for each snippet by traversing the DOM:
    * page title
    * page URL
    * page text (complete)
    * text that appears in the previous paragraph on the page (if not separated by another code or header)
    * text that appears in next paragraph on the page (if not separated by another code or header)
    * comments within the code
    * Nearest header above
    * Structure of parse tree
    * Lexemes
    * Number of lines

#### Extracting links to tutorial pages

1. Left-clicked and copied
2. `$('.toctree-l1 > a').each(function() {console.log("https://docs.python.org/2/tutorial/" + $(this).attr('href'));})`
3. Left-clicked and copied
4. `$('ul.nav-list:first-of-type a').each(function() {console.log($(this).attr('href'));})`
5. `$('div#table-of-contents ul.simple:first-of-type a').each(function() { console.log("http://learnpythonthehardway.org/book/" + $(this).attr('href')); })`
6. Just one page
7. Just one page
8. Just one page
9. Just one page
10. Left-clicked and copied

#### Choice of programming language

We select Python as it is easy to parse fragments of programs than in Java, which may require cleanup before parsing.

#### Choice of features

My intuition is that examples can be clustered according to the following: 
* bags of words for the paragraphs that occur before and after the example
* parse tree, minimizing the distance between trees in the same cluster
* bags of words of lexemes

However, I suspect that more than this may be relevant to suggesting the purpose of a code intent.
The following features may also be important:
* The web page's title
* The web page's URL
* The web page's full text
* The text that appears directly next to the example
* Comments that appear in the code snippet
* The nearest header that appears above the example
* The structure of the code's parse tree
* The relationships between nodes of certain types in the code's parse trees
* The lexemes found when lexing the snippet
* The number of lines in the example

We base this solely on inspecting this example [Java tutorial](http://javabeginnerstutorial.com/core-java-tutorial/variables-in-java/).

### Labeling

As our purpose is to discover how these features might suggest the purpose of the code example, we first determine what the purpose of each snippet is.
We make a best guess about the programming topic that the snippet it trying to teach.
We grow the available classes as we inspect each snippet, and end up with a set of classes based on what we've seen.
Example topics to include are (class definition, iterator, if statement).

### Inspection

I visually inspect the data for the fields for which it might be possible to see a connection between the field and the class label.
These fields include the page title, URL, nearest header, lexemes, text that appears above and below, and number of lines.
For each of these, 

#### SQLite queries

##### View the most common tokens

`SELECT string, c FROM (SELECT token_id, COUNT(token_id) as c FROM snippettoken GROUP BY token_id ORDER BY c DESC LIMIT 100) JOIN token ON token_id = id;`

##### View most common comments

`SELECT c, string FROM (SELECT comment_id, COUNT(*) as c FROM snippetcomment GROUP BY comment_id ORDER BY c DESC LIMIT 100) JOIN comment ON comment_id = id;`

##### View the pages with the most snippets

`SELECT location, COUNT(*) AS c FROM snippet JOIN page ON page_id == page.id GROUP BY location ORDER BY c DESC;`

##### Get the number of snippets from a page

`SELECT COUNT(*) FROM snippet JOIN page ON page_id == page.id WHERE location LIKE "%wikihow%";`

### Learning

We perform LDA to reduce the dimensionality of the textual entities to around 10 dimensions a piece.
Then we form a vector of features using:
* The reduced text above and below
* the reduced page text
* the reduced header text
* reduced counts of lexemes
* number of lines
* reduced comments

Then we perform leave-one-out ten-fold cross-validation to classify all snippets for one language using the data from all the others.

## Expected Outcome

We do not have enough data to make good predictions about the purpose of code from just the code.
However, by inspection, it seems like there is a relationship between the header directly above and the purpose of the code.

## Notes

### Observations

Data from running extraction on our test sources:
* For the "Learn Python the Hard Way" sources, it seems that we have difficulty extracting the text above and below the code examples.

### Errata

### Technical Improvements

### Research Ideas


