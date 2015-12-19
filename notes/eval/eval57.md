# Evaluation 57: Information Needs of Programmers Following Tutorials

<!--# Study Design: Information Needs of Programmers Following Tutorials-->

## Purpose

What makes a bad tutorial?
More specifically, what information might tutorials lack for readers need to follow them?
This study proposes to categorize the information needs that tutorials generate but don't satisfy.
It also produces and understanding of where these information needs are eventually satisfied.
The results of this study could illuminate authoring patterns for writing effective tutorials that, for the most part, include all the necessary information to follow them.
Our findings may suggest how we can link disparate online help sources into tutorials to provide the details authors fail to include.

## Design

### Goals

I want to answer these questions:

1. How often do programmers need to access supplemental information to complete a tutorial?
2. What kinds of additional information sources contain the needed information?
3. What is the size (length) and format (e.g., code example, text, API spec) of the found information?
4. What actions do programmers take to apply this found information to making the code work (e.g., add a line of code, edit arguments of existing code, install a dependency, etc.)

### Procedure

#### Study 1: Programmer Information Needs with Tutorials that Lack Information

<!--Additional complexity will come at coding participant behavior.-->
12+ participants are recruited.
They are asked to follow a web tutorial about how to perform a programming task.
The experimenters preselect tutorials that leave out details (e.g., about installing packages or parameters a user must modify).
The participant is provided with a goal of what they should accomplish by successfully following the tutorial.
They report to the experimenter when they are done.
One example of a tutorial with the right level of detail is [this one](http://hanzratech.in/2015/02/03/face-recognition-using-opencv.html) on face recognition in Python.

#### Study 2: Prevalence of Information Needs in Following Online Tutorials

The purpose of this study is to assess the prevalence of missing information in online programming tutorials at large.
12-36 participants are recruited.
We sample one dozen tutorials from the web for a common programming language (e.g., Python) using the CUTS method (Fourney et al. 2011).
In other words, we query for tutorials using frequent queries mined Google Suggest and ranked with AdWords.
Tutorials from this ranked set, weighting the probability of selecting them by their rank.

<!--One will be with a very controlled set of online tutorials.
This is where we hand-pick tutorials that we expect will be very challenging.
The effort is to determine how programmers seek information when working with a tutorial missing a lot of details and knowledge required for the programmer to understand it with no prior exposure.
One example is giving an advanced D3 usage example to a programmer who has never worked with it before.
In another variant, tutorials will be sampled at random based on popular web queries.
Additional possible variants include giving programmers an objective of a way to attain the result of a tutorial by following that tutorial and nothing else.
Each study will have around a dozen participants or more.-->

### Measures and Data Coding

We answer Q1 (the frequency of accessing supplemental information) by counting how many times the participant looks for information outside the tutorial.
Cues for this will include when a participant initiates a search, takes a break to reason through a problem, or clicks on a link.

To answer Q2-3 about the information sources that satisfy participants' information needs, we code the information sources and chunks that programmers find.
To classify the type of information sources participants find, we use a modified version of the taxonomy given by Li et al. (which includes tutorials, Q&amp;A web sites, API specs, forums, code example sites, previous projects).

Throughout both studies, we capture participants' screen footage to facilitate analysis of their information seeking behavior.

### Participants

Participants for both studies will be recruited from UC Berkeley listservs for EECS and the I-School.
They must have at least one year of programming experience.
They should have at least half a year of experience in the focal language of the tutorial they will complete.

### Materials

Participants are welcome to bring their own laptops.
If so, they have to consent to us recording their screens using a video camera.
If they bring their own laptops, they will have access to their typical development and search tools.
I expect this would make their search and programming behavior more indicative of their typical behavior.

## Notes

### Related Work

#### The Questions that Programmers Ask about Code

* Sillito, Jonathan, Gail C. Murphy, and Kris De Volder. “Questions Programmers Ask During Software Evolution Tasks.” Proceedings of the 14th ACM SIGSOFT International Symposium on Foundations of Software Engineering. New York, NY, USA: ACM, 2006. 23–34. ACM Digital Library. Web. 20 Nov. 2015. SIGSOFT ’06/FSE-14.
* Fritz, Thomas, and Gail C. Murphy. “Using Information Fragments to Answer the Questions Developers Ask.” Proceedings of the 32Nd ACM/IEEE International Conference on Software Engineering - Volume 1. New York, NY, USA: ACM, 2010. 175–184. ACM Digital Library. Web. 19 Nov. 2015. ICSE ’10.
* Li, Hongwei et al. “What Help Do Developers Seek, When and How?” 2013 20th Working Conference on Reverse Engineering (WCRE). N.p., 2013. 142–151. IEEE Xplore. Web.
* Sadowski, Caitlin, Kathryn T. Stolee, and Sebastian Elbaum. “How Developers Search for Code: A Case Study.” Proceedings of the 2015 10th Joint Meeting on Foundations of Software Engineering. New York, NY, USA: ACM, 2015. 191–201. ACM Digital Library. Web. 19 Nov. 2015. ESEC/FSE 2015.
* Duala-Ekoko, Ekwa, and Martin P. Robillard. “Asking and Answering Questions about Unfamiliar APIs: An Exploratory Study.” Proceedings of the 2012 International Conference on Software Engineering. IEEE Press, 2012. 266–276. Google Scholar. Web. 13 Jan. 2015.

#### Programmer information seeking strategies

* Brandt, Joel et al. “Opportunistic Programming: How Rapid Ideation and Prototyping Occur in Practice.” Proceedings of the 4th International Workshop on End-User Software Engineering. New York, NY, USA: ACM, 2008. 1–5. ACM Digital Library. Web. 27 Sept. 2015. WEUSE ’08.
* Piorkowski, David J. et al. “The Whats and Hows of Programmers’ Foraging Diets.” Proceedings of the SIGCHI Conference on Human Factors in Computing Systems. New York, NY, USA: ACM, 2013. 3063–3072. ACM Digital Library. Web. 21 Nov. 2015. CHI ’13.

### Limitations

Tutorials can be used for multiple purposes:
this can include learning a new skill, looking for example code, and reminding oneself of details.
We are interested only in how tutorials fail to help programmers learn a new skill.

<!--
### Technical Improvements

### Research Ideas
 
* Comparative tutorials---what are the features of tutorials that are faster to follow and/or adapt?
* Finding the experts.  Experts can produce useful help, but not all experts are equally helpful, or equally willing to spend their time helping novices learn the ropes on their work.  Where are the good experts?  And how do you automate recruiting and scheduling them?
-->
