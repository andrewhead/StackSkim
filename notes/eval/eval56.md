# Evaluation 56: Steps to execute pieces of example code (Personal)

## Overview

### Purpose

There may be some great user interface addition to the web by making code examples executable and instantly testable.
What are the steps that a programmer usually has to follow to execute a piece of code found online on their machine?
Knowing these steps will inform the design of a system for making online code instantly testable.

The basic thesis of such an interface would be that a smart application may be able to tell better than a novice how code has to be altered in order to make it runnable.

### Summary

## Procedure

### Construction

I pick six tasks of things you can do with Python (based on recent experience).
Each of these tasks require at least three lines of code.

1. Optimize an equation with least-squares [(scipy)](http://docs.scipy.org/doc/scipy/reference/tutorial/optimize.html)
2. Perform face recognition [(user-run site)](http://hanzratech.in/2015/02/03/face-recognition-using-opencv.html)
3. Fit a Gaussian mixture model to code [(scikit-learn)](http://scikit-learn.org/stable/modules/generated/sklearn.mixture.GMM.html)
4. Run a server [(builtins)](https://docs.python.org/2/library/simplehttpserver.html)
5. Define and create a test model [(peewee)](http://docs.peewee-orm.com/en/latest/peewee/quickstart.html)
6. Build a UI [(python-textbok)](http://python-textbok.readthedocs.org/en/latest/Introduction_to_GUI_Programming.html)

For each tutorial, I create a new directory and a virtual environment to mimic the process of "starting fresh".
I try to copy and paste the minimal amount of code to get the example running in the first place.
I also do all of this programming in a file instead of the interactive terminal because, frankly, the code snippets are pretty big.
A user study could elicit whether people want to test these out in an interactive shell or a file.

For each of these tutorials, I record:
* raw video of my process getting the code to run (stored on BDrive "Evaluation 56" folder, at 4x speed)
* the names of files that I created
* a description of the resulting output (How did I know it was working?  UI?  Text?  Anything?)
* the names of packages that I had to install (with pip freeze)
* a description of the sequence of steps I took to get the code running
* a description of each of the bugs or transcription errors I encountered
* a list of several parameters I might want to change
* a list of the user-specified data I might want to run this on
* the time that it takes me to do this (though keep in mind, I've done most of these examples before)

### Expected Outcome

We find out that for these groups of tutorials, the types of output are highly diverse.
However, most of them have packages that can probably be Google'd based on the import statements.
Most of the code runs right off the bat in Python 2.7.
Only one of them (building the server) is appropriate to run without redefining parameters or data for personal use.

## Notes

### Observations

|Task|Time|Files|Output Type|Installed Packages|Bugs/Transcription Errors|Parameters|Data|
|-|-|-|-|-|-|-|-|
|1|23:36|`leastsq_test.py`, `frameworkpython`|stdout, graph|cycler, matplotlib, numpy, pyparsing, python-dateutil, pytz, scipy, six|interactive shell junk needed to be deleted, bad formatting, matplotlib couldn't display from virtual environment, PySide stalled at downloading, set Python path in frameworkpython script, chmod +x on frameworkpython|Fit a different function, alter sine parameters, initial parameter values, amount of noise||
|2|8:01|`face_recognizer.py`, `haarcascade....xml`, `yalefaces/*` (166 files)|stdout,show images|cv2|scan source for malicious code, set path to existing OpenCV distro '*.so' (needs OpenCV installation)|type of classifier, image names, image mode to convert to, face window||
|3|8:50|`gmm_test.py`|stdout|numpy, scikit-learn, scipy|strip out interactive shell artifacts (>>>, ...), reformat with nice whitespace, remove output, space operators, missing numpy and scipy installations, add print statements for introspection, compare results to those published, alter random seed to see if I can make sense of disparity, compare versions of scikit-learn|number of components, number of random points, points to predict||
|4|1:10|`server_test.py`|web server (file browser)||none|host, port||
|5|5:35|`people.db`, `test_model.py`|stdout|peewee|strip out interactive shell prompts, table not created (missing code), ordering problems (Person not defined, then db not defined), looking up how to verify a property on a new record, table already exists on multiple runs of the program|name of database, parameters for created and fetched record||
|6|1:56|`ui_test.py`|stdout,UI|none|no module found for tkinter (due to different Python versions), lookup to pypi failed (it's a default library, but under a different name)|button labels, window name|_|

#### Task 1

The 23:36 task time for task 1 was ludicrous.
Most of this was because I was taking time to run matplotlib within a virtual environment.

#### Task 2

Again, there was a virtualenv problem that took a few minutes to get opencv running within a virtual environment.
Steps that I had to follow was:
1. Skimming the expository text on the page and **looking for runnable source code**
2. Skimming the downloaded source code to make sure that it didn't have any fishy lines
3. Installing the dependencies
4. Properly linking to the dependencies
5. Running the source code

For this task, I didn't attempt to run any of the blocks of code that were on the webpage itself.
It simply did not seem like the most efficient way to test the code, as it was so fragmented.
It might be worth trying this a second time, where I attempt to assemble the code from its pieces on the page.

#### Task 3

We could not reproduce exactly the results that it took to run the code.
One reason for this is that the random number generator may seed differently on different machines.
The tasks in getting this code in reusable form included:
1. Copying and pasting the code
2. Removing junk characters at the beginning of newlines
3. Breaking up the code into semantically meaningful units for better reading
4. Deleting the inline output
5. Adding print statements to reveal the results
6. Comparing the output to that which appeared in the tutorial

#### Task 4

Nothing to report here.
This was a very easy copy-paste-run job!
Though admittedly, I did know how to test it with the browser.
Note that many of these cool tutorials don't have straightforward output.
It's something like "see the graph that gets built" or "note that a server is now running"

#### Task 5

The steps I had to follow were:
1. Copy the first piece of code over and lean it up
2. Copy over the dependency chunks of code
3. Install the packages
4. Look for additional background about the current variables used (db)
5. Rearrange the code so dependencies were run in the right order
6. Fix bug with tables getting created twice by looking up API docs
7. Add a print hook so that I knew that the code was running correctly

#### Task 6

This one was straightforward, except that tkinter has a different name in Python 3 vs. Python 2.
I found an extra piece of help on StackOverflow that described how the name was different.
So I changed the name, and it all appeared to work fine.

#### Testing Procedures

##### Task 1

Note that I took a break from 15:29-20:45 to try and let PySide install.

### Errata

### Technical Improvements

There are some tasks (like running a server) for which it's hard to think of representing them running in an interpreter.
How can we make it so that these tasks *can* be shown sensibly from an online interpreter?

The Peewee example demonstrates something:
* We may want to combine multiple code examples on a page into one test
* We may want to *test* the code on the page rapidly with many different configurations before importing it into the IDE.  The integration effort can be quite high (to get the dependencies installed into your own code, and to write tests), so it's worth it to test before deciding.
* One big challenge of this system (as well as any old tutorial or code snippet) is providing introspection.  This is why writing unit tests can be hard.  It's not evident what can be monitored to cross-check that the execution went correctly.  Or, it may require a different paradigm than what we're used to, for example launching a viewer for a SQLite database.

The face recognition example I inspect demonstrates something else:
* People may want to try out their own data
* Probably, the interpreter should run in the author's version of Python and software packages (maybe an authoring tool should upload this info)
* It would be great to test out the code in the reader's version of Python before exporting

### Research Ideas

A key insight of this work is that when programmers look at example code, **they shop**.
Currently, online example code that is not executable forces them to **commit**.
Overlays can be added to the web to bring back the "shopping" nature of looking at example code, and make it runnable and testable.

An upcoming demo would probably include:
* combining multiple snippets together
* saving past configurations in a table-like form to know whether the code does what you want

Observational studies focused on feasibility assessments could us understand how programmers test code to make sure it will work for their application.

Questions that Marti &amp; Bjoern may ask are, if the point of this study is observational, then why not just keep it at observational?
The answer is that by working with code and examples, I suspect we can dive more deeply into the structure of executable code.
This can inform what features are present to allow us to make some better search interface in the future, or detect the problems that programmers may want to have addressed through a batch of Tutorons.
In other words, by working with code examples, we can better understand what *can* be explained about online code.

There may be work to do in just connecting the right existing user interfaces to make the testing and transfer of code much faster and easier.
