#!echo "run with fora"

from fora.operations import local
import os

for f in os.listdir("."):
    if not os.path.isdir(f):
        continue
    local.script(f"{f}/deploy.py")

