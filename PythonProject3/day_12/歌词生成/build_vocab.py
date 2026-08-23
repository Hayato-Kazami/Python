import jieba
def build_vocab():
    all_words = []
    unique_words = []
    with open('./data/lyrics.txt', 'r', encoding='utf-8') as f:
        for line in f:
            # 去除空行
            if not line.strip():
                continue
            # 使用jieba分词
            words = jieba.lcut(line)
            all_words.append(words)

            # 去重
            for word in words:
                if word not in unique_words:
                    unique_words.append(word)

    # 词表大小
    vocab_size = len(unique_words)

    # 词表映射字典
    vocab_dict = {word: index for index, word in enumerate(unique_words)}

    # 语料
    corpus = []
    # 词表转成索引并用空格隔开
    for words in all_words:
        temp = [vocab_dict[word] for word in words] + [vocab_dict[" "]]
        corpus.extend(temp)

    return unique_words, vocab_dict, corpus, vocab_size

if __name__ == '__main__':
    unique_words, vocab_dict, corpus, vocab_size = build_vocab()
    print("词表:", unique_words)
    print("词表大小:", vocab_size)
    print("词表映射字典:", vocab_dict)
    print("语料:", corpus)
