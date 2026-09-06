import transformers

def text_class_pipeline():
    model = transformers.pipeline(task = "sentiment-analysis",model ="D:/2026_机器&深度/04 代码/day15/PretrainedModel/chinese_sentiment" )

    res = model("大海航行靠舵手，伟大领袖毛主席！")
    print(f"res: {res}")

def feature_extract_pipeline():
    model = transformers.pipeline(task = "feature-extraction",model = "D:/2026_机器&深度/04 代码/day15/PretrainedModel/bert-base-chinese")
    res1 = model("大海航行靠舵手，伟大领袖毛主席！")
    print(res1)

def fill_mask_pipeline():
    model = transformers.pipeline(task = "fill-mask",model = "D:/2026_机器&深度/04 代码/day15/PretrainedModel/chinese-bert-wwm")
    res2 = model("大海航行靠舵手，伟大领袖[MASK]近平！")
    print(res2)

if __name__ == '__main__':
    # text_class_pipeline()
    # feature_extract_pipeline()
    fill_mask_pipeline()