#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
import os.path
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import codecs


INPUT_FILE = os.path.join('data', 'jquery_validation_44.txt')
OUTPUT_FILE = os.path.join('data', 'selectors.txt')


logging.basicConfig(level=logging.INFO, format="%(message)s")


class Record(object):

    def __init__(self, element, start_offset, end_offset):
        self.element = element
        self.start_offset = start_offset
        self.end_offset = end_offset

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
                and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self.__eq__(other)


def get_text(browser, element, start_offset, end_offset):
    GET_TEXT_SCRIPT = """
var node = document.querySelector('{element}');
return node.textContent.substring({start}, {end} + 1)
"""
    text = browser.execute_script(GET_TEXT_SCRIPT.format(
        element=element, start=start_offset, end=end_offset))
    return text


def main():

    records = {}
    keys_seen = []

    with open(INPUT_FILE) as sel_file:

        for line in sel_file.read().split('\r'):

            stripped = line.strip()
            tokens = stripped.split('\t')
            if len(tokens) <= 1:
                continue
            start_offset = int(tokens[0])
            end_offset = int(tokens[1])
            element = tokens[2]
            url = tokens[3]
            aso = int(tokens[4])
            aeo = int(tokens[5])
            rec = Record(element, start_offset, end_offset)
            key = (url, aso, aeo)

            # We take advantage of the fact that the first time that a
            # URL, absolute offset pair appears in the current data
            # file, this is the most specific (lowest-level node in the
            # document) at which it appears.  So we get the text from this
            # low level node, and don't let it get pulled again.
            if key not in keys_seen:
                if url not in records.keys():
                    records[url] = []
                records[url].append(rec)
                keys_seen.append(key)

    with codecs.open(OUTPUT_FILE, 'w', 'utf-8') as out_file:
        browser = webdriver.Firefox()
        for url, url_records in records.items():
            browser.get(url)
            for rec in url_records:
                try:
                    text = get_text(browser, rec.element, rec.start_offset, rec.end_offset)
                except WebDriverException:
                    logging.warn(
                        "Failed to download region: %s,%s,%d,%d",
                        url, rec.element, rec.start_offset, rec.end_offset)
                else:
                    out_file.write(text + '\n')
                    print text


if __name__ == '__main__':
    main()
