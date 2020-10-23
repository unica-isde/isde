import numpy as np
from matplotlib import pyplot as plt
from utils import split_data, plot_ten_images, compute_ts_error
from ml import NearestMeanCentroid
from data_loaders import DataLoaderMNIST, DataLoaderLFW
from data_perturb import DataPerturbUniform

use_faces = False  # True to use LFW, False for MNIST digits

if use_faces is True:
    data_loader = DataLoaderLFW()
else:
    data_loader = DataLoaderMNIST()

x, y = data_loader.load_data()
w = data_loader.width
h = data_loader.height

# list comprehension
titles = ['y: ' + str(i) for i in np.unique(y)]
plt.figure(figsize=(10, 6))
plot_ten_images(x, w, h, titles)
plt.savefig('../figs/examples.pdf')

# split data into TR/TS
Xtr, ytr, Xts, yts = split_data(x, y, tr_fraction=0.6)

# train classifier on clean TR
clf = NearestMeanCentroid()
clf.fit(Xtr, ytr)

# test on clean TS
yc = clf.predict(Xts)
test_error = compute_ts_error(yc, yts)

# perturb data
data_perturb = DataPerturbUniform()
xts_perturbed = data_perturb.perturb_data(Xts)

# test on clean TS
yc = clf.predict(xts_perturbed)
test_error = compute_ts_error(yc, yts)

# plot the perturbed data
titles = ['y: ' + str(i) for i in np.unique(y)]
plt.figure(figsize=(10, 6))
plot_ten_images(xts_perturbed, w, h, titles)
plt.savefig('../figs/examples_perturbed.pdf')

k = np.linspace(0, 5, num=200)
test_error = np.zeros(shape=k.shape)

for i in range(k.size):
    data_perturb.k = k[i]
    xts_perturbed = data_perturb.perturb_data(Xts)
    yc = clf.predict(xts_perturbed)
    test_error[i] = compute_ts_error(yc, yts)

# print(test_error)

plt.figure()
plt.plot(k, test_error)
plt.show()
