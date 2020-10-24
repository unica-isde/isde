import numpy as np
import matplotlib
matplotlib.rcParams['text.usetex'] = True  # enable latex syntax in plots
import matplotlib.pyplot as plt
from ex1.utils import split_data, plot_ten_images, compute_ts_error
from ex1.classifiers import NearestMeanCentroid
from ex1.data_loaders import DataLoaderMNIST, DataLoaderLFW
from ex1.data_perturb import DataPerturbUniform

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
compute_ts_error(yc, yts)  # prints test error

# perturb data
data_perturb = DataPerturbUniform()
xts_perturbed = data_perturb.perturb_data(Xts)

# test on clean TS
yc = clf.predict(xts_perturbed)
compute_ts_error(yc, yts)  # prints test error

# plot unperturbed test data
plt.figure(figsize=(10, 6))
plot_ten_images(Xts, w, h, titles)
plt.savefig('../figs/examples.pdf')

# plot the perturbed data
titles = ['y: ' + str(i) for i in np.unique(y)]
plt.figure(figsize=(10, 6))
plot_ten_images(xts_perturbed, w, h, titles)
plt.savefig('../figs/examples_perturbed.pdf')

k = np.linspace(0, 5, num=100)
test_error = np.zeros(shape=k.shape)

for i in range(k.size):
    data_perturb.k = k[i]
    xts_perturbed = data_perturb.perturb_data(Xts)
    yc = clf.predict(xts_perturbed)
    test_error[i] = compute_ts_error(yc, yts)

# print(test_error)

plt.figure()
plt.plot(k, test_error)
plt.title('Test error')
plt.xlabel(r'Perturbation size (K or $\sigma$)')
plt.savefig('../figs/error_perturbed.pdf')
