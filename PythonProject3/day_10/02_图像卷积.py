import torch
import matplotlib.pyplot as plt

img = plt.imread('./data/img.jpg')
print(img.shape)  

# 构建卷积层
conv = torch.nn.Conv2d(in_channels=3, out_channels=3, kernel_size=3, stride=2, padding=0)
# 图像送入卷积层
img_tensor = torch.tensor(img).permute(2, 0, 1).unsqueeze(0)  
print(img_tensor.shape)  

out = conv(img_tensor.float())

print(out.shape)  

out_img = out.squeeze(0).permute(1, 2, 0).long()
plt.imshow(out_img.detach())
plt.show()