# defining a function
count = 0
check = True

while check:
    print('Hello')
    count += 1
    if count == 6:
        check = False
 

while not at_goal():    
   if not wall_in_front():        
        move()
   else:
        jump2()

        
        
    
 

number_jump = 0

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():        
    turn_right
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
def jump2():    
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
    
    The functions move() and turn_left().
Either the test front_is_clear() or wall_in_front(), right_is_clear() or wall_on_right(), and at_goal().
How to use a while loop and if/elif/else statements.
It might be useful to know how to use the negation of a test (not in Python).