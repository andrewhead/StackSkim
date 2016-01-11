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

        # This is a heuristic for word-count.
        # It will be not be precisely correct, depending on your definition of word.
        # For example, a path like 'com.app.example' is split into three words here.
        word_count = len(re.findall('\w+', p.readme))

        # Another heuristic.
        # In reStructuredText (reST), code blocks are introduced by ending a paragraph
        # with a special marker ::. The block must be indented and separated from the
        # surrounding paragraphs by blank lines. Thus, there must be at least two new line
        # characters after the special marker ::.

        # This may prove to be a broken heuristic. In that case, consider using Sphinx:
        # http://www.sphinx-doc.org/en/stable/index.html
        block_count = len(re.findall('::.*\\n\\n', p.readme))

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

    logging.info("Finished analyzing READMEs.")


if __name__ == '__main__':
    create_tables()
    main()
