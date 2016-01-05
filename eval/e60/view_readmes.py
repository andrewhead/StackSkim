#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
import argparse
import os.path
import codecs
from models import Package
from grip import serve
import ConfigParser


logging.basicConfig(level=logging.INFO, format="%(message)s")
README_DIR = 'readmes'
if not os.path.exists(README_DIR):
    os.makedirs(README_DIR)

# Github API credentals, as grip relies on Github API
gh_config = ConfigParser.ConfigParser()
gh_config.read(os.path.expanduser(os.path.join('~', '.github', 'github.cfg')))
gh_username = gh_config.get('auth', 'username')
gh_password = gh_config.get('auth', 'password')


def main(package_list_path):

    with open(package_list_path) as package_list:

        for line in package_list:

            package_name = line.strip()
            package = Package.get(Package.name == package_name)

            readme_path = os.path.join(README_DIR, package.name) + '.md'
            with codecs.open(readme_path, 'w', encoding='utf8') as readme:
                readme.write(package.readme)

            print "====Showing README for package", package_name
            print "====Press Ctrl+C to continue."
            try:
                serve(
                    path=readme_path,
                    port=8080,
                    browser=True,
                    username=gh_username,
                    password=gh_password,
                )
            except KeyboardInterrupt:
                pass

        print "You have viewed all packages!"


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="View READMEs for NPM packages from database")
    parser.add_argument('packagelist', help="text file with a package name on each line")
    args = parser.parse_args()
    main(args.packagelist)
