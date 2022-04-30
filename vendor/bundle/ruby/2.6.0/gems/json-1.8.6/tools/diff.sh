#!/bin/sh

files=`find ext -name '*.[ch]' -o -name parser.rl`

for f in $files
do
  b=`basename $f`
  g=`find ../ruby/ext/json -name $b`
  d=`diff -u $f $g`
  test -z "$d" && continue
  echo "$d"
  read -p "Edit diff of $b? " a
  case $a in
  [yY]*)
    vimdiff $f $g
    ;;
  esac
done
