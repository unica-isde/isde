import numpy as np

from ex1.data_perturb import DataPerturb


class DataPerturbUniform(DataPerturb):

    def __init__(self, k=1.0):
        self.k = k

    @property
    def k(self):
        return self._k

    @k.setter
    def k(self, value):
        self._k = float(value)

    def perturb_data(self, x):
        noise = np.random.random_sample(size=x.shape)
        scaled_noise = 2 * self._k * noise - self._k
        x_perturbed = x + scaled_noise
        # clipping values outside of [0,1]
        x_perturbed[x_perturbed >= 1] = 1
        x_perturbed[x_perturbed <= 0] = 0
        return x_perturbed
