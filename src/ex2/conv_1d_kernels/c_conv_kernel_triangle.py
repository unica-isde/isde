from .c_conv_kernel import CConvKernel
import numpy as np


class CConvKernelTriangle(CConvKernel):

    def kernel_mask(self):
        self._mask = np.zeros(self.kernel_size)
        for i in range(self.kernel_size // 2):
            self._mask[i] = i + 1
            self._mask[-1-i] = i + 1
        self._mask[(self.kernel_size // 2)] = (self.kernel_size // 2) + 1
        self._mask /= np.sum(self._mask)
