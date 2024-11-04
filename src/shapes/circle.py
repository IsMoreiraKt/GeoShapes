from shapes.shape import Shape
import math



class Circle(Shape):
    def __init__(self, radius: int) -> None:
        self.radius = radius


    def calculate_area(self) -> float:
        return math.pi * (self.radius ** 2)