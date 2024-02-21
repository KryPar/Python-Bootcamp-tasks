class Circle:

    def __init__(self, radius):
        self._radius = radius

    @property
    def diameter(self):
       return 2 *self._radius

    
circle1 = Circle(2)

print(f" Diameter: {circle1.diameter}")


class Person:

    def __init__(self, first_name,last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def first_name(self):
        return self._first_name
    
    @property
    def last_name(self):
        return self._last_name
    
    @first_name.setter
    def first_name(self,f_value):

        if type(f_value) != str or f_value == "":
            raise ValueError("First name cannot be empty")
            
        
        self._first_name = f_value
    
    @last_name.setter
    def last_name(self,l_value):

        if type(l_value) != str or l_value == "":
            raise ValueError("First name cannot be empty")
            
        
        self._last_name =  l_value




person1 = Person("Kevin", "Clain")

person1.first_name= "john"

person1.last_name= "Red"

print(person1.first_name)

print(person1.last_name)


class Rectangle: 

    def __init__ (self, width, height):
        if width < 1 or height < 1:
           raise ValueError("Width and height must be positive numbers.")
        self.width = width  
        self.height = height

    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
    
    @width.setter
    def width(self,value):

        if value < 1:
            raise ValueError("Error, width must be a positive number.")
        else:   
         self._width = value

    @height.setter
    def height(self,value):

        if value < 1:
            raise ValueError("Error, height must be a positive number.")
        else: 
         self._height =  value

    @property
    def area(self):
        return self._width * self._height

rectangle = Rectangle(2,4)



print(rectangle.area)



class BankAccount:
   
   def __init__ (self, account_number, initial_balance):
        self.account_number = account_number
        self._balance = initial_balance

   @property
   def balance(self):
       return  self._balance
   
   
   def deposit(self,amount):
       self._balance += amount
       print(self._balance)

   def withdraw(self,amount):
        self._balance -= amount
        print(self._balance)

   @property
   def is_overdrawn(self):
       if self._balance < 0:
          return True
       else:
           return False
       

bankacc1 = BankAccount (78964512, 2000)

bankacc1.withdraw(200)
      
bankacc1.deposit(400)

print(bankacc1.is_overdrawn)