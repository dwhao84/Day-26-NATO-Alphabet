import pandas as pd

# Read the CSV file
data = pd.read_csv("nato_phonetic_alphabet.csv")
data_dict = data.to_dict()

# TODO 1: Create the dictionary in the format {"A": "Alfa", "B": "Bravo"}
new_dict = {data_dict['letter'][i]: data_dict['code'][i] for i in range(26)}
print("NATO Phonetic Alphabet Dictionary:")
print(new_dict)

# TODO 2: Create a list of phonetic code words from user input
entered_letters = input("Enter your letters: ").upper()

# Build the list of phonetic code words
# 要再重新了解這段寫法
phonetic_words = [new_dict[letter] for letter in entered_letters if letter in new_dict]

print("\nPhonetic code words for your input:")
print(phonetic_words)


