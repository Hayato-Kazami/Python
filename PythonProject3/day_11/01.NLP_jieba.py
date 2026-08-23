import jieba
import jieba.posseg

def user_dict():
    sentence = "传智教育是一家上市公司，旗下有黑马程序员品牌。"
    # 加载自定义词典
    jieba.load_userdict("./userdict.txt")
    cut = jieba.lcut(sentence)
    print(cut)

def posseg():
    sentence = "传智教育是一家上市公司，旗下有黑马程序员品牌。"
    result = jieba.posseg.lcut(sentence)
    print(result)

if __name__ == "__main__":
    user_dict()
    posseg()