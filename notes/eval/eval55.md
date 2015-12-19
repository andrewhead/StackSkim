# Evaluation 55: Programmers' Information Needs

## Overview

### Purpose

Programmers have many information needs, and often rely heavily on external knowledge when writing, refining, and using code.
How could we bring this information to programmers at lower cost?
In this study, we elicit:
* what information needs do programmers have, of various sizes?
* how far do they travel (e.g., within page, start a search, inspect code) to satisfy these needs?
* what information do they ultimately use to satisfy these needs?

<!--
This exploratory evaluation looks to understand the difficulties programmers have in locating and using online help.
In addition, we hope that we can elicit some idea of the severity of these difficulties.
For example, how long does it take for a person to rework copied code so that it runs?
How many pages does a programmer look at before they find a relevant piece of code or a relevant document to learn from?
How often do they encounter bugs or fail to understand what the code actually does?
What epiphanies occur and what information do they need to see in order to get this epiphany?
-->

### Summary

## Procedure

### Participants

There are two contexts I'm interested in studying:
1. programmers working with new languages, libraries, tasks, and technologies in general
2. programmers performing everyday work

An interesting observation is that programmers may have different information needs and satisfy those needs in different ways if they are working on a completely new task, or with a completely new library, as opposed to working with familiar technology and tasks.

For this study, I focus on the former.
First, because this is good practice for arranging contexts where programmers are working with new tasks or technologies.
Second, because I expect that the density of information need will be much higher for programmers working with new tasks or technologies.
The primary challenge of this context is in being sure that all of the requisite software and equipment is available to do finish or at least progress on the task in a timely manner (if this is a software *or* software/hardware project).
The second is making sure that enough progress can be made on the project over the course of the study to make sure that all the data collected isn't just related to getting a new programming language or environment set up on one's computer.
A third challenge is that it will be difficult to compare the results that we view for the different programmers.

To address these challenges, I propose the following:
For the first challenge, one option would be to work with the programmer to iterate on 3 revisions of a project idea before we meet (although how programmers develop this would be, in its own right, an interesting project—see the "Research Ideas" section below).
Another option would be to provide participants with a list of possible projects they could take on.
This could be 5-10 projects with a variety of different languages, all something that a person might want to do on their own—for example:
* make a personal website with an image of yourself and a written bio and test it out locally
* make a virtual piano keyboard that plays musical notes as you click on keys
* make a game where you are racing to get to class
* write a piece of software that will count the number of faces that it finds in an input image
* make an art program
Participants could be given a $20 gift card if they participate, and a $30 gift card if they successfully finish the study in time.
One confound to avoid here is that people's development spirit may be different from their typical behavior (which for some may just be more relaxed) if they are encouraged to be speedy.
They should be given some set of conditions for each project where it is finished, so that they don't stop prematurely.
Another confound is that people may not be as motivated to work on these preset tasks compared to tasks of their choosing.
But if we choose a wide enough expanse, then we're likely to get one or two projects to satisfy each type of person.
It's also important to decouple art from design here.
Participants should be encouraged to make small designs to help motivate them, but should not spend more than 10% of their time on the project designing aesthetics or interactions, so that most of the study time can be spent programming and looking for code.

I find programmers from several different groups:
* upper-class computer science students
* game programmers making games for fun
* middle-aged folks just learning how to code for fun

We recruit them through these means:
* E-mails to the CS160 student mailing list
* Visit and personal pitch to a beginner programmer's startup in Berkeley
* Visit and personal pitch to a Meetup at an Oakland hackerspace

### Tasks

I ask participants to set aside 90-120 minutes.
Beforehand, I ask them to pick a personal project that they want to work on that involves a library they haven't used before.
Then they try to get it done!
After two hours have past, they're allowed to keep going, though they won't receive any extra compensation.
At three hours, I cut them off and they can work no more.

### Measures

I ask participants if I can get a screen recording of their participation.
They are also welcome to use my computer for the sake of this study, but they can also use their own.

During the study, I note the following events:
Related to search behavior:
* Defining an information need (making a query)
* Revising the statement of an information need (revising a query)
* Abandoning a search
* Open search result event
* Visit page from URL event
* Scroll location within the site
* Within-site navigation event

Related to code reuse:
* Fixation on a code example
* Manual entry of code found online
* Copy-and-paste of code
* Revisiting the text surrounding the code
* Inspecting reused code
* Reused code revision
* Returning to an abandoned page

After the study, we answer our original questions:
* For each query, how many times was the query refined and how often was the search abandoned?
* How many results were viewed for each query?
* On pages with multiple examples of code, how many pieces of code did they fixate on?
* When they fixated on code examples, what rationale did the programmer have for fixating vs. moving on?
* How often did users copy and paste code off the Internet?
* How many times did they make and test a revision to a piece of reused code?
* How often did users return to an abandoned page (i.e. one that was deemed irrelevant when a programmer decided to refine the query or view another search result?)

### Things to Keep in Mind

Python documentation across the web seems to be pretty strong.
JavaScript seems to be getting stronger every day.
Java documentation is still difficult to get through and understand, in part because there's so much syntactic overhead needed to write simple lines of code, or systems administration work needed to set up an environment to run.

Asking participants to think aloud may influence how they solve problems.
I wonder if there has been any research on this.

### Expected Outcome

## Notes

### Observations

### Errata

### Technical Improvements

### Research Ideas

What if what we really need to enable is within-code and within-tutorial search, rather than across-document search?
Maybe what people really need is not better access to full documents, but better access to the relevant atoms of information that come from these documents, split up into more easy-to-process chunks.

Marti is interested in developing an understanding of when people want automatic annotations.
One thing that we could do in this study is determine all of they types of questions that programmers ask (i.e. all of the information they need to access) when implementing something new.
Then we can decide for each information need whether those explanations could be sourced from another dataset or generated.

What are programmers' information needs when figuring out the feasibility of a new project?
How often do programmers actually choose to do feasibility analysis?
How often do they assume that the right code is already there, as long as they make the right query?
And how often is that code actually there?
Do end user programmers have any idea on how to do an effective feasibility analysis?
