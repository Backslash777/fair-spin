from pathlib import Path
import os
import re
import shutil
import subprocess

project = Path(__file__).resolve().parents[1]

def remove_sync_metadata():
    for desktop_ini in project.rglob("desktop.ini"):
        try:
            desktop_ini.unlink()
        except FileNotFoundError:
            pass

remove_sync_metadata()
key_folder = project.parent / "Fair Spin keystore - KEEP SAFE"
credentials = (key_folder / "PASSWORDS - KEEP PRIVATE.txt").read_text(encoding="utf-8")
def value(label):
    match = re.search(rf"^{re.escape(label)}: (.+)$", credentials, re.MULTILINE)
    if not match:
        raise SystemExit(f"Missing signing detail: {label}")
    return match.group(1).strip()

env = os.environ.copy()
env.update({
    "FAIR_SPIN_STORE_FILE": str(key_folder / "fair-spin-upload.jks"),
    "FAIR_SPIN_STORE_PASSWORD": value("Keystore password"),
    "FAIR_SPIN_KEY_ALIAS": value("Key alias"),
    "FAIR_SPIN_KEY_PASSWORD": value("Key password"),
})
android = project / "android"
for generated in (
    android / "app" / "build" / "intermediates" / "incremental" / "packageRelease",
    android / "app" / "build" / "outputs" / "apk" / "release",
    android / "app" / "build" / "outputs" / "bundle" / "release",
):
    shutil.rmtree(generated, ignore_errors=True)
subprocess.run(["cmd.exe", "/d", "/c", "gradlew.bat --no-daemon assembleRelease bundleRelease"], cwd=android, env=env, check=True)
remove_sync_metadata()
apk = android / "app" / "build" / "outputs" / "apk" / "release" / "app-release.apk"
aab = android / "app" / "build" / "outputs" / "bundle" / "release" / "app-release.aab"
shutil.copy2(apk, project / "fair-spin.apk")
shutil.copy2(aab, project / "fair-spin.aab")
print(f"Signed APK: {project / 'fair-spin.apk'}")
print(f"Signed AAB: {project / 'fair-spin.aab'}")
