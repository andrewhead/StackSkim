#! /bin/sh

EVAL_DIR=eval
BASE_FILE=base.md
OUTPUT_FILE=index.md

cp $BASE_FILE $OUTPUT_FILE
echo "# Evaluations" >> $OUTPUT_FILE
echo "" >> $OUTPUT_FILE

for file in `ls -r $EVAL_DIR/eval*.md`
do
  shortname=`echo $file | sed 's/\.md$//'`
  title=`head -1 $file | sed 's/^# //'`
  echo "* [$title]($shortname)" >> $OUTPUT_FILE
done
