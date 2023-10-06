#Step 1 
import random
import hangman_art as art
import hangman_words as words

print(art.logo)

chosen_word = random.choice(words.word_list)

lives = 6
end_of_game = False


image = "_"
display = []

for word in chosen_word:
    display.append(image)
    

    
count = 0
while not end_of_game:    
    print(f"hint {chosen_word}")
    guess = input("Guess a letter:").lower()
    
    if guess in chosen_word:
        print(f"You've already guessed {guess}")
    
    for chose in chosen_word:
        if guess == chose:
            display[count] = (guess)                
            print(display)
        count += 1                 
             
    
    if image in display: 
        # guess = input("Guess a letter:").lower()
        count = 0  
    
    if image not in display:
        end_of_game = True
        print("You win")      
      
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")   
        lives -= 1    
        print(display)          
        if lives == 0:
            print("You lost")       
            end_of_game = True 
 
    print(art.stages[lives])
   