# IN DEVELOPMENT :lock::no_entry:

[![Build Status](https://travis-ci.com/darkwizard242/cis-ubuntu-20.04.svg?branch=feature_cis-ubuntu-20.04-development)](https://travis-ci.com/darkwizard242/cis-ubuntu-20.04)

# Ansible Role: cis-ubuntu-20.04

Ansible Role for applying **CIS Ubuntu Linux 20.04 LTS Benchmark v1.0.0**.

## Few Considerations:

Benchmarks around the **_disk partitioning_** and their **_mount points_** from **Section 1** are not applied in this role. The reason is simply that every individual/organization's system architecture and disk layout will likely vary. I would recommend to apply those yourself. Following is a list of those benchmarks:

- 1.1.10 Ensure separate partition exists for /var (Automated)
- 1.1.11 Ensure separate partition exists for /var/tmp (Automated)
- 1.1.12 Ensure nodev option set on /var/tmp partition (Automated)
- 1.1.13 Ensure nosuid option set on /var/tmp partition (Automated)
- 1.1.14 Ensure noexec option set on /var/tmp partition (Automated)
- 1.1.15 Ensure separate partition exists for /var/log (Automated)
- 1.1.16 Ensure separate partition exists for /var/log/audit (Automated)
- 1.1.17 Ensure separate partition exists for /home (Automated)
- 1.1.18 Ensure nodev option set on /home partition (Automated)
- 1.1.19 Ensure nodev option set on removable media partitions (Manual)
- 1.1.20 Ensure nosuid option set on removable media partitions (Manual)
- 1.1.21 Ensure noexec option set on removable media partitions (Manual)

## Requirements

None.

## Role Variables

Default variables for the role tasks are located in `defaults/main/`.

## Dependencies

None

## License

[MIT](https://github.com/darkwizard242/cis-ubuntu-20.04/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
