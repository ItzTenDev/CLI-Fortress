@echo off
REM ===== Installation script for CLIF =====
setlocal

REM Path to your tool's folder (where clif.bat is)
set TOOL_DIR=%~dp0

REM Path to store the launcher
set LAUNCHER_DIR=%USERPROFILE%\AppData\Local\Microsoft\WindowsApps

REM Create the launcher .bat file in WindowsApps
echo @echo off > "%LAUNCHER_DIR%\clif.bat"
echo "%TOOL_DIR%clif.bat" %%* >> "%LAUNCHER_DIR%\clif.bat"

echo.
echo CLIF has been successfully installed. You can now run "clif" from anywhere.
echo If it doesn't work immediately, log out and back in or restart your terminal.
echo.
pause

endlocal
