#! /bin/bash

sqlite3 packages.db <<COMMANDS

.headers on
.mode csv

.output data/packages.csv
SELECT
  name,
  description,
  day_download_count,
  week_download_count,
  month_download_count,
FROM package
WHERE readme IS NOT NULL;

.output data/analysis.csv
SELECT
  package_id,
  code_count,
  word_count
FROM readmeanalysis;

COMMANDS
