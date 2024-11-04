from shapes.shape import Shape



class Square(Shape):
    def __init__(self, side: float) -> None:
        self.side = side


    def calculate_area(self) -> float:
        return self.side ** 2
    

    def calculate_perimeter(self) -> float:
        return 4 * self.side