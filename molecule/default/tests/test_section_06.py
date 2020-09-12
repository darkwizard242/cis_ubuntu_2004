import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


AUDIT_SYSTEM_SCRIPT = "/usr/local/bin/6_1_1_cis_audit_system.sh"


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
