#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
import requests
from bs4 import BeautifulSoup
import argparse
import codecs
import json
import os.path


logging.basicConfig(level=logging.INFO, format="%(message)s")
DEFAULT_PUBLICATIONS = [
    'ICSE',
    'IEEE_Trans._Software_Eng.',
    'ACM_Trans._Softw._Eng._Methodol.',
    'CHI',
    'ICPC',
    'IWPC',
]

FETCH_DIR = 'titles'
if not os.path.exists(FETCH_DIR):
    os.makedirs(FETCH_DIR)
data_fname = lambda pub: os.path.join(FETCH_DIR, pub + '.tsv')


class FileStore(object):

    def __init__(self, fname):
        self.fname = fname
        self.file_ = None

    def writeline(self, title, venue, year, authors):
        self.file_.write(
            '\t'.join([title, venue, year, authors]) + '\n'
        )

    def __enter__(self):
        self.file_ = codecs.open(self.fname, 'w', encoding='utf8')
        self.writeline("Title", "Venue", "Year", "Authors")
        return self

    def __exit__(self, type, value, traceback):
        self.file_.close()

    def save_entry(self, entry):
        title = entry.select('span.title')[0].text
        venues = entry.select('span[itemprop=isPartOf]')
        venue = venues[0].text if len(venues) > 0 else ''
        year = entry.select('span[itemprop=datePublished]')[0].text
        authors = [
            a.text for a in
            entry.select('span[itemprop=author]')
        ]
        self.writeline(title, venue, year, json.dumps(authors))


def fetch_papers(publication, storefunc):

    # This scrapes 1000 titles from dblp
    # It seems like we can only fetch 1000 lines at a time
    # Change 'f' to set the starting point of the download

    BATCH_SIZE = 1000
    batch_start = 0
    fetch_more = True

    while fetch_more:

        resp = requests.get(
            'http://dblp.uni-trier.de/search/publ/inc',
            params={
                'q': 'venue:{venue}:'.format(venue=publication),
                'h': BATCH_SIZE,
                'f': batch_start,
                's': 'yvpc'
            })

        soup = BeautifulSoup(resp.content, 'lxml')
        entries = soup.select('.entry')
        for e in entries:
            storefunc(e)

        fetch_more = (len(entries) > 0)
        batch_start += len(entries)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Fetch titles of all papers from a publication.")
    parser.add_argument('--pub', help='The name of the publication')
    args = parser.parse_args()

    if args.pub:
        with FileStore(data_fname(args.pub)) as datafile:
            fetch_papers(args.pub, datafile.save_entry)
    else:
        for pub in DEFAULT_PUBLICATIONS:
            with FileStore(data_fname(pub)) as datafile:
                fetch_papers(pub, datafile.save_entry)
