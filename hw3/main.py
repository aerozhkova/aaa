class CountVectorizer:
    def __init__(self):
        self.feature_names = []

    def fit_transform(self, text_corpus: list[str]) -> list[list]:
        """ Returns document-term matrix"""
        sentence_words, feature_names = [], []
        feature_names_dict = {}
        for sentence in [text.split() for text in text_corpus]:
            sentence_words.append([word.lower() for word in sentence])
        for word in [word for sent in sentence_words for word in sent]:
            if word not in feature_names_dict:
                feature_names_dict[word] = None
                feature_names.append(word)
        self.feature_names = feature_names
        cnt_matrix = []
        for sentence in sentence_words:
            word_cnt_dict = dict.fromkeys(feature_names, 0)
            for word in sentence:
                word_cnt_dict[word] += 1
            cnt_matrix.append(list(word_cnt_dict.values()))
        return cnt_matrix

    def get_feature_names(self) -> list:
        """ Returns list of unique terms """
        return self.feature_names


if __name__ == '__main__':
    print('Введите тексты через Enter. '
          'Нажмите Ctrl-D (Cmd-D), чтобы сохранить их.')
    corpus = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        corpus.append(line)
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
