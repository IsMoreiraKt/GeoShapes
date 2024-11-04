from shapes.shape import Shape



class Triangle(Shape):
    def __init__(
        self, base: float, height: float, 
        first_side: float, second_side: float
    ) -> None:
        self.base = base
        self.height = height
        self.first_side = first_side
        self.second_side = second_side

    
    def calculate_area(self) -> float:
        return (self.base * self.height) / 2