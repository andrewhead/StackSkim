#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
import sqlparse


logging.basicConfig(level=logging.INFO, format="%(message)s")
QUERIES = [
    "SELECT image FROM graphics WHERE field = '$value' AND anotherfield = '$anothervalue' ORDER BY position;",
    "SELECT * FROM feed WHERE url='http://feeds.feedburner.com/Tutorialzine' LIMIT 2",
    "SELECT email FROM $tablename WHERE email = '$email'",
]


def main():
    
    


if __name__ == '__main__':
    main()
