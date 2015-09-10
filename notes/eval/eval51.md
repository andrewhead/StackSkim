# Evaluation 51: Understanding SQL Examples on the Web

## Overview

### Purpose

We aim to develop an understanding of the types of SQL queries that are used in online programming help and teh kinds of examples of that is operated upon.

### Summary

See the [broad strokes](#broad-strokes) section.

## Procedure

### Preliminary Exploration

We look at the most popular questions on StackOverflow for the SQL tag and inspect the first five examples, and then the five newest questions with more than one answer (`[sql] answers:1`, then click on the 'newest' tab), and observe trends that we describe here.

## Notes

### Observations

#### Most popular questions

The topics of the questions were:
1. [link](http://stackoverflow.com/questions/60174/how-can-i-prevent-sql-injection-in-php): asked about SQL best practices with respect to security. 
2. [link](http://stackoverflow.com/questions/38549/difference-between-inner-and-outer-joins): asked for conceptual explanation of a SQL operation. 
3. [link](http://stackoverflow.com/questions/2334712/update-from-select-using-sql-server): a 'How-To-Do-It' question (Nasehi et al. 2012) for updating rows of a table based on a select from a table.
4. [link](http://stackoverflow.com/questions/92082/add-a-column-with-a-default-value-to-an-existing-table-in-sql-server): a 'How-to-Do-It' question about adding a column to a table.
5. [link](http://stackoverflow.com/questions/653714/insert-results-of-a-stored-procedure-into-a-temporary-table): 'How-to-Do-It' for storing the results of a stored procedure into a temporary table

For question 2, there are several answers with different visualizations, and several answers with examples of data tables that are joined, filled with example data.

Questions 3, 4, and 5 solicited a bunch of example code to perform a task.  On the surface and at a glance, it's difficult to tell what each of these examples do differently from each other.  These examples also do not include any visualizations or examples of the data that the code operates on.  For this type of question (How-To-Do-It), it could be helpful to produce examples of types of data that each one performs on, and special cases of what one example can do that another one cannot.

#### Newest questions

1. [link](http://stackoverflow.com/questions/32506868/sql-error-ora-01489-result-of-string-concatenation-is-too-long): 'Debug/Corrective' question (Nasehi et al. 2012) about error when running query.
2. [link](http://stackoverflow.com/questions/32506868/sql-error-ora-01489-result-of-string-concatenation-is-too-long): 'How-To-Do-It'.  How to select a single record for each ID from a table.
3. [link](http://stackoverflow.com/questions/32506361/adding-an-additional-column-to-sql-union-select): 'How-To-Do-It'.  Appending a name of a record by joining it on ID with another table, and integrating this into an existing query.
4. [link](http://stackoverflow.com/questions/32506346/huge-join-query-leads-to-max-row-size-error): 'Debug/Corrective'.  Request for workarounds for an error message related to a row size greater than the maximum allowable row size.
5. [link](http://stackoverflow.com/questions/32506308/sql-select-single-row-with-two-matching-values): 'Debug/Corrective': question author wants feedback on how to fix a query they believe is incorrect because of unexpected results.

Question 2 looks like a programming by example input.  The questioner provides the data they want to operate on and the result of the operation, and asks for help on formulating the query.  Can we 'mock' programming by example by having the crowd guess the intent of the programmer?  Question 3 also provides example input and output.  Question 5 provides example input data.

The answers to question 4 rephrase the answerer's understanding of the error message or reuse existing documentation to give the question author more information about the error they are debugging.

#### <a name='broad-strokes'>Broad-strokes patterns

In this sample, some of the new questions provided example data before or after the query was performed.  For some popular questions, there were many highly-rated answers that provided code snippets to do the task that the question author requested.

This suggests that we may be able to look at example data used in StackOverflow questions as a starting point for generating example data for a SQL tutoron.  There also may be a space for showing differences in runtime and corner cases for the many examples shown for SQL queries.

### Errata

We work with a small sample.  This is purely to get some inspiration about what kind of data might be embedded within programming examples, and how this data plays into answering those questions.  These observations cannot be generalized without a study of a larger spread of questions and tutorials in programming help.
