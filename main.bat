@echo off
title Hentai Script Launcher

REM Vérifiez si Python est installé
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python n'est pas installé. Veuillez installer Python avant de lancer le script.
    pause
    exit /b
)

REM Animation de détection des dépendances
echo Detection des dependances en cours...

REM Vérifiez si les paquets Python nécessaires sont installés
pip show requests >nul 2>&1
if %errorlevel% neq 0 (
    echo Installation des paquets Python necessaires...
    pip install -r requirements.txt
    echo.
    echo Paquets installes avec succes!
    echo.
    timeout /nobreak /t 2 >nul
)

REM Lancer le script main.py
python main.py

pause
