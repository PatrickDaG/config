## fora

from fora.operations import files, system, systemd
from fora import host

with defaults(file_mode = "644", dir_mode = "755"):
    # fuck arch nothing works
    is_arch = False
    if not host.is_arch:
        system.package(["zfs_autobackup"])

    files.upload(src = f"../../files/zfs_autobackup-config/zfs-local-snapshot.timer", dest = f"/etc/systemd/system/")
    files.upload(src = f"../../files/zfs_autobackup-config/zfs-local-snapshot.service", dest = f"/etc/systemd/system/")

    systemd.daemon_reload()
    systemd.service(service = "zfs-local-snapshot.timer", state = "started", enabled = True)
