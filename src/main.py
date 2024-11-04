def main():
    exit_program = False

    print("----| Welcome to GeoShapes! |----")

    while not exit_program:
        print("Which picture do you want to use for the test?")

        try:
            choice = int(input("0 -> Exit\n1 -> Circle\n2 -> Square\n3 -> Triangle\n\t-> "))
        except TypeError:
            print("Please enter numbers only.")



if __name__ == '__main__':
    main()