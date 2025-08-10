@echo off
set "ORIGINAL_DIR=%CD%"
cd /d "%~dp0"

set PYTHONPATH=%CD%\src\packages
set PYTHONPYCACHEPREFIX=%CD%\.pycache

python -m clif "%ORIGINAL_DIR%"

cd /d "%ORIGINAL_DIR%"
