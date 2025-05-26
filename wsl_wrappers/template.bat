@echo off
setlocal enabledelayedexpansion

:: Initialize the argument string
set ARG_STRING=

:: Loop through each argument
for %%A in (%*) do ( 
    :: Check if argument is a valid file or directory
    if exist "%%~A" (
         :: Convert Windows path to WSL path using wslpath
        for /f "delims=" %%B in ('wsl wslpath "%%~A"') do (
            set ARG_STRING=!ARG_STRING! "%%B"
        )
    ) else (
        set ARG_STRING=!ARG_STRING! %%A
    )
)

:: Run the command in WSL
wsl %WSL_COMMAND% !ARG_STRING!