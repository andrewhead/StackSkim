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
RANDOM_SEED = 566992051031125479  # random int beneath sys.maxint
LOCALHOST = 'http://127.0.0.1:8000'
random.seed(RANDOM_SEED)
PURPOSES = {
    't': 'targeted end use',
    'm': 'miscellany end use',
    'p': 'pedagogical',
    'i': 'invalid tutorial',
}


def label_pages(start_index, unknown_only=False, purpose=None):

    page_query = \
        (Page.select()
             .group_by(Page.link)
             .where(
                 Page.language == 'regex',
                 Page.has_example == 1,
                 ))
    pages = [p for p in page_query]
    random.shuffle(pages)

    browser = webdriver.Firefox()
    print "Press enter to open page.",
    raw_input()
    for i, p in enumerate(pages[start_index:], start=start_index):

        if ((unknown_only and p.purpose != 'unknown') or
           (purpose is not None and p.purpose != purpose)):
            continue

        link = build_local_url(p)
        browser.get(link)

        pshort = ''
        while pshort not in PURPOSES.keys():
            pshort = raw_input(
                "Page {idx} loaded. Type class ({opts}): "
                .format(idx=i, opts=','.join(PURPOSES.keys())))
            pshort = pshort.lower()

        for same_page in Page.select().where(Page.link == p.link):
            same_page.purpose = PURPOSES[pshort]
            same_page.save()

    print "You have labeled the purposes of all pages."
    browser.close()


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
    parser.add_argument(
        "--start", type=int, default=0,
        help="index of document to start at")
    parser.add_argument(
        "--unknown-only", action='store_true',
        help="whether to label only documents with unknown purpose")
    parser.add_argument("--purpose", help="purpose of tutorials that should be labeled")
    args = parser.parse_args()
    label_pages(args.start, args.unknown_only, args.purpose)
