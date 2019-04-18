https://towardsdatascience.com/nlp-extracting-the-main-topics-from-your-dataset-using-lda-in-minutes-21486f5aa925

Чемпионат длился c 14 июня 2018 по 15 июля 2018

Всего 39 789 519 запросов в период с 2018-06-14 00:00:00 по 2018-07-15 23:59:59

1. Подготовка данных

разделим данные на 3 части.

* запросы в начале чемпионата (первые 10 дней)
Всего: 12 850 460

* запросы в середине чемпионата (11 дней между первыми десятью и последними десятью)
Всего: 13 760 275

* запросы в конце чемпионата (последние 10 дней)
Всего: 13 178 784


2. Кластеризация

- Первый подход с использованием классических методов кластеризации. Tf-idf
https://stackoverflow.com/questions/27889873/clustering-text-documents-using-scikit-learn-kmeans-in-python
https://nlpforhackers.io/recipe-text-clustering/
https://pythonprogramminglanguage.com/kmeans-text-clustering/

- Использование латентного распределения Дирихле (LDA)
http://qaru.site/questions/292183/understanding-lda-implementation-using-gensim
https://radimrehurek.com/gensim/tutorial.html
https://towardsdatascience.com/nlp-extracting-the-main-topics-from-your-dataset-using-lda-in-minutes-21486f5aa925

- Векторное представление слов word2vec
http://ai.intelligentonlinetools.com/ml/text-clustering-doc2vec-word-embedding-machine-learning/
https://github.com/gaetangate/word2vec-cluster/blob/master/word2vec_cluster.py
kmeans birch

Дополнительно: обработка, в виде стемминга, лемматизации и очистки

сделать:
стемминг, лемматизация
