# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}
#
# #TDO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
#
# #TDO 2. Create a list of the phonetic code words from a word that the user inputs.

# ---------------------------------------------------------------------------------------------------------------------#


# NATO Alphabet project


import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# My method(to get the required dictionary):
# codes = []
# for (index, row) in data.iterrows():
#     codes.append(row.code)
#
# phonetic_dict = {value[:1]: value for value in codes}


# Angela's method(to get the required dictionary):

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}      # dictionary comprehension

# ********* Either this (Using while loop) *********

# my_bool = True
# while my_bool:
#     user_input = input("Enter a word: ").upper()
#     try:
#         users_code_list = [phonetic_dict[letter] for letter in user_input]        # list comprehension
#     except KeyError:
#         print("Sorry, only letters are allowed")
#     else:
#         print(users_code_list)
#         my_bool = False


# ******** or this (Using functions)*********
def generate_phonetic():
    user_input = input("Enter a word: ").upper()
    try:
        users_code_list = [phonetic_dict[letter] for letter in user_input]        # list comprehension
    except KeyError:
        print("Sorry, only letters are allowed")
        generate_phonetic()
    else:
        print(users_code_list)


generate_phonetic()
