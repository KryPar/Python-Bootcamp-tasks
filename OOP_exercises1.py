# class Rectangle:
#   def __init__(self, width, height):
#     self.width = width
#     self.height = height
       
#   def get_area(self):
#     area = (self.width * self.height)
#     print(f"The area of rectangle is :{area}")

#   def get_perimeter(self):
#     perimeter = 2 * (self.width + self.height)
#     print(f"The perimeter of rectangle is :{perimeter}")

# rectangle = Rectangle(4,5)

# rectangle.get_area()

# rectangle.get_perimeter()

# class Person:

#   def __init__(self, name, age,gender):
#     self.name = name
#     self.age = age
#     self.gender = gender
       
#   def introduce(self):
#     print(f"Hello, my name is {self.name}. I am {self.gender} and I am {self.age} years old.")


# person1 = Person("Ben Hurr", 41,"male")

# person1.introduce()


# class Book:

#     def __init__(self, title, author, gendre):
#        self.title = title
#        self.author = author
#        self.gendre = gendre
       
#     def get_title(self):
#         print(f"Title of book: {self.title}")

#     def get_author(self):
#         print(f"Author of book: {self.author}")

#     def get_gendre(self):
#         print(f"Gendre of book: {self.gendre}")

# book1 = Book("Witcher","Andrzej Sapkowski","Fantasy")

# book1.get_title()
# book1.get_author()
# book1.get_gendre()



# class Student:

#     def __init__(self, name, age, major,GPA):
#        self.name = name
#        self.age = age
#        self.major = major
#        self.GPA = GPA
       
#     def get_name(self):
#         print(f"Name of student: {self.name}")

#     def get_age(self):
#         print(f"Age of student: {self.age}")

#     def get_major(self):
#         print(f"Major of student: {self.major}")

#     def get_GPA(self):
#         print(f"GPA of student: {self.GPA}")

#     def get_calculate(self):
#         if not 0 <= self.GPA <= 4:  
#           print("Invalid GPA")
#         elif self.GPA >= 3.7:
#           print("Grade is A")
#         elif self.GPA >= 3.0:
#           print("Grade is B")
#         elif self.GPA >= 2.0:
#           print("Grade is C")
#         elif self.GPA >= 1.0:
#           print("Grade is D")
#         else:  
#            print("Grade is F")

# student1 = Student("Ken Green",21,"Space engineering", 2.8)

# student1.get_name()
# student1.get_age()
# student1.get_major()
# student1.get_GPA()
# student1.get_calculate()

class Animal:

  def __init__(self, name, species):
    self.name = name
    self.species = species
      
  def get_name(self):
    print(f"Name of animal: {self.name}")

  def get_species(self):
    print(f"Species of student: {self.species}")

  def eat(self,food):
    print(f"{self.name} is eating {food}")

  def sleep(self):
    print(f"{self.name} is sleeping ")  

animal1 = Animal("Rocky","Dog ")

animal1.get_name()

animal1.get_species()

animal1.eat("kibble")

animal1.sleep()