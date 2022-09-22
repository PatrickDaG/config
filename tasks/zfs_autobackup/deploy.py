## fora

from fora.operations import files, system, systemd
from fora import host

with defaults(file_mode = "644", dir_mode = "755"):
    # fuck arch nothing works
    is_arch = False
    if not host.is_arch:
        system.package(["zfs_autobackup"])

    zfs_autobackup_mode = "10,1h2d,1d1m,1w6m,1m200y"
    files.upload(src = f"../../files/zfs_autobackup-config/zfs-local-snapshot.timer", dest = f"/etc/systemd/system/")
    files.template(src = f"../../files/zfs_autobackup-config/zfs-local-snapshot.service.j2", dest = f"/etc/systemd/system/zfs-local-snapshot.service")

    systemd.daemon_reload()
    systemd.service(service = "zfs-local-snapshot.timer", state = "started", enabled = True)
