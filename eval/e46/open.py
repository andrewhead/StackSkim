#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
import argparse
import os.path
import re
import requests
import subprocess
from models import Page
from order import get_test_lists


logging.basicConfig(level=logging.INFO, format="%(message)s")
logging.getLogger('requests').setLevel(logging.WARNING)
PWD = os.path.dirname(os.path.realpath(__file__))
LOCALHOST = 'http://127.0.0.1:8000'
STATUS_NO_PAGES = 2


class ServerNotRunningException(Exception):

    def __init__(self):
        self.message = \
            '\n'.join([
                "",
                "=== ERROR: No fileserver running. ===",
                "Run these commands in another shell:",
                "",
                "cd " + str(PWD),
                "python -m SimpleHTTPServer 8000",
                "",
            ])


def build_local_url(page):
    link = page.link
    link = re.sub('^.*://', '', link)  # strip address type (e.g., http://)
    if not link.endswith('/') and not link.endswith('.html'):
        link += '.html'
    path = os.path.join(
        LOCALHOST,
        'pages',
        page.language,
        page.query,
        str(page.rank),
        link
    )
    return path


def check_server_running():
    ''' Make sure that server is running. '''
    try:
        requests.get(LOCALHOST)
    except requests.ConnectionError:
        raise ServerNotRunningException


def page_at_index(index):
    page = (Page
            .select()
            .where(
                (Page.purpose == 'targeted end use') |
                (Page.purpose == 'miscellany end use')
            )
            .group_by(Page.link)
            .order_by(Page.link)
            .limit(1)
            .offset(index)
            .first())
    return page


def language_page_at_index(language, index, testmode=None):
    if testmode is not None:
        lists = get_test_lists(language)
        if testmode == 'all':
            all_list = []
            for l in lists.values():
                all_list.extend(l)
            page = all_list[index]
        else:
            page = lists[testmode][index]
    else:
        page = (Page
                .select()
                .where(
                    (Page.language == language) |
                    (Page.purpose == 'targeted end use') |
                    (Page.purpose == 'miscellany end use')
                )
                .group_by(Page.link)
                .order_by(Page.link)
                .limit(1)
                .offset(index)
                .first())
    return page


def query_page_at_index(query, index):
    page = (Page
            .select()
            .group_by(Page.link)
            .order_by(Page.link)
            .where(
                (Page.query == query) |
                (Page.purpose == 'targeted end use') |
                (Page.purpose == 'miscellany end use')
            )
            .limit(1)
            .offset(index)
            .first())
    return page


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Open page for evaluation")
    subparsers = parser.add_subparsers(dest='action')

    id_sp = subparsers.add_parser('index')
    id_sp.add_argument('index', help="index of page to open", type=int)

    ml_sp = subparsers.add_parser('ml')
    ml_sp.add_argument('microlanguage', help="name of micro-language")
    ml_sp.add_argument('index', help="index of page to open for that micro-language", type=int)
    ml_sp.add_argument('--testmode', help="if running tests, this is one of {validation,test}")

    query_sp = subparsers.add_parser('query')
    query_sp.add_argument('query', help="query to look up")
    query_sp.add_argument('index', help="index of page to open for that query", type=int)

    test_sp = subparsers.add_parser('test')
    test_sp.add_argument('set', help="name of which set to use, one of {validation,test}")

    args = parser.parse_args()

    try:
        check_server_running()
    except ServerNotRunningException as e:
        raise SystemExit(e.message)

    ''' Fetch page. '''
    page = None
    if args.action == 'index':
        page = page_at_index(args.index)
    elif args.action == 'ml':
        page = language_page_at_index(args.microlanguage, args.index, args.testmode)
    elif args.action == 'query':
        page = query_page_at_index(args.query, args.index)

    ''' Exit if there are no pages left. '''
    if page is None:
        print "No page found for the specified parameters"
        raise SystemExit(STATUS_NO_PAGES)

    ''' Open up file. '''
    path = build_local_url(page)
    print page.link
    subprocess.call(['open', path])
