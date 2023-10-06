import random as rd
import Hangman_art as art
import Hangman_word as words

chosen_word = rd.choice(words.word_list)
word_length = len(chosen_word)
image = "_"
display = []
end_game = False
lives = 6

print(art.logo)

for _ in range(word_length):
    display += image
    

print(f"Psss here's a Hint? {chosen_word}")


while not end_game:
    guess = input("Guess a letter: ").lower()
        
    if guess in display:
         print(f"You already guessed this {guess}.")       
    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        
    if guess not in chosen_word:        
        lives -=1
        print(f"You guessed {guess}, thas's not in the word. You lose on life.")
        if lives == 0:
            end_game = True
            print("You lose")    
        print(art.stages[lives])
       
    print(display) 
    
    if image not in display:
        end_game = True
        print("You win")
    
        

        
    



#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

#TODO-4: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.        

#TODO-5: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

#TODO-6: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.