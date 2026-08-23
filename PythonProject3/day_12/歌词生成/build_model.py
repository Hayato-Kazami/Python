import torch
import torch.nn as nn

class Jay_Chou_Lyrics_Generator(nn.Module):
    def __init__(self, vocab_size):
        super().__init__()
        # embedding层，词表大小 * 词嵌入维度
        self.embed = nn.Embedding(vocab_size, 256)
        # rnn层，词嵌入维度 * 隐藏层维度 * 隐藏层数量
        self.rnn = nn.RNN(256, 512,2, dropout=0.3)
        # 输出层 ，隐藏层维度 * 词表大小
        self.out = nn.Linear(512, vocab_size)

    def forward(self, input,hidden):
        # input: 句子数量 * 句子长度
        # embd：句子数量 * 句子长度 * 词嵌入维度
        embd = self.embed(input)

        # rnn层输入（转置后）：句子长度 * 句子数量 * 词嵌入维度
        # rnn层输出：句子长度 * 句子数量 * 隐藏层维度
        output, hidden = self.rnn(embd.transpose(0,1), hidden)
        # 数据进入输出层
        # output：句子长度x句子的数量x隐藏层的维度 --> 单词的数量x隐藏层的维度
        output = output.reshape(-1, output.shape[-1])
        # 单词的数量x隐藏层的维度 @ 隐藏层的维度x词表大小 -->单词的数量x词表大小
        logits = self.out(output)
        return logits, hidden

    def init_hidden(self,batch_size):
        # 隐藏层的层数xbsx隐藏层的维度
        return torch.zeros(2,batch_size,512)


if __name__ == '__main__':
    from build_vocab import build_vocab

    unique_words, word2indx, word_count, corpus_ids = build_vocab()
    model = Jay_Chou_Lyrics_Generator(word_count)

    input= torch.randint(0,5703,[2,10])
    hidden = model.init_hidden(2)
    output,hidden = model(input,hidden)
    print(output.shape)
    y_pred = torch.argmax(output,dim=-1)
    print(y_pred)
        
