import torch
import torch.nn as nn
from torchsummary import summary

class Model(nn.Module):
    def __init__(self):
        super().__init__()
        # 隐藏层1: 6 → 16
        self.linear1 = nn.Linear(6, 16)
        nn.init.kaiming_normal_(self.linear1.weight)
        nn.init.zeros_(self.linear1.bias)

        # 隐藏层2: 16 → 32
        self.linear2 = nn.Linear(16, 32)
        nn.init.kaiming_normal_(self.linear2.weight)
        nn.init.zeros_(self.linear2.bias)

        # 输出层: 32 → 8（8分类）
        self.out = nn.Linear(32, 8)
        nn.init.xavier_normal_(self.out.weight)
        nn.init.zeros_(self.out.bias)

    def forward(self, x):      # (N, 6)
        x = self.linear1(x)    # (N, 6) @ (6, 16) = (N, 16)
        x = torch.relu(x)

        x = self.linear2(x)    # (N, 16) @ (16, 32) = (N, 32)
        x = torch.relu(x)

        logits = self.out(x)   # (N, 32) @ (32, 8) = (N, 8)
        return logits           # 不经过 softmax，CrossEntropyLoss 内置了


if __name__ == '__main__':
    model = Model()

    # 模拟数据: 4 个样本，每个 6 个特征
    x = torch.randn(4, 6)
    out = model(x)
    print("输出 logits:", out)
    print("输出形状:", out.shape)   # (4, 8) → 4个样本，每行8个类的得分

    # 损失计算
    y_true = torch.randint(0, 8, (4,))   # 随机4个标签，范围0~7
    loss_fn = nn.CrossEntropyLoss()
    loss = loss_fn(out, y_true)
    print("损失值:", loss.item())

    # 模型结构
    summary(model, input_size=(6,), batch_size=4, device='cpu')
    print(model.named_parameters())
    for name, param in model.named_parameters():
        print(name, param, param.shape)