import random
import itertools
import collections
from operator import itemgetter
from itertools import groupby

# sum_list = [1,7,-10,34,2,-8]
# result = sum(sum_list)


# list2 = [3,4,5,4,7]
# result = 1
# for item in list2:
#     result *= item
#
# print(result)

# list = [1,7,10,34,2,8]
# result = max(list)
# print(result)

# list = [51,7,10,34,2,8]
# result = min(list)
# print(result)
#
# list = [1,2,3,7,2,1,5,6,4,8,5,4]
# dup = set()
# uniq = []
# for item in list:
#    if item not in uniq:
#        uniq.append(item)
#    else:
#        dup.add(item)
# print(dup)
# print(uniq)

# list = [34,45,6,5,4,56,7]
# if len(list) == 0:
#     print("List is Empty")
# else:
#     print(list)
#
# list = [10, 22, 44, 23, 4]
# copy = []
# clone = list
# clone2 = []
# for item in list:
#     copy.append(item)
# print(copy)
# print(clone)
#
# clone2 = clone.copy()
# print(clone2)


# Find the List of Words that are Longer than n from a given List of Words
# list = ['Words', 'Longer', 'given', 'Words']
# for item in list:
#     if len(item) > 4: print(item)

# 10. Write a Program that get two lists as input and check if they have at least one common member
# list = [1,2,3,4,5]
# list2 = [5,6,7,8,9]
#
# list_common = [item for item in list if item in list2]
# print(list_common)
#
#
# for item in list:
#     if item in list2:
#         print(item)

# 11. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. (enumerate)

# list1 = ["Cat", "Dog", "Elephant", "Fox", "Tiger", "Lion", "Ponda"]
# list2 = ['Dog', 'Elephant', 'Fox', 'Ponda']
#
# # list1.remove("Cat")
# # list1.remove("Tiger")
# # list1.remove("Lion")
# # list2.remove("Dog")
#
# # animal = [item for item in list1 if item not in ("Cat", "Tiger", "Lion")]
# animal = [item for item in enumerate(list1) if item not in (0,4,5)]
# print(animal)

# 12. Write a Python program to print the numbers of a specified list after removing even numbers from it

# list1 = [7, 32, 81, 20, 25, 14, 23, 27]
# list2 = [7, 81, 25, 23, 27]
# result1 = [item for item in list1 if item % 2 != 0]
# result2 = [item for item in list2 if item % 2 != 0]
# print(result1, result2)

# or
#
# for item in list1:
#     if item % 2 != 0:
#         print(item)
#
# for item in list2:
#     if item % 2 != 0: print(item)

# 13. Write a Python program to shuffle and print a specified list (shuffle)


# animal1 = ["Cat", "Dog", "Elephant", "Fox", "Tiger", "Lion", "Ponda"]
# animal2 = ['Fox', 'Cat', 'Tiger', 'Lion', 'Dog', 'Ponda', 'Elephant']
# random.shuffle(animal1)
# random.shuffle(animal2)
# print(animal1)


# 14. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30

# list1 = [1, 4, 9, 16, 25, 625, 676, 729, 784, 841]
# for item in list1:
#     if item**2 in range(1,30):
#         print(item)

# 15. Write a Python program to generate all permutations of a list in Python. (itertools)
#
# list1 = [1,2,3,5,4]
# list2 = [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
#
# print(list(itertools.permutations(list1)))


# 16. Write a Python program to convert a list of characters into a string
#
# list = ['T','u','t','o','r',' ','J','o','e','s']
# word =''
# for item in list:
#     word += item
# print(word)
#
# word2 = ''.join(list)
# print(word2)


# 17. Write a Python program to find the index of an item in a specified list

# list = [20, 70, 30, 90, 10, 30, 90, 10, 80]
#
# # Item to find the index of 30
#
# # Index Number of Item = 2
#
# print(list.index(30))

# 18. Write a Python program to flatten a shallow list

# list1 = [[20,30,70],[30,90,10], [30,20], [70,90,10,80]]
#
# # [20, 30, 70, 30, 90, 10, 30, 20, 70, 90, 10, 80]
#
# new_list =[]
#
# for item in list1:
#     for i in item:
#         new_list.append(i)
# print(new_list)
#
# merge_list = list(itertools.chain(*list1))
# print(merge_list)

# 19. Write a Python program to add a list to the second list

# list_num =[10, 20, 30, 40]
# list_animals = ["Cat", "Dog", "Lion", "Ponda"]
# merged = [item for item in (list_animals, list_num)]
#
# merged2 = list_num
# for num in list_animals:
#     merged2.append(num)
#
# print(merged2)
#

# 20. Write a Python program to select an item randomly from a list Using random.choice()
# animals = ["Cat", "Dog", "Elephant", "Fox", "Tiger", "Lion", "Ponda"]
# print(random.choice(animals))

# 21. Write a python program to check whether two lists are circularly identical

# list1 = [8, 8, 12, 12, 8]
#
# list2 = [8, 8, 8, 12, 12]
#
# list3 = [1, 8, 8, 12, 12]
#
# if collections.Counter(list1) == collections.Counter(list2):
#     print("True")

# 22. Write a Python program to find the second smallest number in a list
# #
# list_1 = [2,4,56,78,4,34,5,8,9]
# smallest_list = sorted(list_1, reverse=False)
# print(smallest_list[1])


# min_num = min(list)
#
# list.remove(min_num)
# second_smallest = min(list)
# print(second_smallest)


# 23. Write a Python program to find the second largest number in a list

# list1 = [82,4,56,78,4,34,5,100,9]
# sorted_list = sorted(list1, reverse=True)
#
# print(sorted_list[1])

# largest_num = max(list)
# list.remove(largest_num)
# second_largest_num = max(list)
# print(second_largest_num)


# 24. Write a Python program to get unique values from a list

# my_list =[82, 4, 10, 56, 78, 4, 34, 5, 10, 9]
# unique_values = list(set(my_list))
# print(unique_values)

# my_list = [34, 4, 5, 9, 10, 78, 82, 56]
# unique_value = list(set(my_list))
# print(unique_value)

# 26. Create a list by concatenating a given list which range goes from 1 to n


# my_list = ['T', 'J']
# N = 10
# concate_list = []
#
# for count in range(1,N+1):
#     for item in my_list:
#        concate_list.append(item + str(count))
#
#
# conc_list = [item + str(i) for i in range(1, N+1) for item in my_list ]
# print(conc_list)

# 28. Write a Python program to find common items from two lists
#
#
# my_list1 =[23,45,67,78,89,34]
# my_list2 =[34,89,55,56,39,67]
# common_items = sorted([item for item in my_list1 if item in my_list2], reverse=False)
# print(common_items)
#
# set1 = set(my_list1)
# set2 = set(my_list2)
#
# common_ =  sorted(list(set1.intersection(set2)), reverse=False)
# print(common_)



# 29. Write a Python program to split a list based on first character of word

# my_list = ["cat", "dog", "cow", "tiger", "lion", "Fox", "Shark", "Snake", "turtle", "mouse", "monkey", "bear"]
# for ltr, word in groupby(sorted(my_list), key=itemgetter(0)):
#     print(ltr)
#     for w in word:
#         print(" ",w)

# 30. Write a Python program to select the odd number of a list

# my_list = [1,2,4,3,6,7,5,8,9,7,8,9,10]
# odd_number_list = []
#
# odd_number_list2 = [num for num in my_list if num%2 != 0]
# print(odd_number_list2)
#
# for num in my_list:
#     if num%2 != 0:
#         odd_number_list.append(num)
#
# print(odd_number_list)

# 31. Write a Python Program to count unique values inside a list


# my_list = [10, 20, 30, 50, 80, 70, 70, 80, 10]
# new_list = set(my_list)
# print(len(new_list))

# 32. Write a Python Program to List product excluding duplicates


# my_list = [2, 1, 2, 4, 6, 4, 3, 2, 1]
# result = []
# element_couts = collections.Counter(my_list)
# print(element_couts)
#
# for element in my_list:
#     product = element ** element_couts[element]
#     result.append(product)
#
# print(result)

# Duplication removal list product : 144

# 33. Write a Python Program to Extract elements with Frequency greater than 2
#
# my_list = [4, 6, 4, 3, 3, 4, 3, 7, 8, 8]
# frequency = collections.Counter(my_list)
# di = dict(frequency)
# result=[]
#
# for key, value in di.items():
#     if value > 2:
#         result.append(key)
# print(result)
#
#
#
#
# result_2 = [element for element, count in frequency.items() if count > 2]
#
# print(result_2)

# 34. Write a Python Program to Test if List contains elements in Range


[4, 5, 6, 7, 3, 9]