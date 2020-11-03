import numpy as np

from ex1.data_perturb import DataPerturb


class DataPerturbNormal(DataPerturb):

    def __init__(self, sigma=1.0):
        self.sigma = sigma

    @property
    def sigma(self):
        return self._sigma

    @sigma.setter
    def sigma(self, value):
        self._sigma = float(value)

    def perturb_data(self, x):
        noise = np.random.standard_normal(size=x.shape)  # N(0, 1)
        scaled_noise = self.sigma * noise  # N(0, sigma)
        x_perturbed = x + scaled_noise
        # clipping values outside of [0,1]
        x_perturbed[x_perturbed >= 1] = 1
        x_perturbed[x_perturbed <= 0] = 0
        return x_perturbed
