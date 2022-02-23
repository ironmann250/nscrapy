# -*- coding: utf-8 -*-

"""
Unlike configuration.py, this file is meant for static, entire project
encompassing settings, like memoization and caching file directories.
"""

__title__ = 'nscrapy'
__author__ = 'Munyakabera Jean Claude'
__license__ = 'MIT'
__copyright__ = 'Copyright 2016, Munyakabera Jean Claude'

import logging
import os

from cookielib import CookieJar as cj

PARENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

POPULAR_URLS = os.path.join(
    PARENT_DIRECTORY, 'resources/misc/popular_sources.txt')
USERAGENTS = os.path.join(PARENT_DIRECTORY, 'resources/misc/useragents.txt')

STOPWORDS_DIR = os.path.join(PARENT_DIRECTORY, 'resources/text')

# NLP stopwords are != regular stopwords for now...
NLP_STOPWORDS_EN = os.path.join(
    PARENT_DIRECTORY, 'resources/misc/stopwords-nlp-en.txt')
