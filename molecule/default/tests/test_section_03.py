import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


MOD_DCCP_FILE = "/etc/modprobe.d/3.4.1_dccp.conf"


def test_3_4_1_file_exists(host):
    """
    CIS Ubuntu 20.04 v1.0.0 - Rule # 3.4.1
    Tests if /etc/modprobe.d/3.4.1_dccp.conf file exists
    """
    assert host.file(MOD_DCCP_FILE).exists


def test_3_4_1_file_isfile(host):
    """
    CIS Ubuntu 20.04 v1.0.0 - Rule # 3.4.1
    Tests if /etc/modprobe.d/3.4.1_dccp.conf file is a file
    """
    assert host.file(MOD_DCCP_FILE).is_file


def test_3_4_1_file_mode(host):
    """
    CIS Ubuntu 20.04 v1.0.0 - Rule # 3.4.1
    Tests if /etc/modprobe.d/3.4.1_dccp.conf file has mode 0644
    """
    assert host.file(MOD_DCCP_FILE).mode == 0o644


def test_3_4_1_file_user(host):
    """
    CIS Ubuntu 20.04 v1.0.0 - Rule # 3.4.1
    Tests if /etc/modprobe.d/3.4.1_dccp.conf file is owned by user root
    """
    assert host.file(MOD_DCCP_FILE).user == 'root'


def test_3_4_1_file_group(host):
    """
    CIS Ubuntu 20.04 v1.0.0 - Rule # 3.4.1
    Tests if /etc/modprobe.d/3.4.1_dccp.conf file is owned by group root
    """
    assert host.file(MOD_DCCP_FILE).group == 'root'


def test_3_4_2_file_exists(host):
    assert host.file('/etc/modprobe.d/3.4.2_sctp.conf').exists


def test_3_4_2_file_isfile(host):
    assert host.file('/etc/modprobe.d/3.4.2_sctp.conf').is_file


def test_3_4_2_file_mode(host):
    assert host.file('/etc/modprobe.d/3.4.2_sctp.conf').mode == 0o644


def test_3_4_2_file_user(host):
    assert host.file('/etc/modprobe.d/3.4.2_sctp.conf').user == 'root'


def test_3_4_2_file_group(host):
    assert host.file('/etc/modprobe.d/3.4.2_sctp.conf').group == 'root'


def test_3_4_3_file_exists(host):
    assert host.file('/etc/modprobe.d/3.4.3_rds.conf').exists


def test_3_4_3_file_isfile(host):
    assert host.file('/etc/modprobe.d/3.4.3_rds.conf').is_file


def test_3_4_3_file_mode(host):
    assert host.file('/etc/modprobe.d/3.4.3_rds.conf').mode == 0o644


def test_3_4_3_file_user(host):
    assert host.file('/etc/modprobe.d/3.4.3_rds.conf').user == 'root'


def test_3_4_3_file_group(host):
    assert host.file('/etc/modprobe.d/3.4.3_rds.conf').group == 'root'


def test_3_4_4_file_exists(host):
    assert host.file('/etc/modprobe.d/3.4.4_tipc.conf').exists


def test_3_4_4_file_isfile(host):
    assert host.file('/etc/modprobe.d/3.4.4_tipc.conf').is_file


def test_3_4_4_file_mode(host):
    assert host.file('/etc/modprobe.d/3.4.4_tipc.conf').mode == 0o644


def test_3_4_4_file_user(host):
    assert host.file('/etc/modprobe.d/3.4.4_tipc.conf').user == 'root'


def test_3_4_4_file_group(host):
    assert host.file('/etc/modprobe.d/3.4.4_tipc.conf').group == 'root'


def test_3_5_1_1_ufw_package(host):
    assert host.package('ufw').is_installed
