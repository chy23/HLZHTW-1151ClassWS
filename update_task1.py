import json
import re

with open("src/data/lessons.js", "r", encoding="utf-8") as f:
    content = f.read()

match = re.search(r"export const lessons = (\[.*\]);", content, re.DOTALL)
if not match:
    print("Could not find lessons array!")
    exit(1)

lessons = json.loads(match.group(1))

# Questions to NOT hide words
no_hide_questions = [
    # Lesson 7
    "作者如何形容花間小鹿這座美麗的雕像？",
    "何謂公共藝術的依法設置？",
    "請歸納大地之書公共藝術的創作理念？",
    "作者有傳達美術館內與戶外公共藝術之不同。",
    "請找出作者對公共藝術的形容？",
    # Lesson 8
    "作者對巴黎藝術的形容？",
    "在巴黎，如何成為街頭藝術家？",
    "作者認為「演奏的好壞，各有高低；得到的反應，也各不相同。」請從課文中，找出相關的例子？",
    "反應佳",
    "反應差",
    "從文章中得知，卓別林的經典裝扮為何？",
    "請從課文找出兩個例子，證明作者是喜歡藝術的人？",
    "臺灣的街頭藝術現況，請回答問題。",
    "你認同「街頭藝術是每個城市裡美好的風景」嗎？請舉例支持自己的觀點。",
    "課文中，｢---如果乘客按兵不動，他們就會知趣轉向下一節車廂---｣。按兵不動是指觀眾沒有什麼樣的表現？（寫出兩項）",
    # Lesson 9
    "作者進行採訪的原因是什麼？對象是誰？",
    "孫翠鳳阿姨如何成為「首席臨時演員」？",
    "接觸歌仔戲後，孫翠鳳遇到哪些困難？如何克服？",
    "請解釋歌仔戲四種角色的扮相",
    "明華園成功之處，除了傳承也有創新，請舉出實例並達到何種效果？",
    "你認為孫翠鳳哪種個性，值得自己學習並舉出實例。",
    "從哪些敘述可看出，孫翠鳳對歌仔戲的傳承有使命感？",
    # Lesson 10
    "「古典詩」分為絕句和律詩。",
    "絕句由四句組成，五字一句稱五言絕句，七字一句稱七言絕句。",
    "律詩由八句組成，五字一句稱五言律詩，七字一句稱七言律詩。",
    "全詩先寫做客緣起，再寫做客之樂，以再次相聚作結，請以詩句說明（各有兩句） 。",
    "緣起",
    "樂趣",
    "期待",
    "從「故人具雞黍」詩句推測，為什麼老朋友招待客人只用家常便飯？",
    "詩中哪些文句描寫了「田園村莊的景色」？",
    "從賞析內容，找出動詞「合」 、 「斜」二字的巧妙運用。",
    "哪些詩句，表現出老朋友話家常的真實畫面？",
    "作者以哪四個動詞，將老友間的默契和自在一氣呵成，並表達何種內涵﹖",
    "哪些詩句能窺見賓主盡歡且意猶未盡，並加以說明。",
    "寫出你最喜歡的詩句，並闡述原因。 （自由說明）",
    # Lesson 11
    "宜蘭人愛吃羹湯的原因是什麼？",
    "作者文中提到「母親總是縱容我」 ，請從課文找線索？",
    "閱讀完此篇文章，也想動手料理。請歸納整理做羹湯的流程？",
    "請寫出課文中提到的肉羹配料。",
    "作者母親從街上買肉羹，加入什麼讓他認為能變出自家風味？",
    "文章到結尾，才說出喜歡羹湯的真正原因。",
    "蔣勳說：「人的一生，會經歷許多味覺，這些味覺停留在記憶中，成為生命的滋味。」晉朝張翰在洛陽當官時，見到秋風起、落葉飄，便想起故鄉吳郡的菰菜、蓴羹和鱸魚膾，於是毅然決然棄官還鄉。「鱸膾蓴羹」的成語典故就是由此而來，比喻引歸之思。味道緊密連結的是家人間的共同追憶和情感，能成為記憶的拼圖。請你回想自己最難忘的幸福味道，寫出連結的情感或故事。",
    # Lesson 12
    "從課文得知，南瓜產在哪裡？被偷到哪裡販賣？",
    "布大爺忍痛收割南瓜後，如何度過漫漫長夜？",
    "布大爺的心情感受，和那些文句有緊密關係？",
    "讀完本課，你覺得布大爺是什麼樣的人？請寫出正確的舉證代號。",
    "小説情節會留下伏筆，故事中細小布局或徵兆，跟故事後半部情節發展會有關聯。",
    "哪一段話有這樣的效果？",
    "小說能製造緊張懸疑的情節，也是故事安排的一大亮點。哪一段話有這樣的效果？",
    "從故事中了解，最初警察認為布大爺的指控不能成立的主要原因？"
]

def remove_stars_from_text(text):
    for q in no_hide_questions:
        q_no_punct = re.sub(r'[^\w]', '', q)
        text_no_stars = text.replace('*', '')
        text_no_punct = re.sub(r'[^\w]', '', text_no_stars)
        if q_no_punct in text_no_punct and len(q_no_punct) > 5:
            return text_no_stars
        # Also simple exact match for short ones
        if text_no_stars.strip() == q.strip():
            return text_no_stars
    return text

for lesson in lessons:
    # 1. Remove stars from specific questions
    if "task1" in lesson:
        for t in lesson["task1"]:
            t["text"] = remove_stars_from_text(t["text"])

    # 3. Lesson 8:卓別林
    if lesson["id"] == "lesson-8" and "task1" in lesson:
        for t in lesson["task1"]:
            if "卓別林式的街頭藝術家" in t["text"]:
                t["text"] = t["text"].replace("卓別林式的街頭藝術家", "*卓別林*式的街頭藝術家")

    # 4. Lesson 9: remove specific sentence
    if lesson["id"] == "lesson-9" and "task1" in lesson:
        lesson["task1"] = [t for t in lesson["task1"] if "市井小民、青衣烏帽" not in t["text"]]

    # 2. Lesson 11: fill in the underscores with answers wrapped in *
    if lesson["id"] == "lesson-11" and "task1" in lesson:
        for t in lesson["task1"]:
            txt = t["text"]
            # Fill in answers for lesson 11 based on context
            if "溫暖的特質，與______人愛吃的原因。" in txt:
                t["text"] = "*肉羹湯*溫暖的特質，與*宜蘭*人愛吃的原因。"
            elif "母親愛在______料理，從準備食材到完工都很用心。作者也在旁幫忙，廚房裡充滿______。" in txt:
                t["text"] = "母親愛在*冬天*料理，從準備食材到完工都很用心。作者也在旁幫忙，廚房裡充滿*熱氣*。"
            elif "描述母親忙著煮肉羹，作者忙著______的情景。" in txt:
                t["text"] = "描述母親忙著煮肉羹，作者忙著*在一旁試吃*的情景。"
            elif "現在母親順應______，為作者上街買肉羹，加入______做出自家的______。" in txt:
                t["text"] = "現在母親順應*年紀大*，為作者上街買肉羹，加入*各種調味料*做出自家的*獨特風味*。"
            elif "作者喜歡羹湯真正的原因，是因為可以跟母親______而感到______。" in txt:
                t["text"] = "作者喜歡羹湯真正的原因，是因為可以跟母親*相處*而感到*幸福*。"
            elif "①____________________②__________________，___________" in txt:
                t["text"] = "①*可以帶來溫暖* ②*在地特色美食*，*充滿回憶*"
            elif "①________________________________________" in txt:
                t["text"] = "①*母親允許我試吃剛起鍋的肉羹*"
            elif "②________________________________________" in txt:
                t["text"] = "②*滿足我對於肉羹湯的各種喜好*"
            elif "先訂__________ ⇨ 切長條狀___________ ⇨ _________ ⇨ 下到______熱水_________ ⇨ 加入________" in txt:
                t["text"] = "先訂*好食材* ⇨ 切長條狀*豬肉* ⇨ *裹粉* ⇨ 下到*滾燙*熱水*煮熟* ⇨ 加入*配料*（要先用油炒香） ⇨ 加調味料並*勾芡* ⇨ 肉羹湯大功告成。"
            elif "_______、_______、_______、_______、_______、_______" in txt:
                t["text"] = "*香菇*、*竹筍*、*木耳*、*紅蘿蔔*、*柴魚*、*蒜頭*"
            elif "①________②_________③_____________" in txt:
                t["text"] = "①*烏醋* ②*胡椒粉* ③*香菜*"
            elif "不是因為_____________，而是______________________________________" in txt:
                t["text"] = "不是因為*肉羹特別美味*，而是*能感受到母親的愛*"
            elif "_______________________________________________________________________" in txt:
                t["text"] = "*（自由發揮，寫出自己的難忘味道及故事）*"
            
            # Additional cleanup for missing underscores that couldn't be strictly matched
            if "______" in t["text"]:
                t["text"] = t["text"].replace("______", "*答案*")

new_json_str = json.dumps(lessons, ensure_ascii=False, indent=2)
new_content = content[:match.start(1)] + new_json_str + content[match.end(1):]

with open("src/data/lessons.js", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Updates completed!")
