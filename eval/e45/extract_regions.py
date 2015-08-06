#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
import time
import argparse
from selenium import webdriver
from concurrent.futures import ThreadPoolExecutor
import codecs
from progressbar import ProgressBar, Percentage, Bar, RotatingMarker, ETA, Counter
from multiprocessing import Process

from order import get_test_lists
from open import build_local_url, check_server_running, ServerNotRunningException
from server_logger import FileMonitor


logging.basicConfig(level=logging.INFO, format="%(message)s")

FIRST_LINK = 'http://google.com/about'
JQUERY_SCRIPT = """
document.body.appendChild(document.createElement('script')).src =
    'https://code.jquery.com/jquery-2.1.3.min.js';
"""
TUTORONS_UPLOAD_SCRIPT = r"""
var TUTORONS_SERVER = 'http://127.0.0.1:8002';
$.post(TUTORONS_SERVER + '/' + "{lang}", {{
    'origin': window.location.href,
    'document': document.body.innerHTML,
}});
"""
LOAD_TIME = 10
READY_TIME = 5
READY_RATIO = 2
MAX_READY_TIME = 60
FINISH_TIME = 20
MICROLANGUAGES = ['jquery']

exit_logger = False


def browser_get(browser, link):
    browser.get(link)


def load_link(browser, link):
    ''' Return true if load successful, false otherwise. '''

    while True:

        p = Process(target=browser_get, args=(browser, link))
        p.start()
        p.join(LOAD_TIME)
        if p.is_alive():
            p.terminate()
        else:
            break

    while True:

        wait_time = READY_TIME
        start_time = time.time()

        ''' Wait for page to have completely loaded. '''
        while True:
            state = browser.execute_script('return document.readyState;')
            if state == 'complete':
                return True
            if time.time() - start_time > wait_time:
                logging.info("Document %s not ready after %ds", link, wait_time)
                break
            time.sleep(1)

        wait_time = wait_time * READY_RATIO
        if wait_time > MAX_READY_TIME * READY_RATIO:
            logging.error("Skipping document %s.  Was never ready.", link)
            return False
        else:
            logging.info("Increasing wait time to %ds", wait_time)


def open_page(browser, p):
    load_success = load_link(browser, build_local_url(p))
    if load_success is True:
        browser.execute_script(JQUERY_SCRIPT)
        time.sleep(.5)
    return load_success


def run_tutoron(browser, language):
    script = TUTORONS_UPLOAD_SCRIPT.format(lang='css')
    browser.execute_script(script)


def save_detections(server_file, output_file):
    with codecs.open(output_file, 'w', 'utf8') as outfile:
        monitor = FileMonitor(server_file)
        while True:
            line = monitor.get_line()
            if line is not None:
                outfile.write(line + '\n')
            elif exit_logger:
                monitor.finish()
                return
            else:
                time.sleep(.5)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description="load test files into the Firefox browser and query Tutorons server")
    parser.add_argument('testset', help="test set to use: {validation,test}")
    parser.add_argument('server_file', help="server log file with detected regions")
    parser.add_argument('output_file', help="TSV listing all detections")
    parser.add_argument('--count', help="how many pages to open", type=int)
    parser.add_argument('--skip', help="optional index to skip", type=int)
    args = parser.parse_args()

    count = args.count

    try:
        check_server_running()
    except ServerNotRunningException as e:
        raise SystemExit(e.message)

    ''' Listen for updates to server log to save all detections. '''
    pool = ThreadPoolExecutor(max_workers=1)
    future = pool.submit(save_detections, args.server_file, args.output_file)

    ''' Collect webpages for all micro-languages. '''
    pages = []
    for lang in MICROLANGUAGES:
        test_lists = get_test_lists(lang)
        pages.extend([(p, lang) for p in test_lists[args.testset]])

    ''' Set up progress bar. '''
    widgets = [
        'Progress: ', Percentage(), ' ', Bar(marker=RotatingMarker()), ' ', ETA(),
        ' Visited ', Counter(), ' sites.'
    ]
    num_pages = min(len(pages), count) if count is not None else len(pages)
    pbar = ProgressBar(widgets=widgets, maxval=num_pages)
    pbar.start()

    ''' Set up browser. '''
    browser = webdriver.Firefox()
    load_link(browser, FIRST_LINK)  # start by loading something inconsequential

    ''' Open the pages! '''
    for i, (p, l) in enumerate(pages):
        if i >= num_pages:
            break
        elif args.skip is not None and i == args.skip:
            continue
        open_success = open_page(browser, p)
        if open_success is True:
            run_tutoron(browser, l)
        pbar.update(i + 1)

    ''' Let the future do some more work dequeuing events. '''
    print ""
    print "Waiting for server to complete detections (waiting %ss)..." % FINISH_TIME
    time.sleep(FINISH_TIME)
    print "Wait complete.  Now exiting logger thread."
    exit_logger = True

    browser.close()
    pool.shutdown()
