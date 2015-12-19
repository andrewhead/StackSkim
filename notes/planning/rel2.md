# Related Work 2: Programmers Sharing Information

## Code to Save

    # This scrapes 1000 titles from ICSE
    # It seems like we can only fetch 1000 lines at a time
    # Change 'f' to set the starting point of the download
    resp = requests.get(
        'http://dblp.uni-trier.de/search/publ/inc', 
        params={
            'q': 'venue:ICSE:',
            'h': 1000,
            'f': '0',
            's': 'yvpc'
        })

    soup = BeautifulSoup(resp.content, 'lxml')
    entries = soup.select('.entry')

    # This method gets the title and year of the work
    for e in entries:
        title = e.select('span.title')[0].text
        year = e.select('span[itemprop="datePublished"]')[0].text
        print year, title



## Technique

Look through the following publications: ICSE, Empirical Software Engineering, TOSEM, TSE, OOPSLA.
For each one, take a chronological look at the titles.
Extract the titles that appear to be relevant to the following questions:
1. Historically, how have programmers shared information?
2. What are known impediments to programmers sharing information?
3. What are the most difficult forms of information to produce?
4. What do we know about the challenges to developing software with hugely distributed, non-social software development
5. What are the requirements to making terrific programming information?
The information I'm interested in is "How-To" information.

I search DBLP, sorting by decreasing recency.
I filter by venue (e.g., include "venue:ICSE:" in the query for ICSE papers)
I manually inspect each title, and copy it here if it appears relevant.

Additional publications that may be related include:
* Social Software Engineering (SSE)
* User Interface Software &amp; Technology (UIST)
* Human Factors in Computing Systems (CHI)
* Visual Languages and Human-Centered Computing (VL/HCC)
* International Conference on Program Comprehensions (ICPC)
* CrowdSourcing in Software Engineering (CSD)
* Context-Oriented Programming (COP)
* Cooperative and Human Aspects on Software Engineering (CHASE)
* Big Data Software Engineering (BIGDSE)
* Automated Software Engineering (ASE)

## Related Works

*Stopped on p. 1124-5 of ICSE 2011*

Some notes about trends:
* Reasons for difficulty working with information include: the information doesn't exist, it's in an unfamiliar representation, or there's too much to feasibly sift through in a short time
* Information may be shared in real time (sketches), or asynchronously (e-mail, bug reports)
* Programmers have a body of questions for every task.  What are the questions for some new software engineering activities, and what systems can we build to support them in asking those questions?

Some related workshops may include:
* Workshop on SHAring and Reusing architectural Knowledge (SHARK)
* Workshop on search-driven development (SUITE)

### How Have Programmers Shared Information?
#### ICSE
Documenting and sharing knowledge about code
The hidden experts in software-engineering communication
On how often code is cloned across repositories
Informing development decisions: from data to information
Content classification of development emails
Specification patterns from research to industry: A case study in service-based applications
Understanding broadcast based peer review on open source software projects.
Using knowledge elicitation to improve Web effort estimation: Lessons from six industrial case studies.
Build It Yourself! Homegrown Tools in a Large Software Company
Uncertainty, risk, and information value in software requirements and architecture.
Efficient reuse of domain-specific test knowledge: An industrial case in the smart card domain.
How do programmers ask and answer questions on the web?
"Should We Move to Stack Overflow?" Measuring the Utility of Social Media for Developer Support.
Borrowing from the Crowd: A Study of Recombination in Software Design Competitions
Qualitative Analysis of Knowledge Transfer in Pair Programming
Discovering Information Explaining API Types Using Text Classification
Software engineering at the speed of light: how developers stay current using twitter
Asking and answering questions about unfamiliar APIs: An exploratory study
Searching, selecting, and synthesizing source code
Analysis of execution log files
The role of emergent knowledge structures in collaborative software development
#### OOPSLA
Empirical analysis of programming language adoption
Talk versus work: characteristics of developer collaboration on the jazz platform
Rubber ducks, nightmares, and unsaturated predicates: proto-scientific schemata are good for agile
An exploration of program as language
Notation and representation in collaborative object-oriented design: an observational study
Micro patterns in Java code
Tiling Design Patterns - A Case Study Using the Interpreter Pattern
Creating Host Compliance in a Portable Framework: A Study in the Use of Existing Design Patterns
Experience with Representing C++ Program Information in an Object-Oriented Database
Specifications and Their Use in Defining Subtypes
Documenting Frameworks using Patterns
An Empirical Study of the Object-Oriented Paradigm and Software Reuse
Communication as Fair Distribution of Knowledge
### Problems or Challenges with Existing Information Systems
#### ICSE
How do professional developers comprehend software?
Pathways to technology transfer and adoption: achievements and challenges (mini-tutorial)
Departures from optimality: understanding human analyst's information foraging in assisted requirements tracing.
Expectations, outcomes, and challenges of modern code review
Code Reviews Do Not Find Bugs. How the Current Code Review Best Practice Slows Us Down
Reducing human effort and improving quality in peer code reviews using automatic static analysis and reviewer recommendation.
Disengagement in pair programming: Does it matter?
Software process improvement through the identification and removal of project-level knowledge flow obstacles
Information foraging as a foundation for code navigation
Learning to adapt requirements specifications of evolving systems
Understanding understanding source code with functional magnetic resonance imaging
A large-scale empirical study of practitioners' use of object-oriented concepts
Balancing collaboration and discipline in software development processes
Analysing "people" problems in requirements engineering
#### OOPSLA
Reducing the barriers to writing verified specifications
Migrating Relational Data to an OODB: Strategies and Lessons from a Molecular Biology Experience
Experiences Developing and Using an Object-Oriented Library for Program Manipulation
Obstacles in Object-Oriented Software Development
### Information that Isn't Produced Well Enough
#### ICSE
Information needs for software development analytics
Learning to Log: Helping Developers Make Informed Logging Decisions
Automatic Documentation Generation via Source Code Summarization.
AR-miner: mining informative reviews for developers from mobile app marketplace.
An ontology toolkit for problem domain concept location in program comprehension
Characterizing logging practices in open-source software
#### OOPSLA
Use at your own risk: the Java unsafe API in the wild
Detecting API documentation errors
An empirical study of the influence of static type systems on the usability of undocumented software
Reuse of Algorithms: Still a Challenge to Object-Oriented Programming
Issues in the Design and Documentation of Class Libraries
### Information Sharing for Distributed Teams
#### ICSE
Creating a shared understanding of testing culture on a social coding site
Categorizing bugs with social networks: a case study on four open source software communities.
The co-evolution of socio-technical structures in sustainable software development: Lessons from the open source software communities
Does latitude hurt while longitude kills? geographical and temporal separation in a large scale software development project.
How to make best use of cross-company data in software effort estimation?
Distributed development considered harmful?
Collaboration patterns in distributed software development projects
Architectural task allocation in distributed environment: A traceability perspective
Configuring global software teams: a multi-company analysis of project productivity, quality, and profits
The role of domain knowledge and cross-functional communication in socio-technical coordination
Is time-zone proximity an advantage for software development? the case of the brazilian IT industry
What make long term contributors: Willingness and opportunity in OSS community
Knowledge transfer in global software development: leveraging acceptance test case specifications
#### OOPSLA
### Guidelines for Successful Information Sharing
#### ICSE
What good are strong specifications?
How do API documentation and static typing affect API usability?
Systematically selecting a software module during opportunistic reuse
From Developer Networks to Verified Communities: A Fine-Grained Approach
What Makes a Great Software Engineer?
Effects of using examples on structural model comprehension: a controlled experiment.
Enabling the Definition and Enforcement of Governance Rules in Open Source Systems
A degree-of-knowledge model to capture source code familiarity
#### OOPSLA
A Problem-Oriented Analysis of Basic UML Static Requirements Modeling Concepts
How to Preserve the Benefits of Design Patterns
Analyzing and Measuring Reusability in Object-Oriented Designs
What Contributes to Successful Object-Oriented Learning?
Visualizing Objects: Methods for Exploring Human Computer Interaction Concepts
### Augmenting Information Systems
#### ICSE
Ambient awareness of build status in collocated software teams.
Normalizing source code vocabulary to support program comprehension and software quality
Spotting working code examples.
Helping Developers Help Themselves: Automatic Decomposition of Code Review Changesets
Interactive Code Review for Systematic Changes
Improving Student Group Work with Collaboration Patterns: A Case Study
Changeset based developer communication to detect software failures
Where should the bugs be fixed? More accurate information retrieval-based bug localization based on bug reports.
Sketching tools for ideation
Blending freeform and managed information in tables
Pragmatic reuse in web application development
Source Code Curation on StackOverflow: The Vesperin System
ChangeScribe: A Tool for Automatically Generating Commit Messages
Poster: Interactive and Collaborative Source Code Annotation
How Can I Use This Method?
Situational awareness: personalizing issue tracking systems
On extracting unit tests from interactive live programming sessions
Seahawk: stack overflow in the IDE
MCT: a tool for commenting programs by multimedia comments
An approach to documenting and evolving architectural design decisions
Where does this code come from and where does it go? - Integrated code history tracker for open source systems
Inferring class level specifications for distributed systems
Augmented intelligence - The new AI - Unleashing human capabilities in knowledge work
Continuous social screencasting to facilitate software tool discovery
UDesignIt: Towards social media for community-driven design.
Exploring techniques for rationale extraction from existing documents
Influencing the adoption of software engineering methods using social software
Facilitating communication between engineers with CARES
Bridging the divide between software developers and operators using logs
Online sharing and integration of results from mining software repositories
aComment: mining annotations from comments and code to detect interrupt related concurrency bugs
On-demand feature recommendations derived from mining public product descriptions
Capturing tacit architectural knowledge using the repertory grid technique
Towards architectural information in implementation
BQL: capturing and reusing debugging knowledge
StakeSource2.0: using social networks of stakeholders to identify and prioritise requirements
Miler: a toolset for exploring email data
Exploring, exposing, and exploiting emails to include human factors in software engineering
Improving open source software patch contribution process: methods and tools
Building domain specific software architectures from software architectural design patterns
Finding relevant functions in millions of lines of code
Codebook: discovering and exploiting relationships in software repositories
Supporting developers with natural language queries
Using information fragments to answer the questions developers ask.
Mining API mapping for language migration
Adinda: a knowledgeable, browser-based IDE
Supporting program comprehension with source code summarization
Exemplar: EXEcutable exaMPLes ARchive
StakeNet: using social networks to analyse the stakeholders of large-scale software projects
Recurring bug fixes in object-oriented programs
VisAr3D: an approach to software architecture teaching based on virtual and augmented reality
Awareness 2.0: staying aware of projects, developers and tasks using dashboards and feeds
Linking e-mails and source code artifacts
Informal software design knowledge reuse
Failure preventing recommendations
The "physics" of notations: a scientific approach to designing visual notations in software engineering
Summarizing software concerns
Commit 2.0: enriching commit comments with visualization
Staying aware of relevant feeds in context
#### OOPSLA
i3QL: language-integrated live data views
Automated migration of build scripts using dynamic analysis and search-based refactoring
Option contracts
Online feedback-directed optimizations for parallel Java code
Detecting API documentation errors
Optimization coaching: optimizers learn to communicate with programmers
Reusing debugging knowledge via trace-based bug search
Typestate-based semantic code search over partial programs
Taming MATLAB
Automated construction of JavaScript benchmarks
SugarJ: library-based syntactic language extensibility
G-Finder: routing programming questions closer to the experts
A graph-based approach to API usage adaptation
Supporting dynamic, third-party code customizations in JavaScript using aspects
Managing ambiguity in programming by finding unambiguous examples
Design fragments make using frameworks easier
Javana: a system for building customized Java program analysis tools
Isolating and relating concerns in requirements using latent semantic analysis
XSnippet: mining For sample code
ArchMatE: from architectural styles to object-oriented models through exploratory tool support
Modeling architectural patterns using architectural primitives
A constraint-based architecture for local search
Subtext: uncovering the simplicity of programming
Alias annotations for program understanding
Subject-Oriented Design: Towards Improved Alignment of Requirements, Design, and Code
Adaptive Plug-and-Play Components for Evolutionary Software Development
Visualizing Dynamic Software System Information Through High-Level Models
Query-Based Debugging of Object-Oriented Programs
Code Reuse in an Optimizing Compiler
A Functional Layer for Description Logics: Knowledge Representation Meets Object-Oriented Programing
Reuse Contracts: Managing the Evolution of Reusable Assets
Interactive Visualization of Design Patterns Can Help in Framework Understanding
ODE: A Self-Guided, Scenario-Based Learning Environment for Object-Oriented Design Principles.
Streamlining the Project Cycle With Object-Oriented Requirements.
Annotating objects for transport to other worlds
Safely creating correct subclasses without seeing superclass code
Towards agent-oriented assistance for framework instantiation
Highly Efficient and Encapsulated Re-use of Synchronization Code in Concurrent Object-Oriented Languages
Visualizing the Behavior of Object-Oriented Systems
Concurrency Annotations.
Architectures with Pictures
Integrating Information Retrieval and Domain Specific Approaches for Browsing and Retrieval in Object-Oriented Class Libraries
Orwell - A Configuration Management System for Team Programming
A Concurrent Object-Oriented Knowledge Representation Language Orient84/K: Its Features and Implementation
### Relevant to other projects
#### ICSE
Inferring likely mappings between APIs.
LASE: locating and applying systematic edits by learning from examples.
Recovering traceability links between an API and its learning resources
Synthesizing API usage examples.
Semi-automatically extracting FAQs to improve accessibility of software development knowledge
Inferring method specifications from natural language API descriptions
Automatic parameter recommendation for practical API usage
Recommending source code for use in rapid software prototypes
Experiences with text mining large collections of unstructured systems development artifacts at jpl
Searching, selecting, and synthesizing source code
Effectively mapping linguistic abstractions for message-passing concurrency to threads on the Java virtual machine
Measuring subversions: security and legal risk in reused software artifacts
Developers ask reachability questions
Moving into a new software project landscape
Using ethnographic methods in software engineering research
Mining software engineering data
Summarizing software artifacts: a case study of bug reports
Improved social trustability of code search results
#### OOPSLA
Using web corpus statistics for program analysis
Synthesizing Java expressions from free-form queries
Accelerating the creation of customized, language-Specific IDEs in Eclipse
Debug all your code: portable mixed-environment debugging
Towards adaptive programming: integrating reinforcement learning into a programming language
AutoMan: a platform for integrating human-based and digital computation
Speculative analysis of integrated development environment recommendations
Faith, hope, and love: an essay on software science's neglect of human factors
Online feedback-directed optimization of Java
Sifting out the mud: low level C++ code reuse
Jeannie: granting java native interface developers their wishes
Strategies for Scientific Prototyping in Smalltalk
## Selected Works

### Creating and Evolving Developer Documentation: Understanding Decisions of Open Source Contributors

### A Survey of the Use of Crowdsourcing in Software Engineering

### Knowledge Management in Distributed Agile Software Development

### Agile Documentation, Anyone?

## Ideas

* A system that shows a link between changes to code and the relevant parts of documentation.
    * It filling out what has changed recently in your experiment design.
    * How do we make it easier for people to keep good, comprehensive notes?
    * Remind them what they have to write about, and write most of it for them!
    * Consider the domain of experiment and algorithm design, where precision in description is key
* One cool thing about API reference docs is that you always have a checklist of what has been explained and what hasn't.  However, GSGs take and HowTos take design, in need-finding, understanding user prior knowledge (skills and mental models), and refinement based on user outcomes.  This might necessitate a toolkit or certain way of sharing information to ease how GSGs and HowTos are written.
* Some reasons why people don't share their work (document templates, code, videos of the work) is because it could be embarrassing.  It may be embarrassing because it's unfinished/untrue, because it's linked to their identity, or it's sloppy.  Crowds or text analysis might be put to work to anonymize, clean, and complete uncompleted work.
* Juho Kim's work and PeerStudio are successful at helping people out because everyone can help everyone else out.  There are no experts.  The "The hidden experts" paper points to a difficulty that experts might not always be reachable.
* It's likely that *software engineerings* or *graphic designers* may be the first to benefit from augmented reality.  These are the workers that are most likely to *pimp out* their workstations, and that require large amounts of screen real estate.  They may work with many documents at a time.  To find the kingpin market for augmented reality, focus on the professionals who buy lots of big monitors.
* Programming work, design, and research is a cycle of observation and creation.  There are many different forms of both observing and creating.
