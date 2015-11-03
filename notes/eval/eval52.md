# Evaluation 52: What Programming "Primitives" Can Programmers Recall?

## Overview

### Purpose

Certain languages and programming tools are most appropriate for some programming tasks.
Programmers developing opportunistically seem to favor tools that match the task at hand (Brandt et al. 2008).
However, they have also been observed to avoid the use of external libraries the provide necessary functionality (Brandt et al. 2008).

Assuming there are situations where a programmer is deterred from using a language or new tool due to unfamiliarity, we are interested in these questions:

1. How much does a programmer know in their more "fluent" languages?
2. What mechanisms exist to allow them to transfer this knowledge to new tasks?
3. What are the tasks where a programmer would avoid doing a task due to unfamiliarity with a tool?

This evaluation addresses the first of these three questions.

### Summary

## Procedure

Participants are recruited from among student researchers at Berkeley.
For this preliminary study, we seek 8 participants altogether.
A participant is asked to bring their laptop.
Upon arriving, they are asked to pick their most familiar programming language.
If for some reason they don't have the standard libraries and runtime for that language on their computer, they are directed to [CodeChef](https://www.codechef.com/ide) to develop the code (assuming the language is pretty common).
Note that there are some tasks involving I/O that must be skipped when developing in the online IDE.

We ask participants to do the following tasks in this language without consulting outside references.
They should demonstrate that they know how to do the task by showing some result to the reviewer.

| No. | Task | Data | End Condition |
| --- | ---- | ---- | ------------- |
| 1 | Print string | "Hello world" | wrote out a print statement in the language |
| 2 | Execute code | | execute the print statement from the last step |
| 3 | Add two numbers | 2,5 | print sum |
| 4 | Make a list | 'a', 'b', 'c', 'd' | print list |
| 5 | Iterate through a list | see above | print each element on separate line |
| 6 | Replace a substring with another pattern | replace "an" → "ot" for string banana → botota) | print "botota" |
| 7 | Write a method that returns a value | return 11 | print returned value |
| 8 | Type a comment | "this is a comment" (though this value doesn't matter) | show the evaluator |
| 9 |  Read from a file | file text: "line 1\nline 2\nline 3" | print out file contents |

Programmers will be asked to generate the entirety of the code---e.g., without copying and pasting the structure that will add a 'main' to Java.
If needed, the experimenter can provide this knowledge by precisely reciting the syntax of the needed structure.
The experimenter should not provide any guidance on code directly related to the task.
If participants ask whether they should do more than what
If the programmer doesn't know how to do it, have them share what classes, primitives, and methods would be used.
Have them write this down in the comments.

The short list of these tasks for abbreviated trials is 1, 2, 4, 6, and 9.
Hopefully, this list of tasks could be asked over the course of 10 minutes.
This covers both very simple as well as fairly advanced tasks.

For each participant, we ask them additionally:
* About how often do you use this language?
* What is an advanced function in this language that you know of?
* How often do you use a new library to do a programming task?

The following information is recorded:
* the language the programmer chose
* whether they succeeded at each of the 9 tasks above
* participant responses to the follow-up questions
* (optional) video footage of the participant performing the coding, with audio from the microphone

#### Recruitment

The ultimate question is: how can I find people who have their computers, aren't busy, and are willing to help for 15 minutes?
I can ask the following people to help out:

##### The formal

Hi there!
I'm building an understanding of what programmers know about the languages they use.
I'd love to understand what you know about a programming language, so you could become part of a dataset of what programmers know.
While some researchers' tests take a while, this one is only around 15 minutes, basically the length of a coffee break.
Would you like to help out?

##### The informal

Hey!
Do you want to help out with a 15-minute study?
I'm collecting data on how people program.
The test comprises a few programming tasks.
Do you have time to contribute?

##### The e-mail

Subject: Want to help out with 15-minute investigation?
Body:
Hi Person,

I'm doing some lightning-style interviews to learn what people know about the programming languages they use.  Would you be interested in helping out by meeting up for 15 minutes, at a time you're with your computer?

If so, name a time and place in the next few days, and it would be great to meet up!

Andrew

##### People

* Chelsea Finn (ask on Tuesday)
* Mitar Milutinovic (ask on Friday)
* Noah Johnson (ask on Friday)
* Pablo Paredes (e-mail)
* Katie Head (e-mail)
* Christine Gregg (e-mail)
* Invention Lab people (visit)
* Ayush Kumar (e-mail)

###### By diversity

Short list

* Amy Pavel: human-computer interaction
* Ben Caulfield: verification
* Sarah Chasins: programming languages
* Manuel Sabin: theory
* Alex Hall: graphics
* Daniel Seita: data science
* Nathan Zhang: undergraduate
* Jess Hamrick: cognitive science
* Katie Head: accounting
* Christine Gregg: mechanical engineering
* Jeremy Faludi: sustainable design

Long list

* Christie Dierk: human-computer interaction
* Shiri Ginosar: computer vision
* Paul Pearce: security
* Chelsea Finn: robotics
* Adam Hutz: making

##### Places to find people

* Jacobs Institute of Design
* Invention Lab
* Lobby of SDH
* TGIF for the theory folks
* CSGSA Lounge
* Engineering library

I could also look for a diversity of people---the people I know across different disciplines.
Add a question: when did you last have to learn a new language?

Just visit the grad student lounge and look out for people who are eating lunch.
Visit the Invention Lab and ask for volunteers.

### Construction

The intended analysis will include focus on the questions:

* What proportion of programmers are capable of recalling the basic elements of code in a familiar language?
* Which programming tasks seem more difficult to recall the syntax for than others?
* What do programmers know when they don't know how to type something in the target language?

### Expected Outcome

I expect that it will take varying amounts of effort to recall code for each task.
I suspect that difficulty will increase from least to most in this order:

1. Print hello world
2. Add two numbers and assign the value to a third number
3. Type a comment
4. Print each element in a list
5. Execute code
6. Make a list
7. Write a method
8. Replace a substring with another pattern
9. Read from a file

I suspect that almost everyone knows how to print a message, though probably very few know how to perform tasks 8 or 9 without consulting programming help.

## Notes

### Observations

#### By subject

### Errata

### Technical Improvements

Other potential tasks include:
* Counting elements
* Summing numbers
* Deleting an item from a list
* print "Hello world"
* Do an assert statement
* Add two numbers
* Raise a number to  apower
* String replacement
* Make a class
* Structure code for reuse (DRY, e.g., make a method)
* Write a comment
* Execute the code
* Split a string
* Traverse a tree

### Research Ideas
 
For general purpose, libraries, everyone has their cache of go-to libraries and functions.
Some people may be great at file I/O.
Other people might be great at setting up a server.
Yet others may be able to run machine learning routines.
How could we string together groups of co-workers or strangers to allow everyone to program the libraries they are strong with, for others?

What are the social implications of opening up your computer to let others program your project for you, for your environment, from afar?
For example, if someone were to set up Stanford Parse on Katie's computer for executing in Python.
What would Katie have to trust about the helper?
And what would the helper need access to to make sure they can set things up properly?
