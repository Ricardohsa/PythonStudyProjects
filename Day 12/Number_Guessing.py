import random
import arts


print(arts.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")


number_be_gueesed = random.choice(range(1,100))
print(f"Pssst. The correct answer is {number_be_gueesed}")

end_of_game = False
attempts = 10

def compare(number_guessed):
    global attempts 
    global end_of_game
    
    attempts -=1
    if number_guessed == number_be_gueesed:
        end_of_game = True
        return (f"You got it! The answer was {number_be_gueesed}")
    elif attempts == 0 and number_guessed > number_be_gueesed:
        return("Too high\nYou've run out of guesses, you lose.")
    elif attempts == 0 and number_guessed < number_be_gueesed:
        return("Too low\nYou've run out of guesses, you lose.")
    elif number_guessed > number_be_gueesed:       
        # attempts -=1
        return ("Too high\nGuess again.")
    elif number_guessed < number_be_gueesed:       
        # attempts -=1
        return ("Too low\nGuess again.")
    elif attempts == 0:
        end_of_game = True
        return ("You've run out of guesses, you lose")

# print(easy_level) 

while not end_of_game:
    
    if input("Choose a difficulty. Type 'easy' or 'hard': ") == "easy":
        attempts = 10
    else:
        attempts = 5
        
    
    for i in range(1, attempts + 1):
        if end_of_game == True:
            break      
        elif attempts == 0:
            end_of_game = True
            break
        
        print(f"You have {attempts} attempts remaining to guess the number")    
        number_guessed = int(input("Make a guess: "))
        print(compare(number_guessed))      
        
       

