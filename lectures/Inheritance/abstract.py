from abc import ABC


class TestClass(ABC):

    __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        pass
