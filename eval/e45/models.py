#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from peewee import Model, CharField, IntegerField, SqliteDatabase, BooleanField


db = SqliteDatabase('test_pages.db')


class Bigram(Model):
    tag1 = CharField()
    tag2 = CharField()
    count = IntegerField(default=0)

    class Meta:
        database = db


class Trigram(Model):
    tag1 = CharField()
    tag2 = CharField()
    tag3 = CharField()
    count = IntegerField(default=0)

    class Meta:
        database = db
        indexes = (
            (('tag1', 'tag2', 'tag3'), True),
        )


class Page(Model):
    language = CharField()
    query = CharField()
    link = CharField()
    rank = IntegerField()
    title = CharField()
    dest = CharField(default='')
    has_example = BooleanField(null=True)
    notfound = BooleanField(null=True)

    class Meta:
        database = db
        indexes = (
            (('language', 'link', 'query'), True),
        )


def create_tables():
    db.create_tables([Bigram, Trigram, Page], safe=True)
