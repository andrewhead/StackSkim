#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import unittest
import logging
import mock

from evaluate import CssAffinityEvaluator


logging.basicConfig(level=logging.INFO, format="%(message)s")


class CssAffinityTest(unittest.TestCase):

    def setUp(self):
        self.evaluator = CssAffinityEvaluator()

    def test_overall_affinity_averages_all_metric_functions(self):
        self.evaluator.compute_token_type_purity = mock.Mock(return_value=.5)
        self.evaluator.compute_token_value_purity = mock.Mock(return_value=.3)
        self.assertEqual(self.evaluator.evaluate('mock-selector'), .4)

    def test_skip_function_if_returns_None(self):
        self.evaluator.compute_token_type_purity = mock.Mock(return_value=.3)
        self.evaluator.compute_token_value_purity = mock.Mock(return_value=None)
        self.assertEqual(self.evaluator.evaluate('mock-selector'), .3)


class CssTokenTypePurityTest(unittest.TestCase):

    def setUp(self):
        self.evaluator = CssAffinityEvaluator()

    def compute_score(self, selector):
        return self.evaluator.compute_token_type_purity(selector)

    def test_elements_only_has_zero_purity(self):
        self.assertEqual(self.compute_score('div a'), 0)

    def test_id_is_pure(self):
        self.assertEqual(self.compute_score('#my_id'), 1)

    def test_class_is_pure(self):
        self.assertEqual(self.compute_score('.klazz'), 1)

    def test_attribute_is_pure(self):
        self.assertEqual(self.compute_score('[name="nm"]'), 1)

    def test_pseudoclass_is_pure(self):
        self.assertEqual(self.compute_score(':selected'), 1)

    def test_pseudoelement_is_pure(self):
        self.assertEqual(self.compute_score('p::before'), 0.5)

    def test_purity_is_proportion_of_non_elements(self):
        self.assertEqual(self.compute_score('div.klazz a'), float(1)/3)


class CssTokenValuePurityTests(unittest.TestCase):

    def setUp(self):
        self.evaluator = CssAffinityEvaluator()

    def compute_score(self, selector):
        return self.evaluator.compute_token_value_purity(selector)

    def test_single_html_element_has_full_purity(self):
        self.assertEqual(self.compute_score('body'), 1)

    def test_single_nonstandard_html_element_has_no_purity(self):
        self.assertEqual(self.compute_score('notelement'), 0)

    def test_single_css3_pseudoclass_has_full_purity(self):
        self.assertEqual(self.compute_score(':target'), 1)

    def test_single_nonstandard_pseudoclass_has_no_purity(self):
        self.assertEqual(self.compute_score(':nonstandard'), 0)

    def test_single_css3_function_has_full_purity(self):
        self.assertEqual(self.compute_score('p:nth-of-type(3)'), 1)

    def test_single_nonstandard_function_has_no_purity(self):
        self.assertEqual(self.compute_score('p:not-function(3)'), 0.5)

    def test_accept_css2_style_pseudoelements(self):
        self.assertEqual(self.compute_score('p:first-line'), 1)
        self.assertEqual(self.compute_score('p:first-letter'), 1)
        self.assertEqual(self.compute_score('p:before'), 1)
        self.assertEqual(self.compute_score('p:after'), 1)
        self.assertEqual(self.compute_score('p:not-pseudoelement'), 0.5)

    def test_single_css3_pseudoelement_has_full_purity(self):
        self.assertEqual(self.compute_score('p::before'), 1)

    def test_single_nonstandard_pseudoelement_has_no_purity(self):
        self.assertEqual(self.compute_score('p::not-pseudoelement'), 0.5)

    def test_weight_purity_by_proportion_of_pure_names(self):
        self.assertEqual(self.compute_score('notelement body'), 0.5)

    def test_ignore_classname_id_in_socre(self):
        self.assertEqual(self.compute_score('p.klazz div#my-id'), 1)

    def test_return_None_if_no_checkable_nodes(self):
        self.assertIsNone(self.compute_score('.klazz'))


if __name__ == '__main__':
    unittest.main()
