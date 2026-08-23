# MAE损失(L1 Loss)
import torch
y_pre = torch.tensor([[90.], [80.], [70.]])
y_true = torch.tensor([[95.], [85.], [75.]])

L1_loss = torch.nn.L1Loss()
loss = L1_loss(y_pre, y_true)
print(loss)  # 5.0