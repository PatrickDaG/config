# run with fora
## TODO by hand
# postgres user and database

from fora import host, logger
from fora.operations import files, system, systemd

system.package(["nodejs", "libheif", "libvips"])

immich_jwt_secret = None
"""JWT secret (use long random string)"""
immich_postgres_host = None
immich_postgres_username = None
immich_postgres_password = None
immich_postgres_database = None
immich_mapbox_enable = False
immich_mapbox_key = None
immich_upload_path = "/var/lib/immich/upload"

if host.immich_jwt_secret is None:
    raise ValueError("Secret must be set")

system.user(user="immich", home="/var/lib/immich", shell="/sbin/nologin", system=True)
system.user(user="immich", append_groups=True, groups=["redis"])
files.directory(path="/var/lib/immich", owner="immich", group="immich")

files.template(name="Create immich environment file",
        src="../../files/immich-config/env.j2", dest="/var/lib/immich/env", mode="640",
        owner="root", group="immich")

changed = files.upload(src="../../files/immich-config/build.sh", dest="/var/lib/immich/", owner="immich", group="immich", mode="700").changed
if changed or host.connection.stat("/var/lib/immich/app") is None:
    logger.print_indented("Building immich from source...")
    host.connection.run(["runuser", "-u", "immich", "/var/lib/immich/build.sh"], cwd="/var/lib/immich")

files.link(path="/var/lib/immich/app/server/upload", target=host.immich_upload_path)
files.link(path="/var/lib/immich/app/machine-learning/upload", target=host.immich_upload_path)

any_changed = False
any_changed |= files.template(name="Create immich-server service",
        src="../../files/immich-config/server.service.j2",
        dest="/etc/systemd/system/immich-server.service",
        mode="644").changed
any_changed |= files.template(name="Create immich-microservices service",
        src="../../files/immich-config/microservices.service.j2",
        dest="/etc/systemd/system/immich-microservices.service",
        mode="644").changed
any_changed |= files.template(name="Create immich-machine-learning service",
        src="../../files/immich-config/machine-learning.service.j2",
        dest="/etc/systemd/system/immich-machine-learning.service",
        mode="644").changed
any_changed |= files.upload(name="Create immich-web service",
        src="../../files/immich-config/web.service",
        dest="/etc/systemd/system/immich-web.service",
        mode="644").changed

if any_changed:
    systemd.daemon_reload()

# Enable immich
systemd.service(name="Enable and start immich-server", service="immich-server", state="started", enabled=True)
systemd.service(name="Enable and start immich-microservices", service="immich-microservices", state="started", enabled=True)
systemd.service(name="Enable and start immich-machine-learning", service="immich-machine-learning", state="started", enabled=True)
systemd.service(name="Enable and start immich-web", service="immich-web", state="started", enabled=True)

# Ensure routing to the webhost
files.line("/etc/hosts", "127.0.0.1 immich-web immich-server immich-machine-learning immich-microservices") 
