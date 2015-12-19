#! /bin/bash

sqlite3 packages.db <<COMMANDS

.headers on
.mode csv

.output data/packages.csv
SELECT 
  id, 
  name, 
  page_no, 
  stargazers_count,
  forks_count,
  open_issues_count,
  has_wiki,
  subscribers_count,
  github_contributions_count
FROM package;

.output data/analysis.csv
SELECT 
  package_id,
  code_count,
  word_count
FROM readmeanalysis;

COMMANDS
