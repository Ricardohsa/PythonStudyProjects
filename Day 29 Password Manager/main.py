from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letter + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    user_data = []
    website = website_entry.get()
    email = username_entry.get()
    password =password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0:
        messagebox.showerror(title="Oops", message="Please, make sure you enter the Website name!")
    elif len(password) == 0:
        messagebox.showerror(title="Oops", message="Please, make sure you enter the Password!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading the old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Saving update data
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data wth the new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving update data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()

# ---------------------------- SEARCH ------------------------------- #
def find_password():
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
        try:
            jsonData = data[website_entry.get()]
        except KeyError:
            messagebox.showerror(title="Password Recovery", message="No details for the website exists.")
        else:
            email = jsonData['email']
            password = jsonData['password']
            messagebox.showerror(title="Password Recovery", message=f"Email: {email}, Password: {password}")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.eval('tk::PlaceWindow . center')
window.config(padx=50, pady=50, bg="white")

canvas = Canvas()
canvas.config(width=200, height=200, bg="white")
locker_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=locker_image)
canvas.grid(column=1, row=0)

website_label = Label()
website_label.config(text="Website: ", bg="white")
website_label.grid(column=0, row=1)

website_entry = Entry()
website_entry.config(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

username_label = Label()
username_label.config(text="Email/Username: ", bg="white")
username_label.grid(column=0, row=2)

username_entry = Entry()
username_entry.config(width=38, bg="white")
username_entry.grid(column=1, columnspan=2, row=2)
username_entry.insert(0, "r.humberto.sa@gmail.com")

password_label = Label()
password_label.config(text="Password: ", bg="white")
password_label.grid(column=0, row=3)

password_entry = Entry()
password_entry.config(width=21, bg="white")
password_entry.grid(column=1, row=3)

generate_psw_button = Button()
generate_psw_button.config(text="Generate Password", bg="white", command=generator)
generate_psw_button.grid(column=2, row=3)

add_button = Button()
add_button.config(text="Add", bg="white", width=36)
add_button.grid(column=1, columnspan=2, row=4)

add_button.config(command=save_password)

search_button = Button()
search_button.config(text="Search", bg="white", width=12, command=find_password)
search_button.grid(column=2,  row=1)

window.mainloop()
