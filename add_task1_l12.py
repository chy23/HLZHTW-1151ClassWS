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
lessons = json.loads(json_str)

task1_l12 = [
  {
    "indent": 1,
    "text": "一.課文段落結構"
  },
  {
    "indent": 2,
    "text": "（一）背景：（第 1 段）住在羅達的農夫，克服大自然的不利條件，被稱*南瓜大王*。"
  },
  {
    "indent": 2,
    "text": "（二）開端：（第 2、3 段）布大爺雖依依不捨，但仍決定*收割*四十顆心愛的大南瓜。"
  },
  {
    "indent": 2,
    "text": "（三）發展： 1.（第 4 段）收成當天早上，發現南瓜被偷走，判斷南瓜會出現*加迪斯*。"
  },
  {
    "indent": 3,
    "text": "2.（第 5-15 段）布大爺在市場認出親種的南瓜，並和*菜販*起爭執。警察請他提出*確鑿證明*。 3.（第 16-20 段）弗大叔*反駁*並威脅，提不出證據可能因*誣告*進監牢。"
  },
  {
    "indent": 2,
    "text": "（四）高潮：（第 21-23 段）布大爺拿出許多新鮮*南瓜蒂*，果然和南瓜們接得*天衣無縫*，證明自己才是南瓜的主人。"
  },
  {
    "indent": 2,
    "text": "（五）結局：（第 24、25 段）布大爺拿回賣南瓜的錢。慶幸自己留下了「*存根*」，才能讓南瓜*失而復得*。（失去又找回的四字語詞）"
  },
  {
    "indent": 1,
    "text": "二.閱讀理解提問"
  },
  {
    "indent": 1,
    "text": "1.從課文得知，南瓜*產*在哪裡？被偷到哪裡販*賣*？"
  },
  {
    "indent": 2,
    "text": "產：*羅達* 販賣：*加迪斯*"
  },
  {
    "indent": 1,
    "text": "2.布大爺忍痛收割南瓜後，如何度過漫漫長夜？"
  },
  {
    "indent": 2,
    "text": "*慢吞吞的走回家，難過一整夜，根本睡不著，活像隔天要嫁女兒的父親。*"
  },
  {
    "indent": 1,
    "text": "3.布大爺的心情感受，和那些文句有*緊密關係*？"
  },
  {
    "indent": 2,
    "text": "心滿意足、冷靜思考、悲從中來、震驚憤怒絕望",
    "isBox": True
  },
  {
    "indent": 2,
    "text": "① 在案發現場逗留一段時間，清點少掉的南瓜。*冷靜思考*"
  },
  {
    "indent": 2,
    "text": "② 那些南瓜在市場上看起來多漂亮！幸好我有留下存根。*心滿意足*"
  },
  {
    "indent": 2,
    "text": "③ 布大爺發現南瓜被偷走了！*震驚憤怒絕望*"
  },
  {
    "indent": 2,
    "text": "④ 難道您不明白這些南瓜都是我辛苦拉拔長大的嗎？*悲從中來*"
  },
  {
    "indent": 1,
    "text": "4.讀完本課，你覺得布大爺是什麼樣的人？請寫出*正確的舉證代號*。"
  },
  {
    "indent": 2,
    "text": "具有愛心：*ㄅㄇㄉ* 心思細膩：*ㄆㄈㄊ*"
  },
  {
    "indent": 2,
    "text": "ㄅ 他每天都深情的望著它們，感傷的說：「真捨不得和你們分開！」"
  },
  {
    "indent": 2,
    "text": "ㄆ 在冷靜思考後，他得出南瓜不可能留在羅達的結論。"
  },
  {
    "indent": 2,
    "text": "ㄇ 他說著說著悲從中來。"
  },
  {
    "indent": 2,
    "text": "ㄈ 他又在菜園逗留一段時間，是為了留下南瓜蒂來當證據。"
  },
  {
    "indent": 2,
    "text": "ㄉ 他慢吞吞的走回家，難過了一整夜。"
  },
  {
    "indent": 2,
    "text": "ㄊ 他對四十顆南瓜的顏色、形狀，甚至是名字都一清二楚！"
  },
  {
    "indent": 1,
    "text": "5.小説情節會*留下伏筆*，故事中細小布局或徵兆，跟故事後半部情節發展會有關聯。哪一段話有這樣的效果？"
  },
  {
    "indent": 2,
    "text": "*他在案發現場逗留一段時間，清點少掉的南瓜，才動身前往加迪斯。*"
  },
  {
    "indent": 1,
    "text": "6.小說能製造*緊張懸疑*的情節，也是故事安排的一大亮點。哪一段話有這樣的效果？"
  },
  {
    "indent": 2,
    "text": "*他把背包在地上不慌不忙打開來，圍觀的人都很納悶。*"
  },
  {
    "indent": 1,
    "text": "7.從故事中了解，最初警察認為布大爺的指控不能成立的主要原因？"
  },
  {
    "indent": 2,
    "text": "要有*確鑿的證據*"
  }
]

for lesson in lessons:
    if lesson.get("id") == "lesson-12":
        lesson["task1"] = task1_l12
        break

new_json_str = json.dumps(lessons, ensure_ascii=False, indent=2)
new_content = content[:match.start(1)] + new_json_str + content[match.end(1):]

with open("src/data/lessons.js", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Task 1 for Lesson 12 added successfully!")
