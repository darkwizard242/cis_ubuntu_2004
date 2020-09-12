import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


AUDIT_SYSTEM_SCRIPT = "/usr/local/bin/6_1_1_cis_audit_system.sh"
ETC_PASSWD = "/etc/passwd"
ETC_GSHADOW_DASH = "/etc/gshadow-"


def test_6_1_1_script_exists(host):
    """
    CIS Ubuntu 20.04 v1.0.0 - Rule # 6.1.1
    Tests if /usr/local/bin/6_1_1_cis_audit_system.sh file exists
    """
    assert host.file(AUDIT_SYSTEM_SCRIPT).exists


def test_6_1_1_script_isfile(host):
    """
    CIS Ubuntu 20.04 v1.0.0 - Rule # 6.1.1
    Tests if /usr/local/bin/6_1_1_cis_audit_system.sh is a file
    """
    assert host.file(AUDIT_SYSTEM_SCRIPT).is_file


def test_6_1_1_script_mode(host):
    """
    CIS Ubuntu 20.04 v1.0.0 - Rule # 6.1.1
    Tests if /usr/local/bin/6_1_1_cis_audit_system.sh has 0744 mode
    """
    assert host.file(AUDIT_SYSTEM_SCRIPT).mode == 0o744


def test_6_1_1_script_user(host):
    """
    CIS Ubuntu 20.04 v1.0.0 - Rule # 6.1.1
    Tests if /usr/local/bin/6_1_1_cis_audit_system.sh is owned by user root
    """
    assert host.file(AUDIT_SYSTEM_SCRIPT).user == 'root'


def test_6_1_1_script_group(host):
    """
    CIS Ubuntu 20.04 v1.0.0 - Rule # 6.1.1
    Tests if /usr/local/bin/6_1_1_cis_audit_system.sh is owned by group root
    """
    assert host.file(AUDIT_SYSTEM_SCRIPT).group == 'root'


def test_6_1_2_etc_passwd_exists(host):
    """
    CIS Ubuntu 20.04 v1.0.0 - Rule # 6.1.2
    Tests if /etc/passwd file exists
    """
    assert host.file(ETC_PASSWD).exists


def test_6_1_2_etc_passwd_isfile(host):
    """
    CIS Ubuntu 20.04 v1.0.0 - Rule # 6.1.2
    Tests if /etc/passwd is a file
    """
    assert host.file(ETC_PASSWD).is_file


def test_6_1_2_etc_passwd_mode(host):
    """
    CIS Ubuntu 20.04 v1.0.0 - Rule # 6.1.2
    Tests if /etc/passwd has 0644 mode
    """
    assert host.file(ETC_PASSWD).mode == 0o644


def test_6_1_2_etc_passwd_user(host):
    """
    CIS Ubuntu 20.04 v1.0.0 - Rule # 6.1.2
    Tests if /etc/passwd is owned by user root
    """
    assert host.file(ETC_PASSWD).user == 'root'


def test_6_1_2_etc_passwd_group(host):
    """
    CIS Ubuntu 20.04 v1.0.0 - Rule # 6.1.2
    Tests if /etc/passwd is owned by group root
    """
    assert host.file(ETC_PASSWD).group == 'root'


def test_6_1_3_etc_gshadow_dash_exists(host):
    """
    CIS Ubuntu 20.04 v1.0.0 - Rule # 6.1.3
    Tests if /etc/gshadow- file exists
    """
    assert host.file(ETC_GSHADOW_DASH).exists


def test_6_1_3_etc_gshadow_dash_isfile(host):
    """
    CIS Ubuntu 20.04 v1.0.0 - Rule # 6.1.3
    Tests if /etc/gshadow- is a file
    """
    assert host.file(ETC_GSHADOW_DASH).is_file


def test_6_1_3_etc_gshadow_dash_mode(host):
    """
    CIS Ubuntu 20.04 v1.0.0 - Rule # 6.1.3
    Tests if /etc/gshadow- has 0640 mode
    """
    assert host.file(ETC_GSHADOW_DASH).mode == 0o640


def test_6_1_3_etc_gshadow_dash_user(host):
    """
    CIS Ubuntu 20.04 v1.0.0 - Rule # 6.1.3
    Tests if /etc/gshadow- is owned by user root
    """
    assert host.file(ETC_GSHADOW_DASH).user == 'root'


def test_6_1_3_etc_gshadow_dash_group(host):
    """
    CIS Ubuntu 20.04 v1.0.0 - Rule # 6.1.3
    Tests if /etc/gshadow- is owned by group root
    """
    assert host.file(ETC_GSHADOW_DASH).group == 'root'
