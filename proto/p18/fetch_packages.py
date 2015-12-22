#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
import slumber
import argparse
import base64
import re
import time
import requests
from bs4 import BeautifulSoup
import json

from peewee import fn
from models import Package, create_tables
from api import LibrariesIo, Github, default_requests_session


logging.basicConfig(level=logging.INFO, format="%(message)s")
github = Github()
libraries_io = LibrariesIo()


def make_request(method, *args, **kwargs):

    MAX_ATTEMPTS = 5
    RETRY_DELAY = 30
    try_again = True
    attempts = 0
    res = None

    def log_error(err_msg):
        logging.warn(
            "Error (%s) For API call %s, Args: %s, Kwargs: %s",
            str(err_msg), str(method), str(args), str(kwargs)
        )

    while try_again and attempts < MAX_ATTEMPTS:

        try:
            res = method(*args, **kwargs)
            if hasattr(res, 'status_code') and res.status_code not in [200]:
                log_error(str(res.status_code))
                res = None
            try_again = False
        except (slumber.exceptions.HttpNotFoundError):
            log_error("Not Found")
            try_again = False
        except slumber.exceptions.HttpServerError:
            log_error("Server 500")
            try_again = False
        except requests.exceptions.ConnectionError:
            log_error("ConnectionError")
        except requests.exceptions.ReadTimeout:
            log_error("ReadTimeout")

        if try_again:
            logging.warn("Waiting %d seconds for before retrying.", int(RETRY_DELAY))
            time.sleep(RETRY_DELAY)
            attempts += 1

    return res


def fetch_packagenames_from_libraryio(package_count):
    # Currently only fetchers packages in multiples of 30
    # If package_count == -1, then all packages will be fetched

    keep_fetching = True
    page_no = 0
    count_retrieved = 0

    while keep_fetching:

        logging.info("Fetching page %d of package names", page_no)
        packages = make_request(
            libraries_io.search.get,
            q='', platforms='NPM', page=page_no
        )

        if packages is not None:
            for p in packages:
                Package.get_or_create(
                    name=p['name'],
                    repository_url=p['repository_url'],
                    page_no=page_no,
                )

        count_retrieved += len(packages)
        page_no += 1
        keep_fetching = (
            (len(packages) > 0) and
            (package_count == -1 or count_retrieved < package_count)
        )


def github_info(url):
    if 'github.com' in url:
        url = re.sub('^.*(?:github.com)', '', url)
        # Repo name can have slashes, so split on the first two slashes
        _, user, repo_name = url.split('/', 2)
        return (user, repo_name)
    return None


def fetch_github_readmes(packages):

    for p in packages:

        gh_info = github_info(p.repository_url)
        if gh_info is None:
            logging.info(
                "Not fetching README.  " +
                "Package %s does not have a Github repository",
                p.name)
            continue
        user, repo_name = gh_info

        logging.info("Fetching README for %s", p.name)
        readme = make_request(github.repos(user)(repo_name).readme.get)
        if readme is not None:
            p.readme = base64.b64decode(readme['content'])
            p.save()


def fetch_github_stats(packages):

    for p in packages:

        gh_info = github_info(p.repository_url)
        if gh_info is None:
            logging.info(
                "Not fetching stats.  " +
                "Package %s does not have a Github repository",
                p.name)
            continue
        user, repo_name = gh_info

        logging.info("Fetching stats for package %s", p.name)
        repo_info = make_request(
            libraries_io.github(user)(repo_name).get()
        )
        if repo_info is not None:
            p.stargazers_count = repo_info['stargazers_count']
            p.forks_count = repo_info['forks_count']
            p.open_issues_count = repo_info['open_issues_count']
            p.subscribers_count = repo_info['subscribers_count']
            p.github_contributions_count = repo_info['github_contributions_count']
            p.has_wiki = repo_info['has_wiki']
            p.save()


def fetch_package_list():
    res = make_request(
        default_requests_session.get,
        "https://skimdb.npmjs.com/registry/_all_docs",
    )
    if res is not None:
        packages = res.json()['rows']
        for p in packages:
            Package.get_or_create(name=p['id'])


def fetch_npm_data(packages):

    to_count = lambda s: int(s.replace(',', '')) if s != '' else 0

    for p in packages:

        res = make_request(
            default_requests_session.get,
            "https://www.npmjs.com/package/{pkg}".format(pkg=p.name),
        )

        if res is not None:
            page = BeautifulSoup(res.content, 'html.parser')
            p.readme = str(page.select('div#readme')[0])
            p.description = page.select('p.package-description')[0].text
            p.day_download_count = to_count(page.select('strong.daily-downloads')[0].text)
            p.week_download_count = to_count(page.select('strong.weekly-downloads')[0].text)
            p.month_download_count = to_count(page.select('strong.monthly-downloads')[0].text)
            p.dependents = json.dumps(
                [e.text for e in page.select('p.dependents a')])
            p.dependencies = json.dumps(
                [e.text for e in page.select('p.list-of-links:nth-of-type(2) a')])
            p.save()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Download package stats for NPM")
    parser.add_argument(
        '--package-list',
        action='store_true',
        help="fetch list of all packages on NPM"
    )
    parser.add_argument(
        '--npm-data',
        action='store_true',
        help="fetch Node.js data (READMES and downloads)"
    )
    parser.add_argument(
        '--update',
        action='store_true',
        help="only update existing data (currently only for --npm-data"
    )
    parser.add_argument(
        '--lib-packages',
        action='store_true',
        help="fetch package names from Library.IO"
    )
    parser.add_argument(
        '--lib-package-count',
        type=int,
        default=-1,
        help="how many package names to fetch"
    )
    parser.add_argument(
        '--github-readmes',
        action='store_true',
        help="fetch Github READMEs"
    )
    parser.add_argument(
        '--github-stats',
        action='store_true',
        help="fetch Github stats"
    )
    args = parser.parse_args()

    if args.package_list:
        create_tables()
        fetch_package_list()
    if args.npm_data:
        if args.update:
            packages = Package.select().where(Package.description != '')
        else:
            packages = Package.select().where(Package.readme >> None).order_by(fn.Random())
        fetch_npm_data(packages)
    if args.lib_packages:
        create_tables()
        fetch_packagenames_from_libraryio(args.lib_package_count)
    if args.github_readmes:
        fetch_github_readmes(Package.select())
    if args.github_stats:
        fetch_github_stats(Package.select())
