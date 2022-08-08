#!echo "run with fora"

from fora.operations import local
from fora import host

for f in sorted(host.to_install):
    local.script(f"tasks/{f.split('-',1)[1]}/deploy.py")

