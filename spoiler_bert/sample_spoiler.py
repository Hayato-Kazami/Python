"""剧透标注数据分层采样：切分 train/dev/test 并生成 class.txt。

输入：本目录 labeled_spoiler_YYYYMMDD.csv（label_spoiler.py 的输出）
输出：data/ 下的 train.txt / dev.txt / test.txt / class.txt
      每行：弹幕文本 \t 标签索引（0=非剧透 1=剧透）

采样策略：按 (bvid, 剧透标签) 分组 8:1:1 切分。
"""
from pathlib import Path

import pandas as pd

_HERE = Path(__file__).resolve().parent
OUT_DIR = _HERE / "data"

CLASSES = ["非剧透", "剧透"]  # class.txt 顺序，索引 0/1
SEED = 42
TRAIN_RATIO, DEV_RATIO, TEST_RATIO = 0.8, 0.1, 0.1


def clean_text(s):
    return (str(s).replace("\t", " ").replace("\n", " ").replace("\r", " ").strip())


def main():
    files = sorted(_HERE.glob("labeled_spoiler_*.csv"), key=lambda p: p.stat().st_mtime)
    if not files:
        print("没找到 labeled_spoiler_*.csv，请先运行 label_spoiler.py")
        return
    labeled = files[-1]
    print(f"使用 {labeled}")

    df = pd.read_csv(labeled, encoding="utf-8-sig")
    df = df[df["剧透"].isin(CLASSES)].copy()
    df["文本"] = df["内容"].map(clean_text)
    df = df[df["文本"] != ""]

    label2idx = {c: i for i, c in enumerate(CLASSES)}

    train_parts, dev_parts, test_parts = [], [], []
    for (bvid, label), group in df.groupby(["bvid", "剧透"]):
        group = group.sample(frac=1, random_state=SEED)
        n = len(group)
        n_test = max(1, int(n * TEST_RATIO))
        n_dev = max(1, int(n * DEV_RATIO))
        n_train = n - n_test - n_dev
        if n_train < 1:
            n_dev = n_test = 0
        train_parts.append(group.iloc[:n_train])
        dev_parts.append(group.iloc[n_train:n_train + n_dev])
        test_parts.append(group.iloc[n_train + n_dev:])

    splits = {
        "train": pd.concat(train_parts).sample(frac=1, random_state=SEED),
        "dev": pd.concat(dev_parts).sample(frac=1, random_state=SEED),
        "test": pd.concat(test_parts).sample(frac=1, random_state=SEED),
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "class.txt").write_text("\n".join(CLASSES), encoding="utf-8")

    for name, part in splits.items():
        lines = [f"{row['文本']}\t{label2idx[row['剧透']]}" for _, row in part.iterrows()]
        (OUT_DIR / f"{name}.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print("切分完成，输出到", OUT_DIR)
    for name, part in splits.items():
        dist = part["剧透"].value_counts().reindex(CLASSES).fillna(0).astype(int).to_dict()
        print(f"  {name}: {len(part):>5} 条  分布 {dist}")


if __name__ == "__main__":
    main()
