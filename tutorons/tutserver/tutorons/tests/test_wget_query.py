#! /usr/bin/env python
# encoding: utf-8

from __future__ import unicode_literals
import unittest
import logging
import json
from django.test import Client


logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestRenderDescription(unittest.TestCase):

    def setUp(self):
        self.client = Client()

    def get_resp_data(self, payload):
        resp = self.client.post('/wget', content_type='raw', data=payload)
        return json.loads(resp.content)

    def request_short(self, command):
        return self.get_resp_data("\n".join(["<code>", command, "</code>"]))

    def test_describe_one_command(self):
        result = self.request_short("wget http://hello.html")
        self.assertEqual(len(result.keys()), 1)
        self.assertIn("    Here, it downloads content from http://hello.html.",
            result['wget http://hello.html'])

    def test_describe_multiple_commands(self):
        result = self.get_resp_data("""
        <html>
            <body>
                <code>
                    wget http://hello.html
                </code>
                <code>
                    wget http://goodbye.html
                </code>
            </body>
        </html>
        """)
        self.assertEqual(len(result.keys()), 2)
        self.assertIn("    Here, it downloads content from http://hello.html.", 
            result['wget http://hello.html'])
        self.assertIn("    Here, it downloads content from http://goodbye.html.",
            result['wget http://goodbye.html'])

    def test_skip_lines_without_wget(self):
        result = self.get_resp_data("""
        <code>
            wget http://hello.html
            notwget http:/hello.html

        </code>
        """)
        self.assertEqual(len(result.keys()), 1)

    def test_skip_invalid_wget(self):
        result = self.request_short("wget --buzzer fakearg")
        self.assertEqual(len(result.keys()), 0)

    def test_describe_negative_flag(self):
        result = self.request_short("wget -nc http://hello.html")
        self.assertIn("skip downloads that would download to", result['wget -nc http://hello.html'])

    def test_describe_windows_executable(self):
        result = self.request_short("wget.exe http://hello.html")
        self.assertEqual(len(result.keys()), 1)
        self.assertIn('\n'.join([
                "    <span class=\"word_focus\">wget</span> is a Terminal command you run to " +
                    "download a page from the Internet.",
                "    Here, it downloads content from http://hello.html.",
            ]),
            result['wget.exe http://hello.html'])

    def test_describe_options(self):
        result = self.request_short("wget -A *.jpg -l3 http://google.com")
        description = result.values()[0]
        self.assertIn("<p>It uses these options:</p>", description)
        self.assertIn("--accept", description)
        self.assertIn("-A", description)
        self.assertIn(": *.jpg is a comma-separated list of accepted extensions.", description)
        self.assertIn("3 is a maximum recursion depth (inf or 0 for infinite)", description) 

    def testDescribeOptionCombination(self):
        result = self.request_short("wget --recursive -A *.jpg -l3 http://google.com")
        self.assertIn(
            "Recursively scrape web pages linked from http://google.com of type '*.jpg', " +
            "following links 3 times.", 
            result.values()[0])

    def testNoShowShortnameIfOptHasNoShortname(self):
        result = self.request_short("wget --retry-connrefused")
        description = result.values()[0]
        self.assertNotIn('>-r', description)
