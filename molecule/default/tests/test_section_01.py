import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_1_1_1_1_file_exists(host):
    assert host.file('/etc/modprobe.d/1.1.1.1_cramfs.conf').exists


def test_1_1_1_1_file_isfile(host):
    assert host.file('/etc/modprobe.d/1.1.1.1_cramfs.conf').is_file


def test_1_1_1_1_file_mode(host):
    assert host.file('/etc/modprobe.d/1.1.1.1_cramfs.conf').mode == 0o644


def test_1_1_1_1_file_user(host):
    assert host.file('/etc/modprobe.d/1.1.1.1_cramfs.conf').user == 'root'


def test_1_1_1_1_file_group(host):
    assert host.file('/etc/modprobe.d/1.1.1.1_cramfs.conf').group == 'root'


def test_1_1_1_2_file_exists(host):
    assert host.file('/etc/modprobe.d/1.1.1.2_freevxfs.conf').exists


def test_1_1_1_2_file_isfile(host):
    assert host.file('/etc/modprobe.d/1.1.1.2_freevxfs.conf').is_file


def test_1_1_1_2_file_mode(host):
    assert host.file('/etc/modprobe.d/1.1.1.2_freevxfs.conf').mode == 0o644


def test_1_1_1_2_file_user(host):
    assert host.file('/etc/modprobe.d/1.1.1.2_freevxfs.conf').user == 'root'


def test_1_1_1_2_file_group(host):
    assert host.file('/etc/modprobe.d/1.1.1.2_freevxfs.conf').group == 'root'


def test_1_1_1_3_file_exists(host):
    assert host.file('/etc/modprobe.d/1.1.1.3_jffs2.con').exists


def test_1_1_1_3_file_isfile(host):
    assert host.file('/etc/modprobe.d/1.1.1.3_jffs2.con').is_file


def test_1_1_1_3_file_mode(host):
    assert host.file('/etc/modprobe.d/1.1.1.3_jffs2.con').mode == 0o644


def test_1_1_1_3_file_user(host):
    assert host.file('/etc/modprobe.d/1.1.1.3_jffs2.con').user == 'root'


def test_1_1_1_3_file_group(host):
    assert host.file('/etc/modprobe.d/1.1.1.3_jffs2.con').group == 'root'


def test_1_1_1_4_file_exists(host):
    assert host.file('/etc/modprobe.d/1.1.1.4_hfs.conf').exists


def test_1_1_1_4_file_isfile(host):
    assert host.file('/etc/modprobe.d/1.1.1.4_hfs.conf').is_file


def test_1_1_1_4_file_mode(host):
    assert host.file('/etc/modprobe.d/1.1.1.4_hfs.conf').mode == 0o644


def test_1_1_1_4_file_user(host):
    assert host.file('/etc/modprobe.d/1.1.1.4_hfs.conf').user == 'root'


def test_1_1_1_4_file_group(host):
    assert host.file('/etc/modprobe.d/1.1.1.4_hfs.conf').group == 'root'
