class Person:

    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def introduce(self):
        print(f"Hello, my name is {self.first_name} {self.last_name}.")
    

class Employee(Person): 
    def __init__(self,first_name,last_name, employee_id):
        super().__init__(first_name,last_name)
        self.employee_id = employee_id

    def introduce(self):
        print(f"Hello, my name is {self.first_name} {self.last_name} {self.employee_id}.")
    

person1 = Person("John", "Reed")
person1.introduce()

employe1 = Employee ("John", "Reed",17565)
employe1.introduce()

class Shape:

    def __init__(self,color):
        self.color = color

    def description (self):
        print(f"This shape is {self.color} ")

class Square(Shape):
    def __init__(self,color,side_length):
        super().__init__(color)
        self.side_length = side_length

    def description(self):
        print(f"This square is {self.color} and has side length of {self.side_length}")


shape1 = Shape("red")

shape1.description()

square1 = Square("red","5 cm")
square1.description()

class Vehicle:
    def __init__(self,wheels):
        self.wheels = wheels

    def drive (self):
        print(f"The vehicle is driving.")

class Car(Vehicle):
    def __init__(self):
        super().__init__(4)
        
    def drive(self,speed = None):
        if speed is None:
            print("The car is driving")
        else:
            print(f"The car is driving at {speed} mph")


vehicle1 = Vehicle(5)
vehicle1.drive()

car1 = Car()
car1.drive(2)

class Rectangle:

    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width*self.height

class Square(Rectangle):
    def __init__(self,side_lenght):
        super().__init__(side_lenght,side_lenght)
        

    def perimeter(self):
        return 4*self.width


rectangle = Rectangle(4,5)
            
print(f"Rectangle area: {rectangle.area()}")

square = Square(4)
print(f"Square area: {square.area()}")
print(f"Square perimeter: {square.perimeter()}")