@echo off
cd ../venv/Scripts
call activate.bat
cd ../../docs
call make clean
call make html
pause