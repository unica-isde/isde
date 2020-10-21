from abc import ABCMeta, abstractmethod, abstractproperty


class DataLoader(object):
    """
    Abstract class for implementing data loaders,
    returning data X and their class labels y
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def load_data(self):
        raise NotImplementedError('load_data not implemented!')
