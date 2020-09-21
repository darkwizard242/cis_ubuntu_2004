#!/bin/bash -e

awk -F: '($2 == "" ) { print $1 }' /etc/shadow
