from abc import ABCMeta, abstractmethod, abstractproperty


class DataPerturb(object):
    """
    Abstract class for implementing data perturbation models
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def perturb_data(self, x):
        raise NotImplementedError('perturb_data not implemented!')
