#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
import unittest

from evaluate import Region, AccuracyStats


logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestAccuracyChecker(unittest.TestCase):

    def setUp(self):
        self.stats = AccuracyStats()

    def test_compute_that_detected_region_is_true(self):
        truth_regions = {
            ('url0', 0, 1): [Region('url0', 'el0', 0, 1), Region('url0', 'el1', 3, 4)],
            ('url1', 1, 2): [Region('url1', 'el0', 1, 2), Region('url1', 'el1', 2, 3)],
        }
        self.assertTrue(self.stats.is_detected_region_true(
            Region('url0', 'el1', 3, 4), truth_regions))

    def test_compute_that_undetected_region_is_false(self):
        truth_regions = {
            ('url0', 0, 1): [Region('url0', 'el0', 0, 1), Region('url0', 'el1', 3, 4)],
            ('url1', 1, 2): [Region('url1', 'el0', 1, 2), Region('url1', 'el1', 2, 3)],
        }
        self.assertFalse(self.stats.is_detected_region_true(
            Region('url0', 'el2', 0, 1), truth_regions))

    def test_true_region_is_detected(self):
        detected_regions = [Region('url0', 'el0', 0, 1), Region('url1', 'el1', 1, 2)]
        region_candidates = [Region('url0', 'el0', 0, 1), Region('url0', 'el1', 1, 2)]
        self.assertTrue(self.stats.is_true_region_detected(region_candidates, detected_regions))

    def test_true_region_is_not_detected(self):
        detected_regions = [Region('url0', 'el0', 0, 1), Region('url1', 'el1', 1, 2)]
        region_candidates = [Region('url1', 'el1', 0, 1), Region('url0', 'el0', 1, 2)]
        self.assertFalse(self.stats.is_true_region_detected(region_candidates, detected_regions))


if __name__ == '__main__':
    unittest.main()
