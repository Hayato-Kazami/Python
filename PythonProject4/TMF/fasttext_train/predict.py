import fasttext
from config import Config

conf = Config()

# 1.加载模型
model = fasttext.load_model(conf.model_save_path + '/fasttext_train_char_auto.bin')
print(f'模型加载完成')

def predict(data:dict):
    """
    :param data: dict {"text": "xxx"}
    :return: dict {"text": "xxx", "pred_class": "xxx"}
    """
    word = " ".join(list(data['text']))
    res = model.predict(word)
    data['pred_class'] = res[0][0][9:]
    return data


if __name__ == '__main__':
    predict({"text":"河南中招网上填报志愿：12日初三毕业生可确认"})