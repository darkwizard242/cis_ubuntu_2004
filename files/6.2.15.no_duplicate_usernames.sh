#!/bin/bash -e

cut -d: -f1 /etc/passwd | sort | uniq -d | while read x
do
  echo "Duplicate login name ${x} in /etc/passwd"
done
