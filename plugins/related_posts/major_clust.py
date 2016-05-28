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
    return vectorizer.fit_transform(documents)


def visualize_clusters(documents, labels):
    clusters = {}

    for i, label in enumerate(labels):
        clusters.setdefault(label, []).append(documents[i])

    for cluster in clusters:
        print(80*"=")
        print("\n".join(clusters[cluster]))

    return clusters


def majorclust_sklearn(texts):
    vectorizer = TfidfVectorizer()
    corpus_mat = vectorizer.fit_transform(texts)
    num_of_samples, num_of_features = corpus_mat.shape

    cosine_distances = np.zeros((num_of_samples, num_of_samples))
    for i in range(len(texts)):
        cosine_distances[i] = linear_kernel(corpus_mat[i:i+1], corpus_mat).flatten()
        cosine_distances[i, i] = 0

    t = False
    indices = np.arange(num_of_samples)
    while not t:
        t = True
        shuffled_indices = np.arange(num_of_samples)
        shuffle(shuffled_indices)
        for index in shuffled_indices:
            # aggregating edge weights
            new_index = np.argmax(np.bincount(indices,
                                              weights=cosine_distances[index]))
            if indices[new_index] != indices[index]:
                indices[index] = indices[new_index]
                t = False

    print(indices)

    clusters = {}
    for index, target in enumerate(indices):
        clusters.setdefault(target, []).append(texts[index])

    # for cluster in clusters:
    #     print(80*"=")
    #     print("\n".join(clusters[cluster]))


    return clusters


def majorclust2(X):
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

    majorclust_sklearn(texts)

    print()
    print('X' * 40)
    print()

    X = vectorize_documents(texts)
    labels2 = majorclust2(X)
    visualize_clusters(titles, labels2)
    print(set(labels2))
