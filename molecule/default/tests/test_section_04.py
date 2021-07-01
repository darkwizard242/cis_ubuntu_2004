import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


RULE_FILE_413 = "/etc/audit/rules.d/4.1.3.rules"
RULE_FILE_414 = "/etc/audit/rules.d/4.1.4.rules"
RULE_FILE_415 = "/etc/audit/rules.d/4.1.5.rules"
RULE_FILE_416 = "/etc/audit/rules.d/4.1.6.rules"
RULE_FILE_417 = "/etc/audit/rules.d/4.1.7.rules"
RULE_FILE_418 = "/etc/audit/rules.d/4.1.8.rules"
RULE_FILE_419 = "/etc/audit/rules.d/4.1.9.rules"
RULE_FILE_4110 = "/etc/audit/rules.d/4.1.10.rules"
RULE_FILE_4111 = "/etc/audit/rules.d/4.1.11.rules"
RULE_FILE_4112 = "/etc/audit/rules.d/4.1.12.rules"
RULE_FILE_4113 = "/etc/audit/rules.d/4.1.13.rules"
RULE_FILE_4114 = "/etc/audit/rules.d/4.1.14.rules"
RULE_FILE_4115 = "/etc/audit/rules.d/4.1.15.rules"
RULE_FILE_4116 = "/etc/audit/rules.d/4.1.16.rules"
RULE_FILE_4117 = "/etc/audit/rules.d/4.1.17.rules"


def test_4_1_1_1_auditd_package(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 4.1.1.1
    Tests if auditd package is installed
    """
    assert host.package('auditd').is_installed


def test_4_1_1_1_audispd_plugins_package(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 4.1.1.1
    Tests if audispd-plugins package is installed
    """
    assert host.package('audispd-plugins').is_installed


def test_4_1_1_2_auditd_service(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 4.1.1.2
    Tests if auditd service is installed
    """
    assert host.service('auditd').is_enabled


def test_4_1_3_audit_rule_file_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 4.1.3
    Tests if /etc/audit/rules.d/4.1.3.rules file exists
    """
    host.file(RULE_FILE_413).exists


def test_4_1_3_audit_rule_file_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 4.1.3
    Tests if /etc/audit/rules.d/4.1.3.rules file is a file
    """
    host.file(RULE_FILE_413).is_file


def test_4_1_4_audit_rule_file_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 4.1.4
    Tests if /etc/audit/rules.d/4.1.4.rules file exists
    """
    host.file(RULE_FILE_414).exists


def test_4_1_4_audit_rule_file_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 4.1.4
    Tests if /etc/audit/rules.d/4.1.4.rules file is a file
    """
    host.file(RULE_FILE_414).is_file


def test_4_1_5_audit_rule_file_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 4.1.5
    Tests if /etc/audit/rules.d/4.1.5.rules file exists
    """
    host.file(RULE_FILE_415).exists


def test_4_1_5_audit_rule_file_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 4.1.5
    Tests if /etc/audit/rules.d/4.1.5.rules file is a file
    """
    host.file(RULE_FILE_415).is_file


def test_4_1_6_audit_rule_file_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 4.1.6
    Tests if /etc/audit/rules.d/4.1.6.rules file exists
    """
    host.file(RULE_FILE_416).exists


def test_4_1_6_audit_rule_file_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 4.1.6
    Tests if /etc/audit/rules.d/4.1.6.rules file is a file
    """
    host.file(RULE_FILE_416).is_file


def test_4_1_7_audit_rule_file_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 4.1.7
    Tests if /etc/audit/rules.d/4.1.7.rules file exists
    """
    host.file(RULE_FILE_417).exists


def test_4_1_7_audit_rule_file_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 4.1.7
    Tests if /etc/audit/rules.d/4.1.7.rules file is a file
    """
    host.file(RULE_FILE_417).is_file


def test_4_1_8_audit_rule_file_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 4.1.8
    Tests if /etc/audit/rules.d/4.1.8.rules file exists
    """
    host.file(RULE_FILE_418).exists


def test_4_1_8_audit_rule_file_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 4.1.8
    Tests if /etc/audit/rules.d/4.1.8.rules file is a file
    """
    host.file(RULE_FILE_418).is_file


def test_4_1_9_audit_rule_file_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 4.1.9
    Tests if /etc/audit/rules.d/4.1.9.rules file exists
    """
    host.file(RULE_FILE_419).exists


def test_4_1_9_audit_rule_file_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 4.1.9
    Tests if /etc/audit/rules.d/4.1.9.rules file is a file
    """
    host.file(RULE_FILE_419).is_file


def test_4_1_10_audit_rule_file_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 4.1.10
    Tests if /etc/audit/rules.d/4.1.10.rules file exists
    """
    host.file(RULE_FILE_4110).exists


def test_4_1_10_audit_rule_file_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 4.1.10
    Tests if /etc/audit/rules.d/4.1.10.rules file is a file
    """
    host.file(RULE_FILE_4110).is_file


def test_4_1_11_audit_rule_file_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 4.1.11
    Tests if /etc/audit/rules.d/4.1.11.rules file exists
    """
    host.file(RULE_FILE_4111).exists


def test_4_1_11_audit_rule_file_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 4.1.11
    Tests if /etc/audit/rules.d/4.1.11.rules file is a file
    """
    host.file(RULE_FILE_4111).is_file


def test_4_1_12_audit_rule_file_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 4.1.12
    Tests if /etc/audit/rules.d/4.1.12.rules file exists
    """
    host.file(RULE_FILE_4112).exists


def test_4_1_12_audit_rule_file_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 4.1.12
    Tests if /etc/audit/rules.d/4.1.12.rules file is a file
    """
    host.file(RULE_FILE_4112).is_file


def test_4_1_13_audit_rule_file_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 4.1.13
    Tests if /etc/audit/rules.d/4.1.13.rules file exists
    """
    host.file(RULE_FILE_4113).exists


def test_4_1_13_audit_rule_file_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 4.1.13
    Tests if /etc/audit/rules.d/4.1.13.rules file is a file
    """
    host.file(RULE_FILE_4113).is_file


def test_4_1_14_audit_rule_file_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 4.1.14
    Tests if /etc/audit/rules.d/4.1.14.rules file exists
    """
    host.file(RULE_FILE_4114).exists


def test_4_1_14_audit_rule_file_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 4.1.14
    Tests if /etc/audit/rules.d/4.1.14.rules file is a file
    """
    host.file(RULE_FILE_4114).is_file


def test_4_1_15_audit_rule_file_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 4.1.15
    Tests if /etc/audit/rules.d/4.1.15.rules file exists
    """
    host.file(RULE_FILE_4115).exists


def test_4_1_15_audit_rule_file_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 4.1.15
    Tests if /etc/audit/rules.d/4.1.15.rules file is a file
    """
    host.file(RULE_FILE_4115).is_file


def test_4_1_16_audit_rule_file_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 4.1.16
    Tests if /etc/audit/rules.d/4.1.16.rules file exists
    """
    host.file(RULE_FILE_4116).exists


def test_4_1_16_audit_rule_file_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 4.1.16
    Tests if /etc/audit/rules.d/4.1.16.rules file is a file
    """
    host.file(RULE_FILE_4116).is_file


def test_4_1_17_audit_rule_file_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 4.1.17
    Tests if /etc/audit/rules.d/4.1.17.rules file exists
    """
    host.file(RULE_FILE_4117).exists


def test_4_1_17_audit_rule_file_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 4.1.17
    Tests if /etc/audit/rules.d/4.1.17.rules file is a file
    """
    host.file(RULE_FILE_4117).is_file


def test_4_2_1_1_rsyslog_package(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 4.2.1.1
    Tests if rsyslog package is installed
    """
    assert host.package('rsyslog').is_installed


def test_4_2_1_2_rsyslog_service(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 4.2.1.2
    Tests if rsyslog service is enabled
    """
    assert host.service('rsyslog').is_enabled
