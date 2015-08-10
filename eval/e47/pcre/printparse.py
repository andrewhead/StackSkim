#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from antlr4.InputStream import InputStream
from antlr4 import CommonTokenStream, ParseTreeWalker
import argparse
import logging

from parser.PCRELexer import PCRELexer
from parser.PCREParser import PCREParser
from parser.PCREListener import PCREListener


logging.basicConfig(level=logging.INFO, format="%(message)s")


class PCRELiteralCounter(PCREListener):

    def count_literals(self, pattern):

        self.atom_count = 0
        self.literal_count = 0

        walker = ParseTreeWalker()
        input_ = InputStream(pattern)
        lexer = PCRELexer(input_)
        stream = CommonTokenStream(lexer)
        parser = PCREParser(stream)
        tree = parser.parse()

        walker.walk(self, tree)
        return self.literal_count, self.atom_count

    def enterAtom(self, ctx):
        child = ctx.children[0]
        if type(child) == PCREParser.LiteralContext:
            self.literal_count += 1
        self.atom_count += 1


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="describe regular expression parse")
    parser.add_argument('pattern', help='regular expression to parse')
    args = parser.parse_args()
    counter = PCRELiteralCounter()
    lit_count, atom_count = counter.count_literals(args.pattern)
    print "Literal count:", lit_count
    print "Literal count:", atom_count
