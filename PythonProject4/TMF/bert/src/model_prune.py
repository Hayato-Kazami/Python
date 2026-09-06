import torch
from torch.nn.utils import prune
from utils import build_dataloader
from bert_classifier import TMFBertClassifier
from config import Config
from train import model2eval
conf = Config()

# 模型稀疏度函数
def prune_model_sparsity(model):
    # 获取模型中的所有参数
    total_params 