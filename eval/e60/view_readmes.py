#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
import argparse
import os.path
import codecs
from models import Package
import webbrowser


logging.basicConfig(level=logging.INFO, format="%(message)s")
README_DIR = 'readmes'
if not os.path.exists(README_DIR):
    os.makedirs(README_DIR)


def write_readme(path, text):

    with codecs.open(path, 'w', encoding='utf8') as readme:

        # To read spaces properly in the texts that we scraped, the browser needs to be told
        # to read the text as UTF-8.
        readme.write('<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />\n')

        # Add styles to the README to make the task of counting code blocks easier.
        readme.write("\n".join([
            "<style>",
            "  pre {",
            "    background-color: grey;",  # make <pre> blocks grey to easily count them
            "  }",
            "",
            "  body {",
            "    margin: 100px;",  # add margin around content to improve readability
            "  }",
            "",
            "</style>"
        ]))
        readme.write(text)


def main(package_list_path):

    with open(package_list_path) as package_list:

        for line in package_list:

            package_name = line.strip()
            package = Package.get(Package.name == package_name)

            readme_path = os.path.join(README_DIR, package.name) + '.html'
            write_readme(readme_path, package.readme)

            print "====Showing README for package", package_name
            print "====Press Enter to continue."
            webbrowser.open("file://" + os.path.abspath(readme_path))
            raw_input()  # wait for user to type <Enter>

        print "You have viewed all packages!"


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="View READMEs for NPM packages from database")
    parser.add_argument('packagelist', help="text file with a package name on each line")
    args = parser.parse_args()
    main(args.packagelist)
