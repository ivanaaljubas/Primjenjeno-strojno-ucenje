from sklearn import datasets
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
def generate_data(n_samples, flagc):
    
    if flagc == 1:
        random_state = 365
        X,y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
        
    elif flagc == 2:
        random_state = 148
        X,y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
        transformation = [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]]
        X = np.dot(X, transformation)
        
    elif flagc == 3:
        random_state = 148
        X, y = datasets.make_blobs(n_samples=n_samples,
                                    centers=4,
                                    cluster_std=[1.0, 2.5, 0.5, 3.0],
                                    random_state=random_state)

    elif flagc == 4:
        X, y = datasets.make_circles(n_samples=n_samples, factor=.5, noise=.05)
        
    elif flagc == 5:
        X, y = datasets.make_moons(n_samples=n_samples, noise=.05)
    
    else:
        X = []
        
    return X

x = generate_data(500, 1)
kmeans = KMeans(n_clusters=3).fit(x)

inertia = []

for k in range(1,21):
    kmeans = KMeans(n_clusters = k, random_state = 42).fit(x)
    inertia.append(kmeans.inertia_)

plt.plot(range(1,21), inertia)
plt.xlabel("Broj klustera")
plt.ylabel("Vrijednost kriterijske funkcije")
plt.show()

#sto je veci broj klustera to je manja vrijednost kriterijske funkcije
#optimalna kolicina broja klustera odreduje se metodom lakta
#sto bi tu bilo 3-5