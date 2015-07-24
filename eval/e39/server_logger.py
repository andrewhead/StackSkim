#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
import argparse
import time
import re


logging.basicConfig(level=logging.INFO, format="%(message)s")


class FileMonitor(object):

    def __init__(self, filename):
        self.filename = filename
        self.log = open(self.filename)
        self.log.seek(0, 2)
        self.current_origin = 'none'

    def get_header(self):
        return '\t'.join(["timestamp", "origin", "path", "text", "start", "end"])

    def get_line(self):
        line = self.log.readline()
        if line != '':
            m = re.search("Request for page from origin: (.*)$", line)
            self.current_origin = m.group(1) if m is not None else self.current_origin
            m = re.search("Path:(.*),,,Text:(.*),,,Range:\[(.*),(.*)\]", line)
            if m is not None:
                path, text, start, end = m.groups()
                text = text.replace('\t', '<tab>')  # remove tabs so we can print this as TSV
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                return '\t'.join([timestamp, self.current_origin, path, start, end, text])
        return None

    def finish(self):
        self.log.close()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description="Watch a server region log and append regions found in" +
        "TSV format to a local data file.")
    parser.add_argument('log', help='path to server log file')
    args = parser.parse_args()

    monitor = FileMonitor(args.log)
    print monitor.get_header()
    while True:
        line = monitor.get_line()
        if line is not None:
            print line
