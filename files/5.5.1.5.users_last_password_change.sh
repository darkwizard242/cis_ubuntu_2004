#!/bin/bash -e

set -eou pipefail

awk -F: '{print $1}' /etc/shadow | while read -r usr
do
  if [[ $(date --date="$(chage --list "$usr" | grep '^Last password change' | cut -d: -f2)" +%s) > $(date +%s) ]];
  then
    echo "$usr"
  fi
done
