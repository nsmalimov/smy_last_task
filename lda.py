from gensim.corpora.dictionary import Dictionary
from gensim.models import LdaMulticore
from helper import read_queries
from nltk.corpus import stopwords

def cluster_texts(texts):
    dictionary = Dictionary(texts)

    print('dictionary')

    bow_corpus = [dictionary.doc2bow(doc) for doc in texts]

    print('bow_corpus')

    import time
    start = time.time()


    lda_model = LdaMulticore(bow_corpus,
                             num_topics=20,
                             id2word=dictionary,
                             passes=10,
                             workers=4)

    end = time.time()
    print(end - start)

    res = lda_model.print_topics(20)

    for i in res:
        print (i)


if __name__ == "__main__":
    queries_start = read_queries('filtered_prepared/queries_middle',
                                 need_split=True,
                                 need_remove_stop_words=True)

    cluster_texts(queries_start)
