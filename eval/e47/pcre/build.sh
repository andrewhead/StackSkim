#! /bin/bash
GRAMMAR_DIR=src/
GRAMMAR=PCRE.g4
ANTLR='java -Xmx500M org.antlr.v4.Tool'
OUTPUT_DIR=parser

mkdir -p $OUTPUT_DIR
touch $OUTPUT_DIR/__init__.py
cp $GRAMMAR_DIR/$GRAMMAR .
$ANTLR -Dlanguage=Python2 -o $OUTPUT_DIR $GRAMMAR
rm $GRAMMAR
