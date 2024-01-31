print( "Welcome to the Magic Potion shop!")
print ("Here are the potions we offer:")

potions = { "Invisibility Potion": ["Moonstone", "Dragon scale", "Fairy dust"], "Flying Potion": ["Phoenix feather", "Troll tooth", "Mermaid scale"], "Healing Potion": ["Unicorn horn", "Elf hair", "Golden apple"] }

for key in potions :
    print(f"{key}")
choose_p = input ("Which potion would you like to buy ingredients for ?")

if choose_p == "Invisibility Potion":
 print(f"The ingredients for Invisibility Potion are:  " )

 for ingredients in potions[choose_p] :
    print(f"{ingredients}")

 print("Let's start buying the ingredients!")

 ingredients = potions["Invisibility Potion"]
 index = 0

 while index < len(ingredients):
    ingredient = ingredients[index]
    response = input(f"Do you want to buy {ingredient}? (yes/no) ")

    if response.lower() == 'yes':
        print(f"You bought {ingredient}!")
        index += 1
         
 
    else:
        print("You chose to stop shopping.")
        break

 if index == len(ingredients):
    print(f"Congratulations! You bought all the ingredients for {choose_p}!")
 
 
        

elif choose_p == "Flying Potion":
 print("The ingredients for Flying Potion are: ")

 for ingredients in potions[choose_p] :
    print(f"{ingredients}")

 print("Let's start buying the ingredients!")

 ingredients = potions["Flying Potion"]
 index = 0

 while index < len(ingredients):
    ingredient = ingredients[index]
    response = input(f"Do you want to buy {ingredient}? (yes/no) ")

    if response.lower() == 'yes':
        print(f"You bought {ingredient}!")
        index += 1
    else:
        print("You chose to stop shopping.")
        break

 if index == len(ingredients):
    print(f"Congratulations! You bought all the ingredients for {choose_p}!")
 


elif choose_p == "Healing Potion":
 print("The ingredients for Healing Potion are: ")

 for ingredients in potions[choose_p] :
    print(f"{ingredients}")

 print("Let's start buying the ingredients!")

 ingredients = potions["Healing Potion"]
 index = 0

 while index < len(ingredients):
    ingredient = ingredients[index]
    response = input(f"Do you want to buy {ingredient}? (yes/no) ")

    if response.lower() == 'yes':
        print(f"You bought {ingredient}!")
        index += 1
        
    else:
        print("You chose to stop shopping.")
        break

 if index == len(ingredients):
    print(f"Congratulations! You bought all the ingredients for {choose_p}!")



else:
  print ("Wrong potion")


