# run with fora


from fora.operations import files
from fora import host

with defaults(umask= "022", file_mode = "644", dir_mode = "755"):
    files.directory(path = "/var/www/lel.lol/", present=False)
    files.directory(path = "/var/www/lel.lol/")
    homer_version = "22.08.1"
    host.connection.run(["wget", f"https://github.com/bastienwirtz/homer/releases/download/v{homer_version}/homer.zip", "-O", "/var/www/lel.lol/homer.zip"])
    host.connection.run(["unzip", "/var/www/lel.lol/homer.zip", "-d", "/var/www/lel.lol/"])
    files.upload(src = "../../files/homer-config/config.yml", dest = "/var/www/lel.lol/assets/")
    files.upload_dir(src = "../../files/homer-config/img", dest =
            "/var/www/lel.lol/assets/")
