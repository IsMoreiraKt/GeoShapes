from shapes.circle import Circle
from shapes.square import Square
from shapes.triangle import Triangle



def shape_handler(shape_name: str, shape_instance) -> None:
    while True:
        try:
            print(f"What would you like to calculate for the {shape_name}?")
            print("1 -> Area")
            print("2 -> Perimeter")
            print("0 -> Back to Main Menu")
            choice = int(input("Enter your choice: "))

            if choice == 0:
                return
            elif choice == 1:
                print(f"Area of the {shape_name}: {shape_instance.calculate_area()}")
            elif choice == 2:
                print(f"Perimeter of the {shape_name}: {shape_instance.calculate_perimeter()}")
            else:
                print("Please choose a valid option (1, 2, or 0).")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_shape_input(shape_type: str):
    try:
        if shape_type == 'circle':
            radius = float(input("Enter the radius of the circle: "))
            return Circle(radius)
        elif shape_type == 'square':
            side_length = float(input("Enter the length of the square's side: "))
            return Square(side_length)
        elif shape_type == 'triangle':
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            return Triangle(base, height)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return None


def main() -> None:
    print("----| Welcome to GeoShapes! |----")
    
    while True:
        print("Choose a shape to work with:")
        print("0 -> Exit\n1 -> Circle\n2 -> Square\n3 -> Triangle")
        try:
            choice = int(input("Enter your choice: "))
    
            if choice == 0:
                print("Exiting program. Goodbye!")
                break
            elif choice == 1:
                shape_instance = get_shape_input('circle')
    
                if shape_instance:
                    shape_handler('circle', shape_instance)
            elif choice == 2:
                shape_instance = get_shape_input('square')
    
                if shape_instance:
                    shape_handler('square', shape_instance)
            elif choice == 3:
                shape_instance = get_shape_input('triangle')
    
                if shape_instance:
                    shape_handler('triangle', shape_instance)
            else:
                print("Please choose a valid option (0, 1, 2, or 3).")
        except ValueError:
            print("Invalid input. Please enter a valid number.")



if __name__ == "__main__":
    main()