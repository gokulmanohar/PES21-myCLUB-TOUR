@echo off

set "newDir=%~dp0internal"
cd %newDir%
"python" "%~dp0\internal\analysis.py"
