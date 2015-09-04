#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging


logging.basicConfig(level=logging.INFO, format="%(message)s")
INPUT_FILE = 'jquery_validation_50.txt'


def main():

    with open(INPUT_FILE) as ifile:

        old_seen = set()
        new_seen = set()
        new_unique = set()
        seen = set()
        lines = ifile.read()

        for l in lines.split('\n'):

            tokens = l.strip().split(',,,')
            if len(tokens[0]) == 0:
                continue
            url = tokens[3]
            abs_start = tokens[4]
            abs_end = tokens[5]

            id_tuple = (url, abs_start, abs_end)
            if id_tuple not in seen:
                seen.add(id_tuple)

            if id_tuple not in old_seen and len(tokens) < 7:
                old_seen.add(id_tuple)
            if id_tuple not in new_seen and len(tokens) >= 7:
                new_seen.add(id_tuple)
                if id_tuple not in old_seen:
                    new_unique.add(id_tuple)
                    print tokens[6]

        print len(old_seen)
        print len(new_seen)
        print len(new_unique)
        print len(seen)


if __name__ == '__main__':
    main()
