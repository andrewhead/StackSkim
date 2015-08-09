#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
from cssselect.parser import \
    Element, Hash, Class, Pseudo, Attrib, Selector, \
    FunctionalPseudoElement, Function, Negation
from cssselect.parser import SelectorSyntaxError
import cssselect
import re


logging.basicConfig(level=logging.INFO, format="%(message)s")

''' REUSE: Tutorons server code. '''
''' We include None in this list because patterns that match all tags
    (e.g. ".klazz") yield an Element with property 'element' == None. '''
HTML_TAGS = [
    'a', 'abbr', 'address', 'area', 'article', 'aside',
    'audio', 'b', 'base', 'bb', 'bdo', 'blockquote', 'body',
    'br', 'button', 'canvas', 'caption', 'cite', 'code', 'col',
    'colgroup', 'command', 'datagrid', 'datalist', 'dd', 'del',
    'details', 'dfn', 'dialog', 'div', 'dl', 'dt', 'em', 'embed',
    'fieldset', 'figure', 'footer', 'form', 'h1', 'h2', 'h3', 'h4',
    'h5', 'h6', 'head', 'header', 'hr', 'html', 'i', 'iframe', 'img',
    'input', 'ins', 'kbd', 'label', 'legend', 'li', 'link', 'map',
    'mark', 'menu', 'meta', 'meter', 'nav', 'noscript', 'object', 'ol',
    'optgroup', 'option', 'output', 'p', 'param', 'pre', 'progress',
    'q', 'rp', 'rt', 'ruby', 'samp', 'script', 'section', 'select',
    'small', 'source', 'span', 'strong', 'style', 'sub', 'sup',
    'table', 'tbody', 'td', 'textarea', 'tfoot', 'th', 'thead',
    'time', 'title', 'tr', 'ul', 'var', 'video', None,
]

'''
Pure token types are those that are likely to be found in this language but unlikely
syntactically to happen in others.
'''
TOKEN_TYPES = [Element, Hash, Class, Pseudo, Attrib, FunctionalPseudoElement, Function, Negation]
PURE_TOKEN_TYPES = [Hash, Class, Pseudo, Attrib, FunctionalPseudoElement]

'''
Pure pseudo-classes and pseudo-elements from:
http://www.w3.org/TR/css3-selectors/#pseudo-classes
The 'functions' we describe here are called functions by the
cssselect parser, even though they're called pseudo-classes
in the W3C specifications.
':not' is considered a Negation node by cssselect, so we leave it
out in the enumeration here.
'''
PURE_PSEUDOCLASSES = [
    'link', 'visited', 'hover', 'active', 'focus', 'target',
    'enabled', 'disabled', 'checked', 'root', 'first-child',
    'last-child', 'first-of-type', 'last-of-type',
    'only-child', 'only-of-type', 'empty',
]
PURE_FUNCTIONS = [
    'lang', 'nth-child', 'nth-last-child', 'nth-of-type',
    'nth-child', 'nth-last-of-type',
]
PURE_PSEUDOELEMENTS = [
    'first-line', 'first-letter', 'before', 'after',
]


def get_descendants(x):
    ''' REUSE: Tutorons server code. '''
    ''' Get all descendants of an object. '''

    if isinstance(x, list):
        return [i for el in x for i in get_descendants(el)]
    elif hasattr(x, '__dict__'):
        return [x] + [i for child in x.__dict__.values() for i in get_descendants(child)]
    elif isinstance(x, dict):
        return [i for child in x for i in get_descendants(child)]
    else:
        return []


def get_css_nodes(string):
    ''' REUSE: _is_selector in Tutorons server code. '''
    try:
        # cssselect doesn't like links, so we replace them.
        string = re.sub(r"(href.=)([^\]]*)\]", r"\1fakelink]", string)
        tree = cssselect.parse(string)
        selector_nodes = get_descendants(tree)
        return selector_nodes
    except SelectorSyntaxError:
        return []


class CssAffinityEvaluator(object):

    def evaluate(self, text):
        metric_functions = [
            self.compute_token_type_purity,
            self.compute_token_value_purity,
        ]
        scores = []
        for f in metric_functions:
            s = f(text)
            if s is not None:
                scores.append(s)
        return sum(scores) / float(len(scores))

    def compute_token_type_purity(self, text):
        nodes = get_css_nodes(text)
        total_tokens = 0
        pure_tokens = 0
        for n in nodes:
            if self._is_token(n):
                total_tokens += 1
                if self._is_pure_token(n):
                    pure_tokens += 1
        return float(pure_tokens) / total_tokens

    def compute_token_value_purity(self, text):

        '''
        We assign value purity functions for each node type in the parse tree.
        The 'filter' function determines whether this is a node for which we
        want to perform the purity check.
        The 'check' node computes whether the value of the node is pure.
        '''
        value_check_functions = {
            Element: {
                'filter': lambda n: n.element is not None,
                'check': lambda n: n.element in HTML_TAGS,
            },
            Pseudo: {
                'check': lambda n: n.ident in PURE_PSEUDOCLASSES
            },
            Function: {
                'check': lambda n: n.name in PURE_FUNCTIONS
            },
            Selector: {
                'filter': lambda n: n.pseudo_element is not None,
                'check': lambda n: n.pseudo_element in PURE_PSEUDOELEMENTS,
            }
        }

        nodes = get_css_nodes(text)
        total_tokens = 0
        pure_tokens = 0
        for n in nodes:
            if type(n) in value_check_functions:
                functions = value_check_functions[type(n)]
                if 'filter' not in functions or functions['filter'](n):
                    total_tokens += 1
                    if functions['check'](n):
                        pure_tokens += 1

        return pure_tokens / float(total_tokens) if total_tokens > 0 else None

    def _is_token(self, node):
        if type(node) in TOKEN_TYPES:
            if type(node) == Element:
                return node.element is not None
            else:
                return True
        elif type(node) == Selector:
            return node.pseudo_element is not None
        return False

    def _is_pure_token(self, node):
        if type(node) in PURE_TOKEN_TYPES:
            return True
        elif type(node) == Selector and node.pseudo_element is not None:
            return True
        return False


def main():
    pass


if __name__ == '__main__':
    main()
