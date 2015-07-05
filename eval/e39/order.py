#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
import random
import math
import argparse
from models import Page


logging.basicConfig(level=logging.INFO, format="%(message)s")
VALIDATION_RATIO = .5  # percent of pages in validation set
SEED1 = 1


def order_pages(language, random_seed):

    random.seed(random_seed)
    pages = (Page.select()
             .group_by(Page.link)
             .where(
                 Page.language == language,
                 Page.has_example == 1,
                 ))

    ids = [p.id for p in pages]
    random.shuffle(ids)
    ordered_pages = [Page.get(Page.id == id_) for id_ in ids]
    return ordered_pages


def get_test_lists(language, ratio=VALIDATION_RATIO, random_seed=SEED1):

    pages = order_pages(language, random_seed)
    num_pages = len(pages)
    split_index = int(math.floor(num_pages * ratio))
    return {
        'validation': pages[:split_index],
        'test': pages[split_index:],
    }


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Get order of tutorials")
    parser.add_argument('language', help="which language to fetch tutorial order for")
    parser.add_argument('set', help="which set to fetch {'validation', 'test'}")
    args = parser.parse_args()

    lists = get_test_lists(args.language)
    links = [p.link for p in lists[args.set]]
    print ' '.join(links)
