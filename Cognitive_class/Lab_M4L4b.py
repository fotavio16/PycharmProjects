# Hierarchical Clustering - Agglomerative

import numpy as np
from scipy import ndimage
from scipy.cluster import hierarchy
from scipy.spatial import distance_matrix
from matplotlib import pyplot as plt
from sklearn import manifold, datasets
from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets.samples_generator import make_blobs

# Geração dos dados aleatórios
X2, y2 = make_blobs(n_samples=50, centers=[[4,4], [-2, -1], [1, 1], [10,4]], cluster_std=0.9)

# Plota a distribuição
# plt.scatter(X2[:, 0], X2[:, 1], marker='.')
# plt.show()

# Inicia o agrupamento
agglom = AgglomerativeClustering(n_clusters = 4, linkage = 'average')

# Treina o agrupamento
agglom.fit(X2,y2)

# Create a figure of size 6 inches by 4 inches.
plt.figure(figsize=(6, 4))

# These two lines of code are used to scale the data points down,
# Or else the data points will be scattered very far apart.

# Create a minimum and maximum range of X2.
x_min, x_max = np.min(X2, axis=0), np.max(X2, axis=0)

# Get the average distance for X2.
X2 = (X2 - x_min) / (x_max - x_min)

# This loop displays all of the datapoints.
for i in range(X2.shape[0]):
    # Replace the data points with their respective cluster value
    # (ex. 0) and is color coded with a colormap (plt.cm.spectral)
    plt.text(X2[i, 0], X2[i, 1], str(y2[i]),
             color=plt.cm.spectral(agglom.labels_[i] / 10.),
             fontdict={'weight': 'bold', 'size': 9})

# Remove the x ticks, y ticks, x and y axis
plt.xticks([])
plt.yticks([])
plt.axis('off')

# Display the plot
plt.show()

# Display the plot of the original data before clustering
plt.scatter(X2[:, 0], X2[:, 1], marker='.')
plt.show()

dist_matrix = distance_matrix(X2,X2)
print(dist_matrix)

Z = hierarchy.linkage(dist_matrix, 'complete')

dendro = hierarchy.dendrogram(Z)
