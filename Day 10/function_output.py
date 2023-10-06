# Funtions with outputs


def format_name(f_name, l_lastname):
    """Takes the first and the last name and format it in one String.

    Args:
        f_name (_type_): _description_
        l_lastname (_type_): _description_

    Returns:
        _type_: _description_
    """
    if  format_name == ""  or  l_lastname == "":
        return "You didn'r provide valid inputs"
       
    formated_full_name = f_name.title() + " " + l_lastname.title()   
    
    return formated_full_name

formated_name = format_name(input("What's your firstname: "), input("What's your lasttname: "))
print(formated_name)

# print('make IT PASCAL CaSe'.title() )

format_name()