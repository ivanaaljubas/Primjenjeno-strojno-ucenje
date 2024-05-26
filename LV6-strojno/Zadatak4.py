import scipy as sp
from sklearn import cluster, datasets
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


face = mpimg.imread('example_grayscale.png')
    
X = face.reshape((-1, 1)) # We need an (n_sample, n_feature) array
k_means = cluster.KMeans(n_clusters=5,n_init=1)
k_means.fit(X) 
values = k_means.cluster_centers_.squeeze()
labels = k_means.labels_
face_compressed = np.choose(labels, values)
face_compressed.shape = face.shape

plt.figure(1)
plt.imshow(face,  cmap='gray')
plt.show()

plt.figure(2)
plt.imshow(face_compressed,  cmap='gray')
plt.show()

#smanjivanjem broja klustera se smanjuje broj boja te se tako dobija efekt kompresije
#