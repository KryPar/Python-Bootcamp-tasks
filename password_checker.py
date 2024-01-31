import re

def has_numbers(inputString):
   return any(char.isdigit() for char in inputString)

print("Welcome to the Password Checker! ")
print("- It must include at least 1 special character")
print("- It must be at least 7 characters long")
print("- It must include at least 1 number")

i = 0
while i<3 :
 enter_password = input ("Enter your password: ")
 regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

 if len(enter_password) >= 7:
  
   if regex.search(enter_password) == None:   
     print("Password must include at least 1 special character.")
     
   else:
     if has_numbers(enter_password):
       print("Password is strong")
     else: 
       print("Password must include at least 1 number.") 
       
 else:
  print("Password must be at least 7 characters long.")
  
 i += 1

