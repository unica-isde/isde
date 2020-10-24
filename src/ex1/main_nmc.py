import numpy as np
from matplotlib import pyplot as plt
from ex1.utils import split_data, plot_ten_images, compute_ts_error
from ex1.classifiers import NearestMeanCentroid
from ex1.data_loaders import DataLoaderMNIST, DataLoaderLFW


use_faces = False  # True to use LFW, False for MNIST digits

if use_faces is True:
    data_loader = DataLoaderLFW()
else:
    data_loader = DataLoaderMNIST()

x, y = data_loader.load_data()
w = data_loader.width
h = data_loader.height

# list comprehension
titles = ['y: ' + str(i) for i in y]
# ... equivalent to:
# titles = []
# for i in np.unique(y):
#    titles.append('y: ' + str(i))

plt.figure(figsize=(10, 6))
plot_ten_images(x, w, h, titles)
plt.savefig('../figs/examples.pdf')

Xtr, ytr, Xts, yts = split_data(x, y, tr_fraction=0.6)

# data has been loaded and split. Now let's create the classifier.
clf = NearestMeanCentroid()
clf.fit(Xtr, ytr)

classes = np.unique(ytr)  # list of training class labels
titles = ['y: ' + str(i) for i in classes]
plt.figure(figsize=(10, 6))
plot_ten_images(clf.centroids, w, h, titles)
plt.savefig('../figs/centroids.pdf')  # store a pdf in 'figs' folder
# plt.show()  # this displays image on screen

yc = clf.predict(Xts)
test_error = compute_ts_error(yc, yts)
