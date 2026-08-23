import torch
from build_vocab import build_vocab
from build_dataset import Jay_Chou
from build_model import Jay_Chou_Lyrics_Generator
from torch.nn import CrossEntropyLoss
from torch.optim import Adam
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt

def train():
    # 构建词典
    unique_words, vocab_dict, corpus, vocab_size = build_vocab()
    # 构建数据集
    dataset = Jay_Chou(corpus, max_len=32)
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # 构建模型
    model = Jay_Chou_Lyrics_Generator(vocab_size).to(device)
    # 定义损失函数和优化器
    criterion = CrossEntropyLoss()
    optimizer = Adam(model.parameters(), lr=0.001)

    # 训练模型
    epochs = 200
    train_loss = []
    total_iters = 0
    for epoch in range(epochs):
        total_loss = 0.0
        iter_epoch = 0

        # 创建数据集
        dataloader = DataLoader(dataset, batch_size=8, shuffle=True)
        for x_train, y_train in dataloader:
            x_train = x_train.to(device)
            y_train = y_train.to(device)

            # 前向传播
            hidden = model.init_hidden(len(x_train)).to(device)
            output, hidden = model(x_train, hidden)

            # 计算损失
            y_train = y_train.transpose(0, 1).reshape(-1)
            loss = criterion(output, y_train)

            # 反向传播和优化
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            # 记录损失
            total_loss += loss.item()
            iter_epoch += 1
            total_iters += 1

        # 每个 epoch 结束后，记录该 epoch 的平均损失（一个点，曲线更平滑）
        avg_loss = total_loss / iter_epoch
        train_loss.append(avg_loss)
        print(f'Epoch {epoch+1}, Loss {avg_loss:.4f}')

    plt.plot(range(1, len(train_loss) + 1), train_loss)
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title('Training Loss')
    plt.show()
    torch.save(model.state_dict(), './model/Jay_Chou_Lyrics_Generator.pth')

if __name__ == '__main__':
    train()
