# Vision 2: Abstracts Going Forward

## Round 2

In brief, the ideas are:
* A sampler for building augmented code examples with lists of suggestions
* Interface for slicing and cleaning up production code to make usable online code examples
* Sounds that describe code quality, for number of downloads, number of unit tests, number of collaborators
* An interface that re-crafts explanations based on perceived personality
* Manipulable bits for learning what a snippet does by manipulating it and seeing usage examples update
* A single-button compiler of notebooks into reusable modules

### Prose

#### Snippet Buffet: A Menu for Selecting and Understanding Parameters for Online Code Examples

When programmers reuse example code for unfamiliar APIs, the cost of accessing relevant documentation is often too high.
This encourages programmers to engage in trial and error to discover the right parameter values.
We propose that the recent availability of high-quality code examples online makes it possible to embed parameter recommendations and demonstrations of code right next to the example.
To test out this idea, we built Snippet Buffet.
Snippet Buffet provides an overlay for arbitrary online code examples, including a menu of parameters often used for that function, and automatic demonstrations of the code's output to enable rapid discovery of the right parameters.
We build the Buffet to enable rapid construction of SQL 'WHERE' expressions, use of Python built-ins, and visual modification of calls to a graphing API.
Through an in-lab study, we demonstrate that programmers can test out more parameter assignments in the same time, and adapt code faster when using Snippet Buffet.

<!--Common usage is elicited by scanning calls to the API from StackOverflow and other beginner's tutorials.
The interface comprises of a menu system and automatic code previews, and can be extended to the IDE.
We show the system's utility for editing code found for plotting and CSS selectors.-->
<!--Such a data-driven approach can be used to suggest more concise semantic equivalents, arguments that should be used together, and other packages that can either complement or replace the desired functionality.-->

#### Examplify: An Interface for Reshaping Production Code into Publishable Examples

*Stolen from the thought collection of Bjoern Hartmann.*

Many programming libraries never see widespread adoption because they lack reliable usage examples.
Reducing the cost of publishing code examples from code that one has already written could improve the usability of early-stage or obscure programming libraries.
We present Examplify, an IDE plugin that reduces the cost of programmers preparing arbitrary slices of personal code as lightweight, reusable, and understandable examples.
With a preliminary study over thousands of code examples, we elicit what makes a parse tree for production code different from that for an effective online example code.
We instantiate this knowledge in an authoring tool, Examplify.
After programmers select a slice of code, Examplify reduces the code to a draft of a code example by pruning unimportant subtrees from the parse tree and substituting readable variable names.
It then enables a programmer to revise this code, and to augment the example with textual descriptions and unit tests taken from their own code.
We show that it takes programmers less time to build example code with Examplify, and that these examples are rated as more readable and reusable than examples developed without it.

<!--We present techniques for detection of semantically relevant lines of code and detecting prunable subtrees of production code parse trees.-->
<!--Today, programmers wait for a question before publishing code, and clean up their own code, and may make mistakes publishing this code.-->

#### Using Ambient Media to Encourage Responsible Selection and Reuse of Online Code

When in a hurry, programmers are unlikely to inspect the reliability and quality of third-party libraries and online code examples that they integrate into their own code.
This can lead in debugging problems or security vulnerabilities when this code becomes a forgotten piece of a larger project.
We propose augmenting the interfaces programmers use with ambient media to inspire responsible selection and reuse of code found online when online web pages fail to indicate the reliability of found code.
We believe that ambient media can be a visceral, straightforward indicator of software safety.
We design and present a mapping of features of software packages, code examples, and pasted code to audio cues to imply the safety of libraries and examples found in the browser, and the current test coverage of pasted code within the IDE.
We explore how this impacts programmers' behavior in finding and reusing online code.
<!--With our system, users are influenced to select reliable, well-tested third-party libraries on the web, and to provide proper coverage of copied code through unit tests.-->
Through an in-lab study focused on programming activities, we observe that programmers navigating online resources with ambient media write higher quality code and tests, and use more popular software packages.

<!--We believe that for programmers finding libraries for the first time, this could inspire the use of popular, well-supported online examples, and -->
<!--We describe which form of ambient media (sound vs. visuals) is most likely to influence the decisions programmers make when selecting third-party code and writing test coverage.-->
<!--The appropriate ambient media that can be used to convey safety of a piece of example code.-->

#### A Notebook for the Scientist and the Engineer: Supporting Code Reuse and Version Control in Live Programming Notebooks

Today's live programming notebooks offer visual representation and effective storytelling with data at the expense of code reusability and detailed history.
As a result, intermediate results are often lost without being committed.
Exporting the notebook into discrete modules for reuse is difficult, as definitions of data and operations on that data are scattered through the notebook.
We propose augmentations to the programming notebook that integrate the benefits of version control and modular programming into the notebook, to enable both replicability of results and extensibility of the code built.
Through preliminary interviews, we elicit the missing affordances of notebooks based on interviews with academics.
We propose and instantiate interactions and techniques for integrating version control, code slicing, and refactoring code from the notebook into reusable code and accompanying tests.
Though an in-lab study, we find that programmers using our augmented notebook produce higher quality modules for reuse of notebook code, as judged by programming experts, and do so in significantly less time.
<!--There is no easy way to convert a block of code into a module that can be used by other notebooks.-->
<!--Improve the ability for others to reuse code already built as reusable modules where new data can be plugged in.-->

### Lists

#### Snippet Buffet: Building on Found Code with Automatic Parameter Recommendations

Problem: Cost of looking up related arguments is high
Solution Impact: Better plot graphics.  More likely to use options that secure the code.  10x improved adoption of best practices.
Current Approach: Tutorials describe precisely the right options.  Everyone has different opinions.  Tradeoff between conciseness and completeness.
Current Neglect: Material need not appear in the page itself, and can easily appear adaptively and on-demand.
Body Neglect: Leveraging large numbers of code examples online to inspire the discovery of this in a data-driven way.
Solution: Tutorial mining, embedded in menu system and automatic code previews.  Can be extended to the IDE
Construction: StackOverflow, and other beginner tutorials, for python, matplotlib, CSS selectors
Evaluation: Ask programmers to update code for a graph based on an example.  See if it has what they want, and when it doesn't
Materials: May need to start making databases of arguments frequently-used.  Better hardware?
Man-Months: 1 month prototype and pilot.  2 month build-out.  1 month evaluation and write-up.

Types of improvements can include: more concise semantic equivalents, arguments that should be used, other packages that should be used together.

#### Just for You: Automatic Code Help to Suit a Variety of Personalities

Problem: Programmers get discouraged when solving problems and should be guided to use the right problem-solving strategies as beginners.
Solution Impact: Programmers working with online learn-to-program systems have a reduced attrition rate of 50%.
Current Approach: Static help file providing tips.  Hand-written help for CoScripter and Gidget that is tedious to write.
Current Neglect: Automatic generation of code to support a variety of personality types.
Body Neglect: Grammatical understanding of what makes supportive, productive help and instantiation within a program that can create it.
Solution: Code for automatically generating hints that can expand and contract, that pin the blame on the computer, and give vague advice.
Construction: Personality-based detection from Facebook profile of one's background, influences the help that they see.  Using Wordnet, look for advice that refers to the concepts used, but under different names.
Evaluation: Have programers learn from Gidget.  Compare against Idea Garden baseline.  Ask about relevance of the suggestions given.
Materials: Gidget source code.  Should collaborate with Margaret and Mike.
Man-Months: 1 month reading up on best practices for giving effective help.  1 month examples of help generated.  2 months system building.  1 month evaluation and write-up.

#### Examplify: A Tool for Publishing Slices of Production Code as Instructive, Concise Examples

This one was originally Bjoern Hartmann's idea, which was stolen due to its thematic relevance to our work so far.

Problem: Programmers work with examples, but many useful libraries lack easy-to-follow usage examples
Solution Impact: More widespread adoption of early-stage or obscure libraries
Current Approach: Programmers wait for a question before publishing code, and clean up their own code.  They may even make mistakes in the process.
Current Neglect: Low-cost production of snippet code to enable greater reuse
Body Neglect: Technical investigation of the complexity of code examples, of the ideal size, and how to reduce the code
Solution: A plugin for coding that recommends when and what you publish, and prepares a snippet version of your example for later cleanup
Construction: Automatic detection of semantically meaningful units using Sridhara et al. techniques.  Tree comparison, and learning of prunable features from production code as it is reduced.  Packaging into a reusable module too, using simple encapsulation.
Evaluation: Show that it takes less time for programmers to use this tool than to reduce on their own, and that the examples are easier to comprehend
Materials: Programmers with their own source code
Man-Months: 1 month statistics on the profile of common code snippets.  1 month reduction algorithm.  2 months prototyping and building the editor.  1 month write-up.

#### Ambient Media and its Impact on Safe and Responsible Navigation and Reuse of Online Code

Problem: Programmers frequently reuse code, but often without inspection
Solution Impact: 10x improved comprehension of code, to ease debugging later.  Greater use of popular community-maintained code
Current Approach: Curating collections of code, generating explanations of code, static guidelines about secure reuse
Current Neglect: Ambient media's role as a visceral, straightforward indicator of safety for novices
Body Neglect: The appropriate ambient media that can be used to convey safety of browsing
Solution: Suite of software package and code copying metrics to effective audio cues that impact behavior change
Construction: Code triangulation tools to tell what has been tested and what hasn't.  Page scraping with a browser plugin to understand the number of downloads, or counting votes on StackOverflow.  Play a sound using built-in utilities of browser and elsewhere.
Evaluation: Have programmers reuse code from a custom package explorer interface we provide.  Observe the packages they select.  Also, examine the quality of the code and test coverage they produce.
Materials: Custom sounds mixed.
Man-Months: 3 weeks for a simple prototype for package manager, 2 weeks for Eclipse code coverage.  1 month build-out, 2 weeks evaluation.  1 month write-up and follow-up.

#### Supporting the Scientist Engineer: Building Seamless Transitions between the Notebook and Code Modules

Problem: Programmers want to modularize and reuse code from notebooks in other notebooks, and maintain consistency, but there is no easy way to get the benefits of both determinism of the notebook (execution order) and precompiled modules.  Definitions of data and operations on it are scattered throughout the notebook, so there is no one central interface.  It's also difficult to commit intermediate experimental results.
Solution Impact: Easier transition of experimental code to reusable modules.  Improve the ability for others to reuse code already built as reusable modules where new data can be plugged in.  Replicable experimental results.
Current Approach: Jupyter.  All code is in a block, and once it's overwritten, it's gone.  Code migrated has to be copied and pasted to a new file.
Current Neglect: Integration of version management, and getting code ready for reuse.
Body Neglect: Description of the affordances of both interaction patterns (module-based and notebook-based).  An understanding of the steps a programmer follows to port an code from a notebook into a script.
Solution: Interactions for the notebook for compiling into reusable scripts and tests, configuration control for intermediate experiments.
Construction: Tests can probably be formed based on the output that comes out.
Evaluation: Have programmers make code reusable.  Document the problems beforehand.  Measure programmers' ability to make good-looking modules as judged by programming experts
Materials: Jupyter source code (can be obtained)
Man-Months: 3 weeks of observation and reading about notebook-style code execution.  1 month prototype and pilot.  2 months deeper implementation.  1 month evaluation and write-up.

## Round 1

### End User Programming Outsourcing

### Finding the Right Programming Examples in Large Example Spaces

#### Outline

Problem: 
Teachers frequently use examples to demonstrate the behavior of code.
Programmers also read and copy source code from examples when programming opportunistically.
It's not always clear that code will do what someone expects.
This results in manually integrating code to learn whether it will do what is expected.

Solution Impact:
Decreasing the number of edit-debug cycles programmers need (by reducing the number of examples that need to be heavily edited to use).
Less triaged functionality that is left behind as irrelevant.

Current Approach:


Current Neglect:

Body Neglect: 

Solution:

Construction:

Evaluation:

Materials:

Man-Months:

### CodeConv: A Use-Anywhere Converted of Programming Syntax

#### Outline

Problem:
Those programming opportunistically are trying to do it extremely rapidly.


Solution Impact:   
Current Approach:   
Current Neglect:   
Body Neglect:   
Solution:   
Construction:   
Evaluation:   
Materials:   
Man-Months: 

Alternate names: OtherLang

#### Details

For CodeConv there are two elements that are necessary:
* generating the code and
* modifying the code for special cases after the fact. Maybe you need to convert back and forth between the two languages

### Markup Communities: Reasons and Roles for Communal Markup of Coding Examples

#### Outline

Problem:   
Solution Impact:   
Current Approach:   
Current Neglect:   
Body Neglect:   
Solution:   
Construction:   
Evaluation:   
Materials:   
Man-Months: 

### Tutorons Gone Online: Usability in an Online Textbook

### Generating Example Code from Production Code

### Show Me Everything: What Kind of In-Situ Support on the Web Would Programmers Like?

### Hold Up: A Code Reuse Addon That Ask Questions About What You Reuse

### Template

#### Outline

Problem: 

Solution Impact:

Current Approach:

Current Neglect:

Body Neglect: 

Solution:

Construction:

Evaluation:

Materials:

Man-Months:

