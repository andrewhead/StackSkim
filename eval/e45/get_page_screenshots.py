#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
from selenium import webdriver
import os.path
from order import get_test_lists
from open import build_local_url
from PIL import Image


logging.basicConfig(level=logging.INFO, format="%(message)s")
SCREENS_DIR = os.path.join('screenshots')
NUM_PAGES = 20


def main():

    browser = webdriver.Firefox()

    # Get list of validation pages
    pages = get_test_lists('jquery')['validation'][:NUM_PAGES]

    # For each page, save a screenshot
    for i, p in enumerate(pages):
        print "Visiting page:", p.link, "...",
        browser.get(build_local_url(p))
        screenshot_path = os.path.join(SCREENS_DIR, 'page' + str(i) + '.png')
        browser.save_screenshot(screenshot_path)
        print "saved screenshot."
        print "Cropping page...",
        img = Image.open(screenshot_path)
        cropped = img.crop((0, 0, img.width, int(img.width * 1.5)))
        cropped.save(screenshot_path)
        print "cropped."

    browser.close()


if __name__ == '__main__':
    main()
