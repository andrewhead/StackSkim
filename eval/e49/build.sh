#! /bin/sh

ANTLR='java -Xmx500M org.antlr.v4.Tool'
SRC_DIR=parser/
OUTPUT_DIR=parser/gen/
CLASSPATH="$CLASSPATH:$OUTPUT_DIR:$SRC_DIR"

$ANTLR Css.g4 -o $OUTPUT_DIR
CLASSPATH=$CLASSPATH javac parser/gen/*.java
CLASSPATH=$CLASSPATH javac parser/*.java
