#! /bin/sh

EVAL_DIR=eval
PROTO_DIR=proto
BASE_FILE=base.md
OUTPUT_FILE=index.md

function add_notes {
  TITLE=$1
  NOTE_DIR=$2
  PREFIX=$3
  echo "" >> $OUTPUT_FILE
  echo "# $TITLE" >> $OUTPUT_FILE
  echo "" >> $OUTPUT_FILE
  for file in `ls -r $NOTE_DIR/$PREFIX*.md`
  do
    shortname=`echo $file | sed 's/\.md$//'`
    title=`head -1 $file | sed 's/^# //'`
    echo "* [$title]($shortname)" >> $OUTPUT_FILE
  done
}

cp $BASE_FILE $OUTPUT_FILE
add_notes "Evaluations" $EVAL_DIR eval
add_notes "Prototypes" $PROTO_DIR proto
