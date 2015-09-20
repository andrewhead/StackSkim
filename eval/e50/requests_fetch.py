#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
import requests


logging.basicConfig(level=logging.INFO, format="%(message)s")
OUT_FILE = 'requests_version.html'
URL = 'http://127.0.0.1:8000/pages/wget/curl%20php%20wget%20tutorial/8/www.drupal.org/node/23714.html'  # noqa


def main():
    page = requests.get(URL)
    with open(OUT_FILE, 'w') as outfile:
        outfile.write(page.content)


if __name__ == '__main__':
    main()
