import torch
import torch.nn as nn

y_pred = torch.tensor([[10,15,-8],[4,10,12]], dtype=torch.float32)
# 标签编码
y_true = torch.tensor([0,2],dtype = torch.int64)
# 独热编码
# y_true_one_hot = torch.tensor([[1,0,0],[0,1,0]],dtype = torch.float32)

# 交叉熵损失函数
loss = nn.CrossEntropyLoss()
# 计算损失
loss_value = loss(y_pred,y_true)
print(loss_value)

