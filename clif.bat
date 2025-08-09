@echo off
REM ====== CLI-Fortress Windows Launcher ======
setlocal

REM Add src/packages to PYTHONPATH
set PYTHONPATH=%~dp0src\packages

REM Redirect __pycache__ to project-level folder
set PYTHONPYCACHEPREFIX=%~dp0.pycache

REM Run main module
python -m clif

endlocal
