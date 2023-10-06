rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random as rd
player_choise = int(input("What do you choose? Type 0 for Rock, 1  for Paper or 2 for Scissors.\n"))
game_images = [rock, paper, scissors]

if (player_choise < 0) or (player_choise > 2):
    print("You typed an invalid number, you lose")
else:
    print(game_images[player_choise])

    print("Computer chose: ")

    computer_choise = rd.randint(0,2)    
    print(game_images[computer_choise])
        
    if (player_choise == 0) and (computer_choise == 2):
        print("You win")
    elif (player_choise == 1) and (computer_choise == 0):
        print("You win")
    elif (player_choise == 2) and (computer_choise == 1):
        print("You win")
    elif (player_choise == computer_choise):
        print("It's a draw")    
    else:
        print("You lose")