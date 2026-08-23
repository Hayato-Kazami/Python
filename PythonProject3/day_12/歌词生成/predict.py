import torch
from build_vocab import build_vocab
from build_model import Jay_Chou_Lyrics_Generator

def predict(start_word, max_len):
    # 构建词典
    unique_words, vocab_dict, corpus, vocab_size = build_vocab()
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    # 构建模型
    model = Jay_Chou_Lyrics_Generator(vocab_size)
    model.load_state_dict(torch.load('./model/Jay_Chou_Lyrics_Generator.pth'))
    model.to(device)

    # 生成歌词
    hidden = model.init_hidden(1).to(device)
    word_idx = vocab_dict[start_word]

    res_idx = [word_idx]

    for _ in range(max_len):
        # 将word_idx转换为二维张量
        word_idx = torch.tensor([[word_idx]]).to(device)
        # 前向传播
        logits, hidden = model(word_idx, hidden)
        print(logits.shape)
        # 获取预测的单词索引,dim=-1表示在最后一维上进行最大值的索引查找
        word_idx = torch.argmax(logits, dim=-1).item()
        res_idx.append(word_idx)

    # 将索引转换为单词
    for idx in res_idx:
        print(unique_words[idx], end=' ')

if __name__ == '__main__':
    predict('你', 100)