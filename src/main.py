import os



def main():
    exit_program = False

    print("----| Welcome to GeoShapes! |----")

    while not exit_program:
        print("Which picture do you want to use for the test?")

        try:
            choice = int(input("0 -> Exit\n1 -> Circle\n2 -> Square\n3 -> Triangle\n\t-> "))
        
            if (choice == 0):
                exit_program == True
        except TypeError:
            print("Please enter numbers only.")

        print("\n\n\n")



if __name__ == '__main__':
    main()
    os.system('cls' if os.name == 'nt' else 'clear')