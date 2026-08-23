import torch

y_pred = torch.tensor([[0.8, 0.2, 0.5],[0.3, 0.7, 0.1],[0.6, 0.4, 0.5]])
y_true = torch.tensor([[1.0, 1.0, 0.0],[0.0, 1.0, 1.0],[1.0, 0.0, 0.0]])

loss = torch.nn.BCELoss()
lossf = loss(y_pred, y_true)
print(lossf)  