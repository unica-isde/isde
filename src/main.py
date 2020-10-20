from data_loaders import load_mnist_data
from ml import NearestMeanCentroid
import numpy as np

# loads data from a CSV file hosted in our repository
# filename = "https://github.com/unica-isde/isde/raw/master/data/mnist_data.csv"
filename = "../data/mnist_data.csv"

x, y = load_mnist_data(filename, n_samples=1000)

print(x.shape, y.shape)

clf = NearestMeanCentroid()

clf.fit(x, y)
print(clf.centroids)

ypred = clf.predict(x)
print(np.array(y!=ypred).sum())

clf._centroids = None