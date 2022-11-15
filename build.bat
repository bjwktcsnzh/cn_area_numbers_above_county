@echo off
cls


set task1name=trim years_kv_src
echo [+]start %task1name%
python years_trim.py
if "%errorlevel%" == "0" (echo [+]%task1name% success) else (echo [!]%task1name% failed) && goto :end

set task2name=build nums
echo [+]start %task2name%
python years_to_nums.py
if "%errorlevel%" == "0" (echo [+]%task2name% success) else (echo [!]%task2name% failed) && goto :end

set task3name=build cities
echo [+]start %task3name%
python years_to_cities.py
if "%errorlevel%" == "0" (echo [+]%task3name% success) else (echo [!]%task3name% failed) && goto :end

:end