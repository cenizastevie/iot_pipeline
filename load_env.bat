@echo off
for /f "tokens=1,2 delims==" %%i in ('type .env') do set %%i=%%j
