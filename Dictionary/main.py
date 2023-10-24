

# Write a Python script to sort (ascending and descending) a dictionary by value.
# dictionary = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

# ascending = dict(sorted(dictionary.items(), key=lambda item: item[1]))

# descending = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
# print(ascending)

# print(descending)

# Write a Python program to add a key to a dictionary

# Sample Output

# dictionary = {"Name" : "Ram" , "Age" : 23}

# add_key = {"City" : "Salem"}

# dictionary.update(add_key)

# print(dictionary)

# 3. Write a Python program to concatenate following dictionaries to create a new one.

# Sample Output

# dictionary_1 = {"Name" : "Ram" , "Age" : 23}

# dictionary_2 = {"City" : "Salem", "Gender" : "Male"}

# Concatenate Dictionaries = {'Name' : 'Ram', 'Age' : 23, 'City' : 'Salem', 'Gender': 'Male'}

# concatenaded = {}
# concatenaded.update(dictionary_1)
# concatenaded.update(dictionary_2)

# concatanete = {**dictionary_1, **dictionary_2}
# print(concatanete)

# Write a Python program to check whether a given key already exists in a dictionary.

# Sample Output

# my_dict = {'Name' : 'Ram', 'Age' : 23,}
# k = 'Name'

# for key, value in my_dict.items():
#     if key == k:
#         print(f'The {k} is Available in the dictionary')

# Write a Python program to iterate over dictionaries using for loops.


# my_dict = {"Name" : "Ram" , "Age" : 23 , "City" : "Salem", "Gender" : "Male"}

# for key, value in my_dict.items():
#     print(f'{key}: {value}')

#  Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

# l = int(input("Enter a limit: "))
# my_dict = {}
# for i in range(1, l+1):
#     my_dict[i] = i*i


# my_dict2 = {i: i*i for i in range(1, l+1)}
# print(my_dict2)

# 7.Write a Python script to print a dictionary where the keys are numbers between 1 and n (both included) and the values are square of keys.

# limit = int(input("Enter the limit: "))
# new_dict = {i: i**i for i in range(1, limit+1)}
# print(new_dict)

# 10. Write a Python program to sum all the items in a dictionary.


# my_dit = {1 : 23, 2 : 45, 3 : -17, 4 : 87}
# result = 0

# for key, value in my_dit.items():
#     result += value

# print(f"Sum the all items = {result}")


# 11. Access dictionary key’s element by index.

# sample = {"Name" : "Pooja", "Age" : 23, "Gender" : "Female", "City" : "Salem", "Mark" : 488}
# print(sample["Age"])

dict_empty_items = {'Name' : 'Pooja', 'Age' : 23, 'Gender' : None, 'Mark' : 488, 'City' : None}
dict_no_empty = {key: value for key, value in dict_empty_items.items() if value != None}
print(dict_no_empty)