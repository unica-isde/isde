import numpy as np
from matplotlib import pyplot as plt
from utils import split_data, plot_ten_images, compute_ts_error
from ml import NearestMeanCentroid
from data_loaders import DataLoaderMNIST

from sklearn.datasets import fetch_lfw_people

# use_faces = False  # True to use LFW, False for MNIST digits
#
# if use_faces is True:
#     dataset = fetch_lfw_people(min_faces_per_person=10)
#     n_samples, h, w = dataset.images.shape
#     X = dataset.data
#     y = dataset.target
# else:
#     filename = '../data/mnist_data.csv'  # the location of the CSV file
#     X, y = load_mnist_data(filename)
#     h, w = 28, 28


data_loader = DataLoaderMNIST()
print(data_loader.filename)

X, y = data_loader.load_data()
w = data_loader.width
h = data_loader.height

Xtr, ytr, Xts, yts = split_data(X, y, tr_fraction=0.6)

# data has been loaded and split. Now let's create the classifier.
clf = NearestMeanCentroid()
clf.fit(Xtr, ytr)

classes = np.unique(ytr)  # list of training class labels
titles = ['y: ' + str(i) for i in classes]
plot_ten_images(clf.centroids, w, h, titles)
plt.savefig('../figs/centroids.pdf')  # store a pdf in 'figs' folder
# plt.show()  # this displays image on screen

yc = clf.predict(Xts)
test_error = compute_ts_error(yc, yts)
