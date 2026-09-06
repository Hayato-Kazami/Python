"""BiLSTM 直接训练基线（不蒸馏），用于和蒸馏结果做对照，量化知识蒸馏的增益。

对照组设计（只差「有没有老师软标签」这一个变量，其余完全一致）：
    - 模型：BiLSTM（同一个 student_model.py）
    - 学习率：conf.student_lr（与蒸馏的学生一致）
    - 损失：仅 CrossEntropyLoss 硬标签（蒸馏里是 alpha*软损失 + (1-alpha)*硬损失）

运行：python model_direct.py
"""
from pathlib import Path

import torch
from tqdm import tqdm

from config import Config
from utils import build_dataloader
from student_model import BiLSTM
from torch.nn import CrossEntropyLoss
from train import model2eval

conf = Config()

_model_dir = Path(conf.last_model_path).parent
DIRECT_BEST = str(_model_dir / "direct_bilstm_best.pth")
DIRECT_LAST = str(_model_dir / "direct_bilstm_last.pth")


def model2direct(train_loader, dev_loader, model, device):
    loss_fn = CrossEntropyLoss()
    optimizer = torch.optim.AdamW(model.parameters(), lr=conf.student_lr)

    best_f1 = 0.
    total_iters = 0

    for epoch in range(conf.epochs):
        model.train()
        total_loss_epoch = 0.

        for i, (input_ids, attention_mask, labels) in enumerate(
                tqdm(train_loader, total=len(train_loader),
                     desc=f"直接训练 Epoch {epoch + 1}")):
            input_ids = input_ids.to(device)
            attention_mask = attention_mask.to(device)
            labels = labels.to(device)

            logits = model(input_ids, attention_mask)
            loss = loss_fn(logits, labels)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            total_loss_epoch += loss.item()
            total_iters += 1

            if total_iters % 150 == 0:
                f1, report, cm = model2eval(dev_loader, model, device)
                print(f"\nEpoch {epoch + 1}, Iter {i + 1}/{len(train_loader)}, F1: {f1:.4f}")
                model.train()
                if f1 > best_f1:
                    best_f1 = f1
                    torch.save(model.state_dict(), DIRECT_BEST)
                    print(f"保存最佳模型，F1: {best_f1:.4f}")

    torch.save(model.state_dict(), DIRECT_LAST)
    print(f"直接训练完成，最佳 F1: {best_f1:.4f}")
    return best_f1


def main():
    train_dataloader, dev_dataloader, test_dataloader = build_dataloader()
    model = BiLSTM().to(conf.device)
    model2direct(train_dataloader, dev_dataloader, model, conf.device)

    best_model = BiLSTM().to(conf.device)
    best_model.load_state_dict(torch.load(DIRECT_BEST))
    f1, report, cm = model2eval(test_dataloader, best_model, conf.device)
    print(f"直接训练 test F1: {f1:.4f}")


if __name__ == "__main__":
    main()
