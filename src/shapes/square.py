from shapes.shape import Shape



class Square(Shape):
    def __init__(self, side: float) -> None:
        self.side = side


    def calculate_area(self):
        return self.side ** 2