#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
import argparse
import time
import re


logging.basicConfig(level=logging.INFO, format="%(message)s")


def main(logfilename):

    # Print TSV headings
    print '\t'.join(["origin", "path", "text", "start", "end"])
    origin = 'none'

    with open(logfilename) as log:

        log.seek(0, 2)  # seek to the end of the file

        while True:

            line = log.readline()
            if line != '':
                m = re.search("Request for page from origin: (.*)$", line)
                origin = m.group(1) if m is not None else origin

                m = re.search("Path:(.*),,,Text:(.*),,,Range:\[(.*),(.*)\]", line)
                if m is not None:
                    path, text, start, end = m.groups()
                    text = text.replace('\t', '<tab>')  # remove tabs so we can print this as TSV
                    print '\t'.join([origin, path, text, start, end])

            try:
                time.sleep(1)
            except KeyboardInterrupt:
                return


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Watch a server region log and append regions found in" +
        "TSV format to a local data file.")
    parser.add_argument('log', help='path to server log file')
    args = parser.parse_args()
    main(args.log)
