import subprocess
import time
import re
import json

def run(cmd):
    print(f"Running: {cmd}")
    subprocess.run(cmd, shell=True, check=True)

# 讀取 main 分支的原始 index 資料
with open("public/data/lessons_index.json", "r", encoding="utf-8") as f:
    ORIGINAL_INDEX = json.load(f)

print("\n========== 上傳主網址 (總表) ==========")
try:
    run("git push origin main --force")
except Exception as e:
    print(f"警告: 推送主網址失敗: {e}")

for i in range(1, 13):
    branch = f"115-1-L{i}"
    print(f"\n========== 處理分支 {branch} ==========")

    # 每次都從 main 重建分支
    run("git checkout main")
    try:
        run(f"git branch -D {branch}")
    except:
        pass
    run(f"git checkout -b {branch}")

    # 1. 修改 vite.config.js 的 base 路徑
    with open("vite.config.js", "r") as f:
        v = f.read()
    v = re.sub(r"base:\s*'/HLZHTW-1151ClassWS/.*?',", f"base: '/HLZHTW-1151ClassWS/{branch}/',", v)
    with open("vite.config.js", "w") as f:
        f.write(v)

    # 2. 修改 deploy.yml（加上 destination_dir）
    with open(".github/workflows/deploy.yml", "r") as f:
        deploy = f.read()
    deploy = re.sub(r"\s*destination_dir:.*", "", deploy)
    deploy = re.sub(r"(keep_files: true\s*)+", "keep_files: true\n", deploy)
    deploy = deploy.replace("keep_files: true", f"keep_files: true\n          destination_dir: {branch}")
    deploy = re.sub(r"branches: \[.*?\]", f"branches: [ {branch} ]", deploy)
    deploy = re.sub(r"branches:\n      - \S+", f"branches:\n      - {branch}", deploy)
    with open(".github/workflows/deploy.yml", "w") as f:
        f.write(deploy)

    # 3. 從備份的原始 JSON 重建，改成只顯示 1~i 課 (Lazy Loading index)
    sliced_index = ORIGINAL_INDEX[:i]
    with open("public/data/lessons_index.json", "w", encoding="utf-8") as f:
        json.dump(sliced_index, f, ensure_ascii=False, indent=2)

    # 4. 修改 favicon.svg 顏色以區分主網站與分支
    try:
        with open("public/favicon.svg", "r") as f:
            fav = f.read()
        fav = fav.replace("#2563EB", "#EA580C")
        fav = fav.replace("#1E3A8A", "#9A3412")
        fav = fav.replace("#1E40AF", "#9A3412")
        with open("public/favicon.svg", "w") as f:
            f.write(fav)
            
        with open("index.html", "r") as f:
            idx = f.read()
        idx = idx.replace('href="/favicon.jpg"', 'href="/favicon.svg"').replace('type="image/jpeg"', 'type="image/svg+xml"')
        with open("index.html", "w") as f:
            f.write(idx)
    except Exception as e:
        print(f"修改 favicon 失敗: {e}")

    # 提交並強制推送
    run("git add -A")
    try:
        run(f"git commit -m '正確切割：{branch} 顯示第 {i} 至 {i} 課'")
    except:
        pass
    
    try:
        run(f"git push origin {branch} --force")
    except Exception as e:
        print(f"警告: 推送 {branch} 失敗: {e}")

    # GitHub Actions 不太會因為連續 push 塞車，但若真的需要延遲可以保留
    # print(f"等待 10 秒...")
    # time.sleep(10)

run("git checkout main")
print("\n✅ 全部修復並上傳完畢！")
