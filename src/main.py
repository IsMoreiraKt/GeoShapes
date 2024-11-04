from shapes.circle import Circle
from shapes.square import Square
import os



def circle_handler() -> None:
    while True:
        try:
            radius = float(input("Enter the radius of the circle: "))
            circle = Circle(radius)

            while True:
                print("What would you like to calculate?")
                print("1 -> Area")
                print("2 -> Perimeter")
                print("0 -> Back to Main Menu")

                choice = int(input("Enter your choice: "))

                if (choice == 0):
                    return
                elif (choice == 1):
                    print(f"Area of the circle: {circle.calculate_area()}")
                elif (choice == 2):
                    print(f"Perimeter of the circle: {circle.calculate_perimeter()}")
                else:
                    print("Please choose a valid option (1, 2, or 3).")
                    choice = None
        except ValueError:
            print("Invalid input. Please enter a valid number for the radius.")



def square_handler() -> None:
    while True:
        try:
            side_length = float(input("Enter the length of the square's side: "))
            square = Square(side_length)
        except ValueError:
            print("Invalid input. Please enter a valid number for the side length.")



def triangle_handler() -> None:
    pass



def main() -> None:
    exit_program = False

    print("----| Welcome to GeoShapes! |----")

    while not exit_program:
        print("Which picture do you want to use for the test?")

        try:
            choice = int(input("0 -> Exit\n1 -> Circle\n2 -> Square\n3 -> Triangle\n\t-> "))
        
            if (choice == 0):
                exit_program == True
            elif (choice == 1):
                circle_handler()
            elif (choice == 2):
                square_handler()
            elif (choice == 3):
                triangle_handler()
            else:
                print("Only numbers between 0 and 3, please.")
                choice = None
        except TypeError:
            print("Please enter numbers only.")

        print("\n\n\n")



if __name__ == '__main__':
    main()
    os.system('cls' if os.name == 'nt' else 'clear')