## fora

from fora.operations import files, system

with defaults(file_mode = "644", dir_mode = "755"):
    # fuck arch nothing works
    system.package(["zfs_autobackup"])

    files.upload_dir(src = f"../../files/zfs_autobackup/", dest = f"/etc/systemd/system/")

    systemd.daemon_reload()
    systemd.service(service = "zfs-local-snapshot.timer", state = "started", enabled = True)
