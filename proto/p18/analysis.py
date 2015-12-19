#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
import markdown
from bs4 import BeautifulSoup
import re

from models import create_tables, Package, ReadmeAnalysis


logging.basicConfig(level=logging.DEBUG, format="%(message)s")


def main():

    for p in Package.select().where(Package.readme != ''):

        readme_text = p.readme
        html = markdown.markdown(readme_text)
        soup = BeautifulSoup(html, 'html.parser')

        # This is a heuristic for word-count.
        # It will be not be precisely correct, depending on your definition of word.
        # For example, a path like 'com.app.example' is split into three words here.
        word_count = len(re.findall('\w+', soup.text))

        # Another heuristic.  As it's typical that inline code examples occur in <pre>
        # blocks, especially in formatted markdown, we count code blocks based
        # on the appearance of <pre> tags.
        code_blocks = soup.find_all('pre')
        block_count = len(code_blocks)

        try:
            analysis = ReadmeAnalysis.get(ReadmeAnalysis.package == p)
        except ReadmeAnalysis.DoesNotExist:
            analysis = ReadmeAnalysis.create(
                package=p, code_count=block_count, word_count=word_count
            )
            logging.debug("Created README analysis for package %s", p.name)
        else:
            analysis.code_count = block_count
            analysis.word_count = word_count
            analysis.save()
            logging.debug("Updated README analysis for package %s", p.name)


if __name__ == '__main__':
    create_tables()
    main()
