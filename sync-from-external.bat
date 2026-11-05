@echo off
setlocal
rem Mirror Fair Spin from an external drive back to Google Drive.
rem Preview: sync-from-external.bat "E:\0AI\badminton\Fair Spin"
rem Apply:   sync-from-external.bat "E:\0AI\badminton\Fair Spin" APPLY
rem Includes new, changed and deleted files. The private signing folder is included.

set "SOURCE=%~1"
if not defined SOURCE set "SOURCE=E:\0AI\badminton\Fair Spin"
set "DEST=C:\Users\terri\My Drive\Personal\0AI\badminton\Fair Spin"
set "MODE=/L"
if /I "%~2"=="APPLY" set "MODE="

echo Source:      %SOURCE%
echo Destination: %DEST%
if defined MODE echo Mode: DRY RUN ONLY. Review the list, then rerun with APPLY.
if not defined MODE echo Mode: APPLY mirror, including destination deletions.

robocopy "%SOURCE%" "%DEST%" /MIR /COPY:DAT /DCOPY:T /XJ /R:1 /W:1 /MT:8 /NP /NDL /XD .git node_modules .gradle build .android-build /XF desktop.ini %MODE%
if errorlevel 8 (
  echo Sync failed. Check the drive letter, paths and file permissions.
  exit /b 1
)
if defined MODE echo Dry run complete. No files were copied or deleted.
if not defined MODE echo Sync complete, including any required deletions.
exit /b 0
