#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
from peewee import Model, SqliteDatabase,\
    CharField, IntegerField, TextField, ForeignKeyField, BooleanField


logging.basicConfig(level=logging.INFO, format="%(message)s")
db = SqliteDatabase('packages.db')


class Package(Model):

    name = CharField()
    repository_url = CharField(null=True)
    page_no = IntegerField()
    readme = TextField(default='')

    # Github fields
    stargazers_count = IntegerField(null=True, default=None)
    forks_count = IntegerField(null=True, default=None)
    open_issues_count = IntegerField(null=True, default=None)
    has_wiki = BooleanField(null=True, default=None)
    subscribers_count = IntegerField(null=True, default=None)
    github_contributions_count = IntegerField(null=True, default=None)

    class Meta:
        database = db


class ReadmeAnalysis(Model):

    package = ForeignKeyField(Package)
    code_count = IntegerField(default=-1)
    word_count = IntegerField(default=-1)

    class Meta:
        database = db


def create_tables():
    db.create_tables([Package, ReadmeAnalysis], safe=True)
