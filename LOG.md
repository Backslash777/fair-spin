# Fair Spin Android project log

## 2026-11-04 — version 1.3.0 (version code 4)

- Update checker added, based on the check side of the Arcade Apprentice updater (`files/updater.py` in `C:\0AI\Machine Learning`): at most one check every 6 hours, compares `versionCode` against `https://shorethinggames.co.uk/version.json`, and shows a dismissible banner ("Get the update" opens the STG site; "Not now" remembers that version). Fails quietly offline and never blocks play. `fairSpin.updateUrl` in localStorage can override the URL for testing.
- Reviewed the no-Internet design per the deferred plan: `INTERNET` permission restored solely for the update check and opening website/coffee links. Fully offline play unchanged.
- `shorethinggames.co.uk/version.json` published in the site folder; STG homepage bumped to 1.3.0 with release notes.
- Browser tests passed: newer version shows the banner, "Not now" persists across reloads, unreachable server shows nothing and the app is unaffected.
- Signed APK + AAB built (versionCode 4); all copies refreshed (project, G:, D:, STG site folder). NOT YET emulator-tested: 1.3.0 (1.2.0 was fully emulator-tested; the only native change since is the INTERNET permission).
- AA website code was not otherwise reused; the Flarum forum for STG is still to set up (mirror of forum.arcadeapprentice.co.uk on Hostinger).

## 2026-11-04 — version 1.2.0 (version code 3)

- PayPal donation pages created on the Switch Flavours business account, tracked separately per project: Fair Spin (`hosted_button_id=FKDMQ8UX7RQG6`) and Arcade Apprentice (`hosted_button_id=JWL9ZHY4MSK92`). Both USD, $3/$5/$10 presets plus any amount.
- Added a one-time second-launch screen ("Back for another go?"): continue with the same game or pick a different one, with a Fair Spin "Buy us a coffee — takes less than a minute" PayPal link. First launch still shows game selection. Shown once only (`settings.helloDone`), dismissible with Back/Escape; `settings.launches` counter added.
- Added a permanent "Buy me a coffee" PayPal link in the footer next to the copyright, plus a quiet one-line "Free forever — if it earns its keep, buy us a coffee" link directly under the app header.
- Build note: `tools/build_release.py` only runs Gradle — sync `www/index.html` to `android/app/src/main/assets/public/index.html` first (or run `npx cap sync android`), otherwise the APK silently ships the previous HTML.
- Preserved `fairSpin.v1` and the solver fingerprint `39d57ad76f384071891848c4afff947bd742bb3aebd8ae6f3ce7add47fa88834` (verified inside the signed APK).
- Fixed `android/local.properties` SDK path for this PC (was the old terri/Google Drive path). Capacitor 8 requires JDK 21 for the build; JDK 17 fails with "invalid source release: 21".
- Built and signed release APK + AAB (version code 3). Same upload certificate as 1.1.0 (SHA-256 `889708b6…aa8a`), so updates install cleanly over it. Previous 1.1.0 APK/AAB kept as `fair-spin-1.1.0-backup.*`.
- Browser-tested against a local server: first launch picker, second-launch prompt with correct sport label and link, both buttons, single-show behaviour, and footer link all passed.
- Strategy note: shorethinggames.co.uk will host the Fair Spin download and link to Arcade Apprentice; arcadeapprentice.co.uk links back to Shore Thing Games rather than hosting the app.
- Coffee presentation (added during the same session): centered top line reads "Like it? Buy me a coffee"; a round coffee-cup badge with looping steam animation sits above the New Week button (both open the Fair Spin PayPal page); static steam under reduced motion.
- Emulator-tested the final signed 1.2.0 APK (FairSpinTest AVD, paths fixed for this PC): fresh install first-launch picker, second-launch hello with correct sport label, coffee link opens external Chrome (verified via topResumedActivity), full rounds deal correctly, and update-install over 1.1.0 preserved players, settings and the in-progress round exactly. Screenshots saved in `test-evidence/v1-2-*.png`.
- STILL OPEN: the deferred new-week promo (see below). The website update check is DONE (see 1.3.0 above).
- Websites DEPLOYED 2026-11-04: shorethinggames.co.uk is live on Hostinger (Cloud Professional, PHP/HTML), with the signed 1.3.0 APK, browser app, coffee button and version.json. A Flarum 2.0.2 forum is live at forum.shorethinggames.co.uk (own PHP/HTML site, PHP 8.4, fresh MySQL DB u374669645_stgforum), with General, Ideas and Bugfixes tags. Homepage links to the forum added and uploaded via FTP. Forum DB driver set to mariadb. Local copy of the forum package: `forum-build/` (TypeScript sources and .sh/.bat stripped to pass Hostinger's upload check; exposed-resources protection enabled in .htaccess). Credentials are in the workspace `FORUM-CREDENTIALS-keep-private.txt` (not for upload). Note: Hostinger file-manager cards did not respond to automation; FTP is the reliable route for updates.
- Arcade Apprentice DEPLOYED 2026-11-04: the three edited homepages (EN/JA/ZH) are live on arcadeapprentice.co.uk — both coffee links now use the tracked AA PayPal page, plus a Shore Thing Games promo line and footer link. Uploaded via FTP to the STG site then moved into place server-side (the browser extension dropped mid-task; FTP + same-account PHP copies proved the reliable route). Temporary files removed from the server afterwards.
- Forum now links back to the main site: a sticky welcome discussion (id 1) on forum.shorethinggames.co.uk with links to the site and the browser app, created through the Flarum API with a temporary API key (deleted afterwards). STG homepage already links to the forum.
- Websites built 2026-11-04: new `shorethinggames.co.uk/` folder at the workspace root is a complete upload-ready site — homepage with the signed 1.2.0 APK download, a playable browser version at `fair-spin/`, the Fair Spin coffee button, and an Arcade Apprentice card. Includes `UPLOAD NOTES.txt` for Hostinger. Arcade Apprentice pages in `Fair Spin/site pages (Court Dealer removed)/` updated: both coffee links now use the tracked AA donation page (JWL9ZHY4MSK92), and STG promo/footer links added in English, Japanese and Chinese. Both sites tested locally (desktop + 390px mobile); AA page link changes verified in the DOM.

## 2026-11-02

- Created an isolated Android working copy. Original web source remains untouched.
- Protected solver fingerprint before edits: `39d57ad76f384071891848c4afff947bd742bb3aebd8ae6f3ce7add47fa88834` (content between `SOLVER-START` and `SOLVER-END`).
- Selected Capacitor 8.6.0 with App, Haptics and Splash Screen plugins.
- Package: `uk.co.arcadeapprentice.fairspin`. Version: `1.0.0` (version code 1). Portrait orientation and Android 7.0 / API 24 minimum required.
- Bundled Big Shoulders Display and Atkinson Hyperlegible locally with their licence notices. Removed remote font loads and service-worker registration. Removed the Internet permission.
- Added native launcher and adaptive icons, green shuttlecock splash, light/dark system bars, keep-screen-on, Android back handling and native reduced-motion detection.
- Added Capacitor haptics, wheel anticipation and pointer wobble, arcing player deals, court/picker transitions, button feedback and game-specific celebrations.
- Moved players, history and preferences into a polished native-style settings screen. Credit shown as `© 2026 Jonathan Terrington` only.
- Protected solver fingerprint after edits remains `39d57ad76f384071891848c4afff947bd742bb3aebd8ae6f3ce7add47fa88834`.
- Debug APK built successfully. Emulator checks passed for game selection, full and quick spins, player add/remove, attendance, team/court settings, game switching, keyboard, settings/picker back handling, dark mode and restart persistence.
- Three saved rounds checked: no repeated partnership between consecutive rounds. Android remove-animations setting verified and reduced-motion spin completed immediately.
- Signed release APK and AAB built successfully with a new 4096-bit RSA upload key. Key and passwords stored in the sibling `Fair Spin keystore - KEEP SAFE` folder, outside the project.
- Final APK signature verified. Certificate SHA-256: `889708b6db76ae922133d1bed69a0e2de117162de10db5e1fe658e92da22aa8a`.
- Final APK SHA-256: `2c8b69208a550eb1535ddb80755825f9961253ac1f8d6ba699c5773c601a1a35`. Size: 5,145,320 bytes.
- Final AAB SHA-256: `abb64b754c4ef403d9838ca4268caa47eee7094779fa25b7d6634bfdea254fc4`. Size: 4,963,225 bytes.
- Packaged solver fingerprint verified unchanged inside the signed APK. Five local font files and the original `fairSpin.v1` storage key confirmed. No Internet permission; vibration permission only.
- Exact signed release fresh-installed and visually checked on the emulator. A full round passed with Wi-Fi and mobile data disabled. Reinstalling the signed APK as an update preserved players, settings and history. Native green shuttlecock splash visually confirmed.
- Added `INSTALL - Fair Spin.txt` with phone installation and update instructions.
- Added `transfer-logs/` for moving the work to another PC: start guide, build instructions, completed test results and release file manifest. No signing passwords duplicated into the handover documents.

## Product requirements implemented in Fair Spin 1.1.0, 2026-11-02

Status: IMPLEMENTED AND TESTED, awaiting Jonny's review before closing.

- Removed the header gear icon while keeping the players/settings page available through `Total Games`.
- Added eye-catching `Total Games` and `New Week` buttons to the left and right of the wheel. `Total Games` opens the partnership statistics directly and shows the current sport's round count.
- `New Week` resets only the current sport's current-week statistics and round numbering. Totals and other sports remain intact.
- Added `Times partnered total` with the same visual style as `Times partnered tonight`, including teammate pairs from larger-team games.
- Added per-sport round history, weekly markers, solver history, undo behaviour and statistics. Existing rounds are assigned to the sport active during migration, then saved.
- Added a confirmed total reset. It clears tonight, totals and round history only for the current sport, while players, settings and other sports remain intact.
- Preserved `fairSpin.v1` and the solver fingerprint `39d57ad76f384071891848c4afff947bd742bb3aebd8ae6f3ce7add47fa88834`.
- Release version `1.1.0`, version code 2, built with the existing signing key and verified on the emulator in light and dark modes.
- Final APK SHA-256: `e94f31e5087dd89f47c5b21b177787957b9fb3ee472298a2cb23cffbe0568773`. Size: 5,146,028 bytes.
- Final AAB SHA-256: `63424d92dc33cbda2414e69024b522de8bbc599944ee83df2ccf3a4e6ff17213`. Size: 4,963,925 bytes.
- Update and restart tests preserved players, per-sport rounds and week markers. New Week, independent badminton/tennis totals, reset cancellation and confirmed per-sport reset all passed.
- Hardened the build against Google Drive `desktop.ini` metadata and locked package caches by cleaning before/after Gradle tasks and immediately before `:app:packageRelease`.

## Deferred website update feature, recorded 2026-11-02

Status: OPEN and FIRST PRIORITY for later implementation, ahead of the new-week prompt and promotion. Logged only; no app code or builds changed.

- Fair Spin will be hosted on `arcadeapprentice.co.uk`.
- Create a dedicated Fair Spin webpage on Arcade Apprentice before enabling the app's update check.
- The webpage should present Fair Spin, its current Android version, release notes and the official APK download or update instructions.
- Provide the current release details in a reliable form that the app's update feature can read and compare with the installed version.
- Add an update feature that checks the Arcade Apprentice website for a newer Fair Spin release.
- When an update is available, clearly notify the user and provide a way to open the official download or update page.
- Use the website's actual release details and destination links once Fair Spin has been uploaded.
- The update check must fail quietly when offline and must never prevent normal use of the app.
- Review the current no-Internet-permission design when implementing the online update check. Preserve fully offline play and saved data.

## Deferred new-week prompt, recorded 2026-11-02

Status: OPEN for later implementation. Logged only; no app code or builds changed.

- Remember the date when the app was last opened.
- On the first app launch of a different calendar date, ask the user whether they want to start a new week.
- Do not reset weekly statistics automatically. Start a new week only if the user confirms.
- If the user declines, keep the current week and do not ask again on that same date.
- Underneath the new-week question, add a small Arcade Apprentice promotional section with a short description.
- Include a link telling users they can get more useful apps from Arcade Apprentice, plus a `Buy Me a Coffee` link.
- When implementing, get the current wording, destination links and branding details from `arcadeapprentice.co.uk`. Keep the promotion small and secondary to the new-week question.

## Sync helper scripts, recorded 2026-11-02

- Added `sync-to-external.bat` and `sync-from-external.bat` using Robocopy mirror mode for new, changed and deleted files in either direction.
- Both scripts default to a dry run. Synchronisation and deletions require an explicit `APPLY` argument.
- The external path defaults to `E:\0AI\badminton\Fair Spin` and can be supplied as the first argument. Generated build folders are excluded; the private signing folder is included.
- No synchronisation or file copying was run. Jonny is copying files manually for now.
- Added a separate Windows sync GUI in the workspace `aaa sync` folder. It has source/destination pickers, SHA-256 change scanning, NEW/CHANGED/DELETE results, folder swapping and a guarded Sync button.
- The GUI skips missing root folders, excludes generated build folders, and never syncs automatically. Isolated tests passed for new, changed, deleted, excluded and missing paths.
