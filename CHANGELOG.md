# Changelog
Changes/Fixes/Additions addressed in Releases. Dates are in MM/DD/YYYY format.

## [2.0.0](https://github.com/darkwizard242/cis_ubuntu_2004/releases/tag/1.0.3) - TBD

### Added

* Inclusion of "1.1.1.6 Ensure mounting of squashfs filesystems is disabled (Manual)" per "CIS Benchmark for Ubuntu Linux 20.04 LTS v1.1.0"
* Inclusion of "1.4.1 Ensure permissions on bootloader config are not overridden (Automated)" per "CIS Benchmark for Ubuntu Linux 20.04 LTS v1.1.0"

### Fixed/Changed

* [Updated](https://github.com/darkwizard242/cis_ubuntu_2004/commit/1f53384e7ec16371781ca99452e7d902a0de8c2b) testinfra to pytest-testinfra as it has been renamed.
* Benchmark control name change for control 1.1.12
* Benchmark control name change for control 1.1.13
* Benchmark control name change for control 1.1.14
* Benchmark control name change for control 1.1.18
* 1.4.1 control from CIS benchmark version 1.0.0 has been moved to 1.3.1 as per CIS benchmark version 1.1.0
* 1.4.2 control from CIS benchmark version 1.0.0 has been moved to 1.3.2 as per CIS benchmark version 1.1.0
* 1.5.1 control from CIS benchmark version 1.0.0 has been moved to 1.4.2 as per CIS benchmark version 1.1.0
* 1.5.2 control from CIS benchmark version 1.0.0 has been moved to 1.4.3 as per CIS benchmark version 1.1.0

### Removed

* Removal of "1.1.1.7 Ensure mounting of FAT filesystems is limited (Manual)" which has been removed from "CIS Benchmark for Ubuntu Linux 20.04 LTS v1.1.0"

## [1.0.2](https://github.com/darkwizard242/cis_ubuntu_2004/releases/tag/1.0.2) - 10/29/2020

### Fixed

* Fix for "3.3.4 Ensure suspicious packets are logged". Corrected [values](https://github.com/darkwizard242/cis_ubuntu_2004/commit/f5e81396221990176524ab37fad7a080dcc470ef) as required by "CIS Benchmark for Ubuntu Linux 20.04 LTS v1.0.0" official guide.

## [1.0.1](https://github.com/darkwizard242/cis_ubuntu_2004/releases/tag/1.0.1) - 09/28/2020

### Fixed

* Minor workaround for 6.2.2 - [#2](https://github.com/darkwizard242/cis_ubuntu_2004/pull/2/commits/ab20e5c4b20094fc5057b2dfd2c56bec8e8a1faa) causing TravisCI build to fail at random.

## [1.0.0](https://github.com/darkwizard242/cis_ubuntu_2004/releases/tag/1.0.0) - 09/21/2020

### Added
* Ansible Galaxy role for CIS Benchmark for Ubuntu Linux 20.04 LTS v1.0.0 added.
