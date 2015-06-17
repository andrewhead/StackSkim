#! /bin/sh
# Convenience script to cycle through all files to open them in sequence.
# Args:
#   1: starting index to open (default 0)


function link_has_example {

  link=$1

  while [[ 1 ]]
  do
    read -p "Does page contain a code example (y/n): " response
    if printf "%s\n" "$response" | grep -Eq "$(locale yesexpr)"
    then
      val=1
      break
    elif printf "%s\n" "$response" | grep -Eq "$(locale noexpr)"
    then
      val=0
      break
    else
      echo "Invalid response.  Try again."
    fi
  done

  # Update whether this link has a code example
  echo "UPDATE page SET has_example = $val WHERE link='$link';"
  sqlite3 test_pages.db "UPDATE page SET has_example = $val WHERE link='$link';"

}


i=${1:-0}
while [[ 1 ]]
do
  i=$((i+1))
  echo "Opening file $i"
  link=`./open.py index $i`
  echo "Reading file from link: $link"
  link_has_example $link
  if [ $? -eq 2 ]
  then
    echo "Read all files"
    break
  fi
  echo "Press Enter to continue."
  read  # wait for user input to move onto next file
done
