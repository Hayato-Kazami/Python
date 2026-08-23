import torch.nn as nn
import torch

dropout = nn.Dropout(p=0.8)

x = torch.randint(0, 10, (2, 3)).float() 

print(x)
print(dropout(x))
