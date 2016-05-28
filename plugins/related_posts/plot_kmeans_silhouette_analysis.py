"""
===============================================================================
Selecting the number of clusters with silhouette analysis on KMeans clustering
===============================================================================

Silhouette analysis can be used to study the separation distance between the
resulting clusters. The silhouette plot displays a measure of how close each
point in one cluster is to points in the neighboring clusters and thus provides
a way to assess parameters like number of clusters visually. This measure has a
range of [-1, 1].

Silhoette coefficients (as these values are referred to as) near +1 indicate
that the sample is far away from the neighboring clusters. A value of 0
indicates that the sample is on or very close to the decision boundary between
two neighboring clusters and negative values indicate that those samples might
have been assigned to the wrong cluster.

In this example the silhouette analysis is used to choose an optimal value for
``n_clusters``. The silhouette plot shows that the ``n_clusters`` value of 3, 5
and 6 are a bad pick for the given data due to the presence of clusters with
below average silhouette scores and also due to wide fluctuations in the size
of the silhouette plots. Silhouette analysis is more ambivalent in deciding
between 2 and 4.

Also from the thickness of the silhouette plot the cluster size can be
visualized. The silhouette plot for cluster 0 when ``n_clusters`` is equal to
2, is bigger in size owing to the grouping of the 3 sub clusters into one big
cluster. However when the ``n_clusters`` is equal to 4, all the plots are more
or less of similar thickness and hence are of similar sizes as can be also
verified from the labelled scatter plot on the right.
"""

from __future__ import print_function

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

def get_nikola_posts():
    from nikola import Nikola
    conf_filename = 'conf.py'
    with open(conf_filename) as f:
        code = f.read()
    config = {}
    exec(code, None, config)
    site = Nikola(**config)
    site.init_plugins()
    site.scan_posts()
    return [p for p in site.timeline if p.use_in_feeds]


def get_nikola_vectors(our_vectorizer=False):
    from related_posts import get_tf_idf_vectors
    posts = get_nikola_posts()

    if our_vectorizer:
        vectors, vocabulary = get_tf_idf_vectors(posts, stop_words=True, min_df=2, max_df=0.75)
        # vectors, vocabulary = get_tf_idf_vectors(posts, use_tags=True, min_df=2, max_df=0.5)

    else:
        from sklearn.feature_extraction.text import TfidfVectorizer
        from related_posts import _get_post_text
        vectorizer = TfidfVectorizer(max_df=0.75, min_df=2, stop_words='english', use_idf=True)
        vectors = vectorizer.fit_transform([_get_post_text(post) for post in posts])
        vocabulary = vectorizer.get_feature_names()

    return posts, vectors, vocabulary

if __name__ == '__main__':
    print(__doc__)


    # FIXME: There's something wrong with our vectorizer...
    # posts, X1, vocabulary1 = get_nikola_vectors()
    # posts, X2, vocabulary2 = get_nikola_vectors(our_vectorizer=True)
    # The vocabulary matches, but not the vectors.

    posts, X, vocabulary = get_nikola_vectors()


    n_components = 3

    if n_components:
        print('Dimensionality reduction')
        from sklearn.decomposition import TruncatedSVD
        from sklearn.pipeline import make_pipeline
        from sklearn.preprocessing import Normalizer

        svd = TruncatedSVD(n_components)
        normalizer = Normalizer(copy=False)
        lsa = make_pipeline(svd, normalizer)

        X = lsa.fit_transform(X)


    posts_ = np.array(posts)

    print(X.shape)

    range_n_clusters = range(2, 15)

    for n_clusters in range_n_clusters:
        # Create a subplot with 1 row and 2 columns
        fig, ax1 = plt.subplots(1, 1)
        fig.set_size_inches(18, 7)

        # The 1st subplot is the silhouette plot
        # The silhouette coefficient can range from -1, 1 but in this example all
        # lie within [-0.1, 1]
        ax1.set_xlim([-0.1, 1])
        # The (n_clusters+1)*10 is for inserting blank space between silhouette
        # plots of individual clusters, to demarcate them clearly.
        ax1.set_ylim([0, X.shape[0] + (n_clusters + 1) * 10])

        # Initialize the clusterer with n_clusters value and a random generator
        # seed of 10 for reproducibility.
        clusterer = KMeans(n_clusters=n_clusters, n_init=20, max_iter=1000, random_state=10)
        cluster_labels = clusterer.fit_predict(X)

        if n_components:
            original_space_centroids = svd.inverse_transform(clusterer.cluster_centers_)
            ordered_cluter_indices = np.abs(original_space_centroids).argsort()[:, :10]

        else:
            ordered_cluter_indices = np.abs(clusterer.cluster_centers_).argsort()[:, :10]

        for i, cluster_indices in enumerate(ordered_cluter_indices):
            keywords_ = [vocabulary[index] for index in cluster_indices]
            print('Keywords for cluster {}: {}'.format(i, ', '.join(keywords_)))

        print()

        for i, cluster_indices in enumerate(ordered_cluter_indices):
            titles = ['    {}'.format(p.title()) for p in posts_[cluster_labels==i]]
            a, b = 30, len(titles)
            print('Titles for cluster {}: {}'.format(i, ' '.join(titles[:a] + titles[max(a, b-a):])))
            print()

        print()

        # The silhouette_score gives the average value for all the samples.
        # This gives a perspective into the density and separation of the formed
        # clusters
        silhouette_avg = silhouette_score(X, cluster_labels)
        print("For n_clusters =", n_clusters,
              "The average silhouette_score is :", silhouette_avg)

        # Compute the silhouette scores for each sample
        sample_silhouette_values = silhouette_samples(X, cluster_labels)

        y_lower = 10
        for i in range(n_clusters):
            # Aggregate the silhouette scores for samples belonging to
            # cluster i, and sort them
            ith_cluster_silhouette_values = \
                sample_silhouette_values[cluster_labels == i]

            ith_cluster_silhouette_values.sort()

            size_cluster_i = ith_cluster_silhouette_values.shape[0]
            y_upper = y_lower + size_cluster_i

            color = cm.spectral(float(i) / n_clusters)
            ax1.fill_betweenx(np.arange(y_lower, y_upper),
                              0, ith_cluster_silhouette_values,
                              facecolor=color, edgecolor=color, alpha=0.7)

            # Label the silhouette plots with their cluster numbers at the middle
            ax1.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))

            # Compute the new y_lower for next plot
            y_lower = y_upper + 10  # 10 for the 0 samples

        ax1.set_title("The silhouette plot for the various clusters.")
        ax1.set_xlabel("The silhouette coefficient values")
        ax1.set_ylabel("Cluster label")

        # The vertical line for average silhoutte score of all the values
        ax1.axvline(x=silhouette_avg, color="red", linestyle="--")

        ax1.set_yticks([])  # Clear the yaxis labels / ticks
        ax1.set_xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])

        # 2nd Plot showing the actual clusters formed
        # colors = cm.spectral(cluster_labels.astype(float) / n_clusters)
        # ax2.scatter(X[:, 0], X[:, 1], marker='.', s=30, lw=0, alpha=0.7,
        #             c=colors)

        # Labeling the clusters
        # centers = clusterer.cluster_centers_
        # Draw white circles at cluster centers
        # ax2.scatter(centers[:, 0], centers[:, 1],
        #             marker='o', c="white", alpha=1, s=200)

        # for i, c in enumerate(centers):
        #     ax2.scatter(c[0], c[1], marker='$%d$' % i, alpha=1, s=50)

        # ax2.set_title("The visualization of the clustered data.")
        # ax2.set_xlabel("Feature space for the 1st feature")
        # ax2.set_ylabel("Feature space for the 2nd feature")

        plt.suptitle(("Silhouette analysis for KMeans clustering on sample data "
                      "with n_clusters = %d" % n_clusters),
                     fontsize=14, fontweight='bold')

        plt.show()
