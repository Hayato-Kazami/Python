from matplotlib import pyplot as plt
import torch
from sklearn.datasets import make_regression
from torch.utils.data import TensorDataset, DataLoader
import torch.nn as nn
from torch.optim import SGD

# 生成数据集
def get_data():
    x, y, coef = make_regression(n_samples=1000, 
                                n_features=1, 
                                noise=10,
                                bias=7,
                                coef=True)

    x = torch.tensor(x, dtype=torch.float32)
    y = torch.tensor(y, dtype=torch.float32)
    return x, y, coef

if __name__ == "__main__":
    # 获取数据
    x, y, coef = get_data()
    print(x,y,coef)
    print(x.shape,y.shape)

    # 创建数据集和数据加载器
    mydataset = TensorDataset(x, y)
    mydataloader = DataLoader(mydataset, batch_size = 32,shuffle = True)

    # 定义模型
    model = nn.Linear(1,1)

    # 构建损失函数和优化器
    loss = nn.MSELoss()
    optimizer = SGD(model.parameters(), lr=0.5)

    # 训练模型
    # 定义训练次数
    epochs = 100
    epoch_loss = []
    # 遍历训练次数
    for epoch in range(epochs):
        # 定义训练监控日志
        total_loss, total_nums = 0.0,0
        # 遍历数据集
        for x_batch, y_batch in mydataloader:
            # 前向传播
            y_pred = model(x_batch)
            # 计算损失
            loss_value = loss(y_pred, y_batch.unsqueeze(1))
            # 梯度清零
            optimizer.zero_grad()
            # 反向传播
            loss_value.backward()
            # 更新参数
            optimizer.step()
            # 更新训练监控日志
            total_loss += loss_value.item()
            total_nums += 1
        epoch_loss.append(total_loss/total_nums)
        # print(f"Epoch {epoch+1}, Loss: {total_loss/total_nums:.4f}")

    # 模型评估
    # 绘制预测结果
    plt.plot(range(1, epochs+1),epoch_loss)
    plt.title('Loss')
    plt.show()

    # 绘制线性回归曲线
    x_rel = torch.linspace(x.min(), x.max(), 1000)
    y_prd = model(x_rel.unsqueeze(1)).detach()
    y_rel = x_rel * coef + 7
    plt.scatter(x, y)
    plt.plot(x_rel, y_prd, color='red', label='Predicted')
    plt.plot(x_rel, y_rel, color='blue', label='True')
    plt.grid()
    plt.legend()
    plt.show()