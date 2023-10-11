import turtle
import pandas as pd
from turtle import Turtle, Screen

screen = Screen()
screen.title("U.S State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guess_states = []
STYLE = ('Courier', 12, 'italic')
data = pd.read_csv("50_states.csv")

all_states = data.state.tolist()


def write_missing_state(state):
    add_state = Turtle()
    add_state.hideturtle()
    add_state.penup()
    add_state.color("red")
    state_date = data[data["state"] == state]
    add_state.goto(int(state_date.x), int(state_date.y))
    add_state.write(state_date.state.item(), font=STYLE, align="center")
    guess_states.append(answer_state)


while len(guess_states) < 50:
    answer_state = screen.textinput(title=f"{len(guess_states)}"
                                          f"/50States Correct", prompt="What's another state name?").title()
    if answer_state == "Exit":
        missing_states = [item for item in all_states if item not in guess_states]
        df = pd.DataFrame(missing_states)
        df.to_csv("missing_states.csv")
        for state in missing_states:
            write_missing_state(state)
        break
    elif answer_state in all_states:
        add_state = Turtle()
        add_state.hideturtle()
        add_state.penup()
        add_state.color("black")
        state_date = data[data["state"] == answer_state]
        add_state.goto(int(state_date.x), int(state_date.y))
        add_state.write(state_date.state.item(), font=STYLE, align="center")
        guess_states.append(answer_state)






print(missing_states)

# while not not_end_game:
#     answer_state = screen.textinput(title=f"{score}/50States Correct", prompt="What's another state name?")
#     state_name = data[data.state == answer_state]
#
#     if not state_name.empty:
#
#         add_state = Turtle()
#         add_state.hideturtle()
#         add_state.penup()
#         add_state.color("black")
#         x_position = data[data["state"] == answer_state].x
#         y_position = data[data["state"] == answer_state].y
#         add_state.goto(int(x_position), int(y_position))
#         add_state.write(answer_state, font=STYLE, align="center")
#
#
#         correct_states.append(state_name.state)
#
#         score += 1
#
#         print(len(correct_states))
#     else:
#         pass





screen.exitonclick()