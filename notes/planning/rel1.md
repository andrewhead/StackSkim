# Related Work 1: Programmer Information Needs

This review of related work is organized by themes seen in one or more works.
It is designed to inform a new generation of synthesized programming help.

## Information Needs can be Described by Common Questions

* Takeaways
    * Programmers have information needs in two contexts (among others):
        * Dependent / focused on specific source code
            * Understanding the code
                * What does this piece of code do?  (Stolee et al., Sadowski et al.)
                * Where is the referenced code defined? (Sadowski et al., Sillito et al.)
                * What does this output mean? (Ko et al. "understanding")
                * What's going wrong with this piece of code (Stolee et al., Sillito et al. subgraphs, Ko et al. "understanding")
                * What data is being modified /operated upon in this code? (Sillito et al.)
            * Building up a bigger picture
                * What other code is this related to? (Sillito et al.)
            * Project Management / Collaboration
                * Who broke / altered / touched this piece of code?  (Fritz &amp; Murphy, Sadowski et al.)
                * How does this code's style compare to other code's style (Sadowski et al.)
            * Modifying and running the code
                * What dependencies does this code have? (Sadowski et al.)
                * What would it take to move this code to class C? (Sillito et al.)
                * How can data be passed to this point in the code? (Sillito et al.)
                * What are the differences between these two pieces of code? (Sillito et al.)
        * Independent of specific source code
            * What is everyone's progress on tasks? (Fritz &amp; Murphy)
            * Where can I find the code related to my goal (within-project)?  (Sadowski et al., Sillito et al.)
            * What components should I use to do the job?  (Ko et al., Li et al., Stolee et al.)
            * How can I use this component to do this job? (Stolee et al., Sim et al., Sadowski et al.)
    * What this means for Tutorons
        * Must Tutorons-style help be tied to source code?  Could it be independent of source code?
        * Tutorons should be bi-directional.  Explanations (APIs) → usage examples, and usage examples → explanations.
* Categorization schemes
    * type of problem that is being solved (e.g., debugging, finding features, tracking team progress)
        * Ko et al.'s: information barrier for debugging, selection barrier for choosing software
        * Li et al.'s: types of help seeking tasks: feature-oriented, API-oriented, configuration-oriented, error-oriented
        * Sadowski et al.: example-centric "how", code localization "where", etc.
    * amount of system that is being reasoned about
        * Ko et al.: coordinating interfaces vs. selecting new API
        * Sillito et al.: focus, build, subgraphs, and comparisons
        * Duala-Ekoko &amp; Robillard: argument-level vs. class-level
    * type of information domain that is queried over
        * Ko et al.: existing source code vs. online API documentation
        * Fritz &amp; Murphy: domains include source code, change sets, teams, work items, web sites and wiki pages, comments on work items, exception stack traces, and test cases
    * degree of understanding sought
        * Ko et al.: 
        * Brandt et al.: learn, clarify existing knowledge, or recall
        * Sillito et al.: features or subgraphs
        * Stolee et al.: "what does X do" vs. "how do I do X"
    * size of information that is sought
        * Sim et al.: block, subsystem, system
    * questions that are easy or difficult to answer
        * Duala-Ekoko &amp; Robillard: easy or difficult (determined through observation)

## Themes

### There are High Cognitive Demands in Programming and Learning and Using the Right Information

* Parnin &amp; Rugaber 2012

### Programmers Need Information to Extend or Debug Software

* LaToza et al. 2006
* Sillito et al. 2006
* Ko et al. 2006
* Piorkowski et al. 2015

### Programmers Sometimes Look for References instead of Code

* Umarji et al. 2008

### Programmers Sometimes Look for Example Code instead of References

* Umarji et al. 2008
* Brandt et al. 2009
* Stolee et al. 2014

### Information Needs can be Categorized by the Size of Code to Reuse or Understand

* Sillito et al. 2006
* Umarji et al. 2008

### Information Needs Can Be Represented by Common Questions or Categories

* Ko et al. 2004: six learning barriers
* Sillito et al. 2006: four categories, 44 questions
* Sim et al. 2011: reference--as-is reuse continuum, and blocks vs. subsystems vs. systems
* Duala-Ekoko &amp; Robillard 2012: 20 questions about unfamiliar APIs, including five "difficult" questions
* Li et al. 2013: four types of help seeking tasks
* Stolee et al. 2014: seven question types on StackOverflow
* Fritz &amp; Murphy 2015: 78 "multiple domain" questions developers asked
* Sadowski et al. 2015: five categories, 16 questions for motivations behind internal code search at Google

### Programmers Need to Know about the Activity of their Teammates

* Fritz &amp; Murphy 2015
* Sadowski et al. 2015

### Programmers have to re-find information

* Li et al. 2013

### Programmers' Information Needs May Be Satisfied with a Top-Down Approach

* Sillito et al. 2006
* Stylos &amp; Myers 2006

### Programmers' Information Needs May Be Satisfied with a Bottom-Up Approach

* Sillito et al. 2006
* Piorkowski et al. 2015

### There are Subtle Differences between Many Similar Programming Questions

* Fritz &amp; Murphy 2015

### Programmers Rely on Peers to Satisfy Many Information Needs

### Existing Development Systems Don't Support Program Information Seeking Well

## References

Brandt, Joel et al. “Two Studies of Opportunistic Programming: Interleaving Web Foraging, Learning, and Writing Code.” Proceedings of the SIGCHI Conference on Human Factors in Computing Systems. New York, NY, USA: ACM, 2009. 1589–1598. ACM Digital Library. Web. 18 Nov. 2014. CHI ’09.  
Duala-Ekoko, Ekwa, and Martin P. Robillard. “Asking and Answering Questions about Unfamiliar APIs: An Exploratory Study.” Proceedings of the 2012 International Conference on Software Engineering. IEEE Press, 2012. 266–276. Google Scholar. Web. 13 Jan. 2015.  
Fritz, Thomas, and Gail C. Murphy. “Using Information Fragments to Answer the Questions Developers Ask.” Proceedings of the 32Nd ACM/IEEE International Conference on Software Engineering - Volume 1. New York, NY, USA: ACM, 2010. 175–184. ACM Digital Library. Web. 19 Nov. 2015. ICSE ’10.  
Ko, A.J., B.A. Myers, and H.H. Aung. “Six Learning Barriers in End-User Programming Systems.” 2004 IEEE Symposium on Visual Languages and Human Centric Computing. N.p., 2004. 199–206. IEEE Xplore. Web.  
Ko, Andrew J. et al. “An Exploratory Study of How Developers Seek, Relate, and Collect Relevant Information During Software Maintenance Tasks.” IEEE Trans. Softw. Eng. 32.12 (2006): 971–987. ACM Digital Library. Web.  
LaToza, Thomas D., Gina Venolia, and Robert DeLine. “Maintaining Mental Models: A Study of Developer Work Habits.” Proceedings of the 28th International Conference on Software Engineering. New York, NY, USA: ACM, 2006. 492–501. ACM Digital Library. Web. 16 Sept. 2015. ICSE ’06.  
Li, Hongwei et al. “What Help Do Developers Seek, When and How?” 2013 20th Working Conference on Reverse Engineering (WCRE). N.p., 2013. 142–151. IEEE Xplore. Web.  
Parnin, Chris, and Spencer Rugaber. “Programmer Information Needs after Memory Failure.” Program Comprehension (ICPC), 2012 IEEE 20th International Conference on. IEEE, 2012. 123–132. Google Scholar. Web. 28 Feb. 2015.  
Piorkowski, David J. et al. “The Whats and Hows of Programmers’ Foraging Diets.” Proceedings of the SIGCHI Conference on Human Factors in Computing Systems. New York, NY, USA: ACM, 2013. 3063–3072. ACM Digital Library. Web. 21 Nov. 2015. CHI ’13.  
Sadowski, Caitlin, Kathryn T. Stolee, and Sebastian Elbaum. “How Developers Search for Code: A Case Study.” Proceedings of the 2015 10th Joint Meeting on Foundations of Software Engineering. New York, NY, USA: ACM, 2015. 191–201. ACM Digital Library. Web. 19 Nov. 2015. ESEC/FSE 2015.  
Sillito, Jonathan, Gail C. Murphy, and Kris De Volder. “Questions Programmers Ask During Software Evolution Tasks.” Proceedings of the 14th ACM SIGSOFT International Symposium on Foundations of Software Engineering. New York, NY, USA: ACM, 2006. 23–34. ACM Digital Library. Web. 20 Nov. 2015. SIGSOFT ’06/FSE-14.  
Sim, Susan Elliott et al. “How Well Do Search Engines Support Code Retrieval on the Web?” ACM Trans. Softw. Eng. Methodol. 21.1 (2011): 4:1–4:25. ACM Digital Library. Web.  
Stolee, Kathryn T., Sebastian Elbaum, and Daniel Dobos. “Solving the Search for Source Code.” ACM Trans. Softw. Eng. Methodol. 23.3 (2014): 26:1–26:45. ACM Digital Library. Web.  
Stylos, Jeffrey, and Brad A. Myers. “Mica: A Web-Search Tool for Finding API Components and Examples.” Visual Languages and Human-Centric Computing, 2006. VL/HCC 2006. IEEE Symposium on. IEEE, 2006. 195–202. Google Scholar. Web. 17 Dec. 2014.  

### Works not references, but relevant

* Anything on StackOverflow.  Nasehi et al. had a paper that described four types of questions on StackOverflow
