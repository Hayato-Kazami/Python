from config import Config
from tqdm import tqdm
from torch.utils.data import Dataset, DataLoader
import torch

conf = Config()

def load_raw_data(file_path):
    """
    函数功能: 从指定文本文件中加载数据, 处理成'文本内容-标签索引'的元组列表, 供后续数据集封装使用.
    :param file_path: 原始数据文件路径. 文件内容(每行数据)格式为: '文本\t标签'
    :return:
        list: 元素为元组形式, 格式为: [('文本标题', '标签索引'), ('文本标题', '标签索引'), ...]
        例如: [('体验2D 巅峰 倚天屠龙记十大创新概览', 8), ('六月触发考研“多米诺”--统考专业课指导', 3), ...]
    """
    raw_data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in tqdm(f.readlines(), desc='Loading raw data...'):
            # 去除换行符
            line = line.strip()

            # 去除空行
            if not line:
                continue

            # 获取文本和标签
            text, label = line.split('\t',1)

            # 将标签加入列表中
            raw_data.append((text, int(label)))

    return raw_data

# 自定义的数据集类, 封装"文本-标签"数据, 使PyTorch的DataLoader能批量加载.
class TMFDataset(Dataset):
    """
自定义的数据集类, 封装"文本-标签"数据, 使PyTorch的DataLoader能批量加载.
我们自定义的数据集类的作用: 将原始数据(load_raw_data函数的输出结果) 转换为DataLoader可识别的格式.
    """
    def __init__(self, raw_data):
        self.raw_data = raw_data

    def __len__(self):
        return len(self.raw_data)
    def __getitem__(self, item):
        return self.raw_data[item] # 返回元组形式的文本和标签

# 定义数据集的collate_fn函数, 用于批量加载数据
def collate_fn(batch):
    """
    函数功能: 将批量加载的数据转换为PyTorch的Tensor格式.
    :param batch: 批量数据, 元素为元组形式, 格式为: [('文本标题', '标签索引'), ('文本标题', '标签索引'), ...]
    :return:
        包含三个元素的元组, 格式为:
        input_ids: 批量文本的输入ID, 形式为: (batch_size, max_len)
        attention_mask: 批量文本的注意力掩码, 形式为: (batch_size, max_len)
        labels: 批量文本的标签, 形式为: (batch_size)
    """

    # 获取批量数据中的文本和标签
    texts, labels = zip(*batch)

    # 将文本和标签转换为Tensor格式
    input = conf.tokenizer(texts, 
                           padding="max_length",
                           max_length=conf.max_len,
                           truncation=True,
                          return_tensors="pt")
    input_ids = input['input_ids']
    attention_mask = input['attention_mask']
    labels = torch.tensor(labels)

    return input_ids, attention_mask, labels

# 构建数据集加载器
def build_dataloader():
    """
    函数功能: 构建训练集、验证集和测试集的DataLoader加载器.
    :return:
        包含三个Dataloader对象的元组, 格式为:
        (train_dataloader, dev_dataloader, test_dataloader)
    """
    # 加载原始数据
    train_data = load_raw_data(conf.train_data_path)
    dev_data = load_raw_data(conf.dev_data_path)
    test_data = load_raw_data(conf.test_data_path)

    # 构建数据集
    train_dataset = TMFDataset(train_data)
    dev_dataset = TMFDataset(dev_data)
    test_dataset = TMFDataset(test_data)

    # 构建DataLoader加载器
    train_dataloader = DataLoader(train_dataset, 
                                     batch_size=conf.batch_size,
                                     shuffle=True,
                                     collate_fn=collate_fn)
    dev_dataloader = DataLoader(dev_dataset, 
                                    batch_size=conf.batch_size,
                                    shuffle=False,
                                    collate_fn=collate_fn)
    test_dataloader = DataLoader(test_dataset, 
                                    batch_size=conf.batch_size,
                                    shuffle=False,
                                    collate_fn=collate_fn)
    return train_dataloader, dev_dataloader, test_dataloader

def main():
    from bert_classifier import TMFBertClassifier

    # 构建数据集加载器
    train_dataloader, dev_dataloader, test_dataloader = build_dataloader()

    # 实例化模型
    model = TMFBertClassifier().to(conf.device)

  

if __name__ == '__main__':
    train_dataloader, dev_dataloader, test_dataloader = build_dataloader()
    for idx, (input_ids, attention_mask, labels) in tqdm(enumerate(train_dataloader), desc='Loading data...', total=len(train_dataloader)):
        print(input_ids)
        print(attention_mask)
        print(labels)
        break