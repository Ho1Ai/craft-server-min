import hashlib

def countFileHash(filePath):
    sha256 = hashlib.sha256()
    with open(filePath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256.update(byte_block)
    return sha256.hexdigest().lower()

def pkgHexifier(pkg_update_key):
    return hashlib.sha256(pkg_update_key.encode("utf-8")).hexdigest().lower()

# I didn't understand what did this IntelliJ AI write... let it be, gonna reread it when add uploading of packages from a frontend