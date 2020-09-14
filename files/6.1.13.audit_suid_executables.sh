#!/bin/bash -e

PARTITION_SOURCE_LIST=$(df -h --output=target -x tmpfs -x devtmpfs | grep -v Mounted)

find ${PARTITION_SOURCE_LIST} -xdev -type f -perm -4000
