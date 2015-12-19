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

from models import Package, create_tables
from api import LibrariesIo, Github


logging.basicConfig(level=logging.INFO, format="%(message)s")
github = Github()
libraries_io = LibrariesIo()


def call_api(method, *args, **kwargs):

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


def fetch_packages(package_count):
    # Currently only fetchers packages in multiples of 30
    # If package_count == -1, then all packages will be fetched

    keep_fetching = True
    page_no = 0
    count_retrieved = 0

    while keep_fetching:

        logging.info("Fetching page %d of package names", page_no)
        packages = call_api(
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


def fetch_readmes(packages):

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
        readme = call_api(github.repos(user)(repo_name).readme.get)
        if readme is not None:
            p.readme = base64.b64decode(readme['content'])
            p.save()


def fetch_stats(packages):

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
        repo_info = call_api(
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


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Download package stats for NPM")
    parser.add_argument('--packages', action='store_true', help="fetch package names")
    parser.add_argument(
        '--package-count', type=int, default=-1, help="how many package names to fetch")
    parser.add_argument('--readmes', action='store_true', help="fetch READMEs")
    parser.add_argument('--stats', action='store_true', help="fetch Github stats")
    args = parser.parse_args()

    if args.packages:
        create_tables()
        fetch_packages(args.package_count)
    if args.readmes:
        fetch_readmes(Package.select())
    if args.stats:
        fetch_stats(Package.select())
