import torch
import matplotlib.pyplot as plt

_,axs = plt.subplots(1,2)
grad_org = abs(torch.randn(30,)) * 20

axs[0].scatter(range(1,31),grad_org,c='r',label='original')
axs[0].plot(range(1,31),grad_org)

gard_avg = []
beta = 1.5
for i, grad in enumerate(grad_org):
    if i == 0:
        gard_avg.append(grad)
    else:
        gard_avg.append(beta * gard_avg[-1] + (1 - beta) * grad)

axs[1].scatter(range(1,31),gard_avg,c='b',label='avg')
axs[1].plot(range(1,31),gard_avg)

plt.show()
