import fasttext

def train_fasttext():
    model = fasttext.train_supervised('./data/cooking_train.txt')
    model.save_model('./model/cooking_model.bin')
    model_load = fasttext.load_model('./model/cooking_model.bin')
    res = model_load.predict("My crumb cake topping isn't working",k = -1,threshold = 0.1)
    print(res)

def predict_fasttext():
    # 训练模型
    model = fasttext.train_supervised('./data/cooking_train.txt',
                                      epoch=200,
                                      lr=0.5,
                                      wordNgrams=2,
                                      loss='hs')
    # 模型预测 k表示预测结果的数量，threshold表示阈值
    res = model.predict("My crumb cake topping isn't working", k=-1, threshold=0.2)
    # 模型测试
    res = model.test('./data/cooking.pre.valid')
    print(res)

def predict_fasttext_auto():
    # 训练模型
    model = fasttext.train_supervised('./data/cooking_train.txt',
                                      autotuneValidationFile = './data/cooking.pre.valid',
                                      autotuneDuration = 300,
                                      verbose = 3,
                                      loss='hs')
    
    # 模型预测 k表示预测结果的数量，threshold表示阈值
    res = model.predict("My crumb cake topping isn't working", k=-1, threshold=0.2)
    # 模型测试
    res = model.test('./data/cooking.pre.valid')
    print(res)


if __name__ == '__main__':
    predict_fasttext()
    predict_fasttext_auto()