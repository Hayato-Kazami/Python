import torch

class Jay_Chou(torch.utils.data.Dataset):
    def __init__(self, corpus_ids, max_len):
        self.corpus_ids = corpus_ids
        self.max_len = max_len
        # 语料长度
        self.corpus_len = len(self.corpus_ids)
        # 句子数量
        self.sentences_num = self.corpus_len // self.max_len

    def __len__(self):
        return self.sentences_num

    def __getitem__(self, item):
        idx = item * self.max_len
        # 修正负索引
        idx = max(0, idx)
        # 修正超限索引
        idx = min(idx, self.corpus_len - self.max_len - 2)

        x = self.corpus_ids[idx:idx + self.max_len]
        y = self.corpus_ids[idx + 1:idx + self.max_len + 1]
        return torch.tensor(x), torch.tensor(y)

if __name__ == '__main__':
    from build_vocab import build_vocab

    unique_words, vocab_dict, corpus, vocab_size = build_vocab()
    dataset = Jay_Chou(corpus, 32)
    x1, y1 = dataset[10000000]
    print(x1)
    print(y1)
    