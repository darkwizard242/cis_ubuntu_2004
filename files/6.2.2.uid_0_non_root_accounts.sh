#!/bin/bash -e

awk -F: '($3 == 0 && $1 != "root") {i++;print $1 } END {exit i}' /etc/passwd
