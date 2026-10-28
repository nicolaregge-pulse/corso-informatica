@echo off
echo Cancello da C:\lazarus SOLO queste cartelle:
echo   conta, indovina, lazarus 1, lazarus7
echo.
pause
rmdir /s /q "C:\lazarus\conta"
rmdir /s /q "C:\lazarus\indovina"
rmdir /s /q "C:\lazarus\lazarus 1"
rmdir /s /q "C:\lazarus\lazarus7"
echo.
echo Fatto. Cartelle rimaste in C:\lazarus:
dir /b /ad "C:\lazarus"
pause
