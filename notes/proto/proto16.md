# Prototype 16: Convert between languages using Online Example Code

## Overview

### Purpose

How could crowd documentation improve our ability to convert between two languages?
We build a prototype that suggests that queries of the right type can allow us to connect source code examples with similar semantics from different programming languages.

### Summary

The description of this prototype grew too much, so it is now split into the following notes:
* [Evaluation 53](../eval/eval53).  This one is about finding the right features for clustering examples.

## Procedure

### Brainstorming

#### Technical techniques for querying code from one language with code from another

* Search engine loaded with N top examples from StackOverflow
* Look for overlapping English language in explanations of StackOverflow examples
* Reduce parse trees for collections of similar code examples to a canonical one to de-noise the matching
* Inspect comments accompanying code on Github
* Overlap of variable names between the examples
* Overlap of function names between the examples
* Use Google to find a similar example with high (TF/IDF) terms from the source example
* Compare the trees between the two languages, with some rules for how nodes of different languages line up
* Dissect beginner's tutorials to associate headings, nearby text (weighted as it extends outwards) to code examples
* Focus on introductory O'Reilly books as the beginner's tutorials
* Scrape pages that describe programming languages in terms of libraries for other programming languages (see Additional Solutions section)

Dissecting beginner's tutorials has the advantages that: code is likely to run, and cover many basic use cases of a language

### Preliminary Prototypes

We may be able to let StackOverflow do the heavy lifting through a Wizard-of-Oz type of action.

One thing that we could do is the following:
1. Search for questions using a chunk of code from a language
2. Pass the name of the question along with a tag for another language into the StackOverflow engine
3. Show a sample of all code that is received back

An alternate prototype idea is as follows:

A programmer composes a query.
This query indexes into code examples from tutorials and StackOverflow.
The top N queries are returned.
For each answer, similar to explainshell, we scrape the existing reference documentation for a language to describe lexemes in place.
This allows a programmer to select the most relevant code example from the list by attempting to understand its usage.
Essentially, the insight here is that reference documentation often follows predictable patterns.
Probably by programming by demonstration, we can identify which elements on a page are styled in the way of the code.
Then, if the tutorials help pages follow the form of:
* show the syntax of a signature
* describe the lexemes one by one
these elements could pretty easily be extracted from the tutorial after some demonstration.
Then this could be served up in help that helps programmers to choose a code example, with synthesized documentation.
These synthesized explanations also might be of the flavor that Sridhara et al. produced.

#### Prototype Proposal: Mining Common Usage from Online Tutorials

Here is a pipeline for converting code between languages:

##### Preparation: Developing the Corpus

First, we mark all code snippets for 10 beginner tutorials for two languages.
We find these by typing in the query "beginner tutorial <language>" on Google.
We focus on the Java and Python languages.
For each one, we include the paragraph before and the paragraph after.

##### Clustering examples

Code examples can clustered according to several different metrics.
We therefore cluster according to each of these separately:
* bags of words for the paragraphs that occur before and after the example
* parse tree, minimizing the distance between trees in the same cluster
* bags of words of lexemes

As a sanity check, we inspect the clusters that we form in these two different ways.
In this step, we verify that programs clustered together indeed appear to share some theme.
For example, one cluster may represent the introduction of for loops.
We print out the programs and surrouding text to verify the quality of clustering.

###### Alternate means of clustering

After inspecting several examples [like this one](http://javabeginnerstutorial.com/core-java-tutorial/variables-in-java/), we recognize that there are a few different features that may indicate the intent of a code snippet:
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

With a sufficiently large number of examples, we could use machine learning to determine which of these features remain the same across many examples with the same intent, marked as a class.
In this case, we would describe an 'invalid' class as one that is too large to be a coherent snippet

##### Translating a language

Finally, when we make a query in one language, we select the tree with the nearest edit distance in the source language.
We then select the cluster associated with that tree, and retrieve the words from the nearby paragraphs.
We match this bag of words to the closest one from the target tree.
We then show a single tree that is the minimum distance to all other trees from the target cluster.

### Experiments

#### Trying to fetch a semantic meaning of code through a StackOverflow search

Some initial examples that I looked up don't seem to be very promising.
StackOverflow doesn't seem to be very good at determining concepts through the questions or accompanying text when you provide a piece of code as a search query.
As an example, see the search results for these queries:

Defining a class:

    class MyClass(object):  def __init__(self): pass

Iterating through a list:

    for i in list_: print i [python]

List comprhension:

    "a for a in list_" [python]"

These concepts just don't come up mentioned as a focus in the top most relevant answers for these queries with the StackOverflow search engine.

#### Trying to find canonical examples on StackOverflow for elementary components of Python programs

Unfortunately, StackOverflow doesn't seem to be great for describing how to build pretty elementary structures.
For example, for the query "iterate over a list [python]", we find the results [here](http://stackoverflow.com/search?q=iterate+over+a+list+[python]).
The top answers are:

* What does the yield keyword do in Python?
* What is the most "pythonic" way to iterate over a list of chunks?
* Iterate over a list indexes
* Iterate over a list in a class

Note that none of these are simply just called "iterate over a list"---likely there's a lot of extra baggage in the code that can be extracted.
(*However*, consider that perhaps by looking for the most common programming nodes across all of these examples, the greatest common node may be the one that demonstrates how to do that skill.)

### Expected Outcome

For the study of converting via tutorial code examples, we expect that:
* clusters of trees will be coherent (with 70% consistency within-cluster)
* conversion to the target language will result in a snippet that needs to be generalized
* there will be one or two distinct high-frequency textual words that accompany each cluster

## Notes

### Observations

#### Developing the corpus

Unexpected markup of the tutorials included:
* Some code examples simply don't have a lot of text above or beneath them.
For example, [this tutorial](http://javabeginnerstutorial.com/core-java-tutorial/java-basicsgetting-started-with-java/) has a few examples where there is nothing but a heading or the word "Or" either above or below the code example.
Also see [this page](http://javabeginnerstutorial.com/core-java-tutorial/variables-in-java/), where there is no text directly beneath the code example, but only a header that leads into another section.

##### Resulting hypotheses

1. Code covering a similar topic or task will appear on the same page.  Different tasks will appear on different pages.

#### How `howdoi` works

`howdoi` is a utility for fetching code examples for how to perform a programming task.
It source is [here](https://github.com/gleitz/howdoi).
Above, we observed that StackOverflow search doesn't seem to be very good about finding relevant code examples for very simple tasks.
`howdoi` solves this with the following workflow:

* Use Google to search StackOverflow (presumably because Google is better at indexing based on queries for simple tasks)
* Get the first StackOverflow post returned
* Get the code from the first answer for this post, and print it to the terminal

This works out pretty well, and maybe we can similarly use Google to find related code examples.

### Technical Improvements

### Research Ideas

Karaivanov et al. (2014) write about machine translation of source code between C# and Java.
The way they match source and target sentences for training is by using heuristics like matching the names and arguments for the functions.
However, this is really a way to match functions between different languages.
How can we learn source-target correspondences without method signatures, but only provided with large amounts of code for each language?

An approach like that used for "explainshell" may help.
We could run NLP on entry-level programming docs for a language or API documentation.
Code could be matched through parse tree similarity to code examples extracted from docs.
Description could be found from the surrounding text.
This is used to find new descriptions in another language.
Code examples can be extracted from alongside those new descriptions.

What are the fundamental elements of meaning and code that can be extracted from a tutorial page

#### Additional Solutions

Some languages have "starting to use this language if you're already a programmer" guides.  See [this official one for Python](https://wiki.python.org/moin/MovingToPythonFromOtherLanguages).  

Also see this guide for [understanding Python if you're a Java developer](http://antrix.net/static/pages/python-for-java/online/) for inspiration.
A few of the features that seem to be pretty handy are:

* quick comparisons of the history between the two languages
* descriptions of differences in the compiled file formats
* clarification of the runtime executable command for each one
* list of the development environments for each one (which developers may want to know if they want to keep on their way)
* comparison of Java classes to Python object declarations (see [here](http://antrix.net/static/pages/python-for-java/online/#collections))
