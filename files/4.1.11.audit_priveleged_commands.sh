#!/bin/bash -e

set -eou pipefail

for executable in  $(df | grep '^/dev' | awk '{ print $NF }'); do find $executable -xdev -type f -perm -4000 -o -type f -perm -2000 2>/dev/null; done
