"""知识蒸馏：BERT 老师 → BiLSTM 学生（剧透二分类）。

软标签（KL 散度）+ 硬标签（交叉熵）联合训练，温度 T、权重 alpha。
与 model_direct.py 对照，量化「知识蒸馏」带来的增益。

运行：python model_distill.py  （需先跑 train.py 得到老师模型）
"""
from matplotlib import pyplot as plt
import torch
from utils import build_dataloader
from model import SpoilerBertClassifier
from student_model import BiLSTM
from torch.nn import CrossEntropyLoss, KLDivLoss
from config import Config
from train import model2eval
from tqdm import tqdm

conf = Config()


def model2distill(train_loader, dev_loader, teacher_model, student_model, device):
    soft_loss = KLDivLoss(reduction='batchmean')
    hard_loss = CrossEntropyLoss()
    optimizer = torch.optim.AdamW(student_model.parameters(), lr=conf.student_lr)

    T = conf.temperature
    alpha = conf.alpha

    total_iters = 0
    loss_list = []
    iter_list = []
    best_f1 = 0.

    for epoch in range(conf.epochs):
        teacher_model.eval()
        student_model.train()

        for i, (input_ids, attention_mask, labels) in enumerate(
                tqdm(train_loader, total=len(train_loader), desc="模型蒸馏中")):
            input_ids = input_ids.to(device)
            attention_mask = attention_mask.to(device)
            labels = labels.to(device)

            with torch.no_grad():
                teacher_logits = teacher_model(input_ids, attention_mask)

            student_logits = student_model(input_ids, attention_mask)

            soft_losses = soft_loss(torch.log_softmax(student_logits / T, dim=-1),
                                    torch.softmax(teacher_logits / T, dim=-1).detach())
            hard_losses = hard_loss(student_logits, labels)
            loss = alpha * soft_losses * T ** 2 + (1 - alpha) * hard_losses

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            total_iters += 1
            avg_loss = (loss_list[-1] + abs(loss.item())) / 2 if loss_list else abs(loss.item())
            if (i + 1) % 30 == 0 or i + 1 == len(train_loader):
                print(f"\nEpoch {epoch+1}, Iter {i+1}/{len(train_loader)}, Loss: {avg_loss:.4f}")
            loss_list.append(avg_loss)
            iter_list.append(total_iters)

            with open(conf.log_path, 'a', encoding='utf-8') as f:
                f.write(f"Epoch {epoch+1}, Iter {i+1}/{len(train_loader)}, Loss: {avg_loss:.4f}\n")

            if total_iters % 150 == 0:
                f1, report, cm = model2eval(dev_loader, student_model, device)
                print(f"\nEpoch {epoch+1}, Iter {i+1}/{len(train_loader)}, F1 Score: {f1:.4f}")
                if f1 > best_f1:
                    best_f1 = f1
                    torch.save(student_model.state_dict(), conf.student_best_model_path)
                student_model.train()

    torch.save(student_model.state_dict(), conf.student_last_model_path)
    print(f'蒸馏完成，最佳 F1: {best_f1:.4f}')

    plt.plot(iter_list, loss_list)
    plt.title('Loss')
    plt.xlabel('Iterations')
    plt.ylabel('Loss')
    plt.savefig('./loss.png')


def main():
    train_dataloader, dev_dataloader, test_dataloader = build_dataloader()
    teacher_model = SpoilerBertClassifier().to(conf.device)
    teacher_model.load_state_dict(torch.load(conf.best_model_path))
    student_model = BiLSTM().to(conf.device)
    model2distill(train_dataloader, dev_dataloader, teacher_model, student_model, conf.device)

    best_student_model = BiLSTM().to(conf.device)
    best_student_model.load_state_dict(torch.load(conf.student_best_model_path))
    f1, report, confmat = model2eval(test_dataloader, best_student_model, conf.device)
    print(f"蒸馏 test F1: {f1:.4f}")
    print(report)
    print(confmat)


if __name__ == '__main__':
    main()
