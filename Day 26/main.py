import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# keep_ask = True


# while keep_ask:
#     word = input("Enter a word: ").upper()
#     try:
#         list_phonetic = [phonetic_dict[letter] for letter in word]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
#     else:
#         list_phonetic = [phonetic_dict[letter] for letter in word]
#         print(list_phonetic)
#         keep_ask = False



def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
      list_phonetic = [phonetic_dict[letter] for letter in word]
    except KeyError:
      print("Sorry, only letters in the alphabet please.")
      generate_phonetic()
    else:
      list_phonetic = [phonetic_dict[letter] for letter in word]
      print(list_phonetic)

generate_phonetic()