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
    assert host.package('auditd').is_installed


def test_4_1_1_1_audispd_plugins_package(host):
    assert host.package('audispd-plugins').is_installed


def test_4_1_1_2_auditd_service(host):
    assert host.service('auditd').is_enabled


def test_4_1_3_audit_rule_file_exists(host):
    """
    CIS Ubuntu 20.04 v1.0.0 - Rule # 4.1.3
    Tests if /etc/audit/rules.d/4.1.3.rules file exists
    """
    host.file(RULE_FILE_413).exists


def test_4_1_3_audit_rule_file_isfile(host):
    """
    CIS Ubuntu 20.04 v1.0.0 - Rule # 4.1.3
    Tests if /etc/audit/rules.d/4.1.3.rules file is a file
    """
    host.file(RULE_FILE_413).is_file


def test_4_1_4_audit_rule_file_exists(host):
    """
    CIS Ubuntu 20.04 v1.0.0 - Rule # 4.1.4
    Tests if /etc/audit/rules.d/4.1.4.rules file exists
    """
    host.file(RULE_FILE_414).exists


def test_4_1_4_audit_rule_file_isfile(host):
    """
    CIS Ubuntu 20.04 v1.0.0 - Rule # 4.1.4
    Tests if /etc/audit/rules.d/4.1.4.rules file is a file
    """
    host.file(RULE_FILE_414).is_file


def test_4_1_5_audit_rule_file_exists(host):
    """
    CIS Ubuntu 20.04 v1.0.0 - Rule # 4.1.5
    Tests if /etc/audit/rules.d/4.1.5.rules file exists
    """
    host.file(RULE_FILE_415).exists


def test_4_1_5_audit_rule_file_isfile(host):
    """
    CIS Ubuntu 20.04 v1.0.0 - Rule # 4.1.5
    Tests if /etc/audit/rules.d/4.1.5.rules file is a file
    """
    host.file(RULE_FILE_415).is_file


def test_4_1_6_audit_rule_file_exists(host):
    """
    CIS Ubuntu 20.04 v1.0.0 - Rule # 4.1.6
    Tests if /etc/audit/rules.d/4.1.6.rules file exists
    """
    host.file(RULE_FILE_416).exists


def test_4_1_6_audit_rule_file_isfile(host):
    """
    CIS Ubuntu 20.04 v1.0.0 - Rule # 4.1.6
    Tests if /etc/audit/rules.d/4.1.6.rules file is a file
    """
    host.file(RULE_FILE_416).is_file


def test_4_1_7_audit_rule_file_exists(host):
    """
    CIS Ubuntu 20.04 v1.0.0 - Rule # 4.1.7
    Tests if /etc/audit/rules.d/4.1.7.rules file exists
    """
    host.file(RULE_FILE_417).exists


def test_4_1_7_audit_rule_file_isfile(host):
    """
    CIS Ubuntu 20.04 v1.0.0 - Rule # 4.1.7
    Tests if /etc/audit/rules.d/4.1.7.rules file is a file
    """
    host.file(RULE_FILE_417).is_file


def test_4_1_8_audit_rule_file_exists(host):
    """
    CIS Ubuntu 20.04 v1.0.0 - Rule # 4.1.8
    Tests if /etc/audit/rules.d/4.1.8.rules file exists
    """
    host.file(RULE_FILE_418).exists


def test_4_1_8_audit_rule_file_isfile(host):
    """
    CIS Ubuntu 20.04 v1.0.0 - Rule # 4.1.8
    Tests if /etc/audit/rules.d/4.1.8.rules file is a file
    """
    host.file(RULE_FILE_418).is_file


def test_4_1_9_audit_rule_file_exists(host):
    host.file('/etc/audit/rules.d/4.1.9.rules').exists


def test_4_1_9_audit_rule_file_isfile(host):
    host.file('/etc/audit/rules.d/4.1.9.rules').is_file


def test_4_1_10_audit_rule_file_exists(host):
    host.file('/etc/audit/rules.d/4.1.10.rules').exists


def test_4_1_10_audit_rule_file_isfile(host):
    host.file('/etc/audit/rules.d/4.1.10.rules').is_file


def test_4_1_11_audit_rule_file_exists(host):
    host.file('/etc/audit/rules.d/4.1.11.rules').exists


def test_4_1_11_audit_rule_file_isfile(host):
    host.file('/etc/audit/rules.d/4.1.11.rules').is_file


def test_4_1_12_audit_rule_file_exists(host):
    host.file('/etc/audit/rules.d/4.1.12.rules').exists


def test_4_1_12_audit_rule_file_isfile(host):
    host.file('/etc/audit/rules.d/4.1.12.rules').is_file


def test_4_1_13_audit_rule_file_exists(host):
    host.file('/etc/audit/rules.d/4.1.13.rules').exists


def test_4_1_13_audit_rule_file_isfile(host):
    host.file('/etc/audit/rules.d/4.1.13.rules').is_file


def test_4_1_14_audit_rule_file_exists(host):
    host.file('/etc/audit/rules.d/4.1.14.rules').exists


def test_4_1_14_audit_rule_file_isfile(host):
    host.file('/etc/audit/rules.d/4.1.14.rules').is_file


def test_4_1_15_audit_rule_file_exists(host):
    host.file('/etc/audit/rules.d/4.1.15.rules').exists


def test_4_1_15_audit_rule_file_isfile(host):
    host.file('/etc/audit/rules.d/4.1.15.rules').is_file


def test_4_1_16_audit_rule_file_exists(host):
    host.file('/etc/audit/rules.d/4.1.16.rules').exists


def test_4_1_16_audit_rule_file_isfile(host):
    host.file('/etc/audit/rules.d/4.1.16.rules').is_file


def test_4_1_17_audit_rule_file_exists(host):
    host.file('/etc/audit/rules.d/99_4.1.17.rules').exists


def test_4_1_17_audit_rule_file_isfile(host):
    host.file('/etc/audit/rules.d/99_4.1.17.rules').is_file


def test_4_2_1_1_rsyslog_package(host):
    assert host.package('rsyslog').is_installed


def test_4_2_1_2_rsyslog_service(host):
    assert host.service('rsyslog').is_enabled
