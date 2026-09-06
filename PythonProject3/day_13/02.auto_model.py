import tokenizers
import torch
from transformers import AutoModelForQuestionAnswering,AutoModelForMaskedLM,AutoModel,AutoTokenizer,AutoModelForSequenceClassification
from transformers import AutoModelForTokenClassification,AutoModelForSeq2SeqLM,AutoConfig
def auto_text_class():
    tokenizer = AutoTokenizer.from_pretrained("D:/2026_机器&深度/04 代码/day15/PretrainedModel/chinese_sentiment")
    model = AutoModelForSequenceClassification.from_pretrained("D:/2026_机器&深度/04 代码/day15/PretrainedModel/chinese_sentiment")

    input = tokenizer(text=["人生得意须尽欢", "天之道，损不足而奉有余", "会当凌绝顶"],
                      text_pair=["槛外长江空自流", "仰天大笑出门去", "一览众山小"],
                      return_tensors='pt',
                      padding='max_length',
                      max_length=32,
                      truncation=True)

    res = model(**input)
    print(res)

def auto_fetature_extract():
    tokenizer = AutoTokenizer.from_pretrained("D:/2026_机器&深度/04 代码/day15/PretrainedModel/bert-base-chinese")
    model = AutoModel.from_pretrained("D:/2026_机器&深度/04 代码/day15/PretrainedModel/bert-base-chinese")

    input = tokenizer(text=["人生得意须尽欢", "天之道，损不足而奉有余", "会当凌绝顶"],
                      text_pair=["槛外长江空自流", "仰天大笑出门去", "一览众山小"],
                      return_tensors='pt',
                      padding='max_length',
                      max_length=32,
                      truncation=True)

    res = model(**input)
    print(res.last_hidden_state[:, 0, :])

def auto_fill_mask():
    model = AutoModelForMaskedLM.from_pretrained('D:/2026_机器&深度/04 代码/day15/PretrainedModel/chinese-bert-wwm')
    tokenizer = AutoTokenizer.from_pretrained('D:/2026_机器&深度/04 代码/day15/PretrainedModel/chinese-bert-wwm')

    # 1.文本转向量（分词器）
    input = tokenizer(text="[MASK]近平",
                      return_tensors='pt',  # 是否返回张量 注意：用 "pt",代表返回的是pytorch的张量类型
                      padding="max_length",  # 要传"max_length"，max_length这个参数才生效，否则会按照文本中最长的句子作为maxlen
                      max_length=20)
    # 2.获取文本特征（词向量、句向量）
    output=model(**input)
    print(f'output-->{output}')
    print(f'logits-->{output.logits.shape}')
    y_pred = torch.argmax(output.logits,dim=-1)
    print(y_pred)
    # 将索引号转成文本 encode:编码  decode：解码  索引号转成文本
    res = tokenizer.decode(y_pred.squeeze()[2])
    print(f'res -->{res}')

def auto_question_answer():
    model = AutoModelForQuestionAnswering.from_pretrained('D:/2026_机器&深度/04 代码/day15/PretrainedModel/chinese_pretrain_mrc_roberta_wwm_ext_large')
    tokenizer = AutoTokenizer.from_pretrained('D:/2026_机器&深度/04 代码/day15/PretrainedModel/chinese_pretrain_mrc_roberta_wwm_ext_large')
    context = '我叫张三 我是一个程序员 我的喜好是打篮球'
    questions = ['我是谁？', '我是做什么的？', '我的爱好是什么？']
    model.eval()
    # 1.文本转向量（分词器）
    for  question in questions:
        input = tokenizer(question,
                          context,
                          return_tensors='pt',  # 是否返回张量 注意：用 "pt",代表返回的是pytorch的张量类型
                          padding="max_length",  # 要传"max_length"，max_length这个参数才生效，否则会按照文本中最长的句子作为maxlen
                          max_length=20)
        # 2.获取文本特征（词向量、句向量）
        output=model(**input)

        start = torch.argmax(output.start_logits,dim=-1).item()
        end = torch.argmax(output.end_logits,dim=-1).item()
        output_ids = input.input_ids[:,start:end+1]
        print(f'{question}的答案为：')
        print(tokenizer.decode(output_ids.squeeze()))

def auto_test_summarization():
    model = AutoModelForSeq2SeqLM.from_pretrained('D:/2026_机器&深度/04 代码/day15/PretrainedModel/distilbart-cnn-12-6')
    tokenizer = AutoTokenizer.from_pretrained('D:/2026_机器&深度/04 代码/day15/PretrainedModel/distilbart-cnn-12-6')
    text = "BERT is a transformers model pretrained on a large corpus of English data " \
           "in a self-supervised fashion. This means it was pretrained on the raw texts " \
           "only, with no humans labelling them in any way (which is why it can use lots " \
           "of publicly available data) with an automatic process to generate inputs and " \
           "labels from those texts. More precisely, it was pretrained with two objectives:Masked " \
           "language modeling (MLM): taking a sentence, the model randomly masks 15% of the " \
           "words in the input then run the entire masked sentence through the model and has " \
           "to predict the masked words. This is different from traditional recurrent neural " \
           "networks (RNNs) that usually see the words one after the other, or from autoregressive " \
           "models like GPT which internally mask the future tokens. It allows the model to learn " \
           "a bidirectional representation of the sentence.Next sentence prediction (NSP): the models" \
           " concatenates two masked sentences as inputs during pretraining. Sometimes they correspond to " \
           "sentences that were next to each other in the original text, sometimes not. The model then " \
           "has to predict if the two sentences were following each other or not."

    model.eval()
    # 1.文本转向量（分词器）

    input = tokenizer(text,
                      return_tensors='pt',  # 是否返回张量 注意：用 "pt",代表返回的是pytorch的张量类型
                      padding="max_length",  # 要传"max_length"，max_length这个参数才生效，否则会按照文本中最长的句子作为maxlen
                      max_length=20)
    # 2.进行摘要生成
    output = model.generate(**input)
    print(f'output-->{output}')
    print(tokenizer.decode(output.squeeze(), skip_special_tokens=True))

def auto_ner():
    model = AutoModelForTokenClassification.from_pretrained(
        'D:/2026_机器&深度/04 代码/day15/PretrainedModel/roberta-base-finetuned-cluener2020-chinese')
    tokenizer = AutoTokenizer.from_pretrained('D:/2026_机器&深度/04 代码/day15/PretrainedModel/roberta-base-finetuned-cluener2020-chinese')
    config = AutoConfig.from_pretrained('D:/2026_机器&深度/04 代码/day15/PretrainedModel/roberta-base-finetuned-cluener2020-chinese')
    # 1.文本转向量（分词器）
    input = tokenizer(text="我爱中国天安门，天安门上红旗飘",
                      return_tensors='pt',  # 是否返回张量 注意：用 "pt",代表返回的是pytorch的张量类型
                      padding="max_length",  # 要传"max_length"，max_length这个参数才生效，否则会按照文本中最长的句子作为maxlen
                      max_length=20)


    # 2.获取文本特征（词向量、句向量）
    output = model(input.input_ids)
    print(f'output-->{output.logits.shape}')
    y_pred = torch.argmax(output.logits, dim=-1).squeeze().tolist()
    print(y_pred)
    print(config.id2label)
    for i,word in enumerate(input.input_ids.squeeze().tolist()):
        print(f'{tokenizer.decode(word)}:的结果为：{config.id2label[y_pred[i]]}')
        

if __name__ == '__main__':
    auto_ner()