@echo off

call %~dp0\venv\Scripts\activate

cd %~dp0

set TOKEN=5321649166:AAHf7xRuocKPVUOSPTYRGMyVGc4SRUOnRJk

python bot_telegram.py

pause
