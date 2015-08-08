#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from peewee import Model, CharField, IntegerField, SqliteDatabase, BooleanField
import os.path


db = SqliteDatabase(os.path.join(os.pardir, 'e39', 'test_pages.db'))


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
