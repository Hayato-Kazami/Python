import torch
# 打印出正在使用的PyTorch和CUDA版本。
print(torch.__version__)
print(torch.version.cuda)

# 测试GPU是否生效
print(torch.cuda.is_available())