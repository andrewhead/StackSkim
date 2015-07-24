#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
from models import Page
from urlparse import urlparse


logging.basicConfig(level=logging.INFO, format="%(message)s")


def main():
    print '\t'.join(['domain', 'language', 'query', 'has_example', 'notfound'])
    for page in Page.select().group_by(Page.link):
        print '\t'.join(str(_) for _ in [
            urlparse(page.link).netloc,
            page.language,
            page.query,
            page.has_example,
            page.notfound,
        ])


if __name__ == '__main__':
    main()
