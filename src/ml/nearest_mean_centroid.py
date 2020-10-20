import numpy as np
from sklearn.metrics import pairwise_distances


class NearestMeanCentroid():
    """Class for ..."""

    def __init__(self):
        self._centroids = None

    @property
    def centroids(self):
        return self._centroids

    # @centroids.setter
    # def centroids(self, value):
    #     self._centroids = value

    def fit(self, xtr, ytr):
        """
        Estimate the centroid for each class from the training data

        Parameters
        ----------
        xtr
            Training data

        ytr
            Labels

        Returns
        -------
        Classifier with estimated centroids.

        """
        labels = np.unique(ytr)
        self._centroids = np.zeros(shape=(labels.size, xtr.shape[1]))

        for i, label in enumerate(labels):
            self._centroids[i, :] = xtr[ytr == label, :].mean(axis=0)

        return self

    def predict(self, xts):
        """
        Compute predictions on test data.

        Parameters
        ----------
        xts
            Test data

        Returns
        -------
        Predicted labels for the test data.

        """
        if self._centroids is None:
            raise ValueError("Centroids not set. Run fit(x,y) first!")

        dist = pairwise_distances(xts, self._centroids)
        ypred = np.argmin(dist, axis=1)
        return ypred
