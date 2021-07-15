# Changelog

Changes/Fixes/Additions/Removals addressed in Releases. Dates are in MM/DD/YYYY format.

## [2.0.0](https://github.com/darkwizard242/cis_ubuntu_2004/releases/tag/2.0.0) - 07/15/2021

### Added

- Inclusion of "1.1.1.6 Ensure mounting of squashfs filesystems is disabled (Manual)" per "CIS Benchmark for Ubuntu Linux 20.04 LTS v1.1.0"
- Inclusion of "1.4.1 Ensure permissions on bootloader config are not overridden (Automated)" per "CIS Benchmark for Ubuntu Linux 20.04 LTS v1.1.0"
- Inclusion of "1.8.1 Ensure GNOME Display Manager is removed (Manual)" per "CIS Benchmark for Ubuntu Linux 20.04 LTS v1.1.0"
- Inclusion of "1.8.4 Ensure XDCMP is not enabled (Automated)" per "CIS Benchmark for Ubuntu Linux 20.04 LTS v1.1.0"
- Inclusion of "6.2.1 Ensure accounts in /etc/passwd use shadowed passwords (Automated)" per "CIS Benchmark for Ubuntu Linux 20.04 LTS v1.1.0"

### Removed

- Removal of "1.1.1.7 Ensure mounting of FAT filesystems is limited (Manual)" which has been removed from "CIS Benchmark for Ubuntu Linux 20.04 LTS v1.1.0"
- Removal of "6.2.10 Ensure users' .netrc Files are not group or world accessible (Automated)" which has been removed from "CIS Benchmark for Ubuntu Linux 20.04 LTS v1.1.0"

### Fixed

- Fix for "5.2.2 Ensure permissions on SSH private host key files are configured (Automated)". Corrected usage to `chmod` as required by "CIS Benchmark for Ubuntu Linux 20.04 LTS v1.0.0" official guide and reported in [ISSUE #4](https://github.com/darkwizard242/cis_ubuntu_2004/issues/4) by @estenrye.
- Fix for "5.2.3 Ensure permissions on SSH public host key files are configured (Automated)". Corrected usage to `chmod` as required by "CIS Benchmark for Ubuntu Linux 20.04 LTS v1.0.0" official guide and reported in [ISSUE #4](https://github.com/darkwizard242/cis_ubuntu_2004/issues/4) by @estenrye.
- [Updated](https://github.com/darkwizard242/cis_ubuntu_2004/commit/1f53384e7ec16371781ca99452e7d902a0de8c2b) testinfra to pytest-testinfra as it has been renamed.

### Changed

- Benchmark control name change for control 1.1.12
- Benchmark control name change for control 1.1.13
- Benchmark control name change for control 1.1.14
- Benchmark control name change for control 1.1.18
- 1.4.1 control from CIS benchmark version 1.0.0 has been moved to 1.3.1 as per CIS benchmark version 1.1.0
- 1.4.2 control from CIS benchmark version 1.0.0 has been moved to 1.3.2 as per CIS benchmark version 1.1.0
- 1.5.1 control from CIS benchmark version 1.0.0 has been moved to 1.4.2 as per CIS benchmark version 1.1.0
- 1.5.2 control from CIS benchmark version 1.0.0 has been moved to 1.4.3 as per CIS benchmark version 1.1.0
- 1.5.3 control from CIS benchmark version 1.0.0 has been moved to 1.4.4 as per CIS benchmark version 1.1.0
- 1.6.1 control from CIS benchmark version 1.0.0 has been moved to 1.5.1 as per CIS benchmark version 1.1.0
- 1.6.2 control from CIS benchmark version 1.0.0 has been moved to 1.5.2 as per CIS benchmark version 1.1.0
- 1.6.3 control from CIS benchmark version 1.0.0 has been moved to 1.5.3 as per CIS benchmark version 1.1.0
- 1.6.4 control from CIS benchmark version 1.0.0 has been moved to 1.5.4 as per CIS benchmark version 1.1.0
- 1.7.1.1 control from CIS benchmark version 1.0.0 has been moved to 1.6.1.1 as per CIS benchmark version 1.1.0
- 1.7.1.2 control from CIS benchmark version 1.0.0 has been moved to 1.6.1.2 as per CIS benchmark version 1.1.0
- 1.7.1.3 control from CIS benchmark version 1.0.0 has been moved to 1.6.1.3 as per CIS benchmark version 1.1.0
- 1.7.1.4 control from CIS benchmark version 1.0.0 has been moved to 1.6.1.4 as per CIS benchmark version 1.1.0
- 1.8.1.1 control from CIS benchmark version 1.0.0 has been moved to 1.7.1 as per CIS benchmark version 1.1.0
- 1.8.1.2 control from CIS benchmark version 1.0.0 has been moved to 1.7.2 as per CIS benchmark version 1.1.0
- 1.8.1.3 control from CIS benchmark version 1.0.0 has been moved to 1.7.3 as per CIS benchmark version 1.1.0
- 1.8.1.4 control from CIS benchmark version 1.0.0 has been moved to 1.7.4 as per CIS benchmark version 1.1.0
- 1.8.1.5 control from CIS benchmark version 1.0.0 has been moved to 1.7.5 as per CIS benchmark version 1.1.0
- 1.8.1.6 control from CIS benchmark version 1.0.0 has been moved to 1.7.6 as per CIS benchmark version 1.1.0
- Changed GDM related controls as per CIS benchmark version 1.1.0 (control id's are 1.8.1, 1.8.2 and 1.8.3)
- 2.2.1.1 control from CIS benchmark version 1.0.0 has been moved to 2.1.1.1 as per CIS benchmark version 1.1.0
- 2.2.1.2 control from CIS benchmark version 1.0.0 has been moved to 2.1.1.2 as per CIS benchmark version 1.1.0
- 2.2.1.3 control from CIS benchmark version 1.0.0 has been moved to 2.1.1.3 as per CIS benchmark version 1.1.0
- 2.2.1.4 control from CIS benchmark version 1.0.0 has been moved to 2.1.1.4 as per CIS benchmark version 1.1.0
- 2.2.1.4 control from CIS benchmark version 1.0.0 has been moved to 2.1.1.4 as per CIS benchmark version 1.1.0
- 2.2.2 control from CIS benchmark version 1.0.0 has been moved to 2.1.2 as per CIS benchmark version 1.1.0
- 2.2.3 control from CIS benchmark version 1.0.0 has been moved to 2.1.3 as per CIS benchmark version 1.1.0
- 2.2.4 control from CIS benchmark version 1.0.0 has been moved to 2.1.4 as per CIS benchmark version 1.1.0
- 2.2.5 control from CIS benchmark version 1.0.0 has been moved to 2.1.5 as per CIS benchmark version 1.1.0
- 2.2.6 control from CIS benchmark version 1.0.0 has been moved to 2.1.6 as per CIS benchmark version 1.1.0
- 2.2.7 control from CIS benchmark version 1.0.0 has been moved to 2.1.7 as per CIS benchmark version 1.1.0
- 2.2.8 control from CIS benchmark version 1.0.0 has been moved to 2.1.8 as per CIS benchmark version 1.1.0
- 2.2.9 control from CIS benchmark version 1.0.0 has been moved to 2.1.9 as per CIS benchmark version 1.1.0
- 2.2.10 control from CIS benchmark version 1.0.0 has been moved to 2.1.10 as per CIS benchmark version 1.1.0
- 2.2.11 control from CIS benchmark version 1.0.0 has been moved to 2.1.11 as per CIS benchmark version 1.1.0
- 2.2.12 control from CIS benchmark version 1.0.0 has been moved to 2.1.12 as per CIS benchmark version 1.1.0
- 2.2.13 control from CIS benchmark version 1.0.0 has been moved to 2.1.13 as per CIS benchmark version 1.1.0
- 2.2.14 control from CIS benchmark version 1.0.0 has been moved to 2.1.14 as per CIS benchmark version 1.1.0
- 2.2.15 control from CIS benchmark version 1.0.0 has been moved to 2.1.15 as per CIS benchmark version 1.1.0
- 2.2.16 control from CIS benchmark version 1.0.0 has been moved to 2.1.16 as per CIS benchmark version 1.1.0
- 2.2.17 control from CIS benchmark version 1.0.0 has been moved to 2.1.17 as per CIS benchmark version 1.1.0
- 2.3.1 control from CIS benchmark version 1.0.0 has been moved to 2.2.1 as per CIS benchmark version 1.1.0
- 2.3.2 control from CIS benchmark version 1.0.0 has been moved to 2.2.2 as per CIS benchmark version 1.1.0
- 2.3.3 control from CIS benchmark version 1.0.0 has been moved to 2.2.3 as per CIS benchmark version 1.1.0
- 2.3.4 control from CIS benchmark version 1.0.0 has been moved to 2.2.4 as per CIS benchmark version 1.1.0
- 2.3.5 control from CIS benchmark version 1.0.0 has been moved to 2.2.5 as per CIS benchmark version 1.1.0
- 2.3.6 control from CIS benchmark version 1.0.0 has been moved to 2.2.6 as per CIS benchmark version 1.1.0
- 2.4 control from CIS benchmark version 1.0.0 has been moved to 2.3 as per CIS benchmark version 1.1.0
- Benchmark control name change for control 3.5.1.1
- Benchmark control name change for control 3.5.1.4
- Benchmark control name change for control 3.5.1.5
- Benchmark control name change for control 3.5.1.6
- Benchmark control name change for control 3.5.1.7
- Benchmark control name change for control 3.5.2.2
- Benchmark control name change for control 3.5.2.3
- Benchmark control name change for control 3.5.2.4
- Benchmark control name change for control 3.5.2.5
- Benchmark control name change for control 3.5.2.6
- Benchmark control name change for control 3.5.2.7
- Benchmark control name change for control 3.5.2.8
- Benchmark control name change for control 3.5.3.1.2
- Benchmark control name change for control 3.5.3.1.3
- 3.5.3.2.2 control from CIS benchmark version 1.0.0 has been moved to 3.5.3.2.1 as per CIS benchmark version 1.1.0
- 3.5.3.2.3 control from CIS benchmark version 1.0.0 has been moved to 3.5.3.2.2 as per CIS benchmark version 1.1.0
- 3.5.3.2.1 control from CIS benchmark version 1.0.0 has been moved to 3.5.3.2.3 as per CIS benchmark version 1.1.0
- Benchmark control name change for control 3.5.3.2.4
- 3.5.3.3.2 control from CIS benchmark version 1.0.0 has been moved to 3.5.3.3.1 as per CIS benchmark version 1.1.0
- 3.5.3.3.3 control from CIS benchmark version 1.0.0 has been moved to 3.5.3.3.2 as per CIS benchmark version 1.1.0
- 3.5.3.3.1 control from CIS benchmark version 1.0.0 has been moved to 3.5.3.3.3 as per CIS benchmark version 1.1.0
- Benchmark control name change for control 3.5.3.3.4
- 1.3.1 control from CIS benchmark version 1.0.0 has been moved to 5.2.1 as per CIS benchmark version 1.1.0
- 1.3.2 control from CIS benchmark version 1.0.0 has been moved to 5.2.2 as per CIS benchmark version 1.1.0
- 1.3.3 control from CIS benchmark version 1.0.0 has been moved to 5.2.3 as per CIS benchmark version 1.1.0
- 5.2.1 control from CIS benchmark version 1.0.0 has been moved to 5.3.1 as per CIS benchmark version 1.1.0
- 5.2.2 control from CIS benchmark version 1.0.0 has been moved to 5.3.2 as per CIS benchmark version 1.1.0
- 5.2.3 control from CIS benchmark version 1.0.0 has been moved to 5.3.3 as per CIS benchmark version 1.1.0
- 5.2.17 control from CIS benchmark version 1.0.0 has been moved to 5.3.4 as per CIS benchmark version 1.1.0
- 5.2.4 control from CIS benchmark version 1.0.0 has been moved to 5.3.5 as per CIS benchmark version 1.1.0
- 5.2.5 control from CIS benchmark version 1.0.0 has been moved to 5.3.6 as per CIS benchmark version 1.1.0
- 5.2.6 control from CIS benchmark version 1.0.0 has been moved to 5.3.7 as per CIS benchmark version 1.1.0
- 5.2.7 control from CIS benchmark version 1.0.0 has been moved to 5.3.8 as per CIS benchmark version 1.1.0
- 5.2.8 control from CIS benchmark version 1.0.0 has been moved to 5.3.9 as per CIS benchmark version 1.1.0
- 5.2.9 control from CIS benchmark version 1.0.0 has been moved to 5.3.10 as per CIS benchmark version 1.1.0
- 5.2.10 control from CIS benchmark version 1.0.0 has been moved to 5.3.11 as per CIS benchmark version 1.1.0
- 5.2.11 control from CIS benchmark version 1.0.0 has been moved to 5.3.12 as per CIS benchmark version 1.1.0
- 5.2.12 control from CIS benchmark version 1.0.0 has been moved to 5.3.13 as per CIS benchmark version 1.1.0
- 5.2.13 control from CIS benchmark version 1.0.0 has been moved to 5.3.14 as per CIS benchmark version 1.1.0
- 5.2.14 control from CIS benchmark version 1.0.0 has been moved to 5.3.15 as per CIS benchmark version 1.1.0
- 5.2.15 control from CIS benchmark version 1.0.0 has been moved to 5.3.16 as per CIS benchmark version 1.1.0
- 5.2.16 control from CIS benchmark version 1.0.0 has been moved to 5.3.17 as per CIS benchmark version 1.1.0
- 5.2.18 control from CIS benchmark version 1.0.0 has been moved to 5.3.18 as per CIS benchmark version 1.1.0
- 5.2.19 control from CIS benchmark version 1.0.0 has been moved to 5.3.19 as per CIS benchmark version 1.1.0
- 5.2.20 control from CIS benchmark version 1.0.0 has been moved to 5.3.20 as per CIS benchmark version 1.1.0
- 5.2.21 control from CIS benchmark version 1.0.0 has been moved to 5.3.21 as per CIS benchmark version 1.1.0
- 5.2.22 control from CIS benchmark version 1.0.0 has been moved to 5.3.22 as per CIS benchmark version 1.1.0
- 5.3.1 control from CIS benchmark version 1.0.0 has been moved to 5.4.1 as per CIS benchmark version 1.1.0
- 5.3.2 control from CIS benchmark version 1.0.0 has been moved to 5.4.2 as per CIS benchmark version 1.1.0
- 5.3.3 control from CIS benchmark version 1.0.0 has been moved to 5.4.3 as per CIS benchmark version 1.1.0
- 5.3.4 control from CIS benchmark version 1.0.0 has been moved to 5.4.4 as per CIS benchmark version 1.1.0
- 5.4.1.2 control from CIS benchmark version 1.0.0 has been moved to 5.5.1.1 as per CIS benchmark version 1.1.0
- 5.4.1.1 control from CIS benchmark version 1.0.0 has been moved to 5.5.1.2 as per CIS benchmark version 1.1.0
- 5.4.1.3 control from CIS benchmark version 1.0.0 has been moved to 5.5.1.3 as per CIS benchmark version 1.1.0
- 5.4.1.4 control from CIS benchmark version 1.0.0 has been moved to 5.5.1.4 as per CIS benchmark version 1.1.0
- 5.4.1.5 control from CIS benchmark version 1.0.0 has been moved to 5.5.1.5 as per CIS benchmark version 1.1.0
- 5.4.2 control from CIS benchmark version 1.0.0 has been moved to 5.5.2 as per CIS benchmark version 1.1.0
- 5.4.3 control from CIS benchmark version 1.0.0 has been moved to 5.5.3 as per CIS benchmark version 1.1.0
- 5.4.4 control from CIS benchmark version 1.0.0 has been moved to 5.5.4 as per CIS benchmark version 1.1.0
- 5.4.5 control from CIS benchmark version 1.0.0 has been moved to 5.5.5 as per CIS benchmark version 1.1.0
- 5.5 control from CIS benchmark version 1.0.0 has been moved to 5.6 as per CIS benchmark version 1.1.0
- 5.6 control from CIS benchmark version 1.0.0 has been moved to 5.7 as per CIS benchmark version 1.1.0
- 6.1.6 control from CIS benchmark version 1.0.0 has been moved to 6.1.3 as per CIS benchmark version 1.1.0
- 6.1.5 control from CIS benchmark version 1.0.0 has been moved to 6.1.4 as per CIS benchmark version 1.1.0
- 6.1.8 control from CIS benchmark version 1.0.0 has been moved to 6.1.5 as per CIS benchmark version 1.1.0
- 6.1.4 control from CIS benchmark version 1.0.0 has been moved to 6.1.6 as per CIS benchmark version 1.1.0
- 6.1.9 control from CIS benchmark version 1.0.0 has been moved to 6.1.8 as per CIS benchmark version 1.1.0
- 6.1.3 control from CIS benchmark version 1.0.0 has been moved to 6.1.9 as per CIS benchmark version 1.1.0
- 6.2.1 control from CIS benchmark version 1.0.0 has been moved to 6.2.2 as per CIS benchmark version 1.1.0
- 6.2.12 control from CIS benchmark version 1.0.0 has been moved to 6.2.3 as per CIS benchmark version 1.1.0
- 6.2.6 control from CIS benchmark version 1.0.0 has been moved to 6.2.5 as per CIS benchmark version 1.1.0
- 6.2.5 control from CIS benchmark version 1.0.0 has been moved to 6.2.6 as per CIS benchmark version 1.1.0
- 6.2.9 control from CIS benchmark version 1.0.0 has been moved to 6.2.8 as per CIS benchmark version 1.1.0
- 6.2.8 control from CIS benchmark version 1.0.0 has been moved to 6.2.9 as per CIS benchmark version 1.1.0
- 6.2.11 control from CIS benchmark version 1.0.0 has been moved to 6.2.10 as per CIS benchmark version 1.1.0
- 6.2.2 control from CIS benchmark version 1.0.0 has been moved to 6.2.11 as per CIS benchmark version 1.1.0
- 6.2.3 control from CIS benchmark version 1.0.0 has been moved to 6.2.12 as per CIS benchmark version 1.1.0


## [1.0.2](https://github.com/darkwizard242/cis_ubuntu_2004/releases/tag/1.0.2) - 10/29/2020

### Fixed

- Fix for "3.3.4 Ensure suspicious packets are logged". Corrected [values](https://github.com/darkwizard242/cis_ubuntu_2004/commit/f5e81396221990176524ab37fad7a080dcc470ef) as required by "CIS Benchmark for Ubuntu Linux 20.04 LTS v1.0.0" official guide.

## [1.0.1](https://github.com/darkwizard242/cis_ubuntu_2004/releases/tag/1.0.1) - 09/28/2020

### Fixed

- Minor workaround for 6.2.2 - [#2](https://github.com/darkwizard242/cis_ubuntu_2004/pull/2/commits/ab20e5c4b20094fc5057b2dfd2c56bec8e8a1faa) causing TravisCI build to fail at random.

## [1.0.0](https://github.com/darkwizard242/cis_ubuntu_2004/releases/tag/1.0.0) - 09/21/2020

### Added

- Ansible Galaxy role for CIS Benchmark for Ubuntu Linux 20.04 LTS v1.0.0 added.
