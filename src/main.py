import os



def circle_handler() -> None:
    pass



def square_handler() -> None:
    pass



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