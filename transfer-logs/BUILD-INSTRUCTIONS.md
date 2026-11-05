# Fair Spin build instructions

Date: 2026-11-02 (updated 2026-11-04 for 1.3.0)

## Required tools on the new Windows PC

- Node.js with npm
- Java 21 JDK
- Android SDK with Platform 36, Build Tools and Platform Tools
- Python 3 for the included helper scripts

The release was built with Capacitor 8.6.0, Gradle 8.14.3 and Android Gradle Plugin 8.13.0. The Gradle wrapper downloads its own Gradle version.

## Project layout

Keep these folders next to each other:

```text
Fair Spin/
  fair-spin-android/
  Fair Spin keystore - KEEP SAFE/
    fair-spin-upload.jks
    PASSWORDS - KEEP PRIVATE.txt
```

The signing script reads the password file from that sibling folder. Do not duplicate the passwords into this document or the project.

## Setup

1. Open a terminal in `fair-spin-android`.
2. Run `npm ci`.
3. Set `JAVA_HOME` to the Java 21 JDK.
4. Set `ANDROID_HOME` and `ANDROID_SDK_ROOT` to the new Android SDK.
5. Edit `android/local.properties` so `sdk.dir` points to the new SDK. The old PC's path will not work on another machine.
6. Run `npx cap sync android`.

## Build the signed APK and AAB

Run:

```bat
python tools\build_release.py
```

The script reads the signing details from the private sibling folder, builds both release artifacts and copies them to:

```text
fair-spin.apk
fair-spin.aab
```

It also removes Google Drive `desktop.ini` metadata before building, and the Gradle configuration cleans it before and after each task. Package caches are cleared immediately before `:app:packageRelease`. These steps prevent Drive metadata and locked incremental outputs from breaking resource merging or APK packaging. Do not run a background cleaner during AAPT, because that can delete a file while it is being read.

## Useful commands

Sync web assets without building:

```bat
npx cap sync android
```

Build an unsigned development APK through Gradle:

```bat
cd android
gradlew.bat assembleDebug
```

Regenerate launcher and splash assets only if needed:

```bat
python tools\generate_assets.py
```

Asset generation requires Pillow. It is not needed for an ordinary rebuild.

## Protected behaviour

- Do not alter anything between `// SOLVER-START` and `// SOLVER-END` in `www/index.html`.
- Keep the storage key `fairSpin.v1` unchanged.
- Keep all app assets local. Do not restore remote font links.
- Internet permission was deliberately added in 1.3.0 for the update check and external links only. Do not add analytics, ads or any background network calls; offline play must keep working.
- After editing web assets, run `npx cap sync android` before building. If you skip this, `tools/build_release.py` will silently package the previous HTML — it only runs Gradle. (Alternatively, copy `www/index.html` to `android/app/src/main/assets/public/index.html` manually.)

## Verification before distribution

- Confirm the APK signature with Android's `apksigner`.
- Confirm package, version, minimum SDK and permissions with `aapt`.
- Check that the protected solver fingerprint still matches the value in `START-HERE.md`.
- Install and smoke-test the exact release APK.
- Test an update install with the same signing key and confirm saved data survives.

© 2026 Jonathan Terrington
