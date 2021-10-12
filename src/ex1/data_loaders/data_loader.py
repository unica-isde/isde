from abc import ABC, abstractmethod, abstractproperty


class DataLoader(ABC):
    """
    Abstract class for implementing data loaders,
    returning data X and their class labels y
    """

    @abstractmethod
    def load_data(self):
        raise NotImplementedError('load_data not implemented!')
