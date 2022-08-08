## fora

from fora.operations import files, system
from fora import inventory

with defaults(file_mode = "644", dir_mode = "755"):
    system.package(["nginx"])
    nginx_files = [
            "nginx.conf",
            "fastcgi.conf",
            "conf.d/https-reroute.conf",
            "conf.d/ssl.conf",
            "conf.d/nginx-status.conf",
            ]
    for i in nginx_files:
        files.upload(f"../../files/nginx-config/{i}", f"/etc/nginx/{i}")

    files.template("../../files/nginx-config/conf.d/http.conf.j2", "/etc/nginx/conf.d/http.conf")

    nginx_server = []
    for i in nginx_server:
        files.upload(f"../../files/nginx-config/conf.d/server/{i}.conf",
                "/etc/nginx/conf.d/server/{i}.conf")

    files.directory("/etc/nginx/htpasswd/")
    for k,v in inventory.secrets["nginx"]["htpasswd"].items():
        files.upload_content(v,f"/etc/nginx/htpasswd/{k}")

