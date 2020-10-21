import pandas as pd
import numpy as np

from data_loaders import DataLoader


class DataLoaderMNIST(DataLoader):

    def __init__(self, filename='../data/mnist_data.csv'):
        self.filename = filename
        self._width = 28
        self._height = 28

    @property
    def filename(self):
        return self._filename

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @filename.setter
    def filename(self, value):
        if not isinstance(value, str):
            raise TypeError("Filename is not a string!")
        # else
        self._filename = value

    def load_data(self):
        data = pd.read_csv(self._filename)
        data = np.array(data)  # cast pandas dataframe to numpy array
        y = data[:, 0]
        x = data[:, 1:] / 255.0
        return x, y
