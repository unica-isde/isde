from .c_conv_kernel import CConvKernel
import numpy as np


class CConvKernelMovingAverage(CConvKernel):

    def kernel_mask(self):
        kernel = np.ones(shape=self.kernel_size)
        k = np.sum(kernel)
        self._mask = (1 / k) * kernel
