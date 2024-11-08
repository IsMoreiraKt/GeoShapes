# GeoShapes
GeoShapes is a demonstration project that uses Python's abc library to create abstract base classes. The program offers a command-line interface where users can calculate the area and perimeter of basic geometric shapes such as circles, squares and triangles. This project highlights the principles of object-oriented programming, especially the use of abstract classes to define consistent interfaces.

## Features
- **Circle Calculations**
    - Area
    - Perimeter (circumference)
- **Square calculations**
    - Area
    - Perimeter
- **Triangle calculations**
    - Area
    - Perimeter
User-friendly interface with input validation to ensure correct data.

## Structure
The project is structured using abstract base classes to ensure a consistent interface for all shape classes. The Python standard library `abc` is used to define these interfaces.

## Modules
- `shapes.circle`: Contains the Circle class, which inherits from the Shape abstract class and implements methods for calculating area and perimeter.
- `shapes.square`: Contains the Square class, which inherits from the Shape abstract class and implements methods for calculating area and perimeter.
- `shapes.triangle`: Contains the Triangle class, which inherits from the Shape abstract class and implements methods for calculating area and perimeter.
- `shapes.shape`: Contains the Shape abstract base class, defined using the abc library.