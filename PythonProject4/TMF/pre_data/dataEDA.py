import sys
from pathlib import Path
import pandas as pd
from collections import Counter

# 把 TMF 项目根目录加入 sys.path，使 `from data.config import Config` 在任何目录下运行都能导入
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from pre_data.config import Config
conf = Config()

# 获取数据
data = pd.read_csv(conf.train_data_path,
                    sep='\t',
                    names=['text', 'label'])
print(f'训练集样本总数：{len(data)}')

print(data.head(10))

# 统计每个标签的样本数
label_counts = Counter(data['label'])
print(label_counts)

with open(conf.class_data_path, 'r', encoding='utf-8') as f:
    class_names = f.read().split('\n')

for type, count in label_counts.items():
    print(f'标签 {type} 的样本数：{count}')

# 统计每个标签的文本长度
data['text_length'] = data['text'].str.len()
