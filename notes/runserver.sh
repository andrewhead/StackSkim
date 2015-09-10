#! /bin/sh

./makeindex.sh
harp server . -p ${1:-9000}
