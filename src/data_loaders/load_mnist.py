import pandas as pd
import numpy as np


def load_mnist_data(filename, n_samples=None):
    """
    This function returns MNIST handwritten digits and labels as ndarrays.
    """
    data = pd.read_csv(filename)
    data = np.array(data)  # cast pandas dataframe to numpy array
    if n_samples is not None:  # only returning the first n_samples
        data = data[:n_samples, :]
    y = data[:, 0]
    x = data[:, 1:] / 255.0
    return x, y
