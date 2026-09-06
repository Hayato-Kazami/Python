from matplotlib import pyplot as plt
import torch
from utils import build_dataloader
from bert_classifier import TMFBertClassifier
from student_model import BiLSTM
from torch.nn import CrossEntropyLoss,KLDivLoss
from config import Config
from train import model2eval
from tqdm import tqdm
conf = Config()

def model2distill(train_loader, dev_loader, teacher_model, student_model, device):
    # 构建损失函数和优化器
    soft_loss = KLDivLoss(reduction='batchmean')
    hard_loss = CrossEntropyLoss()
    optimizer = torch.optim.AdamW(student_model.parameters(), lr=conf.student_lr)

    # 获取蒸馏模型的参数
    T = conf.temperature
    alpha = conf.alpha

    # 总训练步数和训练时间和总损失
    total_iters = 0
    start_time = 0
    loss_list = []
    iter_list = []
    best_f1 = 0.

    # 训练模型
    for epoch in range(conf.epochs):
        # 将老师模型设置为评估模式
        teacher_model.eval()
        # 将学生模型设置为训练模式
        student_model.train()

        # 每个epoch开始时，重置总损失
        total_loss_epoch = 0

        # 训练循环
        for i,(input_ids, attention_mask, labels) in enumerate(
                                                    tqdm(train_loader,
                                                         total=len(train_loader),
                                                         desc=f"模型蒸馏中")):
            input_ids = input_ids.to(device)
            attention_mask = attention_mask.to(device)
            labels = labels.to(device)

            # 获取老师模型的输出
            with torch.no_grad():
                teacher_logits = teacher_model(input_ids, attention_mask)

            # 获取学生模型的输出
            student_logits = student_model(input_ids, attention_mask)

            # 计算软损失
            soft_losses = soft_loss(torch.log_softmax(student_logits / T, dim=-1), 
                                    torch.softmax(teacher_logits / T, dim=-1).detach())
            
            # 计算硬损失
            hard_losses = hard_loss(student_logits, labels)

            # 计算总损失
            loss = alpha * soft_losses * T ** 2 + (1 - alpha) * hard_losses

            # 梯度清零
            optimizer.zero_grad()

            # 反向传播
            loss.backward()

            # 更新参数
            optimizer.step()

            # 记录总损失和训练步数
            total_loss_epoch += abs(loss.item())
            total_iters += 1

            # 每30步或批次末尾，打印当前损失
            avg_loss = total_loss_epoch / (i+1)
            if (i+1) % 30 == 0 or i+1 == len(train_loader):
                print(f"\nEpoch {epoch+1}, Iter {i+1}/{len(train_loader)}, Loss: {avg_loss:.4f}")
            loss_list.append(avg_loss)
            iter_list.append(total_iters)

            # 保存训练日志
            with open(conf.log_path, 'a', encoding='utf-8') as f:
                f.write(f"Epoch {epoch+1}, Iter {i+1}/{len(train_loader)}, Loss: {avg_loss:.4f}\n")

            # 每150步评估模型并保存最佳模型
            if total_iters % 150 == 0:
                f1, report, cm = model2eval(dev_loader, student_model, device)
                print(f"\nEpoch {epoch+1}, Iter {i+1}/{len(train_loader)}, F1 Score: {f1:.4f}")
                # 如果当前F1分数高于最佳F1分数，则保存最佳模型
                if f1 > best_f1:
                    best_f1 = f1
                    torch.save(student_model.state_dict(), conf.student_best_model_path)
                    with open(conf.log_path, 'a', encoding='utf-8') as f:
                        f.write(f"保存最佳模型，F1 Score: {best_f1:.4f}\n")

                with open(conf.log_path, 'a', encoding='utf-8') as f:
                    f.write(f"Epoch {epoch+1}, Iter {i+1}/{len(train_loader)}, F1 Score: {f1:.4f}\n")
                    f.write(f"Classification Report:\n{report}\n")
                    f.write(f"Confusion Matrix:\n{cm}\n")

                # 将学生模型设置为训练模式
                student_model.train()

    # 4.模型保存
    torch.save(student_model.state_dict(), conf.student_last_model_path)
    print(f'模型保存成功，f1:{best_f1:.4f}')
    with open(conf.log_path, 'a', encoding='utf-8') as f:
        f.write(f'模型保存成功，f1:{best_f1:.4f}\n')

    plt.plot(iter_list, loss_list)
    plt.title('Loss')
    plt.xlabel('Iterations')
    plt.ylabel('Loss')
    plt.savefig('./loss.png')
    plt.show()

def main():
    # 1. 获取数据和数据预处理
    train_dataloader, dev_dataloader, test_dataloader = build_dataloader()
    # 2.加载模型
    # 2.1 加载老师模型
    teacher_model = TMFBertClassifier().to(conf.device)
    teacher_model.load_state_dict(torch.load(conf.teacher_best_model_path))
    # 2.2 加载学生模型
    student_model = BiLSTM().to(conf.device)
    # 3.模型蒸馏
    model2distill(train_dataloader, dev_dataloader, teacher_model, student_model, conf.device)

    # 4.模型评估
    # 4.1加载最优学习模型
    best_student_model = BiLSTM().to(conf.device)
    best_student_model.load_state_dict(torch.load(conf.student_best_model_path))
    f1, report, confmat = model2eval(test_dataloader, best_student_model, conf.device)
    # 5 保存评估结果
    with open(conf.log_path, 'a', encoding='utf-8') as f:
        f.write(f'test f1:{f1:.4f}\n')
        f.write(f'test report:{report}\n')
        f.write(f'test confmat:{confmat}\n')

    
if __name__ == '__main__':
    main()