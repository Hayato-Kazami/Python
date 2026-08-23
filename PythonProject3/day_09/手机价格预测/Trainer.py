import time
import os
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, f1_score, recall_score
import torch
from Create_Dataloader import load_data
from Create_Model import PhonePricePredictor
from torch.nn import CrossEntropyLoss
from torch.optim import Adam

# 训练函数
def model2train(train_loader, test_loader, model, device):
    # 初始化损失函数和优化器
    criterion = CrossEntropyLoss()
    # weight_decay 是 L2 正则，抑制过拟合，让 F1 更稳
    optimizer = Adam(model.parameters(), lr=0.001, weight_decay=1e-4)
    # 学习率调度：验证 F1 连续 patience 个 epoch 不提升时自动降学习率
    scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
        optimizer, mode='max', factor=0.5, patience=10)

    # 训练循环
    epochs = 300
    # 训练监控日志
    train_loss_log = []
    total_iterations = 0
    start_time = time.time()
    # 保存最优模型评估结果
    best_score = 0
    # 确保模型保存目录存在（torch.save 不会自动创建目录）
    os.makedirs('./model', exist_ok=True)

    for epoch in range(epochs):
        total_loss = 0.
        total_iterations_epoch = 0
        # 将模型设置为训练模式，让正则化生效
        model.train()
        for batch_idx, (x_train, y_train) in enumerate(train_loader, start=1):
            # 将数据移动到设备上
            x_train, y_train = x_train.to(device), y_train.to(device)

            # 前向传播
            y_pred = model(x_train)
            # 计算损失
            loss = criterion(y_pred, y_train)
            # 反向传播和优化
            optimizer.zero_grad()
            loss.backward()
            # 更新模型参数
            optimizer.step()
            # 记录损失
            total_loss += loss.item()
            total_iterations_epoch += 1
            total_iterations += 1

            # 每20个迭代或批次末尾打印一次损失
            if batch_idx % 20 == 0 or batch_idx == len(train_loader):
                avg_loss = total_loss / total_iterations_epoch
                train_loss_log.append(avg_loss)
                print(f"Epoch {epoch+1} Iteration {total_iterations} Loss: {avg_loss:.4f} time: {time.time() - start_time:.2f}s")
                total_loss = 0
                total_iterations_epoch = 0

        # 进行模型评估，保存最优模型
        print('=' * 80)
        print(f'模型开始验证...')
        acc, precision, recall, f1, matrix = model2dev(test_loader, model, device)
        print(f'acc-->{acc}')
        print(f'precision-->{precision}')
        print(f'recall-->{recall}')
        print(f'f1-->{f1}')

        # 根据当前 F1 更新学习率
        scheduler.step(f1)

        # 保存最优模型（修复：之前 best_score 一直为 0，导致每个 epoch 都保存）
        if best_score < f1:
            best_score = f1
            torch.save(model.state_dict(), "./model/best_phoneprice_model.pth")
            print(f'>>> 新最优模型已保存, best f1 = {best_score:.4f}')

    # 保存最终模型
    torch.save(model.state_dict(), "./model/last_phoneprice_model.pth")

def model2dev(dev_loader, model, device):
    # 将模型设置为评估模式，让正则化失效
    model.eval()
    # 评估模型
    y_pred = []
    y_true = []
    # 不再计算梯度
    with torch.no_grad():
        for x_test, y_test in dev_loader:
            # 将数据移动到设备上
            x_test, y_test = x_test.to(device), y_test.to(device)
            # 前向传播
            logits = model(x_test)
            preds = torch.argmax(logits, dim=-1)
            y_true.extend(y_test.tolist())
            y_pred.extend(preds.tolist())
    acc = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, average='weighted')
    f1 = f1_score(y_true, y_pred, average='weighted')
    recall = recall_score(y_true, y_pred, average='weighted')
    matrix = confusion_matrix(y_true, y_pred)
    return acc, precision, recall, f1, matrix

# 主函数
def main():
    # 加载数据
    batch_size = 32
    train_dataloader, test_dataloader, input_size, output_size = load_data(batch_size=batch_size)
    # 构建模型
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = PhonePricePredictor(input_size, output_size)
    model.to(device)
    # 训练模型
    model2train(train_dataloader, test_dataloader, model, device)
    # 加载最优模型
    best_model = PhonePricePredictor(input_size, output_size).to(device)
    best_model.load_state_dict(torch.load('./model/best_phoneprice_model.pth'))
    # 评估模型
    acc, precision, recall, f1, matrix = model2dev(test_dataloader, best_model, device)
    print(f'acc-->{acc}')
    print(f'precision-->{precision}')
    print(f'recall-->{recall}')
    print(f'f1-->{f1}')
    print('=' * 80)
    print('模型评估结束！')
    print('=' * 80)
    print('模型保存结束！')

if __name__ == "__main__":
    main()
