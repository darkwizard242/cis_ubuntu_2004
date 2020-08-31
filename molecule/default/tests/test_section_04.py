import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_4_1_1_1_auditd_package(host):
    assert host.package('auditd').is_installed


def test_4_1_1_1_audispd_plugins_package(host):
    assert host.package('audispd-plugins').is_installed


def test_4_1_1_2_auditd_service(host):
    assert host.service('auditd').is_enabled
