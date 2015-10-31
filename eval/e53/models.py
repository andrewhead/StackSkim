#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from peewee import SqliteDatabase, Model
from peewee import CharField, IntegerField, TextField, ForeignKeyField


db = SqliteDatabase('snippets.db')


class Page(Model):
    text = TextField()
    location = CharField(unique=True)
    title = CharField()

    class Meta:
        database = db


class Token(Model):
    string = CharField(unique=True)

    class Meta:
        database = db


class Comment(Model):
    string = CharField(unique=True)

    class Meta:
        database = db


class Snippet(Model):
    page = ForeignKeyField(Page)
    text_above = TextField(null=True)
    text_below = TextField(null=True)
    header = CharField(null=True)
    code = TextField()
    line_count = IntegerField()

    class Meta:
        database = db


class SnippetToken(Model):
    snippet = ForeignKeyField(Snippet)
    token = ForeignKeyField(Token)

    class Meta:
        database = db


class SnippetComment(Model):
    snippet = ForeignKeyField(Snippet)
    comment = ForeignKeyField(Comment)

    class Meta:
        database = db


TABLES = [
    Page,
    Token,
    Comment,
    Snippet,
    SnippetToken,
    SnippetComment,
]


def create_tables():
    db.create_tables(TABLES, safe=True)


def drop_tables():
    db.drop_tables(TABLES, safe=True)
