from abc import ABC, abstractmethod



class Shape(ABC):
    @abstractmethod
    def calculate_area(self) -> float:
        pass

    @abstractmethod
    def calculate_perimeter(self) -> float:
        pass