"""训练剧透检测模型（BERT 二分类）。

剧透是强不平衡二分类，FocalLoss + WeightedRandomSampler 专门针对这种少数类场景。

运行：python train.py  （需先跑 label_spoiler.py + sample_spoiler.py 准备好 data/）
"""
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.optim import AdamW
from transformers import get_linear_schedule_with_warmup
from tqdm import tqdm
from sklearn.metrics import f1_score, classification_report, confusion_matrix

from config import Config
from utils import build_dataloader
from model import SpoilerBertClassifier

conf = Config()


class FocalLoss(nn.Module):
    """Focal Loss：聚焦「难分样本」（剧透少数类往往就是难分样本）。"""
    def __init__(self, gamma=2.0):
        super().__init__()
        self.gamma = gamma

    def forward(self, logits, targets):
        ce_loss = F.cross_entropy(logits, targets, reduction='none')
        pt = torch.exp(-ce_loss)
        return ((1 - pt) ** self.gamma * ce_loss).mean()


def model2eval(loader, model, device):
    model.eval()
    y_pred_list, y_true_list = [], []
    with torch.no_grad():
        for input_ids, attention_mask, labels in tqdm(loader, total=len(loader),
                                                      desc="验证中"):
            logits = model(input_ids.to(device), attention_mask.to(device))
            y_pred_list.extend(torch.argmax(logits, dim=-1).tolist())
            y_true_list.extend(labels.tolist())
    # 主指标：剧透类（少数类/正类）F1。weighted F1 会被「非剧透」主导而虚高，
    # 无法反映剧透检测的真实效果，故直接用剧透类 F1 作为选模型的依据。
    f1 = f1_score(y_true_list, y_pred_list, average='binary', pos_label=1,
                  zero_division=0)
    report = classification_report(y_true_list, y_pred_list, zero_division=0,
                                   target_names=conf.class_list)
    cm = confusion_matrix(y_true_list, y_pred_list)
    return f1, report, cm


def model2train(train_loader, dev_loader, model, device):
    loss_fn = FocalLoss(gamma=2.0)
    optimizer = AdamW(model.parameters(), lr=conf.lr)
    total_steps = len(train_loader) * conf.epochs
    warmup_steps = int(total_steps * conf.warmup_ratio)
    scheduler = get_linear_schedule_with_warmup(optimizer, warmup_steps, total_steps)

    best_f1 = 0
    for epoch in range(conf.epochs):
        model.train()
        for i, (input_ids, attention_mask, labels) in tqdm(
                enumerate(train_loader), total=len(train_loader),
                desc=f"训练中，轮次 {epoch + 1}"):
            input_ids = input_ids.to(device)
            attention_mask = attention_mask.to(device)
            labels = labels.to(device)
            logits = model(input_ids, attention_mask)
            loss = loss_fn(logits, labels)
            optimizer.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optimizer.step()
            scheduler.step()

            if (i + 1) % 50 == 0 or i + 1 == len(train_loader):
                f1, report, cm = model2eval(dev_loader, model, device)
                model.train()
                if f1 > best_f1:
                    best_f1 = f1
                    torch.save(model.state_dict(), conf.best_model_path)
                print(f"轮次 {epoch + 1} 迭代 {i + 1}：最优 F1 {best_f1:.4f}")

    torch.save(model.state_dict(), conf.last_model_path)


def main():
    train_loader, dev_loader, test_loader = build_dataloader()
    model = SpoilerBertClassifier().to(conf.device)
    model2train(train_loader, dev_loader, model, conf.device)

    best = SpoilerBertClassifier().to(conf.device)
    best.load_state_dict(torch.load(conf.best_model_path))
    f1, report, cm = model2eval(test_loader, best, conf.device)
    print(f"剧透检测最优 F1：{f1:.4f}")
    print(report)
    print(cm)


if __name__ == "__main__":
    main()
