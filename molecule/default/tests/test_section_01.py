import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_1_1_1_1_file_exists(host):
    host.file('/etc/modprobe.d/1.1.1.1_cramfs.conf').exists


def test_1_1_1_1_file_isfile(host):
    assert host.file('/etc/modprobe.d/1.1.1.1_cramfs.conf').is_file


def test_1_1_1_2_file_exists(host):
    host.file('/etc/modprobe.d/1.1.1.1_freevxfs.conf').exists


def test_1_1_1_2_file_isfile(host):
    assert host.file('/etc/modprobe.d/1.1.1.1_freevxfs.conf').is_file
