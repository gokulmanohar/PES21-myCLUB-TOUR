@echo off

set "newDir=%~dp0internal"
cd %newDir%
"%~dp0\pythonenv\Scripts\python.exe" "%~dp0\internal\analysis.py"

pause