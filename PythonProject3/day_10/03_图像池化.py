import torch.nn
import matplotlib.pyplot as plt
import numpy as np
img = plt.imread('./data/img.jpg')
print(img.shape)  
fig, ax = plt.subplots(2, 2)
ax[0, 0].imshow(img)

# 实例化最大/平均池化层
max_pool = torch.nn.MaxPool2d(kernel_size=5, stride=3)
avg_pool = torch.nn.AvgPool2d(kernel_size=5, stride=3)

# 进行池化操作
# 最大池化
img_pool = torch.tensor(img).permute(2, 0, 1).unsqueeze(0)
out_max_pool = max_pool(img_pool)
out_max_pool = out_max_pool.squeeze(0).permute(1, 2, 0)
ax[0, 1].imshow(out_max_pool)

# 平均池化
out_avg_pool = avg_pool(img_pool.float())
out_avg_pool = out_avg_pool.squeeze(0).permute(1, 2, 0).long()
ax[1, 0].imshow(out_avg_pool)

plt.show()