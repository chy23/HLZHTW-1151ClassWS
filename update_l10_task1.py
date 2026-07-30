# -*- coding: utf-8 -*-
import json
import re

with open("src/data/lessons.js", "r", encoding="utf-8") as f:
    content = f.read()

match = re.search(r"export const lessons = (\[.*\]);", content, re.DOTALL)
if not match:
    print("Could not find lessons array!")
    exit(1)

lessons = json.loads(match.group(1))

for lesson in lessons:
    if lesson["id"] == "lesson-10" and "task1" in lesson:
        for t in lesson["task1"]:
            if "*緣起*：" in t["text"]:
                t["text"] = t["text"].replace("*緣起*：", "緣起：")
            if "*樂趣*：" in t["text"]:
                t["text"] = t["text"].replace("*樂趣*：", "樂趣：")
            if "*期待*：" in t["text"]:
                t["text"] = t["text"].replace("*期待*：", "期待：")

new_json_str = json.dumps(lessons, ensure_ascii=False, indent=2)
new_content = content[:match.start(1)] + new_json_str + content[match.end(1):]

with open("src/data/lessons.js", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Lesson 10 Task 1 updated successfully!")
