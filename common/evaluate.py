#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
import csv
import os.path
import glob
import time
from selenium import webdriver


logging.basicConfig(level=logging.INFO, format="%(message)s")


def print_stats(detected_regions, truth_regions):
    stats = AccuracyStats()
    prec, found_regions, false_regions = stats.precision(detected_regions, truth_regions)
    rec, rfound_regions, missing_regions = stats.recall(detected_regions, truth_regions)
    '''
    for dgood in sorted([_.text for _ in found_regions]):
        print dgood
    for rgood in sorted([_[1][0].text for _ in rfound_regions.items()]):
        print rgood
    '''
    print "Precision: %.4f (%d/%d), Recall %.4f (%d/%d)" %\
        (prec, len(found_regions), len(detected_regions),
         rec, len(rfound_regions), len(truth_regions.keys()))
    # precisions = stats.link_precisions(detected_regions, truth_regions)
    # recalls = stats.link_recalls(detected_regions, truth_regions)
    # print "Per-page Precision: %.4f, Recall %.4f" %\
    #     (sum(precisions) / len(precisions), sum(recalls) / len(recalls))
    return found_regions, false_regions, missing_regions


class AccuracyStats(object):

    def precision(self, detected_regions, truth_regions):
        correct = 0
        true_regions = []
        false_regions = []
        total = len(detected_regions)
        for d in detected_regions:
            if self.is_detected_region_true(d, truth_regions):
                true_regions.append(d)
                correct = correct + 1
            else:
                false_regions.append(d)
        precision = correct / float(total) if total != 0 else None
        return precision, true_regions, false_regions

    def recall(self, detected_regions, truth_regions):
        found_count = 0
        found = {}
        missing = {}
        total = len(truth_regions.keys())
        for key, true_region_candidates in truth_regions.items():
            if self.is_true_region_detected(true_region_candidates, detected_regions):
                found_count += 1
                found[key] = true_region_candidates
            else:
                missing[key] = true_region_candidates
        recall = found_count / float(total) if total != 0 else None
        # print found_count
        # print len(found.keys())
        return recall, found, missing

    def link_precisions(self, detected_regions, truth_regions):
        precisions = []
        urls = set()
        for key in truth_regions.keys():
            urls.add(key[0])
        for url in urls:
            url_detected_regions = [r for r in detected_regions if r.url == url]
            url_truth_regions = {
                k: region_list
                for (k, region_list) in truth_regions.items()
                if k[0] == url
            }
            p, _, _ = self.precision(url_detected_regions, url_truth_regions)
            if p is not None:
                precisions.append(p)
        return precisions

    def link_recalls(self, detected_regions, truth_regions):
        recalls = []
        urls = set()
        for key in truth_regions.keys():
            urls.add(key[0])
        for url in urls:
            url_detected_regions = [r for r in detected_regions if r.url == url]
            url_truth_regions = {
                k: region_list
                for (k, region_list) in truth_regions.items()
                if k[0] == url
            }
            r, _, _ = self.recall(url_detected_regions, url_truth_regions)
            if r is not None:
                recalls.append(r)
        return recalls

    def is_detected_region_true(self, region, truth_regions):
        for truth_list in truth_regions.values():
            if region in truth_list:
                try:
                    # print "Match"
                    # print "Detected: ", unicode(region)
                    pass
                except:
                    pass
                for r in truth_list:
                    if region == r:
                        try:
                            # print "Truth: ", unicode(r)
                            pass
                        except:
                            pass
                # print ""
                return True
        return False

    def is_true_region_detected(self, region_candidates, detected_regions):
        '''
        A "true" region can be described relative to any number of its parent elements.
        We pass in all of these possible region descriptions as 'region_candidates'.
        '''
        i = 0
        for r in region_candidates:
            if r in detected_regions:
                i += 1
        if i >= 1:
            print "Matches:", i
            print r.text
            return True
        return False


class RegionInspector(object):

    def open_missing_detections(self, missing_regions, start_index=0, debug=True):
        browser = Browser()
        specific_regions = []
        for (_, region_list) in missing_regions.items()[start_index:]:
            ''' Most specific selector will be the longest one. '''
            r = max(region_list, key=lambda r: len(r.element))
            specific_regions.append(r)
        self.display_regions(browser, specific_regions, debug, start_index)

    def open_false_detections(self, false_regions, start_index=0, debug=True):
        browser = Browser()
        self.display_regions(browser, false_regions[start_index:], debug, start_index)

    def display_regions(self, browser, regions, debug, start_index):
        print ""
        print "?? Open next example of missed detection? ",
        for i, r in enumerate(regions, start=start_index):
            try:
                again = raw_input()
                if again.lower() == 'n':
                    break
                self.display_region(browser, r, i, debug)
            except KeyboardInterrupt:
                browser.close()
                return

    def display_region(self, browser, region, index, debug):
        print ""
        print "===== REGION %d =====" % index
        print unicode(region)
        browser.show_region(region)
        if debug:
            print "* Text: ", browser.get_text(region)
            html = browser.get_html(region)
            print "* HTML: ",
            if len(html) > 1000:
                print "too long to render"
            else:
                print html


class Region(object):

    def __init__(self, url, element, start_offset, end_offset, text=None):
        self.url = url
        self.element = element
        self.start_offset = start_offset
        self.end_offset = end_offset
        self.text = text

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
                and self.element == other.element
                and self.url == other.url
                and self.start_offset == other.start_offset
                and self.end_offset == other.end_offset)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __unicode__(self):
        return "{{Text: {text} URL: {url}, Element: {el}, Offsets: ({so}, {eo})}}".format(
            text=self.text, url=self.url, el=self.element, so=self.start_offset, eo=self.end_offset)


def load_detected_regions(filename, valid_urls=None):
    detected_regions = []
    with open(filename) as detected_tsv:
        reader = csv.DictReader(
            detected_tsv, delimiter=str('\t'),
            fieldnames=['timestamp', 'url', 'element', 'start_offset', 'end_offset', 'text'])
        for r in reader:
            if valid_urls is not None and r['url'] in valid_urls:
                detected_regions.append(
                    Region(r['url'], r['element'], r['start_offset'],
                           r['end_offset'], r['text'].decode('utf-8'))
                )
    return detected_regions


def load_groundtruth_regions(filename, delimiter='\t', valid_urls=None):
    '''
    For the manually extracted regions, index each on by the absolute offsets within the page and
    the URL of the page. This is because we extract all possible relative positions of the region
    within the page, but each of these are really the same region.
    '''
    with open(filename, 'rU') as truth_tsv:
        truth_regions = {}
        for line in truth_tsv.readlines():
            tokens = line.strip().split(delimiter)
            if len(line.strip()) == 0:
                continue
            r = {
                'rel_start_offset': tokens[0],
                'rel_end_offset': tokens[1],
                'element': tokens[2],
                'url': tokens[3],
                'abs_start_offset': tokens[4],
                'abs_end_offset': tokens[5],
            }
            if valid_urls is not None and r['url'] in valid_urls:
                key = (r['url'], r['abs_start_offset'], r['abs_end_offset'])
                if key not in truth_regions:
                    truth_regions[key] = []
                region = Region(r['url'], r['element'], r['rel_start_offset'], r['rel_end_offset'])
                truth_regions[key].append(region)
                if len(tokens) > 6:
                    region.text = tokens[6]
        return truth_regions


def save_results(history_dir, false_regions, missing_regions):

    if not os.path.isdir(history_dir):
        os.makedirs(history_dir)

    def get_regions_filename(basename):
        record_index = 0
        while True:
            record_prefix = '{basename}-{record_index}-'.format(
                basename=basename, record_index=record_index)
            record_prefix_path = os.path.join(history_dir, record_prefix)
            if not glob.glob(record_prefix_path + '*'):
                ts = time.strftime('%Y%m%d-%H:%M:%S')
                filename = record_prefix_path + ts + '.tsv'
                return filename
            record_index += 1

    def write_region(file_, r):
        file_.write('\t'.join([r.url, r.element, r.start_offset, r.end_offset]) + '\n')

    false_fn = get_regions_filename('false_detections')
    missing_fn = get_regions_filename('missing_regions')

    with open(false_fn, 'w') as false_file:
        for r in false_regions:
            write_region(false_file, r)

    with open(missing_fn, 'w') as missing_file:
        for _, region_list in missing_regions.items():
            region = max(region_list, key=lambda r: len(r.element))
            write_region(missing_file, region)


class Browser(object):

    def __init__(self):
        self.browser = webdriver.Firefox()

    def close(self):
        self.browser.close()

    def show_region(self, region):
        SHOW_REGION_SCRIPT = '\n'.join([
            "var node = document.querySelector('{element}');",
            "var range = document.createRange();",
            "range.selectNode(node);",
            "var selection = window.getSelection();",
            "selection.addRange(range);",
            "node.scrollIntoView();",
        ])
        self.browser.get(region.url)
        if region.element != '':
            self.browser.execute_script(SHOW_REGION_SCRIPT.format(element=region.element))

    def get_text(self, region):
        GET_TEXT_SCRIPT = '\n'.join([
            "var node = document.querySelector('{element}');",
            "return node.textContent.substring({start_offset}, {end_offset} + 1);",
        ])
        return self.browser.execute_script(GET_TEXT_SCRIPT.format(
            element=region.element, start_offset=region.start_offset,
            end_offset=region.end_offset))

    def get_html(self, region):
        GET_HTML_SCRIPT = '\n'.join([
            "var node = document.querySelector('{element}');",
            "return node.outerHTML;",
        ])
        return self.browser.execute_script(GET_HTML_SCRIPT.format(element=region.element))
