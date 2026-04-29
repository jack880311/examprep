#!/usr/bin/env python3
import json
import re

# 讀取原始 HTML
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 關鍵優化 1: 在 </head> 前添加 iPhone 優化 CSS
mobile_css = '''
        /* ===== iPhone 優化 (螢幕寬度 < 600px) ===== */
        @media (max-width: 600px) {
            body {
                padding: 12px;
            }
            
            .container {
                border-radius: 12px;
            }
            
            .header {
                padding: 20px 16px;
            }
            
            .header h1 {
                font-size: 1.3em;
                margin-bottom: 12px;
            }
            
            .stats {
                gap: 12px;
                font-size: 13px;
            }
            
            .stat-item {
                gap: 4px;
            }
            
            /* 控制列優化：垂直堆疊 */
            .controls {
                flex-direction: column;
                padding: 12px;
                gap: 10px;
            }
            
            .search-box,
            .filter-select {
                width: 100% !important;
                min-width: unset !important;
                padding: 12px 14px !important;
                font-size: 16px !important;
                border-radius: 8px !important;
                min-height: 44px;
                box-sizing: border-box;
            }
            
            .search-box {
                flex: 1;
            }
            
            /* 按鈕優化 */
            .btn {
                padding: 12px 16px !important;
                font-size: 15px !important;
                border-radius: 8px !important;
                min-height: 44px;
                display: flex;
                align-items: center;
                justify-content: center;
                white-space: nowrap;
                flex: 1;
                min-width: 100%;
            }
            
            /* 跳頁和按鈕組合優化 */
            .controls span[style*="display:inline-flex"] {
                width: 100%;
                gap: 8px;
            }
            
            #jumpIdxInput {
                flex: 1;
                min-height: 44px;
                font-size: 16px !important;
            }
            
            /* 題目卡片優化 */
            .question-list {
                padding: 16px;
            }
            
            .question-card {
                padding: 16px;
                margin-bottom: 16px;
                border-radius: 10px;
            }
            
            .question-header {
                flex-wrap: wrap;
                gap: 8px;
            }
            
            .question-text {
                font-size: 1em;
                line-height: 1.6;
                margin-bottom: 16px;
            }
            
            /* 選項優化 */
            .option {
                padding: 14px 12px;
                margin-bottom: 10px;
                min-height: 44px;
                font-size: 15px;
                display: flex;
                align-items: center;
                gap: 12px;
            }
            
            .option-label {
                min-width: 28px;
                font-size: 15px;
            }
            
            /* 詳解區域優化 */
            details {
                padding: 12px;
                margin-top: 12px;
            }
            
            summary {
                font-size: 15px;
                padding: 10px;
                min-height: 44px;
                display: flex;
                align-items: center;
            }
            
            .explanation {
                font-size: 14px;
                line-height: 1.7;
            }
            
            .note-textarea {
                padding: 12px;
                min-height: 80px;
                font-size: 16px;
                border-radius: 8px;
            }
            
            /* 分頁優化 */
            .pagination {
                padding: 16px 12px;
                gap: 8px;
            }
            
            .page-btn {
                padding: 10px 14px;
                font-size: 14px;
                min-height: 40px;
                flex: 1;
                min-width: auto;
            }
            
            /* 隱藏 AI 考試情境行在超小螢幕 */
            .controls:nth-of-type(2) {
                display: none;
            }
            
            /* 答案徽章優化 */
            .answer-badge {
                font-size: 12px;
                padding: 4px 10px;
                display: inline-block;
                margin-top: 4px;
            }
            
            /* 模態框優化 */
            .modal-box {
                width: 95%;
                padding: 20px;
                border-radius: 12px;
            }
            
            .modal-box h2 {
                font-size: 1.2em;
            }
            
            .session-grid {
                grid-template-columns: 1fr;
            }
            
            .session-card {
                padding: 12px 14px;
            }
            
            /* AI 部分隱藏在超小螢幕 */
            .ai-section {
                display: none;
            }
            
            /* 評論區域優化 */
            .comment-item {
                font-size: 13px;
                padding: 10px;
            }
        }
        
        /* 超小螢幕 (< 400px) 額外調整 */
        @media (max-width: 400px) {
            .header h1 {
                font-size: 1.1em;
            }
            
            .stats {
                flex-direction: column;
                gap: 8px;
                font-size: 12px;
            }
            
            .btn {
                padding: 11px 12px !important;
                font-size: 14px !important;
            }
            
            .question-id {
                font-size: 12px;
            }
            
            .option {
                padding: 12px 10px;
                font-size: 14px;
                gap: 10px;
            }
        }
'''

style_close_idx = html.rfind('</style>')
if style_close_idx != -1:
    html = html[:style_close_idx] + mobile_css + '\n    ' + html[style_close_idx:]
else:
    head_close_idx = html.rfind('</head>')
    if head_close_idx != -1:
        html = html[:head_close_idx] + '\n<style>' + mobile_css + '</style>\n' + html[head_close_idx:]

# 保存為 index-mobile.html
with open('index-mobile.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ 已生成 index-mobile.html (Tailscale IP 版本，iPhone 優化)")
print("文件已保存！")
