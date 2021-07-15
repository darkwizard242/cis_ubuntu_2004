import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


CRON_SERVICE = "cron"
ETC_CRONTAB = "/etc/crontab"
CRON_HOURLY = "/etc/cron.hourly"
CRON_DAILY = "/etc/cron.daily"
CRON_WEEKLY = "/etc/cron.weekly"
CRON_MONTHLY = "/etc/cron.monthly"
CRON_D = "/etc/cron.d"
CRON_ALLOW = "/etc/cron.allow"
AT_ALLOW = "/etc/at.allow"
SSHD_CONFIG = "/etc/ssh/sshd_config"
PAM_PWQUALITY = "libpam-pwquality"


def test_5_1_1_cron_service_is_running(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.1.1
    Tests if cron service is running
    """
    assert host.service(CRON_SERVICE).is_running


def test_5_1_1_cron_service_is_enabled(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.1.1
    Tests if cron service is enabled
    """
    assert host.service(CRON_SERVICE).is_enabled


def test_5_1_2_crontab_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.1.2
    Tests if /etc/crontab file exists
    """
    assert host.file(ETC_CRONTAB).exists


def test_5_1_2_crontab_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.1.2
    Tests if /etc/crontab is a file
    """
    assert host.file(ETC_CRONTAB).is_file


def test_5_1_2_crontab_mode(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.1.2
    Tests if /etc/crontab has 0600 mode
    """
    assert host.file(ETC_CRONTAB).mode == 0o600


def test_5_1_2_crontab_user(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.1.2
    Tests if /etc/crontab is owned by user root
    """
    assert host.file(ETC_CRONTAB).user == 'root'


def test_5_1_2_crontab_group(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.1.2
    Tests if /etc/crontab is owned by group root
    """
    assert host.file(ETC_CRONTAB).group == 'root'


def test_5_1_3_cron_hourly_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.1.3
    Tests if /etc/cron.hourly directory exists
    """
    assert host.file(CRON_HOURLY).exists


def test_5_1_3_cron_hourly_is_directory(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.1.3
    Tests if /etc/cron.hourly is a directory
    """
    assert host.file(CRON_HOURLY).is_directory


def test_5_1_3_cron_hourly_mode(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.1.3
    Tests if /etc/cron.hourly has 0700 mode
    """
    assert host.file(CRON_HOURLY).mode == 0o700


def test_5_1_3_cron_hourly_user(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.1.3
    Tests if /etc/cron.hourly is owned by user root
    """
    assert host.file(CRON_HOURLY).user == 'root'


def test_5_1_3_cron_hourly_group(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.1.3
    Tests if /etc/cron.hourly is owned by group root
    """
    assert host.file(CRON_HOURLY).group == 'root'


def test_5_1_4_cron_daily_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.1.4
    Tests if /etc/cron.daily directory exists
    """
    assert host.file(CRON_DAILY).exists


def test_5_1_4_cron_daily_is_directory(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.1.4
    Tests if /etc/cron.daily is a directory
    """
    assert host.file(CRON_DAILY).is_directory


def test_5_1_4_cron_daily_mode(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.1.4
    Tests if /etc/cron.daily has 0700 mode
    """
    assert host.file(CRON_DAILY).mode == 0o700


def test_5_1_4_cron_daily_user(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.1.4
    Tests if /etc/cron.daily is owned by user root
    """
    assert host.file(CRON_DAILY).user == 'root'


def test_5_1_4_cron_daily_group(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.1.4
    Tests if /etc/cron.daily is owned by group root
    """
    assert host.file(CRON_DAILY).group == 'root'


def test_5_1_5_cron_weekly_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.1.5
    Tests if /etc/cron.weekly directory exists
    """
    assert host.file(CRON_WEEKLY).exists


def test_5_1_5_cron_weekly_is_directory(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.1.5
    Tests if /etc/cron.weekly is a directory
    """
    assert host.file(CRON_WEEKLY).is_directory


def test_5_1_5_cron_weekly_mode(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.1.5
    Tests if /etc/cron.weekly has 0700 mode
    """
    assert host.file(CRON_WEEKLY).mode == 0o700


def test_5_1_5_cron_weekly_user(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.1.5
    Tests if /etc/cron.weekly is owned by user root
    """
    assert host.file(CRON_WEEKLY).user == 'root'


def test_5_1_5_cron_weekly_group(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.1.5
    Tests if /etc/cron.weekly is owned by group root
    """
    assert host.file(CRON_WEEKLY).group == 'root'


def test_5_1_6_cron_monthly_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.1.6
    Tests if /etc/cron.montly directory exists
    """
    assert host.file(CRON_MONTHLY).exists


def test_5_1_6_cron_monthly_is_directory(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.1.6
    Tests if /etc/cron.montly is a directory
    """
    assert host.file(CRON_MONTHLY).is_directory


def test_5_1_6_cron_monthly_mode(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.1.6
    Tests if /etc/cron.montly has 0700 mode
    """
    assert host.file(CRON_MONTHLY).mode == 0o700


def test_5_1_6_cron_monthly_user(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.1.6
    Tests if /etc/cron.montly is owned by user root
    """
    assert host.file(CRON_MONTHLY).user == 'root'


def test_5_1_6_cron_monthly_group(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.1.6
    Tests if /etc/cron.montly is owned by group root
    """
    assert host.file(CRON_MONTHLY).group == 'root'


def test_5_1_7_cron_d_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.1.7
    Tests if /etc/cron.d directory exists
    """
    assert host.file(CRON_D).exists


def test_5_1_7_cron_d_is_directory(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.1.7
    Tests if /etc/cron.d is a directory
    """
    assert host.file(CRON_D).is_directory


def test_5_1_7_cron_d_mode(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.1.7
    Tests if /etc/cron.d has 0700 mode
    """
    assert host.file(CRON_D).mode == 0o700


def test_5_1_7_cron_d_user(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.1.7
    Tests if /etc/cron.d is owned by user root
    """
    assert host.file(CRON_D).user == 'root'


def test_5_1_7_cron_d_group(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.1.7
    Tests if /etc/cron.d is owned by group root
    """
    assert host.file(CRON_D).group == 'root'


def test_5_1_8_cron_allow_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.1.8
    Tests if /etc/cron.allow file exists
    """
    assert host.file(CRON_ALLOW).exists


def test_5_1_8_cron_allow_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.1.8
    Tests if /etc/cron.allow is a file
    """
    assert host.file(CRON_ALLOW).is_file


def test_5_1_8_cron_allow_mode(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.1.8
    Tests if /etc/cron.allow has 0640 mode
    """
    assert host.file(CRON_ALLOW).mode == 0o640


def test_5_1_8_cron_allow_user(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.1.8
    Tests if /etc/cron.allow is owned by user root
    """
    assert host.file(CRON_ALLOW).user == 'root'


def test_5_1_8_cron_allow_group(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.1.8
    Tests if /etc/cron.allow is owned by group root
    """
    assert host.file(CRON_ALLOW).group == 'root'


def test_5_1_9_at_allow_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.1.9
    Tests if /etc/at.allow file exists
    """
    assert host.file(AT_ALLOW).exists


def test_5_1_9_at_allow_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.1.9
    Tests if /etc/at.allow is a file
    """
    assert host.file(AT_ALLOW).is_file


def test_5_1_9_at_allow_mode(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.1.9
    Tests if /etc/at.allow has 0640 mode
    """
    assert host.file(AT_ALLOW).mode == 0o640


def test_5_1_9_at_allow_user(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.1.9
    Tests if /etc/at.allow is owned by user root
    """
    assert host.file(AT_ALLOW).user == 'root'


def test_5_1_9_at_allow_group(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.1.9
    Tests if /etc/at.allow is owned by group root
    """
    assert host.file(AT_ALLOW).group == 'root'


def test_5_2_1_sudo_package(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.2.1
    Tests if sudo package is installed
    """
    assert host.package('sudo').is_installed


def test_5_3_1_sshd_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.3.1
    Tests if /etc/ssh/sshd_config file exists
    """
    assert host.file(SSHD_CONFIG).exists


def test_5_3_1_sshd_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.3.1
    Tests if /etc/ssh/sshd_config is a file
    """
    assert host.file(SSHD_CONFIG).is_file


def test_5_3_1_sshd_mode(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.3.1
    Tests if /etc/ssh/sshd_config has 0600 mode
    """
    assert host.file(SSHD_CONFIG).mode == 0o600


def test_5_3_1_sshd_user(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.3.1
    Tests if /etc/ssh/sshd_config is owned by user root
    """
    assert host.file(SSHD_CONFIG).user == 'root'


def test_5_3_1_sshd_group(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.3.1
    Tests if /etc/ssh/sshd_config is owned by group root
    """
    assert host.file(SSHD_CONFIG).group == 'root'


def test_5_4_1_libpam_pwquality_installed(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 5.4.1
    Tests if libpam-pwquality is installed
    """
    assert host.package(PAM_PWQUALITY).is_installed
