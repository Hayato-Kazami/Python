"""数据加载：读「文本\\t标签」格式，构建 DataLoader（剧透强不平衡，用类别平衡采样）。"""
from collections import Counter

import torch
from torch.utils.data import Dataset, DataLoader, WeightedRandomSampler
from tqdm import tqdm

from config import Config

conf = Config()


def load_raw_data(file_path):
    """从「文本\\t标签」文件加载数据，返回 [(text, int_label), ...]。"""
    raw_data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in tqdm(f.readlines(), desc='Loading raw data...'):
            line = line.strip()
            if not line:
                continue
            text, label = line.split('\t', 1)
            raw_data.append((text, int(label)))
    return raw_data


class TMFDataset(Dataset):
    def __init__(self, raw_data):
        self.raw_data = raw_data

    def __len__(self):
        return len(self.raw_data)

    def __getitem__(self, item):
        return self.raw_data[item]


def collate_fn(batch):
    texts, labels = zip(*batch)
    input = conf.tokenizer(texts, padding="max_length", max_length=conf.max_len,
                           truncation=True, return_tensors="pt")
    return input['input_ids'], input['attention_mask'], torch.tensor(labels)


def build_dataloader():
    train_data = load_raw_data(conf.train_data_path)
    dev_data = load_raw_data(conf.dev_data_path)
    test_data = load_raw_data(conf.test_data_path)

    train_dataset = TMFDataset(train_data)
    dev_dataset = TMFDataset(dev_data)
    test_dataset = TMFDataset(test_data)

    # 剧透是少数类，类别平衡采样提高其被抽中概率
    labels = [l for _, l in train_data]
    class_counts = Counter(labels)
    sample_weights = [1.0 / class_counts[l] for l in labels]
    sampler = WeightedRandomSampler(sample_weights, num_samples=len(sample_weights),
                                    replacement=True)

    train_dataloader = DataLoader(train_dataset, batch_size=conf.batch_size,
                                  sampler=sampler, collate_fn=collate_fn)
    dev_dataloader = DataLoader(dev_dataset, batch_size=conf.batch_size,
                                shuffle=False, collate_fn=collate_fn)
    test_dataloader = DataLoader(test_dataset, batch_size=conf.batch_size,
                                 shuffle=False, collate_fn=collate_fn)
    return train_dataloader, dev_dataloader, test_dataloader
