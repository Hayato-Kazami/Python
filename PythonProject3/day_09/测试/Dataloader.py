import torch
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from torch.utils.data import DataLoader, TensorDataset

def load_data(batch_size):
    # 读取数据
    data = pd.read_csv('./dataset/手机价格预测.csv') # DataFrame类型的数据
    # 数据预处理
    # 分离特征和标签
    # x 取所有的行，除了最后一列（特征）
    # y 取所有的行和最后一列（标签）
    x, y = data.iloc[:, :-1], data.iloc[:, -1]
    # 数据集划分,stratify=y.values表示按y的值进行划分，保证每个类别的样本比例一致
    x_train, x_test, y_train, y_test = train_test_split(
        x.values, y.values, test_size=0.2, random_state=42,stratify=y.values)
    #  特征标准化，不同特征量纲差异极大，不标准化网络很难收敛、精度上不去
    #  用均值和标准差对数据进行标准化处理，使得数据的均值为0，标准差为1，即x=(x-mean)/std
    scaler = StandardScaler()
    x_train = scaler.fit_transform(x_train)
    x_test = scaler.transform(x_test)

    # 将数据转换为TensorDataset
    train_dataset = TensorDataset(torch.tensor(x_train, dtype=torch.float32),
                                  torch.tensor(y_train, dtype=torch.long))
    test_dataset = TensorDataset(torch.tensor(x_test, dtype=torch.float32),
                                torch.tensor(y_test, dtype=torch.long))

    # 创建Dataloader，用于批量加载数据集
    # shuffle=True表示每次加载数据集时打乱顺序，shuffle=False表示每次加载数据集时保持顺序不变
    # batch_size表示每次加载的数据量
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

    # 返回训练和测试数据集的Dataloader,特征数量和标签类别数
    return train_loader, test_loader, x.shape[1], len(np.unique(y))