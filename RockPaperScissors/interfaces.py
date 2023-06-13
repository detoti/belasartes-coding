from abc import ABC, abstractmethod

class Strategy (ABC):
    @abstractmethod
    def selection(self) -> None:
        pass