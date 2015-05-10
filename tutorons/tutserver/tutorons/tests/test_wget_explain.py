#! /usr/bin/env python
# encoding: utf-8

from __future__ import unicode_literals
from tutorons.wget.explain import build_help, explain, Option, optcombo_explain, detect
import unittest
import logging


logging.basicConfig(level=logging.INFO, format="%(message)s")


class BuildArgumentHelpTest(unittest.TestCase):

    def testDescribeRecursiveOption(self):
        msg = build_help(longname='--recursive')
        self.assertEqual(msg, "specify recursive download.")

    def testDescribeOutputOption(self):
        msg = build_help(longname="--output-document", value="outfile")
        self.assertEqual(msg, "write documents to outfile.")

    def testDescribeValuedOptionWithNounPrepended(self):
        msg = build_help(longname="--include-directories", value="mydir")
        self.assertEqual(msg, "mydir is a list of allowed directories.")

    def testDescribeValuedOptionWithNounAppended(self):
        msg = build_help(longname="--config", value="myfile")
        self.assertEqual(msg, "specify config file to use (FILE=myfile).")

    def testDescribeOptionByShortname(self):
        msg = build_help(shortname="-nc")
        self.assertEqual(msg, "skip downloads that would download to existing files (overwriting them).")


class DetectWgetTest(unittest.TestCase):

    def test_detect_wget_from_wgetrc(self):
        self.assertFalse(detect('.wgetrc'))


class BuildCompoundHelpTest(unittest.TestCase):

    def testNoExplanationIfNoCombos(self):
        url = "http://google.com"
        # Random grouping of non-existent arguments
        options = [
            Option('', '--tweedledee', None),
            Option('', '--tweedledum', None),
        ]
        exps = optcombo_explain(url, options)
        self.assertEqual(exps, [])


    def testDescribeUserPwCombination(self):
        url = "http://google.com"
        options = [
            Option('', '--user', 'me'),
            Option('', '--password', 'pw'),
        ]
        exps = optcombo_explain(url, options)
        self.assertEqual(exps, [
            "Authenticate at http://google.com with username 'me' and password 'pw'."
        ])

    def testDescribeRACombination(self):
        url = "http://google.com"
        options = [
            Option('-A', '--accept', '*.jpg'),
            Option('-r', '--recursive', None),
        ]
        exps = optcombo_explain(url, options)
        self.assertEqual(exps, [
            "Recursively scrape web pages linked from http://google.com of type '*.jpg'."
        ])

    def testDescribeRLCombination(self):
        url = "http://google.com"
        options = [
            Option('-l', '--level', '4'),
            Option('-r', '--recursive', None),
        ]
        exps = optcombo_explain(url, options)
        self.assertEqual(exps, [
            "Recursively scrape web pages linked from http://google.com, recursing 4 times."
        ])

    def testDescribeRALCombination(self):
        # Note that this should *not* also generate a description for RA or RL, to avoid redundancy
        url = "http://google.com"
        options = [
            Option('-l', '--level', '4'),
            Option('-A', '--accept', '*.jpg'),
            Option('-r', '--recursive', None),
        ]
        exps = optcombo_explain(url, options)
        self.assertEqual(exps, [
            "Recursively scrape web pages linked from http://google.com of type '*.jpg', following links 4 times."
        ])


if __name__ == '__main__':
    unittest.main()
