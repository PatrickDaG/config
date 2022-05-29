#!echo "run with fora"

from fora.operations import local
from fora import host

for f in host.to_install:
    local.script(f"tasks/{f}/deploy.py")

