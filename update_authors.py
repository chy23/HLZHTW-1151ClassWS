# -*- coding: utf-8 -*-
import json
import re

with open("src/data/lessons.js", "r", encoding="utf-8") as f:
    content = f.read()

match = re.search(r"export const lessons = (\[.*\]);", content, re.DOTALL)
if not match:
    print("Could not find lessons array!")
    exit(1)

json_str = match.group(1)
try:
    lessons = json.loads(json_str)
except Exception as e:
    print(f"JSON parsing error: {e}")
    exit(1)

updates = {
    "lesson-7": {"lessonName": "跟著公共藝術去旅行", "author": "張育雯"},
    "lesson-8": {"lessonName": "街頭藝術家", "author": "桂文亞"},
    "lesson-9": {"lessonName": "戲臺上的她與他", "author": "李光福"},
    "lesson-10": {"lessonName": "過故人莊", "author": "孟浩然"},
    "lesson-11": {"lessonName": "來一碗溫暖的羹湯", "author": "陳維鸚"},
    "lesson-12": {"lessonName": "存根", "author": "阿拉爾孔"}
}

for lesson in lessons:
    lid = lesson.get("id")
    if lid in updates:
        lesson["lessonName"] = updates[lid]["lessonName"]
        lesson["author"] = updates[lid]["author"]

new_json_str = json.dumps(lessons, ensure_ascii=False, indent=2)
new_content = content[:match.start(1)] + new_json_str + content[match.end(1):]

with open("src/data/lessons.js", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Authors and lesson names updated successfully!")
