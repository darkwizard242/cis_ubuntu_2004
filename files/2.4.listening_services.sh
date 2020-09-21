#!/bin/bash -e

set -eou pipefail

lsof -i -P -n | grep -v "(ESTABLISHED)"
