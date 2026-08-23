from torch.utils.data import DataLoader
from torchvision.transforms import ToTensor
from torchvision.datasets import CIFAR10
import matplotlib.pyplot as plt
from torchvision import transforms

def load_data(bs):
    # CIFAR-10 每个通道的均值和标准差（官方统计值）
    mean = (0.4914, 0.4822, 0.4465)
    std  = (0.2023, 0.1994, 0.2010)
    # 训练集：随机裁剪 + 水平翻转（数据增强，防止过拟合）+ 归一化
    transform_train = transforms.Compose([
        transforms.RandomCrop(32, padding=4),      # 四周补 4 像素再随机裁回 32，相当于平移
        transforms.RandomHorizontalFlip(),         # 随机左右翻转
        transforms.ToTensor(),
        transforms.Normalize(mean, std),           # 归一化
    ])

    # 测试集：只归一化，不做增强（要和训练集用同样的 mean/std）
    transform_test = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean, std),
    ])
    # 获取数据集对象
    # root: 数据集的根目录
    # train: 是否为训练集
    # download: 是否下载数据集
    # transform: 数据预处理操作，如转换为张量等
    # ToTensor: 将图像转换为张量
    train_dataset = CIFAR10(root='./data', train=True, download=True, transform=transform_train)
    test_dataset = CIFAR10(root='./data', train=False, download=True, transform=transform_test)
    # 构建数据加载器
    train_loader = DataLoader(train_dataset, batch_size=bs, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=bs, shuffle=False)

    return train_dataset,test_dataset,train_loader, test_loader

if __name__ == '__main__':
    train_dataset,test_dataset,train_loader, test_loader = load_data(2)
    # 打印数据集信息
    print(train_dataset.class_to_idx)
    # 打印数据集的形状和类型
    print(train_dataset.data.shape)
    print(type(train_dataset.data))
    # 打印数据集的标签和数量
    print(len(train_dataset.targets))
    # 打印数据集的第0个样本的标签和图像
    print(train_dataset.targets[0])
    data0 = train_dataset.data[0]
    plt.imshow(data0)
    plt.show()

    for x_train, y_train in train_loader:
        print(x_train.shape)
        print(x_train.dtype)
        print(y_train.shape)
        print(y_train.dtype)
        break
        
