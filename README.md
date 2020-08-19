# IN DEVELOPMENT :lock::no_entry:

[![Build Status](https://travis-ci.com/darkwizard242/cis-ubuntu-20.04.svg?branch=feature_cis-ubuntu-20.04-development)](https://travis-ci.com/darkwizard242/cis-ubuntu-20.04)![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/cis-ubuntu-20.04?color=orange&style=flat-square)

# Ansible Role: cis-ubuntu-20.04

Ansible Role for applying **CIS Ubuntu Linux 20.04 LTS Benchmark v1.0.0**.

## 1\. Installation/Download Instructions:

This role is available on Ansible Galaxy. There are a few methods you can utilize to install/download the `cis-ubuntu-20.04` role on your Ansible Controller node either from Ansible Galaxy or directly from the repository.

### Without a requirements.yml file:

- Installing/Downloading latest (default) available tag version:

  ```shell
  ansible-galaxy install darkwizard242.cis-ubuntu-20.04
  ```

- Installing/Downloading specific available tag version (using 1.0.0 as an example):

  ```shell
  ansible-galaxy install darkwizard242.cis-ubuntu-20.04,1.0.0
  ```

- Installing/Downloading specific available branch version from repository (using master branch as an example):

  ```shell
  ansible-galaxy install darkwizard242.cis-ubuntu-20.04,master
  ```

### With a requirements.yml file:

Add to an existing **requirements.yml** file along with your other roles or create a new one to install `cis-ubuntu-20.04`.

- Latest version directly from Ansible Galaxy.

  ```yaml
  - name: darkwizard242.cis-ubuntu-20.04
  ```

- Specific version directly from Ansible Galaxy.

  ```yaml
  - name: darkwizard242.cis-ubuntu-20.04
    version: 1.0.0
  ```

- Specific branch from repository.

  ```yaml
  - name: cis-ubuntu-20.04
    src: https://github.com/darkwizard242/cis-ubuntu-20.04
    version: master
  ```

Installing/Downloading after adding to **requirements.yml** :

```shell
ansible-galaxy install -r requirements.yml
```

**_NOTE:_** Installing a role as mentioned above only downloads the role to have it available for use in your ansible playbooks. You can read up on the roles install/download instructions [here](https://galaxy.ansible.com/docs/using/installing.html).

## 2\. Few Considerations:

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

## 3\. Requirements

None.

## 4\. Role Variables

Role default variables being utilized in role tasks are located in `defaults/main/`.

[defaults/main/main.yml](https://github.com/darkwizard242/cis-ubuntu-20.04/blob/master/defaults/main/main.yml) consists of variables referring to the entire CIS sections such as the following:

```yaml
ubuntu_2004_cis_section1: true
ubuntu_2004_cis_section2: true
ubuntu_2004_cis_section3: true
ubuntu_2004_cis_section4: true
ubuntu_2004_cis_section5: true
ubuntu_2004_cis_section6: true
```

The purpose of above mentioned variables is to indicate that all of tasks pertaining to these sections should be applied through `cis-ubuntu-20.04` role.

Variables for each of the sections are located in their own files.

- Section 1 variables are in [defaults/main/section_01.yml](https://github.com/darkwizard242/cis-ubuntu-20.04/blob/master/defaults/main/section_01.yml)
- Section 2 variables are in [defaults/main/section_02.yml](https://github.com/darkwizard242/cis-ubuntu-20.04/blob/master/defaults/main/section_02.yml)
- Section 3 variables are in [defaults/main/section_03.yml](https://github.com/darkwizard242/cis-ubuntu-20.04/blob/master/defaults/main/section_03.yml)

Role default values for everything in the `cis-ubuntu-20.04` role can be superseded via passing them in a playbook or any other [variable precedence method](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#variable-precedence-where-should-i-put-a-variable).

- ### Important variables

CIS Ubuntu 20.04 hardening benchmarks require purging of many services that can be exploited, have known vulnerabilities, result in an exposure of attack surface or should be disabled if not required. As per the benchmark, by default - all of these services will be purged and the value for their variables has been set to `false`. However, if you still require the use of these services for any reason, please change their values to `true` so that when applying the role in a playbook, the role tasks to _purge_ those services can be **skipped**.

```yaml
ubuntu_2004_cis_require_ipv6: false # Set to `true` if IPv6 is required.
ubuntu_2004_cis_require_xwindows_system: false # Set to `true` if X Windows System is required.
ubuntu_2004_cis_require_cups: false # Set to `true` if CUPS is required.
ubuntu_2004_cis_require_dhcp_server: false # Set to `true` if DHCP server is required.
ubuntu_2004_cis_require_ldap_server: false # Set to `true` if LDAP server is required.
ubuntu_2004_cis_require_nfs_server: false # Set to `true` if NFS server is required.
ubuntu_2004_cis_require_dns_server: false # Set to `true` if DNS server is required.
ubuntu_2004_cis_require_ftp_server: false # Set to `true` if FTP server is required.
ubuntu_2004_cis_require_http_server: false # Set to `true` if HTTP (apache2) server is required.
ubuntu_2004_cis_require_imap_pop3_server: false # Set to `true` if IMAP and POP3 servers are required.
ubuntu_2004_cis_require_samba_server: false  # Set to `true` if Samba daemon is required.
ubuntu_2004_cis_require_squid_server: false # Set to `true` if Squid server is required.
ubuntu_2004_cis_require_snmp_server: false # Set to `true` if SNMP server is required.
ubuntu_2004_cis_require_mail_server: true # Set's postfix to act in local-only mode.
ubuntu_2004_cis_require_rsyncd_server: false # Set to `true` if RSYNC is required.
ubuntu_2004_cis_require_nis_server: false # Set to `true` if NIS server is required.
ubuntu_2004_cis_require_nis_client: false # Set to `true` if NIS client is required.
ubuntu_2004_cis_require_rsh_client: false # Set to `true` if RSH client is required.
ubuntu_2004_cis_require_talk_client: false # Set to `true` if TALK client is required.
ubuntu_2004_cis_require_telnet_client: false # Set to `true` if TELNET client is required.
ubuntu_2004_cis_require_ldap_client: false # Set to `true` if LDAP client is required.
ubuntu_2004_cis_require_rpcbind_client: false # Set to `true` if RPCBIND client is required.
```

## 5\. Dependencies

None

## License

[MIT](https://github.com/darkwizard242/cis-ubuntu-20.04/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
