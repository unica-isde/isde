from sklearn.datasets import fetch_lfw_people

from data_loaders import DataLoader


class DataLoaderLFW(DataLoader):

    def __init__(self, min_faces_per_person=10):
        self._min_faces_per_person = min_faces_per_person
        self._width = None
        self._height = None

    @property
    def min_faces_per_person(self):
        return self._min_faces_per_person

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def load_data(self):
        dataset = fetch_lfw_people(min_faces_per_person=10)
        n_samples, self._height, self._width = dataset.images.shape
        x = dataset.data
        y = dataset.target
        return x, y
