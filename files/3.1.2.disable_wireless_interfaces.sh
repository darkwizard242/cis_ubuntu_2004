#!/bin/bash -e

set -eou pipefail

if [ -n "$(find /sys/class/net/*/ -type d -name wireless)" ];
then
  drivers=$(for driverdir in $(find /sys/class/net/*/ -type d -name wireless | xargs -0 dirname); do basename "$(readlink -f "$driverdir"/device/driver)";done | sort -u)
  for dm in $drivers;
  do
    echo "install $dm /bin/true" >> /etc/modprobe.d/3.1.2_disable_wireless.conf
  done
fi
