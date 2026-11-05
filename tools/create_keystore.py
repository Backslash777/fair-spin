from pathlib import Path
import os
import secrets
import string
import subprocess

project = Path(__file__).resolve().parents[1]
folder = project.parent / "Fair Spin keystore - KEEP SAFE"
folder.mkdir(parents=True, exist_ok=True)
keystore = folder / "fair-spin-upload.jks"
credentials = folder / "PASSWORDS - KEEP PRIVATE.txt"
if keystore.exists() or credentials.exists():
    raise SystemExit("Signing files already exist. Refusing to replace them.")

alphabet = string.ascii_letters + string.digits + "!@#$%^*_-+="
store_password = "".join(secrets.choice(alphabet) for _ in range(28))
key_password = "".join(secrets.choice(alphabet) for _ in range(28))
keytool = Path(os.environ["JAVA_HOME"]) / "bin" / "keytool.exe"
subprocess.run([
    str(keytool), "-genkeypair", "-v",
    "-keystore", str(keystore),
    "-storetype", "JKS",
    "-storepass", store_password,
    "-keypass", key_password,
    "-alias", "fair-spin",
    "-keyalg", "RSA", "-keysize", "4096",
    "-validity", "10000",
    "-dname", "CN=Jonathan Terrington, OU=Arcade Apprentice, O=Arcade Apprentice, L=Blackpool, C=GB"
], check=True, stdout=subprocess.DEVNULL)

credentials.write_text(
    "FAIR SPIN SIGNING DETAILS - KEEP PRIVATE\n"
    "=======================================\n\n"
    "Back up this whole folder somewhere safe. Do not share it or commit it to source control.\n"
    "Use the same upload key for future Fair Spin updates.\n\n"
    f"Keystore file: {keystore.name}\n"
    "Key alias: fair-spin\n"
    f"Keystore password: {store_password}\n"
    f"Key password: {key_password}\n",
    encoding="utf-8"
)
print(f"Created new Fair Spin upload key in: {folder}")
