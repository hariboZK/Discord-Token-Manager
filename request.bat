@echo off
title Discord Token Manager -- Made by Haribo --
echo [*] Gerekli kutuphaneler yukleniyor...
pip install flask requests
echo.
echo [*] Web sunucusu baslatiliyor...
python app.py
pause