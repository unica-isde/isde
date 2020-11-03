from copy import deepcopy


class CConvKernelCombo(object):
    def __init__(self, filters):
        self._filters = []
        self.filters = filters

    @property
    def filters(self):
        return self._filters

    @filters.setter
    def filters(self, value):
        self._filters = value

    def kernel(self, x):
        xp = deepcopy(x)
        for i in range(len(self.filters)):
            xp = self.filters[i].kernel(xp)
        return xp
