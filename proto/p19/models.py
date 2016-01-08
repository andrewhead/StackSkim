#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
from peewee import Model, SqliteDatabase, CharField, IntegerField, TextField, ForeignKeyField


logging.basicConfig(level=logging.INFO, format="%(message)s")
db = SqliteDatabase('packages.db')


class Package(Model):
    name = CharField(index=True)
    repository_url = CharField(null=True, default=None)
    page_no = IntegerField(null=True, default=None)
    readme = TextField(null=True, default=None)

    # PyPI data
    description = CharField(null=True, default=None)
    day_download_count = IntegerField(null=True, default=None)
    week_download_count = IntegerField(null=True, default=None)
    month_download_count = IntegerField(null=True, default=None)

    class Meta:
        database = db


class ReadmeAnalysis(Model):

    package = ForeignKeyField(Package)
    code_count = IntegerField(default=None)
    word_count = IntegerField(default=None)

    class Meta:
        database = db


def create_tables():
    db.create_tables([Package, ReadmeAnalysis], safe=True)
