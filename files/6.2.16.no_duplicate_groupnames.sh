#!/bin/bash -e

cut -d: -f1 /etc/group | sort | uniq -d | while read x
do
  echo "Duplicate group name ${x} in /etc/group"
done
