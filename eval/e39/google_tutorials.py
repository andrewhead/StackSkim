#! /usr/bin/env python
# encoding: utf-8

from __future__ import unicode_literals
import json
import cache
import models
from models import Trigram, Page
import os.path
import peewee
import argparse


API_URL = 'https://www.googleapis.com/customsearch/v1'
API_KEY = 'AIzaSyBcHH5JqkalO6atnpCqZCjvFWFiT8-yC8k'
SEARCH_ID = '011356320933563804135:byoi9uglfjg'

# MICROLANGUAGES = ['wget', 'css-selectors']
MICROLANGUAGES = ['regex']
session = cache.get_session()


def save_page(language, query, link, rank, title):
    try:
        pg = Page.create(language=language, query=query, link=link, rank=rank, title=title)
    except peewee.IntegrityError:
        pg = Page.get(Page.language == language, Page.link == link, Page.query == query)
        pg.language = language
        pg.rank = rank
        pg.title = title
        pg.save()


def get_results(pages=300):

    for ml in MICROLANGUAGES:

        ml_results = []
        ml_links = set()

        trigrams = Trigram.select().where(
            (Trigram.tag1 == ml) |
            (Trigram.tag2 == ml) |
            (Trigram.tag3 == ml)
        ).order_by(Trigram.count.desc())

        for tg in trigrams:

            query = ' '.join([tg.tag1, tg.tag2, tg.tag3]) + ' tutorial'
            res = fetch_results(query)

            for rank, r in enumerate(res, 1):
                save_page(ml, query, r['link'], rank, r['title'])

            for r in res:
                if r['link'] not in ml_links:
                    ml_results.append(r)
                    ml_links.add(r['link'])

            if len(ml_results) >= pages:
                break

        write_results_file(os.path.join('search_results', ml + '-results.json'), ml_results)


def fetch_results(query, num_results=10):
    resp = session.get(API_URL, params={
        'q': query,
        'key': API_KEY,
        'cx': SEARCH_ID,
        'num': num_results,
    })
    respJson = resp.json()
    return respJson['items']


def write_results_file(filename, results):

    with open(filename, 'w') as results_file:
        json.dump(results, results_file, indent=2)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Download Google pages for SO tags")
    parser.add_argument('--init', action='store_true', help='create database tables')
    args = parser.parse_args()
    if args.init:
        models.create_tables()
    get_results()
