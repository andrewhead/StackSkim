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
            q='', platforms='PyPI', page=page_no
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
        "https://pypi.python.org/pypi?%3Aaction=index",
    )
    page = BeautifulSoup(res.content, 'html.parser')
    package_table = page.find('table')
    all_rows = package_table.findAll('tr')
    # Each row represents a single PyPI package.
    for row in all_rows:
        # Each row has 2 columns, a name (hyperlinked) and a description.
        link = row.find('a')
        if link is not None: # Only fetch package if it has a link to its own page.
            # Reformat spacing in extracted name.
            package_name = link.text.replace(u'\xa0', ' ')
            logging.info("New package name: %s", package_name)
            Package.get_or_create(name=package_name)


def fetch_pypi_data(packages):
    END_OF_README = '<a name="downloads">&nbsp;</a>'

    for p in packages:
        # Turn package name into correct URL suffix.
        # Assumes p.name does not have invalid characters for a URL, such as "
        formatted_name = p.name.replace(' ', '/').replace(u'\xa0', '/')

        res = make_request(
            default_requests_session.get,
            "https://pypi.python.org/pypi/{pkg}".format(pkg=formatted_name),
        )

        if res is not None:
            page = BeautifulSoup(res.content, 'html.parser')

            # Package description is the first italicized <p> tag on a PyPI
            # package doc.
            p.description = page.find('p', style="font-style: italic").text
            logging.info("Package description: %s", p.description)

            # README, if it exists, comes after the above italicized package
            # description and ends with END_OF_README.

            # Explicitly decode content into utf-8, rather than default ascii.
            content = res.content.decode('utf-8')

            start_of_readme = '<p style="font-style: italic">' + p.description + '</p>'
            readme_start_index = content.find(start_of_readme) + len(start_of_readme)
            lines = content[readme_start_index:].split('\n')
            readme_lines = []
            for line in lines:
                if line.strip() == END_OF_README:
                    break
                readme_lines.append(line)
            p.readme = '\n'.join(readme_lines)

            download_spans = page.select('ul.nodot')[0].findAll('span')
            # There should be 3 spans: day, week, and month.
            p.day_download_count, p.week_download_count, p.month_download_count = \
                [int(span.text) for span in download_spans]

            logging.info("Day download count: %d", p.day_download_count)
            logging.info("Week download count: %d", p.week_download_count)
            logging.info("Month download count: %d", p.month_download_count)

            p.save()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Download package stats for PyPI")
    parser.add_argument(
        '--package-list',
        action='store_true',
        help="fetch list of all packages on PyPI"
    )
    parser.add_argument(
        '--pypi-data',
        action='store_true',
        help="fetch PyPI data (READMES and downloads)"
    )
    parser.add_argument(
        '--update',
        action='store_true',
        help="only update existing data (currently only for --pypi-data)"
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
    if args.pypi_data:
        if args.update:
            packages = Package.select().where(Package.description != '')
        else:
            packages = Package.select().where(Package.readme >> None).order_by(fn.Random())
        fetch_pypi_data(packages)
    if args.lib_packages:
        create_tables()
        fetch_packagenames_from_libraryio(args.lib_package_count)
    if args.github_readmes:
        fetch_github_readmes(Package.select())
    if args.github_stats:
        fetch_github_stats(Package.select())
