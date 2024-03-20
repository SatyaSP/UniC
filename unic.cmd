@echo off

REM Activate Python virtual environment
set "venv_folder=%~dp0unic_venv"
call "%venv_folder%\Scripts\activate"

set "x=%~1"
set "current_path=%cd%"
set "argument=%current_path%\%x%"

REM Run the command
python "%~dp0unic.py" -n "%argument%"