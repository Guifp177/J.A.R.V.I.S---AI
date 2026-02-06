@echo off
REM LANCHER JARVIS , Recomendável utilizar ele!
chcp 65001 >nul
title J.A.R.V.I.S. OS v1.0
mode con: cols=85 lines=28

:menu
cls
color 0B
echo.
echo    ┌─────────────────────────────────────────────────────────────────────────┐
echo    │ [!] STATUS: SYSTEM ONLINE...                                            │
echo    ├─────────────────────────────────────────────────────────────────────────┤
echo    │                                                                         │
echo    │   ██╗ █████╗ ██████╗ ██╗   ██╗██╗███████╗                               │
echo    │   ██║██╔══██╗██╔══██╗██║   ██║██║██╔════╝                               │
echo    │   ██║███████║██████╔╝██║   ██║██║███████╗                               │
echo    │   ██║██╔══██║██╔══██║╚██╗ ██╔╝██║╚════██║                               │
echo    │   ██║██║  ██║██║  ██║ ╚████╔╝ ██║███████║                               │
echo    │   ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚═╝╚══════╝  INTELLIGENCE INTERFACE       │
echo    │                                                                         │
echo    ├─────────────────────────────────────────────────────────────────────────┤
echo    │                                                                         │
echo    │  [1] INICIAR PROTOCOLO INTEGRAL  (Com Voz)                              │
echo    │  [2] INICIAR MODO FURTIVO        (Silencioso + UI)                      │
echo    │  [3] AUTO-DESTRUIÇÂO T-1         (Sair do Sistema)                      │
echo    │  V1.0 Beta by guifp :0                                                  │
echo    └─────────────────────────────────────────────────────────────────────────┘
echo.
set "opcao="
set /p "opcao= >> SELECIONE UMA DIRETRIZ/PROTOCOLO: "

if "%opcao%"=="1" goto modo_voz
if "%opcao%"=="2" goto modo_silencioso
if "%opcao%"=="3" exit
goto menu

:modo_voz
cls
color 0A
echo.
echo  ===========================================================================
echo  [SYSTEM] ACIONANDO PROTOCOLO DE VOZ...
echo  ===========================================================================
python main.py --voice
pause
goto menu

:modo_silencioso
cls
color 0E
echo.
echo  ===========================================================================
echo  [SYSTEM] ACIONANDO MODO FURTIVO...
echo  ===========================================================================
python main.py
pause
goto menu
