## fora

from fora.operations import files, system, git
from fora import host

if "desktop" in host.groups:
    system.package(["neovim-qt"])

system.package(["neovim"])
for u in host.sys_users:
    with defaults(as_user = u["name"]):
        git.repo("https://github.com/PatrickDaG/nvim-config.git",
                u["home"]+ "/.config/nvim")
