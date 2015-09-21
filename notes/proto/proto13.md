# Prototype 13: Tables that SQL queries operate one

## Overview

### Purpose

We produce examples of tables that SQL queries will operate on and the results of those operations.  We observe the quality of these example tables and generate ideas for building more helpful examples of tables.

### Summary



## Procedure

### Use case

Naomi is making a PHP server for her lab group.  She is following tutorials for setting up a page, and knows she needs a database to fetch some paper names and display their citations on the main page.  She hasn't used SQL in a long time, and sees a couple of queries on the web page.  She wants to understand them better, and see which words control with actions so that she can add her own custom queries.

![Storyboard](../assets/p13-storyboard.jpg "Storyboard")

### Construction

#### Example Queries

We extract three queries from our corpus of documents that we fetched for jQuery in [Evaluation 45](../eval/eval45) by searching the `pages` directory for Evaluation 45 for lines of text with the keyword `SELECT`.  While documents may have other queries than `SELECT` statements (e.g., `CREATE TABLE`, `INSERT INTO`), we focus on `SELECT` only, as it allows us to focus on generating several examples for one query type before moving onto others.  We use the command `find . -name '*.html' -print0 | xargs -0 grep SELECT` from within the `pages` directory to do this.  We take the first query from the first three documents we find with a SQL query that does more than just select columns from a table -- it must perform some filtering, joining, or reordering.

Document: `/ajax jquery json tutorial/3/www.sitepoint.com/ajaxjquery-getjson-simple/index.html`  
Statement: `SELECT image FROM graphics WHERE field = '$value' AND anotherfield = '$anothervalue' ORDER BY position;`

Document: `/google-chrome javascript jquery tutorial/2/tutorialzine.com/2010/06/making-first-chrome-extension/index.html`  
Statement: `SELECT * FROM feed WHERE url='http://feeds.feedburner.com/Tutorialzine' LIMIT 2`

Document: `/javascript jquery validation tutorial/2/www.javascript-coder.com/form-validation/jquery-form-validation-guide.phtml.html`  
Statement: `SELECT email FROM $tablename WHERE email = '$email'`

#### Generating the tables

For each of these queries, we write out an expected data table.  Using the Python package [`sqlparse`](https://pypi.python.org/pypi/sqlparse), we parse the statement.  By walking the parse tree, we generate the expected data table.  Future versions of our routines may benefit from using a tool like [JSqlParser](https://github.com/JSQLParser/JSqlParser/wiki) that structures tokens in a hierarchy rather than a list to make traversal faster and more straightforward.

In the current iteration of table generation, we discover all conditions applied to the table through WHERE clauses.  This could be made into an optimization problem with the following soft constraints on creating the input table:
* Every WHERE condition should show up at least once violated and once obeyed
* There should be a balanced number of violations and satisfactions of each of the WHERE clauses
* Minimize the number of rows (7 or less, the number of chunks in the working memory according to the MHP (Card et al. 1983))
* There should be variety in the value of a column by which a table is ordered (though this might come in at the data generation stage rather instead of the condition generation stage)
We also impose the following hard constraints:
* Every column referenced in the query must appear in the input tablse
* If the query includes a LIMIT, then there should be at least LIMIT+1 records in the table

For more than 3 conditions, it's likely difficult to show only 7 rows and indicate each of the conditions.  This is a point at which it may be advantageous to split the query into sub-queries or conditions, and to show what each one does independently, leaving it to the reader to synthesize what the command does as a whole.

For the tables generated we ask:
* Does this table show what the command does as well as what it *doesn't do*?
* How long does it take to look at the entire table?
* Is the table arranged / formatted in a way that makes the behavior obvious?

### Expected Outcome

#### Expected tables

##### Statement 1: `SELECT email FROM $tablename WHERE email = '$email'`

Input:

| id | email |
| --- | --- |
| 1 | $email |
| 2 | $email |
| 3 | not |
| 4 | $email |

Output:

| id | email |
| --- | --- |
| 1 | $email |
| 2 | $email |
| 4 | $email |

Notes:

Note that we choose to augment this table with an ID column.  Because there was no identifying feature of the columns retrieved as they all have the same value, there should be some way to show correspondence between the initial and final rows of the table.  For example, a mistaken interpretation of what happened for this query might be to assume that the first record was shown three times, if the `id` column wasn't included.

However, note that the `id` column won't actually be returned by this query as it wasn't one of the named columns in the SELECT statement.  This might confuse readers of the table.

##### Statement 2: `SELECT * FROM feed WHERE url='http://feeds.feedburner.com/Tutorialzine' LIMIT 2`

Input:

id | url
--- | ---
1 | http://feeds.feedburner.com/Tutorialzine
2 | http://url.com
3 | http://feeds.feedburner.com/Tutorialzine
4 | http://url2.com
5 | http://feeds.feedburner.com/Tutorialzine

Output:

id | url
--- | ---
1 | http://feeds.feedburner.com/Tutorialzine
3 | http://feeds.feedburner.com/Tutorialzine

Notes:

It may be more "realistic" to augment the input table with additional columns that are relevant to the table.  A feed, for example, may also have a date and a topic for each URL.

Animations that show the effect of each of the individual commands that could be paused and searched for operations would help to show the effect of individual parts of the SQL query.  Otherwise, *multiple examples* may need to be shown in order to demonstrate the effect of each part of the query (e.g., the `WHERE` and `LIMIT` clauses separately).  Or, we could provide explanations for why each row that was omitted was *not* selected.

From an implementation perspective, as long as we can generate the original table, we can actually run the query on the input table and display the real output table, instead of needing to re-implement the SQL query engine to complete our examples.

##### Statement 3: `SELECT image FROM graphics WHERE field = '$value' AND anotherfield = '$anothervalue' ORDER BY position;`

Input:

field | anotherfield | position
--- | --- | ---
cat | $anothervalue | 2
$value | $anothervalue | 4
$value | $anothervalue | 5
$value | dog | 3
$value | $anothervalue | 1

Output:

field | anotherfield | (position)
--- | --- | ---
$value | $anothervalue | (1)
$value | $anothervalue | (4)
$value | $anothervalue | (5)

Notes:

In this case, we include a column that is used for ordering as a hidden column (with `()`) as it describesp

## Notes

### Observations

### Technical Improvements

Improve the fake data by:
* looking for these fields in Github SQLite databases on Github
* searching for regular expressions with the column names and generating strings (like we did in Prototype 9) that satisfy these patterns
* search through data scraped from Enigma.io

### Research Ideas
 
There could be a research project just in mapping code examples to data on which it can operate.  The techniques may be similar to the Bozkurt & Harman paper (2011), but instead of mapping services as inputs and outputs to each other, we would contribute methods of processing source code to determine what kind of data it would operate on, and the subset of data that should be acquired from the service to make for interesting observations.

There may be multiple methods for matching fieldnames to data:
* Finding columns in open source tables that have the same name
* Discovering keywords in the surrounding text that convey what type of data the query may be operating on, and then fetching columns related to those queries
* Searching over a large corpus of related queries, finding nearest neighbor queries that were shown with some data, and replicating that data that was used for the first query
