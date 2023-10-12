def add(*args):
    result = 0
    for num in args:
        result += num
    return (result)


# print(add(10,20,40,60))


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    result = 0
    for key, value in kwargs.items():
        if key == "add":
            result = n + value
        elif key == "multiply":
            result = n * value
    return result

from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=800, height=600)
window.eval('tk::PlaceWindow . center')

# Label
my_label = Label(window, text="My label", anchor="center")
my_label.pack()

def button_click():
    if input.get() != "":
        my_label.config(text=input.get())
    else:
        my_label["text"] = "Button got clicked"



# button
button = Button()
button.config(text="Enter", command=button_click)
button.pack()


# Entry
input = Entry(width=10)
input.pack()


window.mainloop()



print(calculate(2, multiply=3))