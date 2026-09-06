"""BERT 模型 int8 动态量化。

对训练好的 BERT 老师模型（bert_classification_best.pth）做后训练动态量化：
只量化 nn.Linear（embedding / LayerNorm 保持 fp32），评估量化前后的 F1 与体积变化。

关键点：
    - 动态量化是 CPU 推理，量化后的模型不能 .to(cuda)，全程在 CPU 上评估。
    - 本脚本只「读」bert_classification_best.pth，另存量化副本 bert_classification_quantized.pt，
      不覆盖任何原文件 —— 因此不影响模型蒸馏（model_distill.py 仍用 fp32 老师权重）。

运行：python model_quantize.py
"""
import os

import torch
import torch.quantization as quant

from config import Config
from utils import build_dataloader
from bert_classifier import TMFBertClassifier
from train import model2eval

conf = Config()

# 量化模型另存，避免覆盖 fp32 原权重
QUANTIZED_PATH = conf.teacher_best_model_path.replace("best.pth", "quantized.pt")


def main():
    _, _, test_dataloader = build_dataloader()
    cpu = torch.device("cpu")

    # 1. 加载 fp32 老师模型到 CPU（map_location 防止 cuda 保存的权重回放到 GPU）
    model = TMFBertClassifier()
    model.load_state_dict(torch.load(conf.teacher_best_model_path, map_location="cpu"))
    model.eval()

    # 2. 量化前评估（公平对比：同一设备、同一数据）
    f1_before, _, _ = model2eval(test_dataloader, model, cpu)
    print(f"量化前 test F1: {f1_before:.4f}")

    # 3. 动态量化（只量化 Linear 层）
    quantized = quant.quantize_dynamic(model, {torch.nn.Linear}, dtype=torch.qint8)

    # 4. 量化后评估
    f1_after, _, _ = model2eval(test_dataloader, quantized, cpu)
    print(f"量化后 test F1: {f1_after:.4f}")
    print(f"F1 损失: {f1_before - f1_after:.4f}")

    # 5. 保存量化模型（存整个对象，含量化参数 scale/zero_point）
    torch.save(quantized, QUANTIZED_PATH)

    # 6. 体积对比
    size_before = os.path.getsize(conf.teacher_best_model_path)
    size_after = os.path.getsize(QUANTIZED_PATH)
    print(f"体积: {size_before / 1e6:.1f}MB -> {size_after / 1e6:.1f}MB "
          f"(约 {size_before / size_after:.2f}x 压缩)")


if __name__ == "__main__":
    main()
