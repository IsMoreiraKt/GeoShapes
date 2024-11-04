from shapes.shape import Shape


class Circle(Shape):
    def __init__(self, radius: int) -> None:
        self.radius = radius