#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from evaluate import RegexAffinityEvaluator
import logging
import unittest


logging.basicConfig(level=logging.INFO, format="%(message)s")


class RegexAffinityTest(unittest.TestCase):

    def setUp(self):
        self.evaluator = RegexAffinityEvaluator()

    def compute_affinity(self, pattern):
        return self.evaluator.evaluate(pattern)

    def test_nonliteral_has_full_affinity(self):
        self.assertEqual(self.compute_affinity(r'\d'), 1)

    def test_literal_has_no_affinity(self):
        self.assertEqual(self.compute_affinity(r'a'), 0)

    def test_affinity_is_proportion_of_nonliterals_to_all_atoms(self):
        self.assertAlmostEqual(self.compute_affinity(r'\d\wabc\Wd'), float(3)/7)


if __name__ == '__main__':
    unittest.main()
