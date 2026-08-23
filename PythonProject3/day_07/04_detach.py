import numpy as np
import torch

w = torch.tensor(10., requires_grad=True)

w1 = w.detach()

np_w = w1.numpy()

print(np_w)  