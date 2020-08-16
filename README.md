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
  - name: darkwizard242.cis-ubuntu-20.04
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
