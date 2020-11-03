from ex1.utils import plot_ten_images
from ex1.data_loaders import DataLoaderMNIST

from ex2.conv_1d_kernels import CConvKernelMovingAverage, \
    CConvKernelTriangle, CConvKernelCombo

import numpy as np
from random import randint
import matplotlib.pyplot as plt

data_loader = DataLoaderMNIST()
X, y = data_loader.load_data()

# create filter instances
k_avg = CConvKernelMovingAverage()
k_trn = CConvKernelTriangle()
k_cmb = CConvKernelCombo(filters=[k_avg, k_trn, k_avg])

# filters = [k_avg, k_trn, k_cmb]

# take one image at random per class
classes = np.unique(y)
images = np.zeros(shape=(classes.size, X.shape[1]))
for i in range(classes.size):
    images_per_class = X[y == classes[i], :]
    idx = randint(0, images_per_class.shape[0])
    images[i, :] = images_per_class[idx, :]

# no filter
titles = ["digit " + str(i) for i in range(10)]
plot_ten_images(images, 28, 28, titles)
plt.suptitle("Original Images")
plt.savefig('../figs/examples-nofilter.pdf')

# moving average
modified_images_ma = np.zeros(shape=images.shape)
for i in range(images.shape[0]):
    modified_images_ma[i] = k_avg.kernel(images[i])

plot_ten_images(modified_images_ma, 28, 28, titles)
plt.suptitle("Images - moving average filter")
plt.savefig('../figs/examples-mov-avg.pdf')

# triangle
modified_images_triangle = np.zeros(shape=images.shape)
for i in range(images.shape[0]):
    modified_images_triangle[i] = k_trn.kernel(images[i])

plot_ten_images(modified_images_triangle, 28, 28, titles)
plt.suptitle("Images - triangle filter")
plt.savefig('../figs/examples-triangle.pdf')

# combo
modified_images_combo = np.zeros(shape=images.shape)
for i in range(images.shape[0]):
    modified_images_combo[i] = k_cmb.kernel(images[i])

plot_ten_images(modified_images_combo, 28, 28, titles)
plt.suptitle("Images - combo filter")
plt.savefig('../figs/examples-combo.pdf')
