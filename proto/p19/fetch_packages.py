#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
import slumber
import argparse
import time
import requests
from bs4 import BeautifulSoup

from peewee import fn
from models import Package, create_tables
from api import Github, default_requests_session


logging.basicConfig(level=logging.INFO, format="%(message)s")
github = Github()


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


def fetch_package_list():
    res = make_request(
        default_requests_session.get,
        "https://pypi.python.org/pypi?%3Aaction=index",
    )

    # Use BeautifulSoup to parse the HTML and find the package names.
    page = BeautifulSoup(res.content, 'html.parser')
    package_table = page.find('table')
    all_rows = package_table.findAll('tr')

    logging.info("====There are currently %d packages on PyPI.", len(all_rows) - 1)

    num_fetched = 0

    # Each row represents a single PyPI package.
    for row in all_rows:
        # Each row has 2 columns, a name (hyperlinked) and a description.
        link = row.find('a')
        # Only fetch package if it has a link to its own page.
        if link is not None:
            # Reformat spacing in extracted name.
            package_name = link.text.replace(u'\xa0', ' ')
            Package.get_or_create(name=package_name)
            num_fetched += 1
            if num_fetched % 10 == 0:
                logging.info("%d packages fetched.", num_fetched)

    logging.info("====Done fetching package list. There were %d packages.", num_fetched)


def fetch_pypi_data(packages):
    logging.info("Fetching PyPI data for %d packages", len(packages))

    num_fetched = 0

    for p in packages:
        # Turn package name into correct URL suffix.
        # Assumes p.name does not have invalid characters for a URL, such as "
        formatted_name = p.name.replace(' ', '/').replace(u'\xa0', '/')

        res = make_request(
            default_requests_session.get,
            "https://pypi.python.org/pypi/{pkg}/json".format(pkg=formatted_name),
        )

        if res is not None:
            try:
                package_json = res.json()
            except ValueError:
                logging.warn("No JSON Object Could Be Decoded")

            package_info = package_json['info']

            download_info = package_info['downloads']
            p.day_download_count = download_info['last_day']
            p.week_download_count = download_info['last_week']
            p.month_download_count = download_info['last_month']

            # The summary key is the brief description of the package, in just a few lines.
            p.description = package_info['summary']
            # The description key includes details such as installation, usage, and examples.
            p.readme = package_info['description']

            p.save()

            num_fetched += 1
            if num_fetched % 10 == 0:
                logging.info("Done fetching %d packages.", num_fetched)

    logging.info("====Done retrieving package data for all packages. %d packages had data.", num_fetched)


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
    args = parser.parse_args()

    if args.package_list:
        create_tables()
        fetch_package_list()
    if args.pypi_data:
        if args.update:
            packages = Package.select().where(Package.description != '')
        else:
            packages = Package.select().where(Package.readme >> None)
        fetch_pypi_data(packages)
