import subprocess
import shutil
import json
import re
import os

def run(cmd):
    print(f"Running: {cmd}")
    subprocess.run(cmd, shell=True, check=True)

# 準備目標資料夾
FINAL_DIST = "final_dist"
if os.path.exists(FINAL_DIST):
    shutil.rmtree(FINAL_DIST)
os.makedirs(FINAL_DIST)

# 備份原始檔案
with open("vite.config.js", "r", encoding="utf-8") as f:
    ORIGINAL_VITE = f.read()

with open("public/data/lessons_index.json", "r", encoding="utf-8") as f:
    ORIGINAL_INDEX = json.load(f)

try:
    with open("public/favicon.svg", "r", encoding="utf-8") as f:
        ORIGINAL_FAVICON = f.read()
    with open("index.html", "r", encoding="utf-8") as f:
        ORIGINAL_INDEX_HTML = f.read()
except Exception:
    pass

try:
    print("\n========== 1. 編譯主網站 (總表) ==========")
    run("npm run build")
    # 將 dist 內容複製到 final_dist
    shutil.copytree("dist", FINAL_DIST, dirs_exist_ok=True)
    
    print("\n========== 2. 編譯 12 個子版本 ==========")
    for i in range(1, 13):
        branch_name = f"115-1-L{i}"
        print(f"\n--- 編譯 {branch_name} ---")
        
        # 1. 替換 vite.config.js base
        v = re.sub(r"base:\s*'/HLZHTW-1151ClassWS/.*?',", f"base: '/HLZHTW-1151ClassWS/{branch_name}/',", ORIGINAL_VITE)
        with open("vite.config.js", "w", encoding="utf-8") as f:
            f.write(v)
            
        # 2. 裁切 lessons_index.json
        sliced_index = ORIGINAL_INDEX[:i]
        with open("public/data/lessons_index.json", "w", encoding="utf-8") as f:
            json.dump(sliced_index, f, ensure_ascii=False, indent=2)
            
        # 3. 換 Favicon 顏色
        try:
            fav = ORIGINAL_FAVICON.replace("#2563EB", "#EA580C").replace("#1E3A8A", "#9A3412").replace("#1E40AF", "#9A3412")
            with open("public/favicon.svg", "w", encoding="utf-8") as f:
                f.write(fav)
            idx_html = ORIGINAL_INDEX_HTML.replace('href="/favicon.jpg"', 'href="/favicon.svg"').replace('type="image/jpeg"', 'type="image/svg+xml"')
            with open("index.html", "w", encoding="utf-8") as f:
                f.write(idx_html)
        except Exception as e:
            print("修改 favicon 失敗:", e)
            
        # 4. 執行編譯
        run("npm run build")
        
        # 5. 移動到 final_dist
        target_dir = os.path.join(FINAL_DIST, branch_name)
        if os.path.exists(target_dir):
            shutil.rmtree(target_dir)
        shutil.copytree("dist", target_dir)
        
finally:
    print("\n========== 3. 復原原始檔案 ==========")
    with open("vite.config.js", "w", encoding="utf-8") as f:
        f.write(ORIGINAL_VITE)
    with open("public/data/lessons_index.json", "w", encoding="utf-8") as f:
        json.dump(ORIGINAL_INDEX, f, ensure_ascii=False, indent=2)
    try:
        with open("public/favicon.svg", "w", encoding="utf-8") as f:
            f.write(ORIGINAL_FAVICON)
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(ORIGINAL_INDEX_HTML)
    except Exception:
        pass

print("\n✅ 所有編譯完成，發布包已生成於 final_dist/ 資料夾。")
