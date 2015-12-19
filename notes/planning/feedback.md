# Feedback from Peers on Tutorons

## 2015-12-15: Meetup with Matthew

* Brainstorming about Python explanations
    * Some things like `sort` and `sorted` deserve to be described with a comparative example
    * Could be great to have Tutoron inception: nested explanations
    * Could be nice to describe arguments passed to a call
        * How difficult would it be to trace the data path to a definition?

## 2015-12-9: Chat with Tom Yeh

* Not everything meaningful is a CHI paper.  We should respect people who do non-CHI work that is meaningful.
* Consider a plugin architecture like that of hexo in JavaScript for making Tutorons easy to program
* It's surprising that no one has yet mined JavaScript to get some ideas of what to do with it.
    * A study might be interested in understanding how packages change with changes to major and minor versions
* Consider focusing on a more concrete user group (for example, Tom's wife the psychology researcher)

## 2015-12-8: Checkin with Marti

* A vision for the Internet where people know what to write
    * What are the missing links in software packages?
    * Some overview articles for tools or combinations of tools just haven't been written
    * Tutorial authors may be interested in writing about such topics to gain viewership
* How can we suggest what tutorials to write?
    * Crowdsource opinions: what are the things that you've wanted to learn but couldn't find a good resource for?
        * Marti, for example, would ask for a tutorial on pandas
        * "What are the things that you're looking for but never finding"
    * For now, start monitoring sites to get an idea of how viewership changes over time for popular topics.  How long does it take for posts to get traffic?
* A cool idea for a controlled experiment
    * Measure dwell time and time spent on a tutorial
    * Release tutorials on both popular and not-popular topics.  See which gets better long-term viewership

## 2015-12-1: Checkin with Marti

* Tutorials are special for programmers in that documentation was not as easy to read, pervasive, or timely before them
* Let's keep working at the pace of reading and exploring the theory

## 2015-11-30: Thoughts on the Walk from Home

* Forgotten Insights: the valuable knowledge that programmers never store or share
    * A study: watch developers work.  Log their problems.  After they're finished, how many of their insights and solutions can they recall?
    * A tool: the Scrapyard.  Everyone dumps any old thoughts that they had but that they don't want to think about how to share.  Searchable by queries.  Can flip through both specific and generic knowledge.  Others (crowdsourced workers) can categorize the knowledge.
    * A study: when do developers talk about their insights?  Over lunch?  Over e-mail?  How do you connect this back into the source?
    * A study: when can you elicit insights from developers that wouldn't break flow?  Through AR on the way home?  Through conversation at lunch?
* By the way, what is the best place to show these insights and solutions?  How about an overlay over source?

## 2015-11-30: Brainstorming with Bjoern

* Keep Bjoern and Marti in the loop
    * Keep reading.  Summarize the work that I've found.  Share with them.  They probably haven't read it yet.
* Think about Mira's TAPs, but apply it to programming
    * A tutorial that people can experiment on their own data.  For example, face detection tethered to a live stream from your webcam
* One question---StackOverflow is awesome.  But what *can't* it do?
    * It can't fill out conceptual, comprehensive, high-quality documentation to get started with or reference a library
    * It can't provide in-situ guidance on when and how to access documentation
    * It can't answer questions about projects on which there is a shortage of involved documenters and answerers
* How can we push the vision of HelpMeOut further?
    * The strength of HelpMeOut---the specific way of listening for a problem and providing a solution.  Very doable
    * But what about what HelpMeOut doesn't do?
        * What is the constrained problem set on which we can:
            * Listen for a programmer's information need or problems
            * Listen for when the solution to the problem occurs (or at least some reasonable range of time)
            * Refine---what was the actual solution to the problem (*solution capture*)?
            * Refine more---what more should be documented about the solution?  What was the problem, and the solution (*sense-producing*)
* What would it take to crowdsource the development of an entire piece of documentation?
    * For example, start with the documentation generation by Sridhara et al., incorporate the usage examples of Moreno et al., sequence all of it, and then ask for crowd workers and interested developers to contribute through a Find-Fix-Verify type of pattern
* My job going forth: keep reading and reading.  Come up with awesome ideas and share them with both.

## 2015-11-29: The development environment that helps you grow

* Programmers still rely on what they know to program quick jobs and seek information
* Cool research ideas related to this
    * A study and review: how programmers accumulate and apply tacit knowledge
        * Examples where memory is used and possibly helpful include: 
            * What library should I use for this task?
            * Quick command line commands (git committing and pushing are muscle memory)
            * programming a for loop in any language
            * Designing a visualization as a "D3"-style visualization---data-driven, with enter() and exit()
    * A study and review: the roles and risks of memory in programming, software engineering, and personal growth
    * A system: a development environment that knows what you know, and when you should grow
        * The ultimate question: to what degree should a development environment help you *develop* yourself?
        * There are several phenomena it may want to help with:
            * Discovering new libraries to use
            * Providing you with alternatives when you have outgrown existing dependencies
            * Practicing new skills that require rote repetition but enable speedup
                * For example, that library that you always look up

## 2015-11-28: Brainstorming about tutorial mining

* Things that we can understand from programming tutorials
    * How good is a library and its APIs?
    * What is currently a "hot" technology in software development?
    * What are the problems with it?
    * What is the average lifetime of a "hot" software package?
    * What implications does this have for programmers who want to have trusty tools?
    * How does affect change in the lifetime of a software package?

## 2015-11-26: Chatting with Anna

* Ideas for building more useful things
    * Make it faster for programmers to navigate to find relevant code (Ko et al.)
    * Make it faster for programmers to copy-paste / modify
    * Help uninterested programmers ask the right questions when debugging (Burnett)
    * Log crodsrouced programmer fixes and apply them for other programmers (Hartmann et al.)
    * Make it safer to copy-paste/modify code
    * Make sure programmers engage with the concepts they will need to solve problems (Ko, Parnin)
* Comments from Anna and working with sewing machines
    * We are our tools.  How we solve problems and implement stuff is dependent on the tools we use.
    * Changing the tools we work with requires "mental hacks" to connect what the new machine can do to what our old machine could do
* An idea for a conceptual knowledge project
    * Programmers should have certain practical knowledge by the time they need to make quick decisions and debug.
    * You might call this "dense decision-making", or making big decisions based on huge information
    * Whose responsibility is it to make sure programmers have this knowledge: the UI?  OS?  Mentor?  Programmer?  Static docs?
    * Related work: systematic program comprehension (there's a lot of these papers), conceptual meory (Parnin &amp; Rugaber), conceptual knowledge (Ko et al.)
    * Examples of problems programmers need are in both system evolution and most of all **framework choice**
    * A programmer may have questions about what framework to use.  What they need is **practical comparative knowledge**.  One problem is that the answer ("can I do this easily with X framework") may not come from one expert, but from many experts.  Each expert probably only has great experiential knowledge with only one of the systems.  How can we combine this knowledge into a single useful set of answers that answer the programmer's question?
    * One possible answer: a system for buying prototypes.
        * A weaker generalization: how can we make it so that programmers can get working implementation prototypes / definitive answers about the possibility of a framework working, with a high-quality description and recommendation, from experienced people?

## 2015-11-25: An abstracted for beyond the IDE

* Problem: programmers have to leave their programming environment to access information
* Solution Impact: a break from the critical flow and clumsy integration. Possibly 2x reduction in time.
* Current Approach: information in the browser.  IDE allows introspection of code.
* Current Neglect: how do we better serve programmers who use the text editor?
* Body Neglect: establishing the feasibility and benefits of information integrated into the editor
* Solution: simple text-based information queries.  scraping and inserting the information.
* Construction: XCode text entry listening
* Evaluation: how many help documents are looked up (if your fingers don't have to leave the keyboard)?  How many fewer user interface actions take place?  Qualitatively, what are the information needs that we can support (e.g., from Sillito et al.)?  How long does it take to look up new information?
* Materials: Nothing.  Absolutely nothing.
* Man-Months: 2 months to implement the system and map information needs to text, and to build some kind of navigation system (for instance).  1 month to design and conduct a lightweight evaluation.

## 2015-11-23: Weekly Meeting with Marti

* It's interesting to think about how to support help in the four categories from Sillito et al.
* What about paths of programmers through online help?  See Ryan White's paper on "Prediction"
* Marti likes the currently proposed study much better than the 
* Feedback on the study design
    * How can we analyze and understand programmer navigation behavior

## 2015-11-20: Ideas Walking Home

* Bringing adaptive information outside the IDE
    * Techniques for sensing information need: vision, keystrokes, paste (and other methods to watch input and output)
    * Methods for interventions: via comments, side windows, images, source code
* There is a difference between reading code examples to learn and reading them to copy code
* Existing studies of programmer information needs
    * barriers
    * API clarifications
    * Learn skills
    * Clarify existing knowledge
    * Remind
    * Inform about software development progress
    * Find reusable subsystems
    * Find reusable components
    * Assess task feasibility
    * Learn from usage examples
    * Discover where and how to change code
* A magical element of programming search: it's one of the few times when a person intentionally plugs into a wide, unknown community.  I'm guessing that they are simultaneously open-minded (looking for help) and close-minded (frustrated or looking for a one-off solution)

## 2015-11-19: Ideas Walking Home

* Important problems
    * How can we detect a need for learning and connect learners back to high-quality (community-ranked) learning resources?
        * Right now the Internet makes a large amount of incomprehensible knowledge available
            * "Learn anything, but flail in the process"
* Possible products
    * A kit for writing tutorials that listen back
    * Flow-centered crowdsourcing: tapping into tacit knowledge when people are in the zone and have information at hand
        * When do you ask?
        * What questions do you ask?
        * How much can you ask, and how should you ask?
        * Applications:
            * what can't this API do (comments for reusing Scipy routine)
            * what can't this hardware component do (assessed by the parts shop)
    * Extend the powerful online programming knowledge communities to the hardware world
* More n-grams for current research
    * information seeking, EUPs, and hardware
    * explanations and software engineering
    * crowdsourcing, documentation, and  programming
    * programming, information seeking, **long term**

## 2015-11-16: Weekly Meeting with Marti

* Takeaways from UIST: boy, these JavaScript debugging interfaces could use some lighter representations of all that code!
* Marti's suggestions for cool things we could do with tutorial mining:
    * make recommended pairs or sets of tutorials
    * recommend more tutorials based on the current one that is shown
    * think of libraries as being viruses or DNA that weave through other tutorials
    * visualize the "churn" of languages, toolkits, and libraries over time by inspecting cooccurrence of programming terms in tutorials
* About the studies proposed
    * Consider an experiment with the elegance of the research on the psychology of babies.  We want something with that level of elegance, of eliciting just the right information with minimal effort.  Be careful about the design of the wild studies.
    * May want to talk to Josh Hug from CS61B about the wild study
    * The later two lab studies don't map too well to the knowledge that we want to acquire

## 2015-11-09-2015-11-11: Insights from UIST 2015

### Moments of clarity

* How can we make knowledge for programming and making more rapid access?
* You can execute pretty much any pipe dream with the right tools.  So make useful products rather than just any project.
* Great research directions can be described by the conjunction of several words.  As an exercise, try describing your research as three words, or one single word and one compound term.  This is a good way to think broadly about a broadly-appealing problem (example, "micro-tasks for code")
* For a good project, you should satisfy two criteria: is this an awesome project?  And does solving this problem provide valuable knowledge for others?
* Integrated text and visual descriptions for boot-strapping understanding (for example, in PythonTutor)
* To help programmers, we don't need to show exactly some set of relevant information. We need to show *just enough* for the user to fill in the rest
* The Philip Guo model: built something simple that is **really useful** at low cost.  People will start using it.
* To best explore synthesis and explanations, ask: what did D'Antoni and Sridhara leave open for exploration, and rich domains beyond theirs?
* One benefit of supporting JavaScript is that all of the source is visible, if obfuscated

### From others

* Ben Lafreniere: tutorials are designed as uni-directional.  How can you make information flow back into tutorials from their users to make them more useful?
* Juho Kim: it can be easier to get a large number of users by working with online classrooms
* Juho Kim: it would be cool to adapt different granularities of explanations to user preferences.  This could be informed by click data from student participants in a MOOC.
* Juho Kim: this is potentially equally interesting in the education space as it is in a collaborative work space
* Mohammed: how could we work implicit feedback collection into the IDE, for example monitoring the runtime to learn which lines are probably working, and which ones are failing?
* David Mellis: the observational study should come before the system paper
* How could Tutorons perform live collaborative demos like in Oda et al.?
* Jess Cauchard: try two things as a second-year: do something risky, or build a system
* David Mellis: how could we leverage open source code to provide learning experiences for programmers?
* David Mellis: one possible trio of topics: program comprehension, collaboration, online
* David Mellis: have three words to describe what you are trying to do (e.g., novices, machine learning, microcontrollers)

### Brainstorming Ideas

The goal of one's thesis is to take one of the following topics, and give resounding insight on a technique in that area.

#### Some interesting combinations (ordered by rank)

* synthesis and explanations (Sridhara, D'Antoni)
* data mining and examples
* search and examples (Brandt)
* collaborative authoring and fabrication
* software engineering and examples (Oney, Brandt)
* program comprehension and examples
* fabrication and examples
* design and program comprehension
* reuse and examples
* tutorials and design [agency]
* data mining and explanations
* collaborative authoring and examples

#### 1- and 2-grams

* information seeking
* examples
* synthesis
* program comprehension
* fabrication
* collaborative authoring
* search
* data mining
* design
* crowdsourcing
* tutorials
* conversational programmer
* novices
* software engineering
* explanations
* reuse
* telepresence
* audio
* multi-modal explanations
