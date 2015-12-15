# Related Work 3: Tutorial Mining

## Summary so far

<!--
Knowledge stage|Current Way|Future Way|Notes
---------------|-----------|----------|-----
Creation|talking with customers, reviewing coding history, revisiting past code, reading documentation, attending workshops, talking to peers, communities of practice||
Codification|writing docs before, during, and after development (Dagenais &amp; Robillard 2010), generating docs from source (Moreno et al., Sridhara et al.), community feedback (Dagenais &amp; Robillard 2010)||
Transfer|||
Application|||
-->

Knowledge Management stage|Current Way|Future Way|Notes
---------------|-----------|----------|-----
Creation|reading blogs, references, papers; interviewing/inquiring users; experimentation; reading code|reading materials augmented; crowdsourced requirements and experts; crowdsourced navigation of code/mixed source-and-text queries, tools to overcome memory failures; crowdsourced discovery of behavior of code; "crowdsourced forensics" for working with and understanding legacy code|
Codification|embed in framework; code examples; source code; design documents; written tutorials; API references; blog postings; Q&amp;A online; reference manuals/books|tutorial writers listen to the things that scientists program, and write it up and publish it; design document markup embedded in code; text generation of API descriptions, mixed initiative; text generation of developer stories; text analysis of good questions|
Transfer|developer discussions, reading any of the above; workshops; technical presentations; team meetings|remote workshops|
Application|reusing APIs; re-applying example code; advice and decisions when choosing features to implement, etc.|code examples as blocks; an interface for rapidly testing out solutions, ranked by likelihood of ease of implementation; crowdsourced code example cultivation|

### Tools at our disposal

* text analysis
* code analysis
* large corpuses of open source code
* crowdsourcing platforms for both general and software engineering crowdsourcing
* an active community of online tutorial writers
* some open source packages actively used by 1000s of researchers and hobbyists today
* tons of online tutorials and explicit knowledge

### Some more thoughts

* How could you mine common use cases, data, and instructions for writing getting-started guides by instrumenting existing code packages?  Maybe this involves accepting an end-user license agreement.
* Knowledge hand-offs: when designed the right way, it saves time
* Can design and implementation decisions be modeled based on browser and coding history?  Can we capture what is hard about a problem?
* What if a crowd refactored your code as you slept?
* How can you connect hugely distributed and sparse communities of practice to answer each other's questions?

There's an overall trend of externalization of programming knowledge.
This might result in a decrease of tacit knowledge and increase of explicit knowledge.

### Major themes

#### Tutorial Mining

* Extracting and indexing programming tasks (Treude et al. 2015)
* Resolving API names (e.g., Petrosyan et al. 2015, Subramanian et al. 2014)
* Linking to API documentation (e.g., Petrosyan et al. 2015, Subramanian et al. 2014)
* Usage mining (Mooty et al. 2010, Head et al. 2015)
* Understanding coverage (Parnin et al. 2012) and quality (e.g., Mamykina et al. 2011)

#### Code Mining and Processing to Make Better Docs

* Extracting concrete code examples (Moreno et al. 2015)
* Natural language explanations (e.g., Sridhara et al. 2010)

#### Knowledge Sharing in Software Engineering

* It is important to document design decisions during agile development (Selic 2009, position paper)
* There are challenges to developing and maintaining good, useful documentation for frameworks (Dagenais &amp; Robillard 2010)
* Communities contribute to documentation for open source projects (Dagenai &amp; Robillard 2010)
* Activities in knowledge sharing include creation, codification, transfer, and application (Dorairaj et al. 2012)
* Past approaches to knowledge sharing in Crowdsourced Software Engineering (Mao et al. 2015) include:
    * observing emergent programmer behavior (Fast et al. 2014)
    * listening for an applying programming solutions (Hartmann et al. 2010)
    * Integrating crowd documentation into the IDE (e.g., "Seahawk", Ponzanelli et al. 2013)
* Successful community-integrating workflow in the NumPy community (infrastructure, standards, project champions, finances) (Pawlik et al. 2015)
* Authoring tutorial docs (e.g., Ginosar et al. 2013)

### Summary of this installation of related work

Fourney &amp; Terry describe challenges in processing software tutorials.
These are likely relevant challenges for programming tutorials too. 
The other two papers mentioned here describe how to mine tutorials for references to API entities, and how to mine code to make better API documentation.
This shows an already-active area of study in code mining, and a growing body of research in mining programming tutorials.
There are probably a dozen or so papers related to understanding and mining programming tutorials, published at ICSE and other venues.

## Themes

### Animating / Supplementing Existing Programming Docs

* Live API documentation
* How Can I Use This Method?
* Discovering Information Explaining API Types Using Text Classification

## Works

### Mining Online Software Tutorials: Challenges and Open Problems

There are compelling ways data from tutorials could be utilized, including:
* a system could infer the time required to perform a tutorial
* it could infer the target audience (e.g., novice vs. expert)
* it could infer the amount of creativity or input expected of users
* it could be used to infer attributes related to the design of the software, such as missing features, or features that frequently lead to breakdowns in use of the software

Much existing work has focused on executing instructions embedded in tutorials.
Challenges to mining information from tutorials include extracting a single step or operation, extracting command parameters, spatial reasoning, constraining action through purpose clauses,  sequencing steps, handing non-procedural text (657)

### Discovering Information Explaining API Types Using Text Classification

The aim of this paper is to connect API documentation to relevant sections of tutorials.
The challenge they face is locating sections of tutorials that discuss an API.
The authors report an algorithm for fragmenting a page into sections, splitting it into potential API terms, and training a model to predict whether a term refers to an API.
They train this on five pages.

### How Can I Use This Method?
Given an API, the authors mine concrete code examples from software that calls that API.
They do this by performing a backwards slice on the API call and eliminating clones.
They argue that such code examples could be included in API documentation.

### Live API Documentation

### Extracting Development Tasks to Navigate Software Documentation

## Ideas

