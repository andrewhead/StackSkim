#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
import random


logging.basicConfig(level=logging.INFO, format="%(message)s")
SELECTORS_FILE = 'data/selectors_with_urls_pruned.txt'
SELECTORS_PER_URL = 1


def main():

    random.seed(5424233992901990430)
    selectors = {}
    samples = []

    with open(SELECTORS_FILE) as sel_file:
        for line in sel_file.readlines():
            sel, url = line.strip().split(',,,')
            if url not in selectors.keys():
                selectors[url] = []
            selectors[url].append(sel)

    for url, sel_list in selectors.items():
        random.shuffle(sel_list)
        url_samples = sel_list[:SELECTORS_PER_URL]
        samples.extend(url_samples)

    print '\n'.join(samples)


if __name__ == '__main__':
    main()
