from abc import abstractmethod, ABC


class RouterBase(ABC):
    @abstractmethod
    def mount(self, app):
        pass