#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
import argparse
import cache
import peewee
from models import Bigram, Trigram, create_tables


logging.basicConfig(level=logging.INFO, format="%(message)s")
session = cache.get_session()
TARGET_TAGS = ['wget', 'regex', 'css-selectors']


def make_url(tags):
    tag_string = ';'.join(tags)
    return 'https://api.stackexchange.com/2.2/tags/{tags}/related'.format(tags=tag_string)


def fetch_bigrams():
    for tag in TARGET_TAGS:
        resp = session.get(make_url([tag]), params={
            'pagesize': 100,
            'site': 'stackoverflow',
        })
        respJson = resp.json()
        for i in respJson['items']:
            bg, _ = Bigram.get_or_create(tag1=tag, tag2=i['name'])
            bg.count = i['count']
            bg.save()


def fetch_trigrams():

    for tag in TARGET_TAGS:

        # This manual transfer to a list seems necessary, instead of interating
        # through the selected lines, due to an exception that is thrown
        # in the latter case.
        tag_pairs = []
        for bg in Bigram.select().where(Bigram.tag1 == tag):
            tag_pairs.append((bg.tag1, bg.tag2))

        for pair in tag_pairs:
            resp = session.get(make_url([pair[0], pair[1]]), params={
                'pagesize': 100,
                'site': 'stackoverflow',
            })
            respJson = resp.json()
            if 'items' not in respJson.keys():
                continue

            for i in respJson['items']:
                tags = [pair[0], pair[1], i['name']]
                tags_ord = sorted(tags)
                try:
                    tg = Trigram.create(tag1=tags_ord[0], tag2=tags_ord[1], tag3=tags_ord[2])
                except peewee.IntegrityError:
                    tg = Trigram.get(
                        Trigram.tag1 == tags_ord[0],
                        Trigram.tag2 == tags_ord[1],
                        Trigram.tag3 == tags_ord[2],
                    )
                tg.count = i['count']
                tg.save()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Download n-grams of StackOverflow tags")
    parser.add_argument('--init', action='store_true', help='create database tables')
    parser.add_argument('--tri', help='print top 3-grams for a tag')
    args = parser.parse_args()

    if args.tri:
        tgs = Trigram.select().where(
            (Trigram.tag1 == args.tri) |
            (Trigram.tag2 == args.tri) |
            (Trigram.tag3 == args.tri)
        ).order_by(Trigram.count.desc()).limit(10)
        for tg in tgs:
            print ' '.join([tg.tag1, tg.tag2, tg.tag3])
    else:
        if args.init:
            create_tables()
        fetch_bigrams()
        fetch_trigrams()
