import math
# # If Else statement
# print("Welcome to the rollercoaster!! ")
# height = int(input("What is your Height in cm? "))
# age = int(input("What is your age? "))

# bill = 0

# if height >= 120:
#     print('Congratulation 🎊 , you can ride')
#     if (age < 12):        
#         bill = 5
#         print('Child tickt are $5')
#     elif (age >= 12 and age < 18):
#          bill = 7
#          print('Youth tickt are $7')
#     elif(age >= 18 and age <=44):
#          bill = 12
#          print('Adult tickt are $12')
#     elif(age >= 45 and age <= 55):
#          bill = 0
#          print('Adult tickt are $0')

#     wants_photo = input("Do you want a photo taken? Y or N.")         
    
#     if (wants_photo == "Y"):
#         # adds $3
#         bill = bill + 3
        
        
#     print(f"Your final bill is {bill} ")

# else:
#    print("Sorry 😞, you can't ride ")


# # 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# if number % 2 == 0:
#     print('This is an even number.')
# else:
#     print('This is an odd number.')
    
    
# # 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# bmi =  math.ceil((weight/ (height **2)))

# if bmi < 18.5:
#     print(f"Your BMI is {bmi}, you are underweight.")    
# elif bmi > 18.5 and bmi < 25:
#     print(f"Your BMI is {bmi}, you have a normal weight.")    
# elif bmi > 25 and bmi < 30:
#     print(f"Your BMI is {bmi}, you are slightly overweight.")    
# elif bmi > 30 and bmi < 35:
#     print(f"Your BMI is {bmi}, you are obese.")        
# elif bmi > 35:
#     print(f"Your BMI is {bmi}, you are clinically obese.")        
    
    
# Leap Year
# year = int(input("Which year do you want to check year\n"))
# if (year % 4) == 0:
#     if (year % 100) == 0:
#         if (year % 5) == 0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")        
#     else:
#         print("Leap year.")    
# else:
#     print("Not leap year.")
        

#  Pizzza

# # 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# pizza_price = 0

# # toppings
# pepperoni_small_pizza = 2
# pepperoni_medium_large = 3
# extra_cheese_price = 1

# if (size == "S"):
#    pizza_price = 15 
#    if (add_pepperoni == "Y"):
#        pizza_price = pizza_price + pepperoni_small_pizza
       
#    if ( extra_cheese == "Y"):
#        pizza_price = pizza_price + extra_cheese_price
# elif (size == 'M'):
#     pizza_price = 20
#     if (add_pepperoni == "Y"):
#        pizza_price = pizza_price + pepperoni_medium_large
       
#     if ( extra_cheese == "Y"):
#        pizza_price = pizza_price + extra_cheese_price
# elif (size == 'L'):
#     pizza_price = 25
#     if (add_pepperoni == "Y"):
#        pizza_price = pizza_price + pepperoni_medium_large
       
#     if ( extra_cheese == "Y"):
#        pizza_price = pizza_price + extra_cheese_price       
       
# print(f"Your final bill is: ${pizza_price}.")

# 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇    
# name1 = name1.lower()
# name2 = name2.lower()

# t = name1.count('t') + name2.count('t')
# r = name1.count('r') + name2.count('r')
# u = name1.count('u') + name2.count('u')
# e = name1.count('e') + name2.count('e')
# totalTrue = (t + r + u+ e)

# l = name1.count('l') + name2.count('l')
# o = name1.count('o') + name2.count('o')
# v = name1.count('v') + name2.count('v')
# e = name1.count('e') + name2.count('e')
# totalLove = (l + o + v + e)

# loveScore = int(str(totalTrue) + str(totalLove))

# if (loveScore < 10) or (loveScore > 90):
#     print(f"Your score is {loveScore}, you go together like coke and  mentos.")
# elif (loveScore >= 40) and (loveScore <= 50):
#     print(f"Your score is {loveScore}, you are alright together.")
# else:    
#     print(f"Your score is {loveScore}.")

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
choice1 =  input('You\'re at a crossroad, where do you want to go? "left" or "right".\n')



if choice1 == 'right':
    print("You fell into a hole. Game Over. 🕳️🕳️🕳️🕳️🕳️🕳️🕳️")
elif choice1 == 'left':
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
    if choice2 == "swim":
        print("You get attacked by an angry trout. Game Over")
    elif choice2 == 'wait':
        door = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n')
        if door == "red":
            print("Burned by fire. Game Over. 🔥🔥🔥🔥🔥🔥")
        elif door == "blue":
            print("Eaten by beasts. Game Over. 👹👹👹👹👹👹")
        elif door == "yellow":
            print("You Win! 🏆🏆🏆🏆🏆")
        else:
            print("You chose a door that doesn't exist. Game Over. 😭😭😭😭😭")
    else:
        print("You chose a option that doesn't exist. Game Over. 😭😭😭😭😭")
else:
    print("You chose a option that doesn't exist. Game Over. 😭😭😭😭😭")
            