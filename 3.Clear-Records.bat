@echo off

set "newDir=%~dp0internal"
cd %newDir%
"python" "%~dp0\internal\clear_record.py"

pause