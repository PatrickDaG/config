## fora inventory file

hosts = [
         dict(name = "patgen"   , url = "root@localhost"   ,groups = ["desktop"]),
         dict(name = "elisabeth"   , url = "root@lel.lol"     ,groups = ["server"]),
         ]

import toml
import subprocess
with open("secrets.toml.gpg", "rb") as _f:
    secrets = toml.loads(subprocess.run(["gpg", "--quiet", "--decrypt"], input = _f.read(), stdout = subprocess.PIPE, check = True).stdout.decode())
