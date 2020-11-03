import numpy as np
import matplotlib
matplotlib.rcParams['text.usetex'] = True  # enable latex syntax in plots
import matplotlib.pyplot as plt
from ex1.utils import split_data, plot_ten_images, compute_ts_error
from ex1.classifiers import NearestMeanCentroid
from ex1.data_loaders import DataLoaderMNIST, DataLoaderLFW
from ex1.data_perturb import DataPerturbUniform, DataPerturbNormal

use_faces = False  # True to use LFW, False for MNIST digits

if use_faces is True:
    data_loader = DataLoaderLFW()
else:
    data_loader = DataLoaderMNIST()

x, y = data_loader.load_data()
w = data_loader.width
h = data_loader.height

# split data into TR/TS
Xtr, ytr, Xts, yts = split_data(x, y, tr_fraction=0.6)

# train classifier on clean TR
clf = NearestMeanCentroid()
clf.fit(Xtr, ytr)

# test on clean TS
yc = clf.predict(Xts)
compute_ts_error(yc, yts)  # prints test error

# perturb data
data_perturb_uniform = DataPerturbUniform()
data_perturb_normal = DataPerturbNormal()
xts_perturbed = data_perturb_uniform.perturb_data(Xts)

# test on clean TS
yc = clf.predict(xts_perturbed)
compute_ts_error(yc, yts)  # prints test error

# plot unperturbed test data
titles = ['y: ' + str(i) for i in yts]
plt.figure(figsize=(10, 6))
plot_ten_images(Xts, w, h, titles)
plt.savefig('../figs/examples.pdf')

# plot the perturbed data (w/ uniform perturbation)
plt.figure(figsize=(10, 6))
plot_ten_images(xts_perturbed, w, h, titles)
plt.savefig('../figs/examples_perturbed.pdf')

param_values = np.linspace(0, 5, num=100)
test_error_uniform = np.zeros(shape=param_values.shape)
test_error_normal = np.zeros(shape=param_values.shape)

for i in range(param_values.size):
    data_perturb_uniform.k = param_values[i]
    data_perturb_normal.sigma = param_values[i]
    xts_perturbed = data_perturb_uniform.perturb_data(Xts)
    yc = clf.predict(xts_perturbed)
    test_error_uniform[i] = compute_ts_error(yc, yts)
    xts_perturbed = data_perturb_normal.perturb_data(Xts)
    yc = clf.predict(xts_perturbed)
    test_error_normal[i] = compute_ts_error(yc, yts)

# print(test_error)

plt.figure()
plt.plot(param_values, test_error_uniform, 'b', label="uniform")
plt.plot(param_values, test_error_normal, 'r', label="normal")
plt.title('Test error')
plt.xlabel(r'Perturbation size (K or $\sigma$)')
plt.legend()
plt.savefig('../figs/error_perturbed.pdf')
