#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
import unittest
from bs4 import BeautifulSoup

from get_snippets import extract_text_above, extract_text_below, extract_header_above,\
    extract_tokens, extract_comments, extract_code, is_text


logging.basicConfig(level=logging.INFO, format="%(message)s")


def make_doc(self, *lines):
    return BeautifulSoup('\n'.join(lines), 'lxml')


def get_code_node(self, *lines):
    soup = make_doc(*lines)
    return soup.code


class ExtractCodeTest(unittest.TestCase):

    def test_clean_interactive_carets(self):
        code_node = get_code_node(
            "<html>",
            "  <body>",
            "    <p>Text above</p>",
            "    <code>&gt;&gt;&gt; print 'Hello'</code>",
            "  </body>",
            "</html>",
        )
        code = extract_code(code_node)
        self.assertEqual(code, "print 'Hello'")

    def test_clean_interactive_carets_on_multiple_lines(self):
        code_node = get_code_node(
            "<html>",
            "  <body>",
            "    <p>Text above</p>",
            "    <code>&gt;&gt;&gt; print 'Hello'",
            "&gt;&gt;&gt; print 'Goodbye'</code>",
            "  </body>",
            "</html>",
        )
        code = extract_code(code_node)
        self.assertEqual(code, "print 'Hello'\nprint 'Goodbye'")

    def test_clean_interactive_ellipses(self):
        code_node = get_code_node(
            "<html>",
            "  <body>",
            "    <p>Text above</p>",
            "    <code>...     pass</code>",
            "  </body>",
            "</html>",
        )
        code = extract_code(code_node)
        self.assertEqual(code, "    pass")

    def test_leave_midline_carets(self):
        code_node = get_code_node(
            "<html>",
            "  <body>",
            "    <p>Text above</p>",
            "    <code>print 'Hello &gt;&gt;&gt; all!'</code>",
            "  </body>",
            "</html>",
        )
        code = extract_code(code_node)
        self.assertEqual(code, "print 'Hello >>> all!'")


class TextCheckTest(unittest.TestCase):

    def test_is_not_text_if_just_numbers(self):
        self.assertFalse(is_text(" 1\n 2\n 3\n"))

    def test_is_not_text_if_just_numbered_list(self):
        self.assertFalse(is_text("1.\n2.\n3.\n"))

    def test_is_not_text_if_just_space(self):
        self.assertFalse(is_text(" \t\t\n"))

    def test_alphabetic_message_is_text(self):
        self.assertTrue(is_text("hello"))


class ExtractTextTest(unittest.TestCase):

    def test_get_text_above_from_p(self):
        code_node = get_code_node(
            "<html>",
            "  <body>",
            "    <p>Text above</p>",
            "    <code>This is code</code>",
            "  </body>",
            "</html>",
        )
        text = extract_text_above(code_node)
        self.assertEqual(text, "Text above")

    def test_get_text_above_from_p_multiple_siblings_away(self):
        code_node = get_code_node(
            "<html>",
            "  <body>",
            "    <p>Text above</p>",
            "    <script>var i = 0;</script>",
            "    <code>This is code</code>",
            "  </body>",
            "</html>",
        )
        text = extract_text_above(code_node)
        self.assertEqual(text, "Text above")

    def test_get_text_above_from_div(self):
        code_node = get_code_node(
            "<html>",
            "  <body>",
            "    <div>Text above</div>",
            "    <code>This is code</code>",
            "  </body>",
            "</html>",
        )
        text = extract_text_above(code_node)
        self.assertEqual(text, "Text above")

    def test_get_text_above_from_aunt_node(self):
        code_node = get_code_node(
            "<html>",
            "  <body>",
            "    <p>Text above</p>",
            "    <div>",
            "      <code>This is code</code>",
            "    </div>",
            "  </body>",
            "</html>",
        )
        text = extract_text_above(code_node)
        self.assertEqual(text, "Text above")

    def test_get_none_if_no_text_above(self):
        code_node = get_code_node(
            "<html>",
            "  <body>",
            "    <code>This is code</code>",
            "  </body>",
            "</html>",
        )
        text = extract_text_above(code_node)
        self.assertIsNone(text)

    def test_get_none_if_no_text_below_header_above(self):
        code_node = get_code_node(
            "<html>",
            "  <body>",
            "    <p>Text above</p>",
            "    <h2>Header</h2>",
            "    <code>This is code</code>",
            "  </body>",
            "</html>",
        )
        text = extract_text_above(code_node)
        self.assertIsNone(text)

    def test_do_not_get_text_above_from_plain_string_in_parent(self):
        code_node = get_code_node(
            "<html>",
            "  <body>",
            "    <div>Text before<code>This is code</code></div>",
            "  </body>",
            "</html>",
        )
        text = extract_text_above(code_node)
        self.assertIsNone(text)

    '''
    As the next methods on extracting the text below a code node rely on the
    same mechanisms as extracting the text above a code node, we test a few cases
    here, without being comprehensive, leaving that for the examples above.
    '''
    def test_get_text_below_from_p(self):
        code_node = get_code_node(
            "<html>",
            "  <body>",
            "    <code>This is code</code>",
            "    <p>Text below</p>",
            "  </body>",
            "</html>",
        )
        text = extract_text_below(code_node)
        self.assertEqual(text, "Text below")

    def test_get_text_below_from_div(self):
        code_node = get_code_node(
            "<html>",
            "  <body>",
            "    <code>This is code</code>",
            "    <p>Text below</p>",
            "  </body>",
            "</html>",
        )
        text = extract_text_below(code_node)
        self.assertEqual(text, "Text below")


class ExtractHeaderTest(unittest.TestCase):

    def test_get_header_type_h6_above(self):
        code_node = get_code_node(
            "<html>",
            "  <body>",
            "    <h6>Header</h6>",
            "    <code>This is code</code>",
            "  </body>",
            "</html>",
        )
        text = extract_header_above(code_node)
        self.assertEqual(text, "Header")

    def test_get_header_type_h2_above(self):
        code_node = get_code_node(
            "<html>",
            "  <body>",
            "    <h2>Header</h2>",
            "    <code>This is code</code>",
            "  </body>",
            "</html>",
        )
        text = extract_header_above(code_node)
        self.assertEqual(text, "Header")

    def test_get_header_several_siblings_above(self):
        code_node = get_code_node(
            "<html>",
            "  <body>",
            "    <h2>Header</h2>",
            "    <p>Text between</p>",
            "    <code>This is code</code>",
            "  </body>",
            "</html>",
        )
        text = extract_header_above(code_node)
        self.assertEqual(text, "Header")

    def test_get_header_from_aunt_node(self):
        code_node = get_code_node(
            "<html>",
            "  <body>",
            "    <h2>Header</h2>",
            "    <div>",
            "      <code>This is code</code>",
            "    </div>",
            "  </body>",
            "</html>",
        )
        text = extract_header_above(code_node)
        self.assertEqual(text, "Header")

    def test_get_header_none_if_no_header(self):
        code_node = get_code_node(
            "<html>",
            "  <body>",
            "    <code>This is code</code>",
            "  </body>",
            "</html>",
        )
        text = extract_header_above(code_node)
        self.assertIsNone(text)


class GetTokensTest(unittest.TestCase):

    def test_extract_tokens(self):
        code_node = get_code_node(
            "<html>",
            "  <body>",
            "    <code>for i in range(0, 1):",
            "    print \"Hello world\"</code>",
            "  </body>",
            "</html>",
        )
        tokens = extract_tokens(code_node)
        self.assertEqual(
            tokens,
            ['for', 'i', 'in', 'range', '(', '0', ',', '1', ')', ':', '\n', '    ', 'print',
             '"Hello world"', '', ''])

    def test_accept_unfinished_docstrings(self):
        code_node = get_code_node(
            "<html>",
            "  <body>",
            "    <code>print 'Hello'",
            "'''",
            "docstring</code>",
            "  </body>",
            "</html>",
        )
        tokens = extract_tokens(code_node)
        self.assertEqual(
            tokens,
            ['print', '\'Hello\'', '\n']
        )

    def test_get_partial_results_upon_indentation_error(self):
        code_node = get_code_node(
            "<html>",
            "  <body>",
            "    <code>for i in l:",
            "    pass",
            "  print 'Hello'",
            "</code>",
            "  </body>",
            "</html>",
        )
        tokens = extract_tokens(code_node)
        self.assertEqual(
            tokens,
            ['for', 'i', 'in', 'l', ':', '\n', '    ', 'pass', '\n']
        )


class ExtractCommentsTest(unittest.TestCase):

    def test_extract_inline_comment(self):
        code_node = get_code_node(
            "<html>",
            "  <body>",
            "    <code>print 'hello'  # inline comment</code>",
            "  </body>",
            "</html>",
        )
        comments = extract_comments(code_node)
        self.assertEqual(comments, ["inline comment"])

    def test_extract_multiple_inline_comments(self):
        code_node = get_code_node(
            "<html>",
            "  <body>",
            "    <code>print 'hello'  # comment 1",
            "print 'hello'  # comment 2</code>",
            "  </body>",
            "</html>",
        )
        comments = extract_comments(code_node)
        self.assertEqual(comments, ["comment 1", "comment 2"])

    def test_extract_block_comment(self):
        code_node = get_code_node(
            "<html>",
            "  <body>",
            "    <code>'''",
            "Multi-",
            "line",
            "comment.",
            "'''</code>",
            "  </body>",
            "</html>",
        )
        comments = extract_comments(code_node)
        self.assertEqual(comments, ["\nMulti-\nline\ncomment.\n"])

    def test_ignore_plain_string(self):
        code_node = get_code_node(
            "<html>",
            "  <body>",
            "    <code>print 'hello'",
            "'''"
            "Multi-",
            "line",
            "comment.",
            "'''</code>",
            "  </body>",
            "</html>",
        )
        comments = extract_comments(code_node)
        self.assertEqual(len(comments), 1)

    def test_get_partial_results_upon_indentation_error(self):
        code_node = get_code_node(
            "<html>",
            "  <body>",
            "    <code>for i in l:",
            "    pass",
            "    # comment",
            "  print 'Hello'",
            "</code>",
            "  </body>",
            "</html>",
        )
        comments = extract_comments(code_node)
        self.assertEqual(comments, ['comment'])


if __name__ == '__main__':
    unittest.main()
