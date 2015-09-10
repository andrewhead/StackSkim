# Vision 1: SQL Examples

A note for those things that have not yet come to pass.

## SQL Examples

Can we leverage online examples, Q&As and documents to generate instructive examples of code?

We focus on the languages of SQL, CSS selectors, and regular expressions as a starting point as they represent code that operate on a large variety of input data but produce results for a particular purpose.  You should be able to reverse engineer the intent of regular expressions and SQL queries in terms of describable terms by inspecting them and seeing the data they perform well on.

Additional languages this might work well are those that process data, like the Mongo database query language with MapReduce, and dataflow languages like OSC in Max, and even Blossom, utilities that stream like gstreamer, string processing that occurs in Perl.  The tools we produce here, may have an application in the domain of code reviews for developers that are attempting to understand what others' code does.

One challenge here is that there may not be a lot of examples that are automatically paired with online code examples.

### Technical approaches

We want to produce examples of what a piece of code does.  In the case of SQL queries, regular expressions

#### Data sources



##### Code examples

For regular expressions, a good repository of practical examples can be found on StackOverflow for searching for examples with the `mod-rewrite` tag.
SQL examples could likely be found by scraping StackOverflow for the `sql` tag.  We might be able to find "canonical" examples by squashing the StackOverflow queries to a representative set, by grouping together similar parse trees of the queries.

##### Data examples

Our techniques will be looking for data that the code examples can operate on and transform.  An appropriate database for an example will need:
* as many columns as the database query refers to, of the same datatypes (which may be inferred from the WHERE operations performed)
* records that are both included and excluded by each query condition
* if multiple tables exist, we need to satisfy these conditions for both tables, and they need to be joined on a criteria of the type that is joined in the query string
* preferably, the meaning of the columns in the queried table in the code example match the meanings of the columns in the example table.

Sources of SQL tables include:
* A scrape of all files names with the suffix .db from Github repositories.  We may want to restrict ourselves to repositories with &gt; 50 stars to ensure we con't download a database with malicious code.
* Start from a few formatted tables included as part of StackOverflow top-answered tables or textbook examples, then mutate the columns within rules and readability (e.g., if something looks like an integer, change it within integer bounds.  And keep it coherent numbers -- multiples of 10 within the range of the WHERE conditions)  For strings, we can look for similar terms from WordNet or look for cooccurrence from Google N-grams.
* Scrape SQL tutorials, look for downloadable files with some SQL extension, inspect, and then use as a basis, or for plaintext that's formatted as a table.
* Or use non-SQL data sources.  For example, Microsoft Excel tables that are from tutorial pages, or just collected at random from peers.  See if there are Google Sheets examples.  The formatting of the cells in this case may indicate the datatype of each row.
* Go to some large open data hub such as Enigma.io, and choose several tables at random
