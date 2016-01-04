#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
import ConfigParser
from requests.auth import AuthBase
import slumber
import os.path
import cache


logging.basicConfig(level=logging.INFO, format="%(message)s")
default_requests_session = cache.get_session(timeout=1)
default_requests_session.headers['User-Agent'] =\
    "Austin Le (for academic analysis) <austinhle@berkeley.edu>"

lib_config = ConfigParser.ConfigParser()
lib_config.read(os.path.expanduser(os.path.join('~', '.libraries_config')))
libraries_io_api_key = lib_config.get('api', 'API_KEY')


class LibrariesIoAuth(AuthBase):
    def __init__(self, api_key):
        self.api_key = api_key

    def __call__(self, request):
        request.data['api_key'] = self.api_key
        return request


class LibrariesIo(slumber.API):
    def __init__(self, *args, **kwargs):
        session = cache.get_session(timeout=1.5)
        session.params['api_key'] = libraries_io_api_key
        super(self.__class__, self).__init__(
            'https://libraries.io/api',
            session=session,
            *args, **kwargs
        )


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
