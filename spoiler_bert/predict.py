"""剧透检测预测：加载模型，提供单条/批量预测接口。"""
import torch

from config import Config
from model import SpoilerBertClassifier

conf = Config()

_model = None


def load_model():
    """懒加载模型（进程内缓存，只加载一次）。"""
    global _model
    if _model is None:
        _model = SpoilerBertClassifier().to(conf.device)
        _model.load_state_dict(torch.load(conf.best_model_path, map_location=conf.device))
        _model.eval()
    return _model


@torch.no_grad()
def classify_batch(texts, batch_size=64):
    """批量预测，返回 ['非剧透','剧透', ...]，顺序与输入一致。"""
    model = load_model()
    results = []
    for i in range(0, len(texts), batch_size):
        batch = texts[i:i + batch_size]
        enc = conf.tokenizer(batch, return_tensors='pt', max_length=conf.max_len,
                             padding='max_length', truncation=True)
        logits = model(enc['input_ids'].to(conf.device),
                       enc['attention_mask'].to(conf.device))
        preds = torch.argmax(logits, dim=-1).tolist()
        results.extend([conf.class_list[p] for p in preds])
    return results


def classify(text):
    return classify_batch([text])[0]


if __name__ == '__main__':
    for s in ["最后男主其实是反派", "哈哈哈哈笑死我了", "前排打卡"]:
        print(f"{s!r:20} -> {classify(s)}")
