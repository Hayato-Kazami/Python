import os
import time
import torch
from torch.nn import CrossEntropyLoss
from torch.optim import Adam
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from Dataloader import load_data
from Model import Price_Predict_Model

# 训练函数
def train(train_loader, test_loader, model, device):
    # 设置优化器和损失函数
     # weight_decay 是 L2 正则，抑制过拟合，让 F1 更稳
    optimizer = Adam(model.parameters(), lr=1e-3, weight_decay=1e-4)
    criterion = CrossEntropyLoss()
    # 实例化学习率调整器
    # 评估指标经过10个epoch不改善，学习率减半
    scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
        optimizer, mode='max', patience=10, factor=0.5,)

    # 训练循环
    epochs = 300
    # 记录训练的损失和迭代次数
    train_losses = []
    train_iters = []
    start_time = time.time()

    # 初始化最佳 F1 和最佳模型路径
    best_f1 = 0
    # 全局迭代计数器（跨 epoch 累计）
    total_iters = 0
    # 确保模型保存目录存在
    os.makedirs('./modles', exist_ok=True)

    for epoch in range(epochs):
        total_loss = 0
        total_iter = 0
        # 将模型设置为训练模式（正则化生效）
        model.train()
        for batch_idx, (x_train, y_train) in enumerate(train_loader, start=1):
            # 将数据移动到设备（GPU 或 CPU）
            x_train, y_train = x_train.to(device), y_train.to(device)

            # 前向传播
            y_pred = model(x_train)
            # 计算损失
            loss = criterion(y_pred, y_train)
            # 反向传播
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            # 记录损失和迭代次数
            total_loss += loss.item()
            total_iter += 1
            total_iters += 1

            # 每20个迭代和批次末尾
            if batch_idx % 20 == 0 or batch_idx == len(train_loader):
                # 单轮平均损失=单轮总损失/单轮迭代次数
                avg_loss = total_loss / total_iter
                # 更新训练日志
                train_losses.append(avg_loss)
                # 打印训练日志
                print(f'Epoch {epoch+1}/{epochs}, Iter {total_iters}, Loss: {avg_loss:.4f}') 
                # 清零损失和迭代次数   
                total_loss = 0
                total_iter = 0

        # 模型评估
        print('Evaluating model...')
        acc, precision, recall, f1, matrix = evaluate(test_loader, model, device)
        print(f'accuracy: {acc:.4f}')
        print(f'precision: {precision:.4f}')
        print(f'recall: {recall:.4f}')
        print(f'f1: {f1:.4f}')
        print(f'confusion matrix:\n{matrix}')

        # 更新学习率
        # f1_score经过10个epoch不改善，学习率减半
        scheduler.step(f1)

        # 保存最佳模型
        if f1 > best_f1:
            best_f1 = f1
            torch.save(model.state_dict(), './modles/best_model.pth')
            print(f'Best F1: {best_f1:.4f}, Model saved to ./modles/best_model.pth')

    # 保存最终模型
    torch.save(model.state_dict(), './modles/final_model.pth')
    print('Training completed.')

def evaluate(eva_loader, model, device):
    # 将模型设置为评估模式（正则化不生效）
    model.eval()
    # 评估模型
    y_pred = []
    y_true = []
    # 不再计算梯度
    with torch.no_grad():
        for x_test, y_test in eva_loader:
            # 将数据移动到设备（GPU 或 CPU）
            x_test, y_test = x_test.to(device), y_test.to(device)
            # 前向传播
            logits = model(x_test)
            # 获取预测类别
            # torch.argmax 返回最大值的索引，即预测类别
            # logits 是模型输出的预测概率，dim=-1 表示在最后一维上求最大值和索引
            preds = torch.argmax(logits, dim=-1)
            # 将预测类别和真实类别添加到列表中
            y_pred.extend(preds.tolist())
            y_true.extend(y_test.tolist())

    # 计算评估指标（多分类，用 macro 平均）
    acc = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, average='macro')
    recall = recall_score(y_true, y_pred, average='macro')
    f1 = f1_score(y_true, y_pred, average='macro')
    matrix = confusion_matrix(y_true, y_pred)

    return acc, precision, recall, f1, matrix

# 主函数
def main():
    # 加载数据
    batch_size = 32
    train_loader, test_loader, input_dim, output_dim = load_data(batch_size=batch_size)
    # 构建模型
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = Price_Predict_Model(input_dim, output_dim)
    model.to(device)
    # 训练模型
    train(train_loader, test_loader, model, device)
    #加载最优模型
    best_model = Price_Predict_Model(input_dim, output_dim).to(device)
    best_model.load_state_dict(torch.load('./modles/best_model.pth'))
    #评估最优模型
    acc, precision, recall, f1, matrix = evaluate(test_loader, best_model, device)
    print(f'Best F1: {f1:.4f}')
    print(f'Confusion matrix:\n{matrix}')
    print('Evaluation completed.')

if __name__ == '__main__':
    main()