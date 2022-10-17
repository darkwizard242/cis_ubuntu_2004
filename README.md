[![Build Status](https://travis-ci.com/darkwizard242/cis_ubuntu_2004.svg?branch=master)](https://travis-ci.com/darkwizard242/cis_ubuntu_2004) ![Ansible Role](https://img.shields.io/ansible/role/50862?color=dark%20green) ![Ansible Role](https://img.shields.io/ansible/role/d/50862?color=dark&style=flat-square) ![Ansible Quality Score](https://img.shields.io/ansible/quality/50862?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=cis_ubuntu_2004&metric=alert_status)](https://sonarcloud.io/dashboard?id=cis_ubuntu_2004) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/cis_ubuntu_2004?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/cis_ubuntu_2004?color=orange&style=flat-square)

# Ansible Role: cis_ubuntu_2004 :computer:

Ansible Role for applying **CIS Benchmark for Ubuntu Linux 20.04 LTS**.

Currently supported and available versions are:

- CIS Benchmark for Ubuntu Linux 20.04 LTS v1.1.0
- CIS Benchmark for Ubuntu Linux 20.04 LTS v1.0.0

## Versioning

The below table specifies the versions of role available on [Ansible Galaxy](https://galaxy.ansible.com/darkwizard242/cis_ubuntu_2004) and [GitHub Releases](https://github.com/darkwizard242/cis_ubuntu_2004/releases), in terms of the corresponding [CIS Benchmark for Ubuntu Linux 20.04 LTS](https://www.cisecurity.org/benchmark/ubuntu_linux).

CIS Ubuntu 20.04 Benchmark Version | Ansible Galaxy Version                   | Repository Tag Version
---------------------------------- | ---------------------------------------- | ----------------------------------------
1.0.0                              | 1.0.0, 1.0.1, 1.0.2                      | 1.0.0, 1.0.1, 1.0.2
1.1.0                              | 2.0.0, 2.0.1, 2.1.0, 3.0.0, 3.1.0, 3.2.0 | 2.0.0, 2.0.1, 2.1.0, 3.0.0, 3.1.0, 3.2.0

## 1\. Installation/Download Instructions:

This role is available on Ansible Galaxy. There are a few methods you can utilize to install/download the `cis_ubuntu_2004` role on your Ansible Controller node either from Ansible Galaxy or directly from the repository.

### Without a requirements.yml file:

- Installing/Downloading latest (default) available tag version:

  ```shell
  ansible-galaxy install darkwizard242.cis_ubuntu_2004
  ```

- Installing/Downloading specific available tag version (using 3.2.0 as an example):

  ```shell
  ansible-galaxy install darkwizard242.cis_ubuntu_2004,3.2.0
  ```

- Installing/Downloading specific available branch version from repository (using `master` branch as an example, `master` will always be compliant to latest available version of **CIS Ubuntu 20.04 Benchmark**):

  ```shell
  ansible-galaxy install darkwizard242.cis_ubuntu_2004,master
  ```

- Installing/Downloading specific available branch version from repository (using `feature/cis_version_1.1.0` branch as an example which complies with latest updates for **CIS Ubuntu 20.04 Benchmark Version v1.1.0**):

  ```shell
  ansible-galaxy install darkwizard242.cis_ubuntu_2004,feature/cis_version_1.1.0
  ```

- Installing/Downloading specific available branch version from repository (using `feature/cis_version_1.0.0` branch as an example which complies with latest updates for **CIS Ubuntu 20.04 Benchmark Version v1.0.0**):

  ```shell
  ansible-galaxy install darkwizard242.cis_ubuntu_2004,feature/cis_version_1.0.0
  ```

### With a requirements.yml file:

Add to an existing **requirements.yml** file along with your other roles or create a new one to install `cis_ubuntu_2004`.

- Latest version directly from Ansible Galaxy.

  ```yaml
  - name: darkwizard242.cis_ubuntu_2004
  ```

- Specific version directly from Ansible Galaxy.

  ```yaml
  - name: darkwizard242.cis_ubuntu_2004
    version: 3.2.0
  ```

- Specific branch from repository.

  ```yaml
  - name: cis_ubuntu_2004
    src: https://github.com/darkwizard242/cis_ubuntu_2004
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
- 1.1.12 Ensure /var/tmp partition includes the nodev option (Automated)
- 1.1.13 Ensure /var/tmp partition includes the nosuid option (Automated)
- 1.1.14 Ensure /var/tmp partition includes the noexec option (Automated)
- 1.1.15 Ensure separate partition exists for /var/log (Automated)
- 1.1.16 Ensure separate partition exists for /var/log/audit (Automated)
- 1.1.17 Ensure separate partition exists for /home (Automated)
- 1.1.18 Ensure /home partition includes the nodev option (Automated)
- 1.1.19 Ensure nodev option set on removable media partitions (Manual)
- 1.1.20 Ensure nosuid option set on removable media partitions (Manual)
- 1.1.21 Ensure noexec option set on removable media partitions (Manual)

Following benchmarks from **Section 4** has also not been implemented:

- 4.2.1.5 Ensure rsyslog is configured to send logs to a remote log host (Automated)
- 4.2.1.6 Ensure remote rsyslog messages are only accepted on designated log hosts. (Manual)
- 4.3 Ensure logrotate is configured (Manual)

## 3\. Requirements

None.

## 4\. Role Variables

Role default variables being utilized in role tasks are located in `defaults/main/`.

[defaults/main/main.yml](https://github.com/darkwizard242/cis_ubuntu_2004/blob/master/defaults/main/main.yml) consists of variables referring to the entire CIS sections like the following and the system breaking variables like the ones mentioned in [Important Variables](https://github.com/darkwizard242/cis_ubuntu_2004/tree/master#important-variables) section:

```yaml
ubuntu_2004_cis_section1: true
ubuntu_2004_cis_section2: true
ubuntu_2004_cis_section3: true
ubuntu_2004_cis_section4: true
ubuntu_2004_cis_section5: true
ubuntu_2004_cis_section6: true
```

The purpose of above mentioned variables is to indicate that all of tasks pertaining to these sections should be applied through `cis_ubuntu_2004` role.

Variables for each of the sections are located in their own files.

- Section 1 variables are in [defaults/main/section_01.yml](https://github.com/darkwizard242/cis_ubuntu_2004/blob/master/defaults/main/section_01.yml)
- Section 2 variables are in [defaults/main/section_02.yml](https://github.com/darkwizard242/cis_ubuntu_2004/blob/master/defaults/main/section_02.yml)
- Section 3 variables are in [defaults/main/section_03.yml](https://github.com/darkwizard242/cis_ubuntu_2004/blob/master/defaults/main/section_03.yml)
- Section 4 variables are in [defaults/main/section_04.yml](https://github.com/darkwizard242/cis_ubuntu_2004/blob/master/defaults/main/section_04.yml)
- Section 5 variables are in [defaults/main/section_05.yml](https://github.com/darkwizard242/cis_ubuntu_2004/blob/master/defaults/main/section_05.yml)
- Section 6 variables are in [defaults/main/section_06.yml](https://github.com/darkwizard242/cis_ubuntu_2004/blob/master/defaults/main/section_06.yml)

Role default values for everything in the `cis_ubuntu_2004` role can be superseded via passing them in a playbook or any other [variable precedence method](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#variable-precedence-where-should-i-put-a-variable).

- ### Important variables

CIS Ubuntu 20.04 hardening benchmarks require purging of many services that can be exploited, have known vulnerabilities, result in an exposure of attack surface or should be disabled if not required. As per the benchmark, by default - all of these services will be purged and the value for their variables has been set to `false`. However, if you still require the use of these services for any reason, please change their values to `true` so that when applying the role in a playbook, the role tasks to _purge_ those services can be **skipped**.

Along with the above mentioned explanation for some variables, there are also other variables that define whether a specific service is desired on the system or not (for e.g. SSH daemon), parameters for configuration of various tools (for e.g. auditd) etc. These can also be overridden in a playbook.

```yaml
# Set to `true` if IPv6 is required.
ubuntu_2004_cis_require_ipv6: false

# Set to `true` if Wireless is required.
ubuntu_2004_cis_require_wireless: false

# Set to `true` if system is supposed to act as a router.
ubuntu_2004_cis_require_router: false

# Set to `false` if SSH daemon is not required.
ubuntu_2004_cis_require_ssh_server: true

# Variable to store strong Ciphers for SSH daemon.
ubuntu_2004_cis_require_ssh_ciphers: chacha20-poly1305@openssh.com,aes256-gcm@openssh.com,aes128-gcm@openssh.com,aes256-ctr,aes192-ctr,aes128-ctr

# Variable to store strong MAC Algorithms for SSH daemon.
ubuntu_2004_cis_require_ssh_macs: hmac-sha2-512-etm@openssh.com,hmac-sha2-256-etm@openssh.com,hmac-sha2-512,hmac-sha2-256

# Variable to store strong Key Exchange Algorithms for SSH daemon.
ubuntu_2004_cis_require_ssh_kexalgorithms: curve25519-sha256,curve25519-sha256@libssh.org,diffie-hellman-group14-sha256,diffie-hellman-group16-sha512,diffie-hellman-group18-sha512,ecdh-sha2-nistp521,ecdh-sha2-nistp384,ecdh-sha2-nistp256,diffie-hellman-group-exchange-sha256

# Variable to store Client Alive Interval in seconds for SSH daemon.
ubuntu_2004_cis_require_ssh_clientaliveinterval: '300'

# Variable to store number of Client Alive Count Max for SSH daemon.
ubuntu_2004_cis_require_ssh_clientalivecountmax: '3'

# Variable to store Login Grace Time in seconds for SSH daemon.
ubuntu_2004_cis_require_ssh_logingracetime: '60'

# Variable to store AllowUsers for SSH daemon.
ubuntu_2004_cis_require_ssh_allowusers: ubuntu vagrant

# Variable to store AllowGroups for SSH daemon.
ubuntu_2004_cis_require_ssh_allowgroups: ubuntu vagrant

# Variable to store DenyUsers for SSH daemon.
ubuntu_2004_cis_require_ssh_denyusers: bogus dummy

# Variable to store DenyGroups for SSH daemon.
ubuntu_2004_cis_require_ssh_denygroups: bogus dummy

# Variable to store minimum length and characters class for pam password quality.
ubuntu_2004_cis_require_pam_pwquality:
  - key: 'minlen'
    value: '14'
  - key: 'minclass'
    value: '4'

# Variable to store value of PASS_MAX_DAYS for password expiration.
ubuntu_2004_cis_require_passmaxdays: '365'

# Variable to store value of PASS_MIN_DAYS for password change.
ubuntu_2004_cis_require_passmindays: '1'

# Variable to store value of INACTIVE to set set the default password inactivity period to 30 days.
ubuntu_2004_cis_require_passwarnage: '7'

# Variable to store value of PASS_WARN_AGE for setting password expiration alert in number of days.
ubuntu_2004_cis_require_passinactive: '30'

# Variable to store value of Shell Timeout in seconds.
ubuntu_2004_cis_require_shell_timeout: '900'

# Variable to store value of group name that will be required for the use of su execution.
ubuntu_2004_cis_require_su_group: sugroup

# Variable to store value log file to which the cron job execution propagates for 6.1.1 Audit system file permissions (Manual) task to review.
ubuntu_2004_cis_require_audit_system_file_permissions_logfile: /var/log/6_1_1_cis_audit_system.log

# can be one of 'iptables' or 'nftables' or 'ufw'.
ubuntu_2004_cis_firewall: ufw

# IF 'ufw' is used, setting to 'yes' allows for a UFW git application profile to be configured and allowed.
ubuntu_2004_cis_section3_rule_3_5_1_7_ufw_require_git_profile: yes

# IF 'ufw' is used, setting to 'yes' allows for a UFW HTTP application profile to be configured and allowed.
ubuntu_2004_cis_section3_rule_3_5_1_7_ufw_require_http_profile: yes

# IF 'ufw' is used, setting to 'yes' allows for a UFW HTTPS application profile to be configured and allowed.
ubuntu_2004_cis_section3_rule_3_5_1_7_ufw_require_https_profile: yes

# IF 'ufw' is used, setting to 'true' will deny all incoming connections by default. Operates same as `ufw default deny incoming`. Set to `false` if you don't require this to be applied.
ubuntu_2004_cis_section3_rule_ufw_default_deny_incoming: true

# IF 'ufw' is used, setting to 'true' will deny all outgoing connections by default. Operates same as `ufw default deny outgoing`. Set to `false` if you don't require this to be applied.
ubuntu_2004_cis_section3_rule_ufw_default_deny_outgoing: true

# IF 'ufw' is used, setting to 'true' will deny all routed connections by default. Operates same as `ufw default deny routed`. Set to `false` if you don't require this to be applied.
ubuntu_2004_cis_section3_rule_ufw_default_deny_routed: true

# IF 'nftables' is used, setting to 'true' will deny all input/forward/output connections by default, leaving the system unreachable. Set to `false` if you don't require this to be applied or to lose connectivity.
ubuntu_2004_cis_section3_rule_3_5_2_8: true

# IF 'iptables' is used, setting to 'true' will deny all inbound connections on ipv4 by default, leaving the system unreachable. Set to `false` if you don't require this to be applied or to lose connectivity.
ubuntu_2004_cis_section3_rule_iptables_ipv4_default_deny_input: true

# IF 'iptables' is used, setting to 'true' will deny all outbound connections on ipv4 by default, leaving the system unreachable. Set to `false` if you don't require this to be applied or to lose connectivity.
ubuntu_2004_cis_section3_rule_iptables_ipv4_default_deny_output: true

# IF 'iptables' is used, setting to 'true' will deny all forward connections on ipv4 by default, leaving the system unreachable. Set to `false` if you don't require this to be applied or to lose connectivity.
ubuntu_2004_cis_section3_rule_iptables_ipv4_default_deny_forward: true

# IF 'iptables' is used and ipv6 is enabled, setting to 'true' will deny all inbound connections on ipv4 by default, leaving the system unreachable. Set to `false` if you don't require this to be applied or to lose connectivity.
ubuntu_2004_cis_section3_rule_iptables_ipv6_default_deny_input: true

# IF 'iptables' is used and ipv6 is enabled, setting to 'true' will deny all outbound connections on ipv4 by default, leaving the system unreachable. Set to `false` if you don't require this to be applied or to lose connectivity.
ubuntu_2004_cis_section3_rule_iptables_ipv6_default_deny_output: true

# IF 'iptables' is used and ipv6 is enabled, setting to 'true' will deny all forward connections on ipv4 by default, leaving the system unreachable. Set to `false` if you don't require this to be applied or to lose connectivity.
ubuntu_2004_cis_section3_rule_iptables_ipv6_default_deny_forward: true

# can be one of 'ntp' or 'chrony' or 'systemd-timesyncd'.
ubuntu_2004_cis_time_synchronization: systemd-timesyncd

# Auditd backlog limit to store sufficient records at boot time.
ubuntu_2004_cis_auditd_backloglimit: '8192'

# Log file size for auditd logs. Set as appropriate.
ubuntu_2004_cis_auditd_maxlogfile: '25'

# Action to take when auditd logs have reached max size. Set as appropriate.
ubuntu_2004_cis_auditd_maxlogfileaction: keep_logs

# Action to take for low space left for auditd. Set as appropriate.
ubuntu_2004_cis_auditd_spaceleftaction: email

# Who to mail for auditd. Set as appropriate.
ubuntu_2004_cis_auditd_actionmailacct: root

# Option to halt when audit logs are full. Set as appropriate.
ubuntu_2004_cis_auditd_adminspaceleftaction: halt

# Users allowed to schedule cronjobs.
ubuntu_2004_cis_cron_allow_users:
  - root
  - ubuntu

# Users allowed to use 'at' to schedule jobs.
ubuntu_2004_cis_at_allow_users:
  - root
  - ubuntu

# Set to `true` if X Windows System is required.
ubuntu_2004_cis_require_xwindows_system: false

# Set to `true` if CUPS is required.
ubuntu_2004_cis_require_cups: false

# Set to `true` if DHCP server is required.
ubuntu_2004_cis_require_dhcp_server: false

# Set to `true` if LDAP server is required.
ubuntu_2004_cis_require_ldap_server: false

# Set to `true` if NFS server is required.
ubuntu_2004_cis_require_nfs_server: false

# Set to `true` if DNS server is required.
ubuntu_2004_cis_require_dns_server: false

# Set to `true` if FTP server is required.
ubuntu_2004_cis_require_ftp_server: false

# Set to `true` if HTTP (apache2) server is required.
ubuntu_2004_cis_require_http_server: false

# Set to `true` if IMAP and POP3 servers are required.
ubuntu_2004_cis_require_imap_pop3_server: false

# Set to `true` if Samba daemon is required.
ubuntu_2004_cis_require_samba_server: false

# Set to `true` if Squid server is required.
ubuntu_2004_cis_require_squid_server: false

# Set to `true` if SNMP server is required.
ubuntu_2004_cis_require_snmp_server: false

# To avoid setting postfix to act in local-only mode. Define as `false`  if postfix is required act in local-only mode.
ubuntu_2004_cis_require_mail_server: true

# Set to `true` if RSYNC is required.
ubuntu_2004_cis_require_rsyncd_server: false

# Set to `true` if NIS server is required.
ubuntu_2004_cis_require_nis_server: false

# Set to `true` if NIS client is required.
ubuntu_2004_cis_require_nis_client: false

# Set to `true` if RSH client is required.
ubuntu_2004_cis_require_rsh_client: false

# Set to `true` if TALK client is required.
ubuntu_2004_cis_require_talk_client: false

# Set to `true` if TELNET client is required.
ubuntu_2004_cis_require_telnet_client: false

# Set to `true` if LDAP client is required.
ubuntu_2004_cis_require_ldap_client: false

# Set to `true` if RPCBIND client is required.
ubuntu_2004_cis_require_rpcbind_client: false
```

## 5\. Dependencies

None

## 6\. Example playbooks:

Example playbooks have been provided in [playbook-examples](https://github.com/darkwizard242/cis_ubuntu_2004/blob/master/playbook-examples) folder. It contains playbooks with defaults and customized requirements.

**NOTE:** Considering that some of the CIS controls around networking may break the system and leave the user incapable of performing logging back into the system. I would recommend that you apply or experiment using the [playbook-examples/playbook_with_custom_firewall_changes.yml](https://github.com/darkwizard242/cis_ubuntu_2004/blob/master/playbook-examples/playbook_with_custom_firewall_changes.yml) playbook first. Modify the connection type and hosts in the playbook to match your needs.

### Applying examples:

If you are using any of the provided playbooks in playbook-examples folder, you can choose either one of them and run the following command to apply them:

```shell
ansible-playbook playbook_with_defaults.yml
```

```shell
ansible-playbook playbook_with_custom_firewall_changes.yml
```

```shell
ansible-playbook playbook_with_ipv6.yml
```

```shell
ansible-playbook playbook_with_ufw.yml
```

Assuming you create your own custom playbook named **myplaybook.yml**, you may simply run it with the following command.

```shell
ansible-playbook myplaybook.yml
```

### Applying examples using tags:

All tasks in the role have tags assigned to them based on the CIS Level assignment, rule number and the section number. By default, both Level 1 and Level 2 controls will be applied. Hence, if you wish to run customized applies for levels, rule numbers or sections - you can use the following examples:

Example for only applying Level 1 controls:

```shell
ansible-playbook <playbook-name-here>.yml --tags "level_1"
```

Example for only applying Level 2 controls:

```shell
ansible-playbook <playbook-name-here>.yml --tags "level_2"
```

Example for applying controls of a specific section (i.e. section 4 of CIS Ubuntu 20.04 benchmark as an example):

```shell
ansible-playbook <playbook-name-here>.yml --tags "section4"
```

Example for applying a specific control (i.e. control 6.2.2 of CIS Ubuntu 20.04 benchmark as an example):

```shell
ansible-playbook <playbook-name-here>.yml --tags "rule_6_2_2"
```

## 7\. Local Development and CI/CD:

For local development of the **cis_ubuntu_2004** role, please perform the following:

- Fork the repo.
- Clone it locally.
- Install Vagrant on your machine. Installation instructions available [here](https://www.vagrantup.com/docs/installation) or if you need, you can utilize [darkwizard242.vagrant](https://galaxy.ansible.com/darkwizard242/vagrant) role to install - but please confirm if it supports your OS.
- Install Virtualbox on your machine. Installation instructions available [here](https://www.virtualbox.org/wiki/Downloads) or or if you need, you can utilize [darkwizard242.virtualbox](https://galaxy.ansible.com/darkwizard242/virtualbox) role to install - but please confirm if it supports your OS.
- Install required modules using:

  ```shell
  # To install pip modules globally when running as a non-root user.
  sudo -H python3 -m pip install -U molecule ansible-lint flake8 pytest-testinfra molecule-vagrant
  ```

  OR

  ```shell
  # To install pip modules local to user directory when running as a non-root user.
  python3 -m pip install -U molecule ansible-lint flake8 pytest-testinfra molecule-vagrant
  ```

- Make changes and run `molecule test` or `molecule converge`.

**molecule test** command will run the entire suite of configured molecule test sequence.

**molecule converge** command will only create the vagrant instance and apply all operations defined in the role.

Ofcourse, you can also simply download the code for **cis_ubuntu_2004** role, make changes and run it via ansible-playbook on a testbox if you are not familiar with [molecule](https://molecule.readthedocs.io/en/latest/).

When you create a Pull Request - it will automatically trigger a TravisCI build [here](https://travis-ci.com/github/darkwizard242/cis_ubuntu_2004/pull_requests). The configuration for TravisCI build is present in [.travis.yml](https://github.com/darkwizard242/cis_ubuntu_2004/blob/master/.travis.yml) This will perform various tasks such as:

- Clone code from pull request.
- Perform repository cache update.
- Install pre-requisite packages.
- Install Vagrant and Virtualbox.
- Perform SonarCloud code quality check for the entire repository code base.
- Run molecule test (which will provision a vagrant box, apply the role code and run TestInfra test suite for **cis_ubuntu_2004** role).

## 8\. Contributing:

Contributions are most welcome. Instructions for contributing have been mentioned [here](https://github.com/darkwizard242/cis_ubuntu_2004/blob/master/CONTRIBUTING.md).

## Inspiration

Inspired by the great work done by many of the members of Ansible Community ([Florian Utz](https://github.com/florianutz) and [ansible-lockdown](https://github.com/ansible-lockdown) to name a few among many). Keep rocking :metal:

## License

[MIT](https://github.com/darkwizard242/cis_ubuntu_2004/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).
