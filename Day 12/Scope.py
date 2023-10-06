# # Scope
# enemies = 1

# def increase_enemies():
#   print(f"enemies inside function: {enemies}")
#   return enemies + 1

# enemies = increase_enemies()
# print(f"enemies outside function: {enemies}")


# Local Scope

# def drink_potion():
#     position_strenght = 2
#     print(position_strenght)
    
# drink_potion()
# print(position_strenght)

# Global
# player_health = 10

# def game():
#     def drink_potion():
#         position_stregth = 2
#         print(player_health)
        
#     drink_potion()
    
    
# game()


# Constant
PI = 3.14159


def food():
    i = 100
    return 100


food()