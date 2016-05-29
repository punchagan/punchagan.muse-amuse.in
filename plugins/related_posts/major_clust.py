from random import shuffle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import numpy as np

from scipy.spatial.distance import cdist


DOCUMENTS = [
    "foo blub baz",
    "foo bar baz",
    "asdf bsdf csdf",
    "foo bab blub",
    "csdf hddf kjtz",
    "123 456 890",
    "321 890 456 foo",
    "123 890 uiop",
]


def vectorize_documents(documents, **kwargs):
    vectorizer = TfidfVectorizer(**kwargs)
    return vectorizer.fit_transform(documents), vectorizer.get_feature_names()


def visualize_clusters(X, documents, labels, vocabulary):
    clusters = {}

    for i, label in enumerate(labels):
        clusters.setdefault(label, []).append((X[i], documents[i]))

    for cluster in clusters:
        print(80*"=")
        for vector, title in clusters[cluster]:
            print('{} - {}'.format(title, ','.join(top_words(vector, vocabulary))))

    return clusters


def top_words(vector, vocabulary, n=10):
    return [vocabulary[i] for i in np.argsort(vector.toarray()[0])[::-1][:n]]


def majorclust(X):
    # convert sparse matrix to array
    if not isinstance(X, np.ndarray):
        X = X.toarray()

    n_samples, _ = X.shape
    cosine_distances = 1 - cdist(X, X, 'cosine')
    np.fill_diagonal(cosine_distances, 0)

    finished = False
    labels = np.arange(n_samples)
    while not finished:
        finished = True
        for i in range(n_samples):
            j = np.argmax(cosine_distances[i])
            if labels[i] != labels[j]:
                labels[i] = labels[j]
                finished = False

    return labels


if __name__ == '__main__':

    from related_posts import _get_post_text
    from plot_kmeans_silhouette_analysis import get_nikola_posts

    posts = get_nikola_posts()
    shuffle(posts)
    titles = [p.title() for p in posts]
    texts = [_get_post_text(p) for p in posts]

    X, vocabulary = vectorize_documents(texts)
    labels = majorclust(X)
    visualize_clusters(X, titles, labels, vocabulary)
    print(set(labels), len(set(labels)))
