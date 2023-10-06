import random
import art
import game_data 
score = 0
is_game_over = True


def select_option_a():
    """Select the first celebrity to be compared

    Returns:
        _type_: _description_
    """

    random_celebrity = random.randint(0, 49)
    
    return game_data.data[random_celebrity]


option_a = select_option_a()


def select_option_b():
    """Select the second celebrity to be compared

    Returns:
        _type_: _description_
    """
    random_celebrity = random.randint(0, 49)
    
    if game_data.data[random_celebrity] != option_a:
        return game_data.data[random_celebrity]
    else:
        random_celebrity = random.randint(0, 49)
        return game_data.data[random_celebrity]  
    

option_b = select_option_b()


def compare_celebrities(guess):
    """  compare two celebrities and return a score 1 if the user guess correct or zero if the user is wrong.

    Returns:
        _type_: _description_
    """
    if guess == "A" and int(option_a['follower_count']) > int(option_b['follower_count']):
        return 1
    elif guess == "B" and int(option_b['follower_count']) > int(option_a['follower_count']):
        return 1
    else:
        return 0


def play_game():

    print(f"Compare A: {option_a['name']}, {option_a['description']}, from {option_a['country']}, "
          f"number of followers {option_a['follower_count']} ")

    print(art.vs)

    print(f"Compare B: {option_b['name']}, {option_b['description']}, from {option_b['country']}, "
          f"number of followers {option_b['follower_count']} ")


print(art.logo)


while is_game_over is not False:
    total_score = 0
    play_game()

    total_score += compare_celebrities(input("Who's has more followers Type? 'A' or 'B': "))

    score += total_score
    
    if total_score == 0:
        is_game_over = False
        print(f"Sorry, that's wrong. Final score: {score}")
    else:
        print(f"You're right! Current score: {score}")
        option_a = option_b
        option_b = select_option_b()
     