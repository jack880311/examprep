#!/usr/bin/env python3
"""Parse ace.md (from examtopics-downloader) into structured questions.json."""
import json
import re
from pathlib import Path

SRC = Path(__file__).parent / "ace.md"
OUT = Path(__file__).parent / "questions.json"

text = SRC.read_text(encoding="utf-8")

# Split on the question-separator line ("----...----" with at least 20 dashes)
blocks = re.split(r"\n-{20,}\n", text)

questions = []
header_re = re.compile(r"##\s+Examtopics\s+Associate\s+Cloud\s+Engineer[_\s]*(\d+)\s+question\s+#(\d+)", re.I)
opt_re = re.compile(r"^\*\*([A-F]):\*\*\s*(.+?)(?=\n\*\*[A-F]:\*\*|\n\*\*Answer|\Z)", re.DOTALL | re.MULTILINE)
answer_re = re.compile(r"\*\*Answer:\s*([A-F](?:\s*[, ]?\s*[A-F])*)\*\*")
ts_re = re.compile(r"\*\*Timestamp:\s*([^*]+)\*\*")
link_re = re.compile(r"\[View on ExamTopics\]\((https?://[^)]+)\)")
comments_re = re.compile(r"^Comments:\s*(.*)$", re.MULTILINE | re.DOTALL)

for b in blocks:
    b = b.strip()
    if not b:
        continue
    hm = header_re.search(b)
    if not hm:
        continue
    topic, qnum = hm.group(1), hm.group(2)

    # Question body is between header and first option
    first_opt = opt_re.search(b)
    if not first_opt:
        continue
    qbody = b[hm.end():first_opt.start()].strip()

    # Options
    # Grab substring from first option to Answer marker
    ans_m = answer_re.search(b)
    opts_region = b[first_opt.start(): ans_m.start() if ans_m else len(b)]
    options = {}
    for m in opt_re.finditer(opts_region):
        options[m.group(1)] = m.group(2).strip()

    answer = ans_m.group(1).replace(" ", "") if ans_m else ""

    ts = ts_re.search(b)
    link = link_re.search(b)
    cm = comments_re.search(b)
    comments = cm.group(1).strip() if cm else ""

    questions.append({
        "topic": int(topic),
        "qnum": int(qnum),
        "id": f"T{topic}-Q{qnum}",
        "question": qbody,
        "options": options,
        "answer": answer,
        "timestamp": ts.group(1).strip() if ts else "",
        "link": link.group(1) if link else "",
        "comments_raw": comments,
    })

# Sort stably: by topic then qnum
questions.sort(key=lambda x: (x["topic"], x["qnum"]))

# Assign display index
for i, q in enumerate(questions, 1):
    q["idx"] = i

OUT.write_text(json.dumps(questions, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Parsed {len(questions)} questions → {OUT}")
if questions:
    s = questions[0]
    print(f"First: {s['id']} ans={s['answer']} opts={list(s['options'])}")
