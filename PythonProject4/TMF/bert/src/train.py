import torch
from config import Config
from utils import build_dataloader
from bert_classifier import TMFBertClassifier
from torch.nn import CrossEntropyLoss
from tqdm import tqdm
from torch.optim import AdamW
from sklearn.metrics import f1_score,classification_report,confusion_matrix
conf = Config()

# 定义模型训练函数
def model2train(train_dataloader, dev_dataloader, model, device):
    # 定义损失函数和优化器
    loss_fn = CrossEntropyLoss()
    optimizer = AdamW(model.parameters(), lr=conf.lr)

    # 最优分数和总迭代次数
    best_f1 = 0
    total_iters = 0
    # 训练循环
    for epoch in range(conf.epochs):
        total_loss = 0. # 初始化当前迭代总损失
        total_iter_epoch = 0. # 初始化当前轮次总迭代次数

        # 将模型设置为训练模式
        model.train()

        for i, (input_ids, attention_mask, labels) in tqdm(enumerate(train_dataloader),
                                                           total=len(train_dataloader),
                                                           desc= f"模型训练中，当前轮次为：{epoch+1}"):
            # 将数据移动到设备上
            input_ids = input_ids.to(device)
            attention_mask = attention_mask.to(device)
            labels = labels.to(device)
            # 前向传播
            logits = model(input_ids, attention_mask)
           # 计算损失
            loss = loss_fn(logits, labels)
            # 反向传播和优化
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            # 记录训练监控信息
            total_loss += loss.item()
            total_iter_epoch += 1
            total_iters += 1

            # 每20个迭代打印一次当前轮次的平均损失
            if (i+1) % 20 == 0:
                avg_loss = total_loss / total_iter_epoch
                print(f"当前轮次：{epoch+1}，当前迭代：{i+1}，平均损失：{avg_loss:.4f}")
                # 保存训练日志
                with open(conf.log_path, 'a', encoding='utf-8') as f:
                    f.write(
                        f"当前轮次：{epoch+1}，当前迭代：{i+1}，平均损失：{avg_loss:.4f}\n"
                    )
            # 每500个迭代进行一次验证,保存最优模型
            if (i+1) % 500 == 0 or i+1 == len(train_dataloader):
                f1, report, cm = model2eval(dev_dataloader, model, device)
                model.train()
                if f1 > best_f1:
                    best_f1 = f1
                    torch.save(model.state_dict(), conf.teacher_best_model_path)
                print(f"当前轮次：{epoch+1}，当前迭代：{i+1}，最优分数：{best_f1:.4f}")
           # 保存验证日志
                with open(conf.log_path, 'a', encoding='utf-8') as f:
                    f.write(f"当前轮次：{epoch+1}，当前迭代：{i+1}，最优分数：{best_f1:.4f}\n")
                    f.write(f"验证报告：{report}\n")
                    f.write(f"混淆矩阵：{cm}\n")
    # 保存模型
    torch.save(model.state_dict(), conf.teacher_last_model_path)

def model2eval(dev_dataloader, model, device):
    # 将模型设置为评估模式
    model.eval()
    y_pred_list, y_true_list = [], []

    with torch.no_grad():
        for input_ids, attention_mask, labels in tqdm(dev_dataloader,
                                                        total=len(dev_dataloader),
                                                        desc="模型验证中"):
            # 将数据移动到设备上
            input_ids = input_ids.to(device)
            attention_mask = attention_mask.to(device)
            labels = labels.to(device)
            # 前向传播
            logits = model(input_ids, attention_mask)
            # 获取预测结果
            y_pred = torch.argmax(logits, dim=-1)
            y_pred_list.extend(y_pred.tolist())
            y_true_list.extend(labels.tolist())

        # 计算评估指标
        f1 = f1_score(y_true_list, y_pred_list, average='weighted', zero_division=0)
        report = classification_report(y_true_list, y_pred_list, zero_division=0)
        cm = confusion_matrix(y_true_list, y_pred_list)
        return f1, report, cm

def main():
    # 加载数据集
    train_dataloader, dev_dataloader, test_dataloader = build_dataloader()
    # 加载模型
    model = TMFBertClassifier().to(conf.device)
    # 训练模型
    model2train(train_dataloader, dev_dataloader, model, conf.device)
    # 模型评估
    model_best = TMFBertClassifier().to(conf.device)
    model_best.load_state_dict(torch.load(conf.teacher_best_model_path))
    f1_best, report_best, cm_best = model2eval(test_dataloader, model_best, conf.device)
    print(f"最优分数：{f1_best:.4f}")
    print("最优报告：")
    print(report_best)
    print("最优混淆矩阵：")
    print(cm_best)
    # 保存评估结果
    with open(conf.log_path, 'a', encoding='utf-8') as f:
        f.write(f"最优分数：{f1_best:.4f}\n")
        f.write("最优报告：")
        f.write(report_best)
        f.write("最优混淆矩阵：")
        f.write(str(cm_best))

if __name__ == '__main__':
    main()
