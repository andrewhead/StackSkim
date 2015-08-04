#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
import codecs


logging.basicConfig(level=logging.INFO, format="%(message)s")


def main():

    with codecs.open('javascript_text.txt', 'r', 'utf-8') as js_file:
        with codecs.open('beautifulsoup_text.txt', 'r', 'utf-8') as bs_file:
            js_text = js_file.read()
            bs_text = bs_file.read()

    for i in range(min([len(js_text), len(bs_text)])):
        if js_text[i] != bs_text[i]:
            print "==== Mismatch at index ====", i
            print "Javascript: ", repr(js_text[i])
            print "BeautifulSoup: ", repr(bs_text[i])
            print "* Javascript before: "
            print repr(js_text[i-50:i])
            print "* BeautifulSoup before: "
            print repr(bs_text[i-50:i])
            print "* Javascript after: "
            print repr(js_text[i:i+50])
            print "* BeautifulSoup after: "
            print repr(bs_text[i:i+50])
            break


if __name__ == '__main__':
    main()
