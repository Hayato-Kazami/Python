import fasttext

def train_word2vec():
    # 训练word2vec模型
    model = fasttext.train_unsupervised('./data/bj30ad')
    # 保存模型
    model.save_model('./model/word2vecbin')
    # 加载模型
    model_load = fasttext.load_model('./model/word2vecbin')
    print(model_load)
    print(model)

def getvec():
    # 模型加载
    model_load = fasttext.load_model('./model/word2vecbin')
    # 获取词向量
    vec = model_load.get_word_vector('dog')
    print(vec)

def model_test():
    model_load = fasttext.load_model('./model/word2vecbin')
    res = model_load.get_nearest_neighbors('dog', k=5)
    print(res)
    res = model_load.get_nearest_neighbors('music', k=5)
    print(res)

def model_funt():
    model = fasttext.train_unsupervised(input='./data/bj30ad', 
                                        model='skipgram',
                                        dim=256,
                                        lr=0.05)
    res = model.get_nearest_neighbors('funk', k=5)
    print(res)

if __name__ == '__main__':
    
    model_funt()