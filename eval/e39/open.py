#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
import argparse
from models import Page
import os.path
import re
import requests
import subprocess


logging.basicConfig(level=logging.INFO, format="%(message)s")
logging.getLogger('requests').setLevel(logging.WARNING)
PWD = os.path.dirname(os.path.realpath(__file__))
LOCALHOST = 'http://127.0.0.1:8000'
STATUS_NO_PAGES = 2


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Open page for evaluation")
    subparsers = parser.add_subparsers(dest='action')

    id_sp = subparsers.add_parser('index')
    id_sp.add_argument('index', help='index of page to open')
    ml_sp = subparsers.add_parser('ml')
    ml_sp.add_argument('microlanguage', help='name of micro-language')
    ml_sp.add_argument('index', help='index of page to open for that micro-language')
    query_sp = subparsers.add_parser('query')
    query_sp.add_argument('query', help='query to look up')
    query_sp.add_argument('index', help='index of page to open for that query')
    args = parser.parse_args()

    ''' Fetch page. '''
    page = None
    if args.action == 'index':
        page = (Page
                .select()
                .group_by(Page.link)
                .order_by(Page.link)
                .limit(1)
                .offset(args.index)
                .first())
    elif args.action == 'ml':
        page = (Page
                .select()
                .where(Page.language == args.microlanguage)
                .group_by(Page.link)
                .order_by(Page.link)
                .limit(1)
                .offset(args.index)
                .first())
    elif args.action == 'query':
        page = (Page
                .select()
                .group_by(Page.link)
                .order_by(Page.link)
                .where(Page.query == args.query)
                .limit(1)
                .offset(args.index)
                .first())

    ''' Exit if there are no pages left. '''
    if page is None:
        raise SystemExit(STATUS_NO_PAGES)

    ''' Adjust link to a local link. '''
    if page is not None:
        link = page.link
        link = re.sub('^.*://', '', link)  # strip address type (e.g., http://)
    else:
        print "No page found for the specified parameters"
    if not link.endswith('/') and not link.endswith('.html'):
        link += '.html'

    ''' Make sure that server is running. '''
    server_running = False
    try:
        requests.get(LOCALHOST)
        server_running = True
    except requests.ConnectionError:
        print ""
        print "=== ERROR: No fileserver running. ==="
        print "Run these commands in another shell:"
        print ""
        print "cd " + str(PWD)
        print "python -m SimpleHTTPServer 8000"
        print ""

    ''' Open up file. '''
    if server_running:
        path = os.path.join(
            LOCALHOST, 'pages', page.language, page.query, str(page.rank), link)
        print page.link
        subprocess.call(['open', path])
