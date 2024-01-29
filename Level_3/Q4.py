# Define a class named Shape and its subclass Square. The Square
# class has an init function which takes length as argument. Both
# classes have an area function which can print the area of the
# shape where Shape’s area is 0 by default.

class Shape:
    def __init__(self):
        pass
    
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    
    def area(self):
        return self.length ** 2

# Create instances of Square
square1 = Square(5)
square2 = Square(7)

# Calculate and print the area of squares
print("Area of square 1:", square1.area())
print("Area of square 2:", square2.area())


