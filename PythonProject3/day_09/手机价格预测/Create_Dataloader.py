import numpy as np
import torch
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
from torch.utils.data import TensorDataset, DataLoader

def load_data(batch_size):
    # 读取数据
    data = pd.read_csv('./dataset/手机价格预测.csv')
    # 特征选择
    x, y = data.iloc[:, :-1], data.iloc[:, -1]
    # 数据集划分（stratify 保证各类别在训练/测试集中比例一致）
    x_train, x_test, y_train, y_test = train_test_split(
        x.values, y.values, test_size=0.2, random_state=42, stratify=y.values)

    # 特征标准化：不同特征量纲差异极大，不标准化网络很难收敛、精度上不去
    scaler = StandardScaler()
    x_train = scaler.fit_transform(x_train)
    x_test = scaler.transform(x_test)

    # 将数据转换为 torch.tensor（标签必须是 long 类型，CrossEntropyLoss 才能正常工作）
    train_dataset = TensorDataset(
        torch.tensor(x_train, dtype=torch.float32),
        torch.tensor(y_train, dtype=torch.long))
    test_dataset = TensorDataset(
        torch.tensor(x_test, dtype=torch.float32),
        torch.tensor(y_test, dtype=torch.long))

    # 构建数据加载器（测试集不需要打乱）
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

    # 返回训练集、测试集、特征数、标签数
    return train_loader, test_loader, x.shape[1], len(np.unique(y))
