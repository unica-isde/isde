from abc import ABC, abstractmethod
import numpy as np
from copy import deepcopy


class CConvKernel(ABC):

    def __init__(self, kernel_size=3):
        self._mask = None
        self.kernel_size = kernel_size  # call setter (odd number)

    @property
    def kernel_size(self):
        return self._kernel_size

    @property
    def mask(self):
        return self._mask

    @abstractmethod
    def kernel_mask(self):
        raise NotImplementedError("Method not implemented yet")

    @kernel_size.setter
    def kernel_size(self, value):
        if (value % 2) == 0:
            raise ValueError("The kernel size must be an odd number.")
        # else:
        self._kernel_size = value
        self.kernel_mask()

    def kernel(self, x):
        xp = deepcopy(x)
        k = int((self.kernel_size - 1) / 2)
        for i in range(k, x.size - k):
            v = x[i - k:i + k + 1]
            xp[i] = np.dot(v, self._mask)
        return xp
