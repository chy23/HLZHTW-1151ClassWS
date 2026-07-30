import json
import re

with open("src/data/lessons.js", "r", encoding="utf-8") as f:
    content = f.read()

match = re.search(r"export const lessons = (\[.*\]);", content, re.DOTALL)
if not match:
    print("Could not find lessons array!")
    exit(1)

lessons = json.loads(match.group(1))

task3_data = {
    "lesson-7": {
        "practices": [
            {"ex": "好不(熱絡)！", "pr": "好不(熱鬧)！ / 好不(無聊)！"},
            {"ex": "像(樹枝)般(昂揚)的(鹿角)", "pr": "像(太陽)般(燦爛)的(笑容) / 像(宮殿)般(華麗)的(住宅)"},
            {"ex": "若(公共建設的經費為五千萬元)，就必須(設置價值五十萬元以上的公共藝術品)。", "pr": "若(想達到自己的目標)，就必須(努力到底，一刻也不能鬆懈)。"}
        ],
        "sentences": [
            {"word": "一方面……另一方面……", "ex": "當我住院時，爸爸一方面不停的安慰我，另一方面為我忙進忙出，操心不已。"}
        ]
    },
    "lesson-8": {
        "practices": [
            {"ex": "(脣上)一(撇)(小)(黑鬍)", "pr": "(胸前)一(朵)(大)(紅花)"}
        ],
        "sentences": [
            {"word": "即使……也……", "ex": "人若驕傲自滿，即使取得再大的成就，也無法獲得他人尊重。"}
        ]
    },
    "lesson-9": {
        "practices": [
            {"ex": "一(次)又一(次)的(登臺)後", "pr": "一(口)又一(口)的(餵食)後 / 一(回)又一(回)的(討論)後"},
            {"ex": "其實(我)(沒有堅持一定要演小生)，像(樊梨花、白素貞的戲)，還有(獅子王的花臉)，甚至是(丑角)，(我)也(演過)。", "pr": "其實(哥哥)(喜歡各種球類運動)，像(桌球、羽球)，還有(網球和棒球)，甚至是(撞球)，(哥哥)也(打過)。"},
            {"ex": "舞臺上正好有年輕演員在排練薛平貴與王寶釧，你們一邊(看)，我一邊(說明)，這樣比較容易了解。", "pr": "上課時，我們一邊(專心聽講)，一邊(寫課堂筆記)，方便我們回家後複習。"}
        ],
        "sentences": [
            {"word": "不但……更……", "ex": "這隻柴犬超級聰明，不但會安撫主人情緒，更會耍寶娛樂大家。"}
        ]
    },
    "lesson-10": {
        "practices": [
            {"ex": "(翠綠)的(樹林)(圍繞)著(村莊)", "pr": "(火紅)的(楓葉)(環抱)著(寺廟)"},
            {"ex": "(青翠)的(山巒)在(城外)(連綿不斷)", "pr": "(美麗)的(蝴蝶)在(花園裡)(翩翩起舞)"},
            {"ex": "(全詩)先(寫做客緣起)，再(寫做客之樂)，最後(以期盼再次相聚作結)。", "pr": "(同樂會)先(由同學表演才藝)，再(一起玩趣味遊戲)，最後(以分組進行歌唱接龍收尾)。"}
        ],
        "sentences": [
            {"word": "除了……也……", "ex": "暑假期間，除了有校隊到學校練習，我們也會去幫忙布置教室。"}
        ]
    },
    "lesson-11": {
        "practices": [
            {"ex": "(天寒時)，特別想(來碗羹)", "pr": "(用餐後)，特別想(喝檸檬水)"},
            {"ex": "(勾芡)的(湯汁)(濃稠)(不易散熱)", "pr": "(強烈)的(陽光)(酷熱)(難以忍受)"},
            {"ex": "(勾芡的湯汁濃稠不易散熱)，即便(是起鍋一會兒)，(碗裡)也(還是熱騰騰的)。", "pr": "(刺激的比賽精彩無法言喻)，即便(最後輸了球)，(我)也(會永遠記得這場比賽)。"}
        ],
        "sentences": [
            {"word": "不是……而是……", "ex": "我喜歡這件新衣服，不是因為它很流行，而是因為它是奶奶送我的禮物。"}
        ]
    },
    "lesson-12": {
        "practices": [
            {"ex": "(說)著(說)著(悲從中來)", "pr": "(唱)著(唱)著(泣不成聲) / (想)著(想)著(心花怒放)"},
            {"ex": "(終於)(流下)(欣慰)的(淚水)", "pr": "(總算)(完成)(艱難)的(任務) / (立刻)(浮現)(慈愛)的(笑容)"}
        ],
        "sentences": [
            {"word": "一……就……", "ex": "一聽到地震警報，我們就急忙躲到桌下。"},
            {"word": "……竟然……", "ex": "大家整裝就緒，準備登機，竟然聽到飛機停飛的廣播。"}
        ]
    }
}

for lesson in lessons:
    l_id = lesson["id"]
    if l_id in task3_data:
        lesson["practices"] = task3_data[l_id]["practices"]
        lesson["sentences"] = task3_data[l_id]["sentences"]

new_json_str = json.dumps(lessons, ensure_ascii=False, indent=2)
new_content = content[:match.start(1)] + new_json_str + content[match.end(1):]

with open("src/data/lessons.js", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Task 3 updated successfully!")
