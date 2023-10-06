# Think of a dictionay been like a Table. where the left hand side we have the KEY (Bug, Function or Lopp) and the right side definition VALUE/

programmig_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    }


owner_pets_dictionary = {}


def insert_onwer(key, valeu):
    owner_pets_dictionary[key] = valeu

def change_petname(name, pet_name):
    if owner_pets_dictionary["ricardo"] == name:
       owner_pets_dictionary["ricardo"] = pet_name
  
     


insert_onwer("ricardo", "ulk")
insert_onwer("miguel", "leon")


owner_pets_dictionary["Michelle"] = "Katita"

print(owner_pets_dictionary)


for key in owner_pets_dictionary:    
#     name = input("What's your name:").lower()
#     pet_name = input("What's your pet's name:").lower()
     if key == "ricardo":
        owner_pets_dictionary[key] = "Hulk"


print(owner_pets_dictionary)


