#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
import random
from selenium import webdriver
import re
import os.path
import argparse

from models import Page

logging.basicConfig(level=logging.INFO, format="%(message)s")
RANDOM_SEED = 2118541086421706986  # random int beneath sys.maxint
LOCALHOST = 'http://127.0.0.1:8000'
random.seed(RANDOM_SEED)
OUTPUT_FILE = 'classes.csv'


def main(start_index):

    page_query = \
        (Page.select()
             .group_by(Page.link)
             .where(
                 Page.language == 'regex',
                 Page.has_example == 1,
                 ))
    pages = [p for p in page_query]
    random.shuffle(pages)

    with open(OUTPUT_FILE, 'a') as outfile:

        browser = webdriver.Firefox()
        print "Press enter to open page.",
        raw_input()
        for i, p in enumerate(pages[start_index:], start=start_index):
            link = build_local_url(p)
            browser.get(link)
            class_ = raw_input("Page {idx} loaded. Type class: ".format(idx=i))
            outfile.write(',,,'.join([link, class_]) + '\n')
            outfile.flush()


def build_local_url(page):

    link = page.link
    link = re.sub('^.*://', '', link)  # strip address type (e.g., http://)
    if not link.endswith('/') and not link.endswith('.html'):
        link += '.html'
    path = os.path.join(
        LOCALHOST,
        'pages',
        page.language,
        page.query,
        str(page.rank),
        link
    )
    return path


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Classify regular expression docs")
    parser.add_argument("--start", type=int, default=0, help="index of document to start at")
    args = parser.parse_args()
    main(args.start)
