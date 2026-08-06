import json
import re
import os

with open("src/data/lessons.js", "r", encoding="utf-8") as f:
    content = f.read()

match = re.search(r"export const lessons = (\[.*\]);", content, re.DOTALL)
lessons = json.loads(match.group(1))

os.makedirs("public/data", exist_ok=True)

index = []
for l in lessons:
    # metadata for sidebar
    index.append({
        "id": l["id"],
        "lessonNum": l.get("lessonNum", ""),
        "lessonName": l.get("lessonName", ""),
        "author": l.get("author", "")
    })
    
    # save individual lesson full data
    with open(f"public/data/{l['id']}.json", "w", encoding="utf-8") as f:
        json.dump(l, f, ensure_ascii=False, indent=2)

# save index
with open("public/data/lessons_index.json", "w", encoding="utf-8") as f:
    json.dump(index, f, ensure_ascii=False, indent=2)

print("Data split complete.")
