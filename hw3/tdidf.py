from count_vectorizer import CountVectorizer
import math


def tf_transform(count_matrix):
    tf_matrix = []
    for row in count_matrix:
        row_sum = sum(row)
        tf_row = [round(el / row_sum, 3) for el in row]
        tf_matrix.append(tf_row)
    return tf_matrix


def idf_transform(count_matrix):
    doc_cnt = len(count_matrix)
    idf_matrix = []
    for i in range(len(count_matrix[0])):
        word_freq = 0
        for matrix_row in count_matrix:
            if matrix_row[i] > 0:
                word_freq += 1
        idf_matrix.append(round(math.log((doc_cnt + 1) /
                                         (word_freq + 1)) + 1, 3))
    return idf_matrix


class TfidfTransformer:
    def fit_transform(self, count_matrix):
        tfidf_matrix = []
        for row in tf_transform(count_matrix):
            tfidf_row = []
            for a, b in zip(row, idf_transform(count_matrix)):
                tfidf_row.append(round(a * b, 3))
            tfidf_matrix.append(tfidf_row)
        return tfidf_matrix


class TfidfVectorizer(CountVectorizer):
    def __init__(self):
        super().__init__()
        self._transformer = TfidfTransformer()

    def fit_transform(self, corpus):
        count_matrix = super().fit_transform(corpus)
        return self._transformer.fit_transform(count_matrix)


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(tfidf_matrix)
