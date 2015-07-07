#! /bin/sh
# Convenience script to cycle through all files to open them in sequence.
# Args:
#   1: starting index to open (default 0)


function link_has_example {

  link=$1

  while [[ 1 ]]
  do
    echo "Does page contain a code example?"
    read -p "Yes, No, Unfound (y/n/u): " response
    if printf "%s\n" "$response" | grep -Eq "$(locale yesexpr)"
    then
      has_example=1
      notfound=0
      break
    elif printf "%s\n" "$response" | grep -Eq "$(locale noexpr)"
    then
      has_example=0
      notfound=0
      break
    elif [ "$response" == "u" ]
    then
      has_example=0
      notfound=1
      break
    else
      echo "Invalid response.  Try again."
    fi
  done

  # Update whether this link has a code example
  sqlite3 test_pages.db "UPDATE page SET has_example = $has_example WHERE link='$link';"
  sqlite3 test_pages.db "UPDATE page SET notfound = $notfound WHERE link='$link';"
  echo "Stored (has_example = $has_example, notfound = $notfound)"

}


lang=$1
i=${2:-0}
while [[ 1 ]]
do
  i=$((i+1))
  link=`./open.py ml $lang $i`
  echo "Opening file $i ($link)"
  link_has_example $link
  echo "========================"
  if [ $? -eq 2 ]
  then
    echo "Read all files"
    break
  fi
done
