import os
import torch
from sklearn.metrics import accuracy_score
from torch.nn import CrossEntropyLoss
from torch.optim import Adam
from CNN_Model import CNN
from CNN_Dataloader import load_data

# 训练函数
def train(model, train_loader, test_loader, device):
    # 设置优化器和损失函数
    # weight_decay 是 L2 正则，抑制过拟合，让 F1 更稳,lr 是学习率
    optimizer = Adam(model.parameters(), lr=1e-3, weight_decay=1e-4)
    criterion = CrossEntropyLoss()
    # 学习率优化器
    scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
        optimizer,mode='max', patience=10, factor=0.5,)

    # 训练循环
    epochs = 30
    # 训练监控日志
    train_losses = []
    total_iters = 0
    best_acc = 0
    train_loss = 0.
    # 确保模型保存目录存在（torch.save 不会自动创建目录）
    os.makedirs('./models', exist_ok=True)
    for epoch in range(epochs):
        total_iter = 0
        # 将模型设置为训练模式
        model.train()
        for batch_idx, (x_train, y_train) in enumerate(train_loader, start=1):
            # 将数据移动到设备（GPU 或 CPU）
            x_train = x_train.to(device)
            y_train = y_train.to(device)
            # 前向传播
            y_pred = model(x_train)
            # 计算损失
            loss = criterion(y_pred, y_train)
            # 反向传播
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            # 记录损失
            train_loss += loss.item()
            total_iters += 1
            total_iter += 1
            # 每 200 个迭代和批次末尾打印一次损失
            if batch_idx % 200 == 0 or batch_idx == len(train_loader):
                avg_loss = train_loss / total_iter
                train_losses.append(avg_loss)
                print(f'Epoch [{epoch+1}/{epochs}], Iter [{total_iters}], Loss: [{avg_loss:.4f}]')
                train_loss = 0
                total_iter = 0

        # 模型评估
        acc = evaluate(model, test_loader, device)
        print(f'accuracy: {acc:.4f}')

        # 根据评估结果调整学习率
        scheduler.step(acc)

        # 保存最佳模型
        if acc > best_acc:
            best_acc = acc
            torch.save(model.state_dict(), './models/best_img_model.pth')
            print(f'Best Acc: {best_acc:.4f}, Model saved to ./models/best_img_model.pth')

    # 保存最终模型
    torch.save(model.state_dict(), './models/final_img_model.pth')
    print('Final Model saved to ./models/final_img_model.pth')

def evaluate(model, test_loader, device):
    # 将模型设置为评估模式
    model.eval()
    y_pred = []
    y_true = []
    # 遍历测试集
    with torch.no_grad():
        for x_test, y_test in test_loader:
            # 将数据移动到设备（GPU 或 CPU）
            x_test = x_test.to(device)
            y_test = y_test.to(device)
            # 前向传播
            logits = model(x_test)
            # 获取预测标签
            # torch.argmax 返回最大值的索引，即预测类别
            # logits 是模型输出的预测概率，dim=-1 表示在最后一维上求最大值和索引
            preds = torch.argmax(logits, dim=-1)
            # 将预测类别和真实类别添加到列表中
            y_pred.extend(preds.tolist())
            y_true.extend(y_test.tolist())

    # 计算准确率
    acc = accuracy_score(y_true, y_pred)
    return acc

def main():
    # 加载数据
    bs = 32
    train_dataset, test_dataset, train_loader, test_loader = load_data(bs)
    # 设置设备（GPU 或 CPU）
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    # 创建模型
    model = CNN()
    # 将模型移动到设备
    model.to(device)
    # 训练模型
    train(model, train_loader, test_loader, device)
    # 加载最佳模型
    best_model = CNN().to(device)
    best_model.load_state_dict(torch.load('./models/best_img_model.pth'))
    # 评估最佳模型
    acc = evaluate(best_model, test_loader, device)
    print(f'Best Model accuracy: {acc:.4f}')
    print('Done!')

if __name__ == '__main__':
    main()