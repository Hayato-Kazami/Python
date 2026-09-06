"""用大模型给弹幕打「剧透 / 非剧透」标签。

用途：识别剧透类弹幕，前端可自动折叠，避免没看到该处的观众被剧透。

输入：../Scraping/labeled_20260830.csv（已有情绪标签的弹幕，取「内容」列）
输出：本目录 labeled_spoiler_YYYYMMDD.csv（原列 + 新增「剧透」列，值：非剧透 / 剧透）

流程：断点续标 + 批量送 LLM + 温和限速。

运行前：在下面配置区填 API_KEY（OpenAI 兼容接口，DeepSeek 等）。
"""
import csv
import json
import os
import re
import time
from datetime import date
from pathlib import Path

import pandas as pd
from openai import OpenAI

# ============================ 配置区 ============================
API_KEY = ""  # ← 填你的 key（DeepSeek 等 OpenAI 兼容接口）
BASE_URL = "https://api.deepseek.com"
MODEL = "deepseek-chat"
# ================================================================

HERE = Path(__file__).resolve().parent
INPUT_CSV = str(HERE.parent / "Scraping" / "labeled_20260830.csv")  # 已有情绪标签的弹幕
BATCH_SIZE = 30

LABELS = ["非剧透", "剧透"]
HEADER_OUT = ["内容", "视频标题", "bvid", "出现时间秒", "发送时间",
              "颜色", "模式", "字号", "弹幕池", "标签", "剧透"]


def partial_path() -> str:
    return str(HERE / "labeled_spoiler_partial.csv")


SYSTEM_PROMPT = (
    "你是 B 站弹幕剧透标注员。判断每条弹幕是否「剧透」，二选一：\n"
    "- 剧透：透露了关键剧情信息——结局、反转、伏笔回收、角色命运（谁死/谁赢/谁黑化/谁在一起）、"
    "关键真相、凶手是谁等，会让没看到该处的观众提前知道剧情。\n"
    "- 非剧透：不透露关键剧情，只表达情绪、玩梗、打卡、提问、陈述与剧情无关的内容。\n\n"
    "规则：\n"
    "1. 剧透的关键是「透露了具体关键剧情」，不是「提到某角色名/作品名」。\n"
    "2. 「XX 是凶手」「XX 死了」「最后他们在一起了」「这里埋了伏笔后面会回收」→ 剧透。\n"
    "3. 纯情绪（泪目/哈哈/刀死我了）、玩梗、打卡、吐槽画质 → 非剧透。\n"
    "4. 只输出 JSON，不要任何解释或多余文字。"
)


def build_user_prompt(items):
    lines = "\n".join(f"{i}. {t}" for i, t in enumerate(items))
    return (
        f"判断下面 {len(items)} 条弹幕是否剧透，按编号顺序返回 JSON 数组，"
        f'每项形如 {{"id": 编号, "label": "非剧透|剧透"}}，不要输出其他内容：\n\n{lines}'
    )


def parse_reply(text, n):
    t = text.strip()
    t = re.sub(r"^```[a-zA-Z]*\s*", "", t)
    t = re.sub(r"\s*```$", "", t)
    start, end = t.find("["), t.rfind("]")
    if start == -1 or end == -1:
        raise ValueError("回复里没有 JSON 数组")
    arr = json.loads(t[start:end + 1])
    label_by_id = {int(item["id"]): item["label"] for item in arr}
    result = []
    for i in range(n):
        lab = label_by_id.get(i)
        if lab not in LABELS:
            raise ValueError(f"第 {i} 条标签非法：{lab!r}")
        result.append(lab)
    return result


def label_batch(client, items, retries=3):
    for attempt in range(retries):
        try:
            resp = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": build_user_prompt(items)},
                ],
                temperature=0,
            )
            return parse_reply(resp.choices[0].message.content, len(items))
        except Exception as e:
            print(f"    批次标注失败（第 {attempt + 1}/{retries} 次）：{e}")
            if attempt < retries - 1:
                time.sleep(3 * (attempt + 1))
    return None


def main():
    if not API_KEY.strip():
        print("请先在脚本顶部配置区填 API_KEY。")
        return

    df = pd.read_csv(INPUT_CSV, encoding="utf-8-sig", dtype=str)
    print(f"读入 {len(df)} 条弹幕")

    done_texts = set()
    done_rows = []
    p = partial_path()
    if os.path.exists(p):
        with open(p, encoding="utf-8-sig", newline="") as f:
            r = csv.DictReader(f)
            for row in r:
                done_texts.add(row["内容"])
                done_rows.append(row)
        print(f"检测到已标注 {len(done_texts)} 条，将跳过。")

    pool = df[~df["内容"].isin(done_texts)].reset_index(drop=True)
    print(f"本次待标注 {len(pool)} 条")

    client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

    new_file = not os.path.exists(p)
    pf = open(p, "a", encoding="utf-8", newline="")
    writer = csv.writer(pf)
    if new_file:
        writer.writerow(HEADER_OUT)

    n = len(pool)
    try:
        for start in range(0, n, BATCH_SIZE):
            chunk = pool.iloc[start:start + BATCH_SIZE]
            items = chunk["内容"].astype(str).tolist()
            labels = label_batch(client, items)
            if labels is None:
                print(f"    [{start}/{n}] 标注失败，跳过本批")
                continue
            for (_, row), lab in zip(chunk.iterrows(), labels):
                writer.writerow([
                    row["内容"], row.get("视频标题", ""), row["bvid"],
                    row.get("出现时间秒", ""), row.get("发送时间", ""),
                    row.get("颜色", ""), row.get("模式", ""),
                    row.get("字号", ""), row.get("弹幕池", ""),
                    row.get("标签", ""), lab,
                ])
            pf.flush()
            print(f"    [{start + len(chunk)}/{n}] 已标 {start + len(chunk)} 条")
            time.sleep(0.5)
    finally:
        pf.close()

    rows = done_rows + list(csv.DictReader(open(p, encoding="utf-8-sig", newline="")))
    seen, uniq = set(), []
    for row in rows:
        if row["内容"] in seen:
            continue
        seen.add(row["内容"])
        uniq.append(row)

    out = HERE / f"labeled_spoiler_{date.today().strftime('%Y%m%d')}.csv"
    with open(out, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(HEADER_OUT)
        for row in uniq:
            w.writerow([row.get(k, "") for k in HEADER_OUT])

    n_spoiler = sum(1 for r in uniq if r.get("剧透") == "剧透")
    print(f"\n标注完成：共 {len(uniq)} 条，其中剧透 {n_spoiler} 条，已保存到 {out}")


if __name__ == "__main__":
    main()
