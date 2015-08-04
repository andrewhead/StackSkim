#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
from bs4 import BeautifulSoup
import codecs


logging.basicConfig(level=logging.INFO, format="%(message)s")


def main():
    with codecs.open('drupal_page.html', 'r', 'utf-8') as drupal_file,\
            codecs.open('soup_text.txt', 'w', 'utf-8') as soup_file:
        soup = BeautifulSoup(drupal_file.read())
        text = soup.text
        soup_file.write(text)


if __name__ == '__main__':
    main()
