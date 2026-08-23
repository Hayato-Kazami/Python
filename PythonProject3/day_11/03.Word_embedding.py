import jieba
import torch
def word_embedding():
    sentence = "传智是一家IT培训机构"
    word_list = list(set(jieba.lcut(sentence)))

    # 构建词向量
    embedding = torch.nn.Embedding(num_embeddings=len(word_list),
                                   embedding_dim=4)
    for i, word in enumerate(word_list):
        print(f"Word: {word}, Embedding: {embedding(torch.tensor([i]))}")

if __name__ == "__main__" :
    word_embedding()
