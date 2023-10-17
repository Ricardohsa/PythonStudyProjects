import random
from tkinter import *
import pandas as pd
import random

FONT_NAME = "Courier"
BACKGROUND_COLOR = "#B1DDC6"
timer = 0
to_learn = {}
# ---------------------------- RANDON WORD ------------------------------- #

try:
    words = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = words.to_dict(orient="records")


current_card = []


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text, text='French', fill="black")
    canvas.itemconfig(new_word, text=current_card['French'], fill="black")
    canvas.itemconfig(card_back_ground, image=card_front_img)
    flip_timer = window.after(3000, flip_card)


def generate_know_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text, text='French', fill="black")
    canvas.itemconfig(new_word, text=current_card['French'], fill="black")
    canvas.itemconfig(card_back_ground, image=card_front_img)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(title_text, text='English', fill="white")
    canvas.itemconfig(new_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_back_ground, image=card_back_img)

# ---------------------------- WORDS LEARNED ------------------------------- #

def is_know():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card")
window.eval('tk::PlaceWindow . center')
window.config(padx=10, pady=10, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas()
canvas.config(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
card_back_ground = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, columnspan=2, row=0)

title_text = canvas.create_text(400, 200, text="Title", fill="black", font=("Ariel", 40, "italic"))
new_word = canvas.create_text(400, 350, text="Current", fill="black", font=("Ariel", 35, "bold"))

wrong_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_img)
unknown_button.config(highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

right_img = PhotoImage(file="images/right.png")
known_button = Button(image=right_img)
known_button.grid(column=1, row=1)
known_button.config(highlightthickness=0, command=is_know)


next_card()
window.mainloop()
