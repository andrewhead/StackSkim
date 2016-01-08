#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
import ConfigParser
import slumber
import os.path
import cache


logging.basicConfig(level=logging.INFO, format="%(message)s")
default_requests_session = cache.get_session(timeout=1)
default_requests_session.headers['User-Agent'] =\
    "Austin Le (for academic analysis) <austinhle@berkeley.edu>"

gh_config = ConfigParser.ConfigParser()
gh_config.read(os.path.expanduser(os.path.join('~', '.gitconfig')))
gh_username = gh_config.get('auth', 'username')
gh_password = gh_config.get('auth', 'password')


class Github(slumber.API):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(
            'https://api.github.com',
            auth=(gh_username, gh_password),
            session=cache.get_session(timeout=1.0),
            *args, **kwargs
        )
