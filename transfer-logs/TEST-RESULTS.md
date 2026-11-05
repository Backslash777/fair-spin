# Fair Spin test results

Date: 2026-11-04 (updated with 1.2.0 and 1.3.0 results)

## Fair Spin 1.2.0 emulator checks passed (2026-11-04)

Test device: FairSpinTest Android emulator, API 36, 1080 × 2400. Exact signed 1.2.0 APK.

- Fresh install showed the game picker on first launch; badminton selected correctly.
- Second launch showed the one-time "Back for another go?" screen with the correct "Same game — Badminton" label and the coffee line. It dismissed correctly and did not reappear.
- Tapping a coffee link opened the external Chrome browser, verified through the foreground activity. It did not hijack the app.
- Three full rounds dealt proper doubles on both courts, with Total Games counting correctly.
- Update install over 1.1.0 preserved players, settings and the in-progress round exactly (same teams, same round shown on relaunch).
- New in 1.2.0: centered "Like it? Buy me a coffee" top line, animated coffee-cup badge above New Week, footer coffee link.
- Screenshots saved as `test-evidence/v1-2-*.png`.
- Protected solver fingerprint unchanged inside the signed APK.

## Fair Spin 1.3.0 update-checker checks passed (2026-11-04, browser)

- A newer version in `version.json` showed the update banner with the correct version text.
- "Not now" dismissed the banner and remembered that version across reloads.
- An unreachable `version.json` produced no banner and no errors; the app carried on normally.
- The live https://shorethinggames.co.uk/version.json is in place and returns the current release.
- NOT YET emulator-tested: 1.3.0. The only native change since the fully-tested 1.2.0 is the added Internet permission.

## Remaining device-specific gap

Testing used an emulator, not a physical phone. Native haptic calls are implemented, but their physical feel has not been checked on a phone.

© 2026 Jonathan Terrington

---

# Earlier results: 1.1.0 (2026-11-02)

Test device: FairSpinTest Android emulator, API 36, 1080 × 2400.

## Interaction and visual checks passed

- Initial game picker rendered correctly in light and dark modes.
- Selected badminton and switched to tennis.
- Completed full one-by-one spins and quicker all-at-once spins.
- Wheel, courts and Spin button fit on the main phone screen without scrolling in the tested layout.
- Added a player using the full software keyboard, then removed that player with confirmation.
- Marked Michelle as not present.
- Changed players a side and number of courts.
- Players/settings screen opened and rendered correctly.
- Android back closed settings without exiting.
- Android back closed the game picker without exiting.
- Light and dark app colours and system bars matched correctly.
- Native green shuttlecock splash was visually confirmed.

## Persistence checks passed

- Players, settings and rounds were stored under `fairSpin.v1`.
- A force-close and reopen preserved sport, courts, team size, dealing preference, rounds, active players, attendance and removed-player state.
- The exact signed release APK was reinstalled as an update and retained players, settings and history.

## Pairing checks passed

Three consecutive saved rounds were inspected. There were no repeated partnerships from round 1 to round 2, or from round 2 to round 3.

The solver fingerprint inside the signed APK matched the original source exactly.

## Offline checks passed

- Wi-Fi and mobile data were disabled.
- The exact signed release completed a full round successfully.
- The final APK declares vibration permission but no Internet permission.
- Five font files are bundled locally.
- No service-worker registration remains in the packaged page.

## Reduced-motion check passed

Android animation scales were set to zero. The app detected this setting and a spin completed without the normal animation delay. Normal animation settings were restored afterwards.

## Release verification passed

- Signed APK built and installed successfully.
- Signed AAB built successfully.
- APK signature verified.
- Handover APK checksum matched the exact installed and tested APK.
- Package `uk.co.arcadeapprentice.fairspin`, version `1.1.0`, version code 2, minimum SDK 24, target SDK 36 and portrait orientation confirmed from the packaged manifest.

## Fair Spin 1.1.0 feature checks passed

- Version `1.1.0`, version code 2, installed over 1.0.0 with existing players and rounds preserved.
- Wheel-side `Total Games` and `New Week` buttons rendered correctly in light and dark modes. The header gear icon is removed.
- `Total Games` opened the partnership view with `Times partnered tonight` and `Times partnered total` tables.
- `New Week` reset the current sport's weekly view to Round 1 while preserving its total and other sports.
- A new-week spin incremented the total correctly.
- Badminton and tennis maintained independent totals: two badminton rounds and one tennis round during testing.
- Reset cancellation preserved all rounds. Confirmed reset removed badminton data while preserving the tennis round, players and settings.
- Final release restart preserved players, per-sport rounds and week markers.
- Protected solver fingerprint remained unchanged.

© 2026 Jonathan Terrington
