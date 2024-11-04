from shapes.shape import Shape
import math



class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius


    def calculate_area(self) -> float:
        return math.pi * (self.radius ** 2)
    

    def calculate_perimeter(self) -> float:
        return 2 * math.pi * self.radius