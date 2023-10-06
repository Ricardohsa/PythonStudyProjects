# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random as rd
len_list = len(names)
who_pays = str(names[rd.randint(0,len_list - 1)])
print(f"{who_pays} is going to but the meal today!")