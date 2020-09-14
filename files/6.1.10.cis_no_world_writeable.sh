#!/bin/bash -e

PARTITION_SOURCE_LIST=$(df -h --output=target -x tmpfs -x devtmpfs | grep -v Mounted)

for FILENAME in $(find ${PARTITION_SOURCE_LIST} -xdev -type f -perm -0002);
do
  chmod o-w ${FILENAME}
done
