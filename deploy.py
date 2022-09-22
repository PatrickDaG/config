#!echo "run with fora"

from fora.operations import local
from fora import host

print(sorted(host.to_install))
for f in sorted(host.to_install):
    local.script(f"tasks/{f.split('-',1)[1]}/deploy.py")

