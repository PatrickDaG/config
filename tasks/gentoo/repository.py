## fora

from fora.operations import files

with defaults(umask = "022", file_mode = "644", dir_mode = "755"):
    files.upload("../../files/gentoo-config/patrickdag.conf",
            dest = "/etc/portage/repos.conf/patrickdag.conf")
    files.upload("../../files/gentoo-config/waffle—builds.conf",
            dest = "/etc/portage/repos.conf/waffle-builds.conf")
