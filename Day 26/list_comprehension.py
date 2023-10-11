#new_list = [new_item for item in list]
names = ["Alex", 'Beth', "Caroline", "Dave", "Eleanor", "Freddie"]
new_list_names = [name.upper() for name in names if len(name) > 5]
print(new_list_names)


base = 3
exponent = 4
print(pow(base, exponent))