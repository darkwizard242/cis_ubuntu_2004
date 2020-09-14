#!/bin/bash -e

LIST=$(grep ^shadow:[^:]*:[^:]*:[^:]+ /etc/group) || true
if [[ ${LIST} = "" ]];
then
  echo "Nothing to remediate."
else
  echo "Requires remediation for: ${LIST}"
fi
