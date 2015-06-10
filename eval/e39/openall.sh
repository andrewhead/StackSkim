#! /bin/sh
# Convenience script to cycle through all files to open them in sequence.
# Args:
#   1: starting index to open (default 0)

i=${1:-0}
while [[ 1 ]]
do
  i=$((i+1))
  echo "Opening file $i"
  ./open.py index $i
  if [ $? -eq 2 ]
  then
    echo "Read all files"
    break
  fi
  echo "Press Enter to continue."
  read  # wait for user input to move onto next file
done
