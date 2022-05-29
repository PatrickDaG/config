#run with fora

from fora.operations import system, files, git
from fora import host

home_dir = host.connection.home_dir()

system.package(
        name = "Installing zsh dependencies",
        packages = ["ripgrep", "git", "fzf"])

is_arch = False

with defaults(umask = "022",file_mode = "644", dir_mode = "755"):
    files.directory(path = "/usr/share/zsh/repos/")
    git.repo(url = "https://github.com/romkatv/powerlevel10k", path = "/usr/share/zsh/repos/romkatv/powerlevel10k", update = True)
    git.repo(url = "https://github.com/Aloxaf/fzf-tab", path = "/usr/share/zsh/repos/Aloxaf/fzf-tab", update = True)
    git.repo(url = "https://github.com/zdharma-continuum/fast-syntax-highlighting", path = "/usr/share/zsh/repos/zdharma-continuum/fast-syntax-highlighting", update = True)
    git.repo(url = "https://github.com/larkery/zsh-histdb", path = "/usr/share/zsh/repos/larkery/zsh-histdb", update = True)


    files.upload(src = "../../files/home-config/zshrc", dest = "/etc/zsh/zshrc")
    files.upload(src = "../../files/home-config/gitconfig", dest = "/etc/gitconfig")
    files.template(src = "../../files/home-config/zshenv.j2", dest = "/etc/zsh/zshenv")
    files.file(path = "/etc/zsh/zprofile", present=False)
