#!/bin/bash
# GCP ACE 題庫練習系統 - 伺服器啟動腳本

# 強制改變到腳本所在目錄（修復 Finder 雙擊時的工作目錄問題）
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR" || exit 1

echo "🚀 啟動 GCP ACE 題庫練習系統..."
echo "📍 工作目錄: $(pwd)"
echo ""

# 檢查 Python
if ! command -v python3 &> /dev/null; then
    echo "❌ 錯誤: 找不到 Python 3"
    echo "請先安裝 Python 3.6 或更新版本"
    sleep 3
    exit 1
fi

# 檢查檔案
if [ ! -f "questions.json" ] || [ ! -f "explanations.json" ] || [ ! -f "index.html" ]; then
    echo "❌ 錯誤: 缺少必要檔案"
    echo "需要的檔案："
    [ ! -f "questions.json" ] && echo "  ❌ questions.json"
    [ ! -f "explanations.json" ] && echo "  ❌ explanations.json"
    [ ! -f "index.html" ] && echo "  ❌ index.html"
    echo ""
    echo "請確認這些檔案都在: $SCRIPT_DIR"
    sleep 3
    exit 1
fi

echo "✅ 檔案檢查通過"
echo "  ✓ questions.json"
echo "  ✓ explanations.json"
echo "  ✓ index.html"
echo ""
echo "📌 正在啟動伺服器..."
echo "🌐 開啟瀏覽器進入: http://localhost:8000"
echo "⏹️  按 Ctrl+C 停止伺服器"
echo ""

# 啟動伺服器
python3 -m http.server 8000
