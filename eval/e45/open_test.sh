#! /bin/sh
# Convenience script to cycle through all files to open them in sequence.
# Args:
#   1: language to look for tutorial files for
#   2: index of file in the sequence


i=${2:--1}
lang=$1
testmode=${3:-'all'}
while [[ 1 ]]
do
  i=$((i+1))
  link=`./open.py ml $lang $i --testmode $testmode`
  echo "========================"
  echo "Opening file $i ($link)"
  if [ $? -eq 2 ]
  then
    echo "Read all files"
    break
  fi
  echo "Press enter to continue"
  read
done
