#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
import cache
from bs4 import BeautifulSoup, Tag, NavigableString
import tokenize
import re
from StringIO import StringIO
import argparse
from progressbar import ProgressBar, Percentage, Bar, RotatingMarker, ETA, Counter

import models
from models import Page, Snippet, Token, Comment, SnippetComment, SnippetToken
from sites import SITES


logging.basicConfig(level=logging.INFO, format="%(message)s")
HEADER_TAGS = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
TEXT_TAGS = ['p', 'div']
NONTEXT_TAGS = ['script']
requests_session = cache.get_session()


def extract_code(node):
    code_text = node.text
    code_text = re.sub('^>>> ', '', code_text, flags=re.MULTILINE)
    code_text = re.sub('^\.\.\. ', '', code_text, flags=re.MULTILINE)
    return code_text


def is_text(text):
    # The heuristic we use here is that we only consider a string to be a textual description
    # if it contains at least two consecutive alphabetic letters
    if not re.match('[A-Za-z]{2}', text):
        return False
    return True


def extract_text(node, node_iterator):
    '''
    Extract the first text found from an iterator of nodes.  Return None if no nodes contain
    text, or if a header is reached before text is found.
    '''

    def _parents(n):
        return [p for p in n.parents]

    parents = _parents(node)
    descendants = [d for d in node.descendants]
    lineage = parents + descendants

    for n in node_iterator:
        if n not in lineage:
            if type(n) == Tag:
                if n.name in TEXT_TAGS and is_text(n.text):
                    return n.text
                elif n.name in HEADER_TAGS:
                    return None
            elif type(n) == NavigableString and is_text(unicode(n)):
                parent_tags = [p.name for p in _parents(n) if hasattr(p, 'name')]
                if not set(parent_tags).intersection(HEADER_TAGS + NONTEXT_TAGS):
                    return unicode(n)

    return None


def extract_text_above(node):
    return extract_text(node, node.previous_elements)


def extract_text_below(node):
    return extract_text(node, node.next_elements)


def extract_header_above(node):
    for sib in node.previous_siblings:
        if type(sib) == Tag and sib.name in HEADER_TAGS:
            return sib.text
    return None


class TokenizeError(Exception):
    pass


def tokenize_string(string):
    buff = StringIO(string)
    try:
        for tok in tokenize.generate_tokens(buff.readline):
            yield tok
    except tokenize.TokenError:
        pass
    except IndentationError:
        raise TokenizeError


def extract_tokens(node):

    code = extract_code(node)
    token_generator = tokenize_string(code)
    tokens = []

    while True:
        try:
            (_, tok_str, _, _, _) = token_generator.next()
        except (StopIteration, TokenizeError):
            break
        else:
            tokens.append(tok_str)

    return tokens


def extract_comments(node):

    code = extract_code(node)
    comments = []
    token_generator = tokenize_string(code)

    while True:
        try:
            (tok_type, tok_str, _, _, _) = token_generator.next()
        except (StopIteration, TokenizeError):
            break
        else:
            if tok_type == tokenize.COMMENT:
                stripped = re.sub('#\s*', '', tok_str)
                comments.append(stripped)
            elif tok_type == tokenize.STRING:
                BLOCK_COMMENT_PATT = r'^(\'{3}|"{3})(.*)(\1)$'
                if re.match(BLOCK_COMMENT_PATT, tok_str, flags=re.DOTALL):
                    stripped = re.sub(BLOCK_COMMENT_PATT, r'\2', tok_str, flags=re.DOTALL)
                    comments.append(stripped)

    return comments


def save_snippet(node, page):

    snippet = Snippet.create(
        page=page,
        text_above=extract_text_above(node),
        text_below=extract_text_below(node),
        header=extract_header_above(node),
        code=extract_code(node),
        line_count=len(node.text.split('\n')),
    )

    for tok_str in extract_tokens(node):
        token, _ = Token.get_or_create(string=tok_str)
        SnippetToken.create(
            snippet=snippet,
            token=token,
        )

    for comment_str in extract_comments(node):
        comment, _ = Comment.get_or_create(string=comment_str)
        SnippetComment.create(
            snippet=snippet,
            comment=comment,
        )

    return snippet


def main():

    ''' Set up progress bar. '''
    page_count = reduce(lambda cnt, site: cnt + len(site['pages']), SITES, 0)
    widgets = [
        'Progress: ', Percentage(), ' ', Bar(marker=RotatingMarker()), ' ', ETA(),
        '  Saved ', Counter(), '/', str(page_count), ' sites.'
    ]
    pbar = ProgressBar(widgets=widgets, maxval=page_count)
    pbar.start()
    page_index = 0

    for site in SITES:

        selector = site['selector']

        for url in site['pages']:

            resp = requests_session.get(url)
            soup = BeautifulSoup(resp.text, 'lxml')
            page = Page.create(
                text=soup.text,
                location=url,
                title=soup.title.text if soup.title is not None else ''
            )

            code_nodes = soup.select(selector)
            for node in code_nodes:
                save_snippet(node, page)

            page_index += 1
            pbar.update(page_index)

    pbar.finish()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Fetch snippets and save code and text")
    args = parser.parse_args()

    if Page.table_exists():
        print "Data exists!  Truncate tables to continue? (y/n): ",
        decision = raw_input()
        if decision == 'y':
            print "Truncating tables."
            models.drop_tables()
        else:
            raise SystemExit("Leaving tables alone.  Now exiting.")

    models.create_tables()
    main()
