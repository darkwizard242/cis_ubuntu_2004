import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


MOD_DCCP_FILE = "/etc/modprobe.d/3.4.1_dccp.conf"
MOD_SCTP_FILE = "/etc/modprobe.d/3.4.2_sctp.conf"
MOD_RDS_FILE = "/etc/modprobe.d/3.4.3_rds.conf"
MOD_TIPC_FILE = "/etc/modprobe.d/3.4.4_tipc.conf"


def test_3_4_1_file_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 3.4.1
    Tests if /etc/modprobe.d/3.4.1_dccp.conf file exists
    """
    assert host.file(MOD_DCCP_FILE).exists


def test_3_4_1_file_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 3.4.1
    Tests if /etc/modprobe.d/3.4.1_dccp.conf file is a file
    """
    assert host.file(MOD_DCCP_FILE).is_file


def test_3_4_1_file_mode(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 3.4.1
    Tests if /etc/modprobe.d/3.4.1_dccp.conf file has mode 0644
    """
    assert host.file(MOD_DCCP_FILE).mode == 0o644


def test_3_4_1_file_user(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 3.4.1
    Tests if /etc/modprobe.d/3.4.1_dccp.conf file is owned by user root
    """
    assert host.file(MOD_DCCP_FILE).user == 'root'


def test_3_4_1_file_group(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 3.4.1
    Tests if /etc/modprobe.d/3.4.1_dccp.conf file is owned by group root
    """
    assert host.file(MOD_DCCP_FILE).group == 'root'


def test_3_4_2_file_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 3.4.2
    Tests if /etc/modprobe.d/3.4.2_sctp.conf file exists
    """
    assert host.file(MOD_SCTP_FILE).exists


def test_3_4_2_file_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 3.4.2
    Tests if /etc/modprobe.d/3.4.2_sctp.conf file is a file
    """
    assert host.file(MOD_SCTP_FILE).is_file


def test_3_4_2_file_mode(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 3.4.2
    Tests if /etc/modprobe.d/3.4.2_sctp.conf file has mode 0644
    """
    assert host.file(MOD_SCTP_FILE).mode == 0o644


def test_3_4_2_file_user(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 3.4.2
    Tests if /etc/modprobe.d/3.4.2_sctp.conf file is owned by user root
    """
    assert host.file(MOD_SCTP_FILE).user == 'root'


def test_3_4_2_file_group(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 3.4.2
    Tests if /etc/modprobe.d/3.4.2_sctp.conf file is owned by group root
    """
    assert host.file(MOD_SCTP_FILE).group == 'root'


def test_3_4_3_file_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 3.4.3
    Tests if /etc/modprobe.d/3.4.3_rds.conf file exists
    """
    assert host.file(MOD_RDS_FILE).exists


def test_3_4_3_file_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 3.4.3
    Tests if /etc/modprobe.d/3.4.3_rds.conf file is a file
    """
    assert host.file(MOD_RDS_FILE).is_file


def test_3_4_3_file_mode(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 3.4.3
    Tests if /etc/modprobe.d/3.4.3_rds.conf file has mode 0644
    """
    assert host.file(MOD_RDS_FILE).mode == 0o644


def test_3_4_3_file_user(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 3.4.3
    Tests if /etc/modprobe.d/3.4.3_rds.conf file is owned by user root
    """
    assert host.file(MOD_RDS_FILE).user == 'root'


def test_3_4_3_file_group(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 3.4.3
    Tests if /etc/modprobe.d/3.4.3_rds.conf file is owned by group root
    """
    assert host.file(MOD_RDS_FILE).group == 'root'


def test_3_4_4_file_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 3.4.4
    Tests if /etc/modprobe.d/3.4.4_tipc.conf file exists
    """
    assert host.file(MOD_TIPC_FILE).exists


def test_3_4_4_file_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 3.4.4
    Tests if /etc/modprobe.d/3.4.4_tipc.conf file is a file
    """
    assert host.file(MOD_TIPC_FILE).is_file


def test_3_4_4_file_mode(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 3.4.4
    Tests if /etc/modprobe.d/3.4.4_tipc.conf file has mode 0644
    """
    assert host.file(MOD_TIPC_FILE).mode == 0o644


def test_3_4_4_file_user(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 3.4.4
    Tests if /etc/modprobe.d/3.4.4_tipc.conf file is owned by user root
    """
    assert host.file(MOD_TIPC_FILE).user == 'root'


def test_3_4_4_file_group(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 3.4.4
    Tests if /etc/modprobe.d/3.4.4_tipc.conf file is owned by group root
    """
    assert host.file(MOD_TIPC_FILE).group == 'root'


def test_3_5_1_1_ufw_package(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 3.5.1.1
    Tests if ufw package is installed
    """
    assert host.package('ufw').is_installed
