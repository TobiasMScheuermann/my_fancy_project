@echo off
cd ../venv/Scripts
call activate.bat
cd ../../docs
call make html
pause