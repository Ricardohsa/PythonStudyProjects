def create_letters():
    with open("./Names/invited_names.txt") as names_to_invite:
        names = names_to_invite.readlines()
        list_guest =[sub.replace('\n', '') for sub in names]
        for guest in list_guest:
            get_letter(guest)


def get_letter(guest):
    with open("./Letters/starting_letter.txt") as letter_ie:
        letter_ = letter_ie.read()
        new_letter = (letter_.replace("[name]", guest))
        save_letter(new_letter, guest)


def save_letter(letter_content, guest):
    filename = f"../Output/ReadyToSend/letter_for_{guest}.txt"
    with open(filename, "a") as letter:
        letter.write(letter_content)


create_letters()
