import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


AUDIT_SYSTEM_SCRIPT = "/usr/local/bin/6_1_1_cis_audit_system.sh"
ETC_PASSWD = "/etc/passwd"
ETC_GSHADOW_DASH = "/etc/gshadow-"
ETC_SHADOW = "/etc/shadow"
ETC_GROUP = "/etc/group"
ETC_PASSWD_DASH = "/etc/passwd-"
ETC_SHADOW_DASH = "/etc/shadow-"
ETC_GROUP_DASH = "/etc/group-"
ETC_GSHADOW = "/etc/gshadow"


def test_6_1_1_script_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.1
    Tests if /usr/local/bin/6_1_1_cis_audit_system.sh file exists
    """
    assert host.file(AUDIT_SYSTEM_SCRIPT).exists


def test_6_1_1_script_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.1
    Tests if /usr/local/bin/6_1_1_cis_audit_system.sh is a file
    """
    assert host.file(AUDIT_SYSTEM_SCRIPT).is_file


def test_6_1_1_script_mode(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.1
    Tests if /usr/local/bin/6_1_1_cis_audit_system.sh has 0744 mode
    """
    assert host.file(AUDIT_SYSTEM_SCRIPT).mode == 0o744


def test_6_1_1_script_user(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.1
    Tests if /usr/local/bin/6_1_1_cis_audit_system.sh is owned by user root
    """
    assert host.file(AUDIT_SYSTEM_SCRIPT).user == 'root'


def test_6_1_1_script_group(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.1
    Tests if /usr/local/bin/6_1_1_cis_audit_system.sh is owned by group root
    """
    assert host.file(AUDIT_SYSTEM_SCRIPT).group == 'root'


def test_6_1_2_etc_passwd_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.2
    Tests if /etc/passwd file exists
    """
    assert host.file(ETC_PASSWD).exists


def test_6_1_2_etc_passwd_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.2
    Tests if /etc/passwd is a file
    """
    assert host.file(ETC_PASSWD).is_file


def test_6_1_2_etc_passwd_mode(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.2
    Tests if /etc/passwd has 0644 mode
    """
    assert host.file(ETC_PASSWD).mode == 0o644


def test_6_1_2_etc_passwd_user(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.2
    Tests if /etc/passwd is owned by user root
    """
    assert host.file(ETC_PASSWD).user == 'root'


def test_6_1_2_etc_passwd_group(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.2
    Tests if /etc/passwd is owned by group root
    """
    assert host.file(ETC_PASSWD).group == 'root'


def test_6_1_3_etc_group_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.3
    Tests if /etc/passwd- file exists
    """
    assert host.file(ETC_PASSWD_DASH).exists


def test_6_1_3_etc_group_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.3
    Tests if /etc/passwd- is a file
    """
    assert host.file(ETC_PASSWD_DASH).is_file


def test_6_1_3_etc_group_mode(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.3
    Tests if /etc/passwd- has 0644 mode
    """
    assert host.file(ETC_PASSWD_DASH).mode == 0o644


def test_6_1_3_etc_group_user(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.3
    Tests if /etc/passwd- is owned by user root
    """
    assert host.file(ETC_PASSWD_DASH).user == 'root'


def test_6_1_3_etc_group_group(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.3
    Tests if /etc/passwd- is owned by group root
    """
    assert host.file(ETC_PASSWD_DASH).group == 'root'


def test_6_1_4_etc_group_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.4
    Tests if /etc/group file exists
    """
    assert host.file(ETC_GROUP).exists


def test_6_1_4_etc_group_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.4
    Tests if /etc/group is a file
    """
    assert host.file(ETC_GROUP).is_file


def test_6_1_4_etc_group_mode(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.4
    Tests if /etc/group has 0644 mode
    """
    assert host.file(ETC_GROUP).mode == 0o644


def test_6_1_4_etc_group_user(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.4
    Tests if /etc/group is owned by user root
    """
    assert host.file(ETC_GROUP).user == 'root'


def test_6_1_4_etc_group_group(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.4
    Tests if /etc/group is owned by group root
    """
    assert host.file(ETC_GROUP).group == 'root'


def test_6_1_5_etc_group_dash_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.5
    Tests if /etc/group- file exists
    """
    assert host.file(ETC_GROUP_DASH).exists


def test_6_1_5_etc_group_dash_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.5
    Tests if /etc/group- is a file
    """
    assert host.file(ETC_GROUP_DASH).is_file


def test_6_1_5_etc_group_dash_mode(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.5
    Tests if /etc/group- has 0644 mode
    """
    assert host.file(ETC_GROUP_DASH).mode == 0o644


def test_6_1_5_etc_group_dash_user(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.5
    Tests if /etc/group- is owned by user root
    """
    assert host.file(ETC_GROUP_DASH).user == 'root'


def test_6_1_5_etc_group_dash_group(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.5
    Tests if /etc/group- is owned by group root
    """
    assert host.file(ETC_GROUP_DASH).group == 'root'


def test_6_1_6_etc_shadow_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.6
    Tests if /etc/shadow file exists
    """
    assert host.file(ETC_SHADOW).exists


def test_6_1_6_etc_shadow_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.6
    Tests if /etc/shadow is a file
    """
    assert host.file(ETC_SHADOW).is_file


def test_6_1_6_etc_shadow_mode(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.6
    Tests if /etc/shadow has 0640 mode
    """
    assert host.file(ETC_SHADOW).mode == 0o640


def test_6_1_6_etc_shadow_user(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.6
    Tests if /etc/shadow is owned by user root
    """
    assert host.file(ETC_SHADOW).user == 'root'


def test_6_1_6_etc_shadow_group(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.6
    Tests if /etc/shadow is owned by group root
    """
    assert host.file(ETC_SHADOW).group == 'root'


def test_6_1_7_etc_shadow_dash_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.7
    Tests if /etc/shadow- file exists
    """
    assert host.file(ETC_SHADOW_DASH).exists


def test_6_1_7_etc_shadow_dash_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.7
    Tests if /etc/shadow- is a file
    """
    assert host.file(ETC_SHADOW_DASH).is_file


def test_6_1_7_etc_shadow_dash_mode(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.7
    Tests if /etc/shadow- has 0640 mode
    """
    assert host.file(ETC_SHADOW_DASH).mode == 0o640


def test_6_1_7_etc_shadow_dash_user(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.7
    Tests if /etc/shadow- is owned by user root
    """
    assert host.file(ETC_SHADOW_DASH).user == 'root'


def test_6_1_7_etc_shadow_dash_group(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.7
    Tests if /etc/shadow- is owned by group root
    """
    assert host.file(ETC_SHADOW_DASH).group == 'root'


def test_6_1_8_etc_gshadow_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.8
    Tests if /etc/gshadow file exists
    """
    assert host.file(ETC_GSHADOW).exists


def test_6_1_8_etc_gshadow_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.8
    Tests if /etc/gshadow is a file
    """
    assert host.file(ETC_GSHADOW).is_file


def test_6_1_8_etc_gshadow_mode(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.8
    Tests if /etc/gshadow has 0640 mode
    """
    assert host.file(ETC_GSHADOW).mode == 0o640


def test_6_1_8_etc_gshadow_user(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.8
    Tests if /etc/gshadow is owned by user root
    """
    assert host.file(ETC_GSHADOW).user == 'root'


def test_6_1_8_etc_gshadow_group(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.8
    Tests if /etc/gshadow is owned by group root
    """
    assert host.file(ETC_GSHADOW).group == 'root'


def test_6_1_9_etc_gshadow_dash_mode(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.9
    Tests if /etc/gshadow- has 0640 mode
    """
    assert host.file(ETC_GSHADOW_DASH).mode == 0o640


def test_6_1_9_etc_gshadow_dash_user(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.9
    Tests if /etc/gshadow- is owned by user root
    """
    assert host.file(ETC_GSHADOW_DASH).user == 'root'


def test_6_1_9_etc_gshadow_dash_group(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.9
    Tests if /etc/gshadow- is owned by group root
    """
    assert host.file(ETC_GSHADOW_DASH).group == 'root'


def test_6_1_9_etc_gshadow_dash_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.9
    Tests if /etc/gshadow- file exists
    """
    assert host.file(ETC_GSHADOW_DASH).exists


def test_6_1_9_etc_gshadow_dash_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 6.1.9
    Tests if /etc/gshadow- is a file
    """
    assert host.file(ETC_GSHADOW_DASH).is_file
