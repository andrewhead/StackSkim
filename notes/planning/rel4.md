# Related Work 4: Programmers Sharing Information

## Questions

Has anybody asked the following questions?
* How do programmers externalize their memory?  What are the tradeoffs?
* What are the methods that programmers share information?  What are the most effective ways for sharing information quickly and densely?
* How do programmers document their code for others to reuse?  What are the challenges people face when using that documentation?

To what extent are these questions answered by previous literature?
What is the previous literature's answers to these questions?

## Technique

I am interested in the following publications:
TOSEM, TSE, ICSE, ICPC, and CHI.

In the first round of filtering, I am interested in learning about strong theoretical results related to:
1. Memory: what programmers decide to remember, and how they could improve their performance with better memory management
2. Information sharing: how programmers share information, and challenges to doing this successfully
3. Documentation: ways that programmers encode their knowledge for themselves and others

I search DBLP, sorting by decreasing recency.
I filter by venue (e.g., include "venue:ICSE:" in the query for ICSE papers)
I manually inspect each title.
In OS X Numbers, I assign each title a tag of "Memory", "Information Sharing", "Documentation", "Other", or "None" to each title.
I use the single letters M, I, D, O, and N for this.
I make an assumption that any one paper will only belong to one of these two categories.
In a future round of filtering, I'll provide multiple labels to these titles.
I filter the titles that show to be one of the three categories above.

I select from the list of relevant papers to a topic 10 papers from each publication that appear to cover a breadth of time ranges and relevant subcategories.
For each of these, I code their answer to the questions I state at the top of this document.
From this, I make a thesis.
Based on these results, I try to introduce new contexts and knowledge about the programming ecosystem that could enable new, interesting knowledge.

The methodology and focus of this survey is similar to that in [Related Work 2](rel2).

## Codes

* Reverse engineering information from derivative information stores (e.g., software architecture recovery)

## Ideas

There are multiple forms of information sharing:
* Horizontal: between peers, on the same issue
* Vertical: producing information for others to use for another task ("handoff point")
* Personal: documenting for your own recall
* Collaborative: sharing with others
* Purposeful: documentation is written to explicitly store ideas
* Derivative: artifacts are developed with knowledge (e.g., code).  Information must be reverse engineered by inspection.

Interesting questions:
* What is the proportion of comments that end up getting accessed again by their authors, or other authors?
