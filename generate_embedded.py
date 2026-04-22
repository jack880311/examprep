#!/usr/bin/env python3
"""
生成嵌入式 HTML - 將 JSON 資料直接嵌入到 index.html 中
"""
import json
import sys

def generate_embedded_html():
    # 讀取 JSON 檔案
    with open('questions.json', 'r', encoding='utf-8') as f:
        questions = json.load(f)
    
    with open('explanations.json', 'r', encoding='utf-8') as f:
        explanations = json.load(f)
    
    # 讀取原始 HTML
    with open('index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # 建立嵌入式資料變數
    # 注意：ensure_ascii=False 保留 Unicode 字符，但 backtick (`) 在 <script> 內嵌時
    # 會被瀏覽器 JS 引擎誤判為 template literal 語法，導致後續題目無法載入。
    # 解決方法：將 backtick 替換為 Unicode escape \u0060，功能完全等效。
    questions_json = json.dumps(questions, ensure_ascii=False, indent=2).replace('`', '\\u0060')
    explanations_json = json.dumps(explanations, ensure_ascii=False, indent=2).replace('`', '\\u0060')
    
    # 在 <script> 標籤前插入資料
    data_script = f"""    <script>
        // ===== 嵌入式題庫資料（直接嵌入，無需載入外部檔案）=====
        const embeddedQuestionsData = {questions_json};
        const embeddedExplanationsData = {explanations_json};
        // ===== 資料嵌入結束 =====
    </script>

"""
    
    # 在最後的 <script> 之前插入
    script_tag = "    <script>"
    insert_pos = html_content.rfind(script_tag)
    
    if insert_pos != -1:
        embedded_html = html_content[:insert_pos] + data_script + html_content[insert_pos:]
    else:
        embedded_html = html_content
    
    # 寫入嵌入式 HTML
    with open('index-embedded.html', 'w', encoding='utf-8') as f:
        f.write(embedded_html)
    
    file_size = len(embedded_html.encode('utf-8')) / (1024 * 1024)
    print(f"✅ 成功生成 index-embedded.html (大小: {file_size:.2f} MB)")
    print("🎯 使用方法: 直接雙擊 index-embedded.html 開啟即可，無需伺服器")

if __name__ == '__main__':
    try:
        generate_embedded_html()
    except Exception as e:
        print(f"❌ 錯誤: {e}", file=sys.stderr)
        sys.exit(1)
