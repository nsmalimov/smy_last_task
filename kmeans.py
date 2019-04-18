from helper import read_queries
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
import collections
from pprint import pprint

def cluster_texts(texts, clusters=10):
    vectorizer = TfidfVectorizer(stop_words='english',
                                 max_df=0.5,
                                 min_df=0.1,
                                 lowercase=True)

    tfidf_model = vectorizer.fit_transform(texts)

    print ("vectorizer.fit_transform end")

    km_model = KMeans(n_clusters=clusters, max_iter=100)
    km_model.fit(tfidf_model)

    clustering = collections.defaultdict(list)

    for idx, label in enumerate(km_model.labels_):
        clustering[label].append(idx)

    print("Top terms per cluster:")
    order_centroids = km_model.cluster_centers_.argsort()[:, ::-1]
    terms = vectorizer.get_feature_names()
    for i in range(clusters):
        print ("Cluster %d:" % i)
        for ind in order_centroids[i, :10]:
            print (' %s' % terms[ind])
        print ('')

    return clustering

if __name__ == "__main__":
    queries_start = read_queries('queries_start')

    clusters = cluster_texts(queries_start, 7)