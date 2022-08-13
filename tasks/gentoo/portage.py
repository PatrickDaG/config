## fora

from fora.operations import files

with defaults(umask = "022", file_mode = "644", dir_mode = "755"):
    files.upload("../../files/gentoo-config/world",
            dest = "/var/lib/portage/world")
    files.upload("../../files/gentoo-config/package.license",
            dest = "/etc/portage/package.license")
    files.upload("../../files/gentoo-config/make.conf",
            dest = "/etc/portage/make.conf")
    files.upload_dir(src = "../../files/gentoo-config/env",
            dest = "/etc/portage/")
    files.upload_dir(src = "../../files/gentoo-config/package.env",
            dest = "/etc/portage/")
    files.upload_dir(src = "../../files/gentoo-config/package.use",
            dest = "/etc/portage/")
    files.upload_dir(src = "../../files/gentoo-config/repos.conf",
            dest = "/etc/portage/")

