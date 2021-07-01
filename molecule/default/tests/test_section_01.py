import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


CRAMFS_MOD_FILE = "/etc/modprobe.d/1.1.1.1_cramfs.conf"
FREEVXFS_MOD_FILE = "/etc/modprobe.d/1.1.1.2_freevxfs.conf"
JFFS2_MOD_FILE = "/etc/modprobe.d/1.1.1.3_jffs2.conf"
HFS_MOD_FILE = "/etc/modprobe.d/1.1.1.4_hfs.conf"
HFSPLUS_MOD_FILE = "/etc/modprobe.d/1.1.1.5_hfsplus.conf"
SQUASHFS_MOD_FILE = "/etc/modprobe.d/1.1.1.6_squashfs.conf"
UDF_MOD_FILE = "/etc/modprobe.d/1.1.1.7_udf.conf"
TMP_MOUNT_FILE = "/etc/systemd/system/tmp.mount"
TMP_MOUNT_SYSTEMD = "tmp.mount"
DEV_SHM = "/dev/shm"
FSTAB_FILE = "/etc/fstab"
USBSTORAGE_MOD_FILE = "/etc/modprobe.d/1.1.24_usb-storage.conf"
GRUB_D_CUSTOM40_FILE = "/etc/grub.d/40_custom"
BOOT_GRUB = "/boot/grub/grub.cfg"
PROC_CPUINFO = "/proc/cpuinfo"
ETC_MOTD = "/etc/motd"
ETC_ISSUE = "/etc/issue"
ETC_ISSUE_NET = "/etc/issue.net"


def test_1_1_1_1_file_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.1.1
    Tests if /etc/modprobe.d/1.1.1.1_cramfs.conf file exists
    """
    assert host.file(CRAMFS_MOD_FILE).exists


def test_1_1_1_1_file_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.1.1
    Tests if /etc/modprobe.d/1.1.1.1_cramfs.conf is a file
    """
    assert host.file(CRAMFS_MOD_FILE).is_file


def test_1_1_1_1_file_mode(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.1.1
    Tests if /etc/modprobe.d/1.1.1.1_cramfs.conf has 0644 mode
    """
    assert host.file(CRAMFS_MOD_FILE).mode == 0o644


def test_1_1_1_1_file_user(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.1.1
    Tests if /etc/modprobe.d/1.1.1.1_cramfs.conf is owned by user root
    """
    assert host.file(CRAMFS_MOD_FILE).user == 'root'


def test_1_1_1_1_file_group(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.1.1
    Tests if /etc/modprobe.d/1.1.1.1_cramfs.conf is owned by group root
    """
    assert host.file(CRAMFS_MOD_FILE).group == 'root'


def test_1_1_1_2_file_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.1.2
    Tests if /etc/modprobe.d/1.1.1.2_freevxfs.conf file exists
    """
    assert host.file(FREEVXFS_MOD_FILE).exists


def test_1_1_1_2_file_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.1.2
    Tests if /etc/modprobe.d/1.1.1.2_freevxfs.conf is a file
    """
    assert host.file(FREEVXFS_MOD_FILE).is_file


def test_1_1_1_2_file_mode(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.1.2
    Tests if /etc/modprobe.d/1.1.1.2_freevxfs.conf has 0644 mode
    """
    assert host.file(FREEVXFS_MOD_FILE).mode == 0o644


def test_1_1_1_2_file_user(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.1.2
    Tests if /etc/modprobe.d/1.1.1.2_freevxfs.conf is owned by user root
    """
    assert host.file(FREEVXFS_MOD_FILE).user == 'root'


def test_1_1_1_2_file_group(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.1.2
    Tests if /etc/modprobe.d/1.1.1.2_freevxfs.conf is owned by group root
    """
    assert host.file(FREEVXFS_MOD_FILE).group == 'root'


def test_1_1_1_3_file_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.1.3
    Tests if /etc/modprobe.d/1.1.1.3_jffs2.conf file exists
    """
    assert host.file(JFFS2_MOD_FILE).exists


def test_1_1_1_3_file_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.1.3
    Tests if /etc/modprobe.d/1.1.1.3_jffs2.conf is a file
    """
    assert host.file(JFFS2_MOD_FILE).is_file


def test_1_1_1_3_file_mode(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.1.3
    Tests if /etc/modprobe.d/1.1.1.3_jffs2.conf has 0644 mode
    """
    assert host.file(JFFS2_MOD_FILE).mode == 0o644


def test_1_1_1_3_file_user(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.1.3
    Tests if /etc/modprobe.d/1.1.1.3_jffs2.conf is owned by user root
    """
    assert host.file(JFFS2_MOD_FILE).user == 'root'


def test_1_1_1_3_file_group(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.1.3
    Tests if /etc/modprobe.d/1.1.1.3_jffs2.conf is owned by group root
    """
    assert host.file(JFFS2_MOD_FILE).group == 'root'


def test_1_1_1_4_file_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.1.4
    Tests if /etc/modprobe.d/1.1.1.4_hfs.conf file exists
    """
    assert host.file(HFS_MOD_FILE).exists


def test_1_1_1_4_file_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.1.4
    Tests if /etc/modprobe.d/1.1.1.4_hfs.conf is a file
    """
    assert host.file(HFS_MOD_FILE).is_file


def test_1_1_1_4_file_mode(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.1.4
    Tests if /etc/modprobe.d/1.1.1.4_hfs.conf has 0644 mode
    """
    assert host.file(HFS_MOD_FILE).mode == 0o644


def test_1_1_1_4_file_user(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.1.4
    Tests if /etc/modprobe.d/1.1.1.4_hfs.conf is owned by user root
    """
    assert host.file(HFS_MOD_FILE).user == 'root'


def test_1_1_1_4_file_group(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.1.4
    Tests if /etc/modprobe.d/1.1.1.4_hfs.conf is owned by group root
    """
    assert host.file(HFS_MOD_FILE).group == 'root'


def test_1_1_1_5_file_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.1.5
    Tests if /etc/modprobe.d/1.1.1.5_hfsplus.conf file exists
    """
    assert host.file(HFSPLUS_MOD_FILE).exists


def test_1_1_1_5_file_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.1.5
    Tests if /etc/modprobe.d/1.1.1.5_hfsplus.conf is a file
    """
    assert host.file(HFSPLUS_MOD_FILE).is_file


def test_1_1_1_5_file_mode(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.1.5
    Tests if /etc/modprobe.d/1.1.1.5_hfsplus.conf has 0644 mode
    """
    assert host.file(HFSPLUS_MOD_FILE).mode == 0o644


def test_1_1_1_5_file_user(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.1.5
    Tests if /etc/modprobe.d/1.1.1.5_hfsplus.conf is owned by user root
    """
    assert host.file(HFSPLUS_MOD_FILE).user == 'root'


def test_1_1_1_5_file_group(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.1.5
    Tests if /etc/modprobe.d/1.1.1.5_hfsplus.conf is owned by group root
    """
    assert host.file(HFSPLUS_MOD_FILE).group == 'root'


def test_1_1_1_6_file_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.1.6
    Tests if /etc/modprobe.d/1.1.1.6_squashfs.conf file exists
    """
    assert host.file(SQUASHFS_MOD_FILE).exists


def test_1_1_1_6_file_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.1.6
    Tests if /etc/modprobe.d/1.1.1.6_squashfs.conf is a file
    """
    assert host.file(SQUASHFS_MOD_FILE).is_file


def test_1_1_1_6_file_mode(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.1.6
    Tests if /etc/modprobe.d/1.1.1.6_squashfs.conf has 0644 mode
    """
    assert host.file(SQUASHFS_MOD_FILE).mode == 0o644


def test_1_1_1_6_file_user(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.1.6
    Tests if /etc/modprobe.d/1.1.1.6_squashfs.conf is owned by user root
    """
    assert host.file(SQUASHFS_MOD_FILE).user == 'root'


def test_1_1_1_6_file_group(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.1.6
    Tests if /etc/modprobe.d/1.1.1.6_squashfs.conf is owned by group root
    """
    assert host.file(SQUASHFS_MOD_FILE).group == 'root'


def test_1_1_1_7_file_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.1.7
    Tests if /etc/modprobe.d/1.1.1.7_udf.conf file exists
    """
    assert host.file(UDF_MOD_FILE).exists


def test_1_1_1_7_file_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.1.7
    Tests if /etc/modprobe.d/1.1.1.7_udf.conf is a file
    """
    assert host.file(UDF_MOD_FILE).is_file


def test_1_1_1_7_file_mode(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.1.7
    Tests if /etc/modprobe.d/1.1.1.7_udf.conf has 0644 mode
    """
    assert host.file(UDF_MOD_FILE).mode == 0o644


def test_1_1_1_7_file_user(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.1.7
    Tests if /etc/modprobe.d/1.1.1.7_udf.conf is owned by user root
    """
    assert host.file(UDF_MOD_FILE).user == 'root'


def test_1_1_1_7_file_group(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.1.7
    Tests if /etc/modprobe.d/1.1.1.7_udf.conf is owned by group root
    """
    assert host.file(UDF_MOD_FILE).group == 'root'


def test_1_1_2_tmp_mount_file_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.2
    Tests if /etc/systemd/system/tmp.mount file exists
    """
    assert host.file(TMP_MOUNT_FILE).exists


def test_1_1_2_tmp_mount_file_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.2
    Tests if /etc/systemd/system/tmp.mount is a file
    """
    assert host.file(TMP_MOUNT_FILE).is_file


def test_1_1_2_tmp_mount_file_mode(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.2
    Tests if /etc/systemd/system/tmp.mount has 0644 mode
    """
    assert host.file(TMP_MOUNT_FILE).mode == 0o644


def test_1_1_2_tmp_mount_file_user(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.2
    Tests if /etc/systemd/system/tmp.mount is owned by user root
    """
    assert host.file(TMP_MOUNT_FILE).user == 'root'


def test_1_1_2_tmp_mount_file_group(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.2
    Tests if /etc/systemd/system/tmp.mount is owned by group root
    """
    assert host.file(TMP_MOUNT_FILE).group == 'root'


def test_1_1_2_tmp_mount_service_enabled(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.2
    Tests if tmp.mount service is enabled
    """
    assert host.service(TMP_MOUNT_SYSTEMD).is_enabled


def test_1_1_2_tmp_mount_service_running(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.2
    Tests if tmp.mount service is running
    """
    assert host.service(TMP_MOUNT_SYSTEMD).is_running


def test_1_1_3_tmp_mount_nodev(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.3
    Tests if /etc/systemd/system/tmp.mount contains nodev
    """
    assert host.file(TMP_MOUNT_FILE).contains('nodev')


def test_1_1_4_tmp_mount_nosuid(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.4
    Tests if /etc/systemd/system/tmp.mount contains nosuid
    """
    assert host.file(TMP_MOUNT_FILE).contains('nosuid')


def test_1_1_5_tmp_mount_noexec(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.5
    Tests if /etc/systemd/system/tmp.mount contains noexec
    """
    assert host.file(TMP_MOUNT_FILE).contains('noexec')


def test_1_1_6_dev_shm_mount_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.6
    Tests if mountpoint for /dev/shm exists
    """
    assert host.mount_point(DEV_SHM).exists


def test_1_1_7_dev_shm_mount_nodev(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.7
    Tests if mountpoint for /dev/shm in /etc/fstab has nodev option
    """
    assert host.file(FSTAB_FILE).contains('nodev')


def test_1_1_8_dev_shm_mount_nosuid(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.8
    Tests if mountpoint for /dev/shm in /etc/fstab has nosuid option
    """
    assert host.file(FSTAB_FILE).contains('nosuid')


def test_1_1_9_dev_shm_mount_noexec(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.9
    Tests if mountpoint for /dev/shm in /etc/fstab has noexec option
    """
    assert host.file(FSTAB_FILE).contains('noexec')


def test_1_1_24_file_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.24
    Tests if /etc/modprobe.d/1.1.24_usb-storage.conf file exists
    """
    assert host.file(USBSTORAGE_MOD_FILE).exists


def test_1_1_24_file_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.24
    Tests if /etc/modprobe.d/1.1.24_usb-storage.conf is a file
    """
    assert host.file(USBSTORAGE_MOD_FILE).is_file


def test_1_1_24_file_mode(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.24
    Tests if /etc/modprobe.d/1.1.24_usb-storage.conf has 0644 mode
    """
    assert host.file(USBSTORAGE_MOD_FILE).mode == 0o644


def test_1_1_24_file_user(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.24
    Tests if /etc/modprobe.d/1.1.24_usb-storage.conf is owned by user root
    """
    assert host.file(USBSTORAGE_MOD_FILE).user == 'root'


def test_1_1_24_file_group(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.1.24
    Tests if /etc/modprobe.d/1.1.24_usb-storage.conf is owned by group root
    """
    assert host.file(USBSTORAGE_MOD_FILE).group == 'root'


def test_1_3_1_aide_package(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.3.1
    Tests if aide package is installed
    """
    assert host.package('aide').is_installed


def test_1_3_1_aide_common_package(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.3.1
    Tests if aide-common package is installed
    """
    assert host.package('aide-common').is_installed


def test_1_4_2_40custom_file_mode(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.4.2
    Tests if /etc/grub.d/40_custom has 0744 mode
    """
    assert host.file(GRUB_D_CUSTOM40_FILE).mode == 0o755


def test_1_4_2_40custom_file_superusers(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.4.2
    Tests if /etc/grub.d/40_custom contains superusers
    """
    assert host.file(GRUB_D_CUSTOM40_FILE).contains('superusers')


def test_1_4_2_40custom_file_password(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.4.2
    Tests if /etc/grub.d/40_custom contains password
    """
    assert host.file(GRUB_D_CUSTOM40_FILE).contains('password')


def test_1_4_3_grub_file_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.4.3
    Tests if /boot/grub/grub.cfg file exists
    """
    assert host.file(BOOT_GRUB).exists


def test_1_4_3_grub_file_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.4.3
    Tests if /boot/grub/grub.cfg is a file
    """
    assert host.file(BOOT_GRUB).is_file


def test_1_4_3_grub_file_mode(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.4.3
    Tests if /boot/grub/grub.cfg has 0400 mode
    """
    assert host.file(BOOT_GRUB).mode == 0o400


def test_1_4_3_grub_file_user(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.4.3
    Tests if /boot/grub/grub.cfg file is owned by user root
    """
    assert host.file(BOOT_GRUB).user == 'root'


def test_1_4_3_grub_file_group(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.4.3
    Tests if /boot/grub/grub.cfg file is owned by group root
    """
    assert host.file(BOOT_GRUB).group == 'root'


def test_1_5_1_xd_nx_pae(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.5.1
    Tests if /proc/cpuinfo file contains pae
    """
    assert host.file(PROC_CPUINFO).contains('pae')


def test_1_5_1_xd_nx_nx(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.5.1
    Tests if /proc/cpuinfo file contains nx
    """
    assert host.file(PROC_CPUINFO).contains('nx')


def test_1_5_4_systemd_coredump_package(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.5.4
    Tests if systemd-coredump package is installed
    """
    assert host.package('systemd-coredump').is_installed


def test_1_6_1_1_apparmor_package(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.6.1.1
    Tests if apparmor package is installed
    """
    assert host.package('apparmor').is_installed


def test_1_7_1_motd_file_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.7.1
    Tests if /etc/motd file exists
    """
    assert host.file(ETC_MOTD).exists


def test_1_7_1_motd_file_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.7.1
    Tests if /etc/motd file is a file
    """
    assert host.file(ETC_MOTD).is_file


def test_1_7_1_motd_file_mode(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.7.1
    Tests if /etc/motd file has mode 0644
    """
    assert host.file(ETC_MOTD).mode == 0o644


def test_1_7_1_motd_file_user(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.7.1
    Tests if /etc/motd file is owned by user root
    """
    assert host.file(ETC_MOTD).user == 'root'


def test_1_7_1_motd_file_group(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.7.1
    Tests if /etc/motd file is owned by group root
    """
    assert host.file(ETC_MOTD).group == 'root'


def test_1_7_2_issue_file_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.7.2
    Tests if /etc/issue file exists
    """
    assert host.file(ETC_ISSUE).exists


def test_1_7_2_issue_file_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.7.2
    Tests if /etc/issue file is a file
    """
    assert host.file(ETC_ISSUE).is_file


def test_1_7_2_issue_file_mode(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.7.2
    Tests if /etc/issue file has mode 0644
    """
    assert host.file(ETC_ISSUE).mode == 0o644


def test_1_7_2_issue_file_user(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.7.2
    Tests if /etc/issue file is owned by user root
    """
    assert host.file(ETC_ISSUE).user == 'root'


def test_1_7_2_issue_file_group(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.7.2
    Tests if /etc/issue file is owned by group root
    """
    assert host.file(ETC_ISSUE).group == 'root'


def test_1_7_3_issue_net_file_exists(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.7.3
    Tests if /etc/issue.net file exists
    """
    assert host.file(ETC_ISSUE_NET).exists


def test_1_7_3_issue_net_file_isfile(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.7.3
    Tests if /etc/issue.net file is a file
    """
    assert host.file(ETC_ISSUE_NET).is_file


def test_1_7_3_issue_net_file_mode(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.7.3
    Tests if /etc/issue.net file has mode 0644
    """
    assert host.file(ETC_ISSUE_NET).mode == 0o644


def test_1_7_3_issue_net_file_user(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.7.3
    Tests if /etc/issue.net file is owned by user root
    """
    assert host.file(ETC_ISSUE_NET).user == 'root'


def test_1_7_3_issue_net_file_group(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.7.3
    Tests if /etc/issue.net file is owned by group root
    """
    assert host.file(ETC_ISSUE_NET).group == 'root'


def test_1_7_4_motd_file_mode(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.7.4
    Tests if /etc/motd file has mode 0644
    """
    assert host.file(ETC_MOTD).mode == 0o644


def test_1_7_5_issue_file_mode(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.7.5
    Tests if /etc/issue file has mode 0644
    """
    assert host.file(ETC_ISSUE).mode == 0o644


def test_1_7_6_issue_net_file_mode(host):
    """
    CIS Ubuntu 20.04 v1.1.0 - Rule # 1.7.6
    Tests if /etc/issue.net file has mode 0644
    """
    assert host.file(ETC_ISSUE_NET).mode == 0o644
