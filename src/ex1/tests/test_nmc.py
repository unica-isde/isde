import unittest
import numpy as np

from ex1 import NearestMeanCentroid


class TestNMC(unittest.TestCase):

    def setUp(self):
        n_samples = 100
        n_features = 20
        self.x = np.zeros(shape=(n_samples, n_features))  # a matrix of zeros
        self.y = np.zeros(shape=(n_samples,))  # some random labels
        self.y[int(n_samples / 2):] = 1  # y =[0 ... 0 1...1]
        self.clf = NearestMeanCentroid()

    def test_fit(self):
        # check if centroids are None right after init
        self.assertIsNone(self.clf.centroids)
        self.clf.fit(self.x, self.y)

        self.assertIsNotNone(self.clf.centroids)
        n_classes = np.unique(self.y).size
        n_features = self.x.shape[1]
        self.assertEqual((n_classes, n_features), self.clf.centroids.shape)
        self.assertTrue((self.clf.centroids == 0).all())

    def test_predict(self):
        self.assertIsNone(self.clf.centroids)
        self.clf.fit(self.x, self.y)
        yc = self.clf.predict(self.x)
        self.assertTrue(yc.ndim == 1)
        self.assertEqual(yc.shape[0], self.x.shape[0])


if __name__ == '__main__':
    unittest.main()
