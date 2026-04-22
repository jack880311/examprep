@echo off
REM GCP ACE 題庫練習系統 - 伺服器啟動腳本 (Windows)

REM 改變到腳本所在目錄
cd /d "%~dp0" || exit /b 1

echo 🚀 啟動 GCP ACE 題庫練習系統...
echo 📍 工作目錄: %cd%
echo.

REM 檢查 Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ 錯誤: 找不到 Python
    echo 請先安裝 Python 3.6 或更新版本
    pause
    exit /b 1
)

REM 檢查檔案
set missing=0
if not exist "questions.json" (
    echo ❌ 缺少: questions.json
    set missing=1
)
if not exist "explanations.json" (
    echo ❌ 缺少: explanations.json
    set missing=1
)
if not exist "index.html" (
    echo ❌ 缺少: index.html
    set missing=1
)

if %missing% equ 1 (
    echo.
    echo 請確認這些檔案都在: %cd%
    pause
    exit /b 1
)

echo ✅ 檔案檢查通過
echo   ✓ questions.json
echo   ✓ explanations.json
echo   ✓ index.html
echo.
echo 📌 正在啟動伺服器...
echo 🌐 開啟瀏覽器進入: http://localhost:8000
echo ⏹️  按 Ctrl+C 停止伺服器
echo.

REM 啟動伺服器
python -m http.server 8000
pause
