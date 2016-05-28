"""
=================================================
Demo of affinity propagation clustering algorithm
=================================================

Reference:
Brendan J. Frey and Delbert Dueck, "Clustering by Passing Messages
Between Data Points", Science Feb. 2007

"""
print(__doc__)

import numpy as np
from sklearn.cluster import AffinityPropagation
from sklearn import metrics


##############################################################################
# Generate sample data
# centers = [[1, 1], [-1, -1], [1, -1]]
# X, labels_true = make_blobs(n_samples=300, centers=centers, cluster_std=0.5,
#                             random_state=0)

from plot_kmeans_silhouette_analysis import get_nikola_vectors
posts, X, vocabulary = get_nikola_vectors(our_vectorizer=True)
posts_ = np.array(posts)

##############################################################################
# Compute Affinity Propagation
af = AffinityPropagation(preference=-10).fit(X)
cluster_centers_indices = af.cluster_centers_indices_
labels = af.labels_
print(labels)

n_clusters_ = len(cluster_centers_indices)

print('Estimated number of clusters: %d' % n_clusters_)
# print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
# print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
# print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
# print("Adjusted Rand Index: %0.3f"
#       % metrics.adjusted_rand_score(labels_true, labels))
# print("Adjusted Mutual Information: %0.3f"
#       % metrics.adjusted_mutual_info_score(labels_true, labels))
print("Silhouette Coefficient: %0.3f"
      % metrics.silhouette_score(X, labels, metric='sqeuclidean'))

cluster_centers = X[cluster_centers_indices]
ordered_cluter_indices = np.abs(cluster_centers).argsort()[:, :10]

for i, cluster_indices in enumerate(ordered_cluter_indices):
    keywords_ = [vocabulary[index] for index in cluster_indices]
    print('Keywords for cluster {}: {}'.format(i, ', '.join(keywords_)))

print()

for i, cluster_indices in enumerate(ordered_cluter_indices):
    titles = ['    {}'.format(p.title()) for p in posts_[labels==i]]
    a, b = 30, len(titles)
    print('Titles for cluster {}: {}'.format(i, ' '.join(titles[:a] + titles[max(a, b-a):])))
    print()

print()


##############################################################################
# Plot result
import matplotlib.pyplot as plt
from itertools import cycle

plt.close('all')
plt.figure(1)
plt.clf()

colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
for k, col in zip(range(n_clusters_), colors):
    class_members = labels == k
    cluster_center = X[cluster_centers_indices[k]]
    plt.plot(X[class_members, 0], X[class_members, 1], col + '.')
    plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
             markeredgecolor='k', markersize=14)
    for x in X[class_members]:
        plt.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)

plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()
