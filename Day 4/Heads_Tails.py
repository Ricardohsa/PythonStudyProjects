#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇
import random 

head_Tail =random.randint(0,1)

if (head_Tail == 0):
    print("Heads")
else:
    print("Tails")