#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import subprocess
import logging
from models import Page
import os.path
import os
import re
import requests
from progressbar import ProgressBar, Percentage, Bar, RotatingMarker, ETA, Counter


logging.basicConfig(level=logging.INFO, format="%(asctime)s: %(message)s", filename='.fetch.log')
USER_AGENT = 'Andrew Tutorial Lookup'


def main():

    ''' Set up progress bar. '''
    widgets = [
        'Progress: ', Percentage(), ' ', Bar(marker=RotatingMarker()), ' ', ETA(),
        ' Downloaded ', Counter(), ' sites.'
    ]
    pbar = ProgressBar(widgets=widgets, maxval=Page.select().count())
    pbar.start()

    page_index = 0
    for page in Page.select():

        dest = os.path.join('pages', page.language, page.query, str(page.rank))
        if not os.path.isdir(dest):
            os.makedirs(dest)

        output, return_code = run_wget(page.link, dest)
        bad_ssl = False
        if return_code == 5:  # SSL error -- double-check with requests package
            try:
                requests.get(page.link)
                output, return_code = run_wget(page.link, dest, skip_certificate=True)
            except requests.exceptions.SSLError:
                bad_ssl = True

        ''' Run wget to fetch page and all it's dependencies. '''
        ''' First downloaded file is the index.  Store where it's saved. '''
        save_locs = re.findall(r"^Saving to: '(.*)'$", output, re.MULTILINE)
        if bad_ssl or len(save_locs) == 0:
            logging.warn("Failed fetch (code=%d): %s", return_code, page.link)
        else:
            page.dest = save_locs[0]
            page.save()
            logging.info("Fetched file (code=%d): %s", return_code, page.link)

        page_index += 1
        pbar.update(page_index)

    pbar.finish()


def run_wget(link, dest, skip_certificate=False):
    try:
        args = [
            'wget', '-p', '-k', '-P', dest,
            '--span-hosts', '--tries=3',
            '-e', 'robots=off',  # w3schools doesn't let robots get html files
            '--user-agent="%s"' % USER_AGENT,  # many sites refuse unnamed user-agent
            '--adjust-extension', link,
        ]
        if skip_certificate:
            args += ['--no-check-certificate']
        output = subprocess.check_output(args, stderr=subprocess.STDOUT)
        return_code = 0
    except subprocess.CalledProcessError as cpe:
        output = cpe.output
        return_code = cpe.returncode
    return output, return_code


if __name__ == '__main__':
    main()
