############DEBUGGING#####################

# Describe Problem
# for llop run from 1 to 20
# supposed to print the statement when i is equal to 20 
# the for loop goes from 1 to 19
# options: 1 change the for loop to run from 1 to 21 or add 20 + 1, or change the if 
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
      
# my_function()

# # Reproduce the Bug
# list index out of range
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# # Play Computer
# it doesn't compare when the input is equal to 1980 do 1994
# year = int(input("What's your year of birth?"))
# if year >= 1980 and year <= 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# age = int(input("How old are you?"))
# if age > 18:
#    print(f"You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])

for number in range(1, 101):  
  if (number % 3 == 0 and number % 5 == 0):
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")  
  else:
    print([number])