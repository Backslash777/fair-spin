# Fair Spin chat and project handover

Date: 2026-11-04

## Current state

Fair Spin 1.3.0 is complete as a signed Android release. The original web app was not edited. All work is in the copied `fair-spin-android` project.

- App name: Fair Spin
- Package: `uk.co.arcadeapprentice.fairspin`
- Version: `1.3.0`
- Version code: `4`
- Minimum Android: 7.0 / API 24
- Target and compile SDK: 36
- Orientation: portrait
- Capacitor: 8.6.0
- App plugin: 8.1.2
- Haptics and Splash Screen plugins: 8.0.2
- Fully offline play. Internet permission was added in 1.3.0 solely for the update check and for opening website/coffee links; the check fails quietly offline
- Saved-data key remains `fairSpin.v1`
- Wheel-side `Total Games` and `New Week` controls
- Separate current-week and all-time partnership tables
- Independent round history, weekly markers, totals and resets for each sport
- 1.2.0 added: a one-time second-launch "Back for another go?" screen (same game or different), a centered "Like it? Buy me a coffee" top line, an animated coffee-cup badge above New Week, and a footer coffee link
- 1.3.0 added: a quiet update checker that compares against https://shorethinggames.co.uk/version.json (at most one check every 6 hours) and shows a dismissible update banner

The protected pairing solver is unchanged. Its SHA-256 fingerprint between `SOLVER-START` and `SOLVER-END` is:

`39d57ad76f384071891848c4afff947bd742bb3aebd8ae6f3ce7add47fa88834`

## Live on the internet (2026-11-04)

- https://shorethinggames.co.uk — the official Fair Spin home: APK download, browser play, coffee button, `version.json`
- https://forum.shorethinggames.co.uk — Flarum forum with General, Ideas and Bugfixes sections
- https://arcadeapprentice.co.uk — coffee links now use the tracked Arcade Apprentice PayPal page; it links out to Shore Thing Games rather than hosting the app
- Donations are tracked separately per project through two PayPal donation pages (Fair Spin and Arcade Apprentice), USD $3/$5/$10 plus any amount

## Files to copy to the other PC

Copy these two items together, preserving their sibling-folder relationship:

1. `fair-spin-android` (the whole project folder)
2. `Fair Spin keystore - KEEP SAFE` (the private signing folder)

The original `fair-spin` web folder is not needed to build the Android app. The Android project's `www` folder contains the working web copy.

Do not copy the old machine's `.android-tools` folder and expect it to work unchanged. Install the build tools on the new PC and update the paths described in `BUILD-INSTRUCTIONS.md`.

## Handover documents

- `BUILD-INSTRUCTIONS.md`: setup, signing and rebuilding
- `TEST-RESULTS.md`: checks actually completed on the emulator and in the browser
- `FILE-MANIFEST.txt`: release locations, sizes and checksums
- `../LOG.md`: chronological project log
- `../INSTALL - Fair Spin.txt`: phone installation instructions

## Important warnings

- Keep the signing folder private. Do not commit it or send it publicly.
- Do not put the keystore passwords into source files or build logs.
- For future releases, increment `versionCode` and update `versionName` in `android/app/build.gradle`.
- Install updates over the existing app. Do not uninstall first, because that removes saved players, settings and history.
- The exact signed 1.2.0 release was tested on an emulator. 1.3.0 has been browser-tested only so far. Physical haptic feel has not been checked on a phone.

## Likely next task

Emulator-test 1.3.0 with the live update checker, then the Google Play listing and release checklist. The signed AAB is ready for a later Play upload.

© 2026 Jonathan Terrington
