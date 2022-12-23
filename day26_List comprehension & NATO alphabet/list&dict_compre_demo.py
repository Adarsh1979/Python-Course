# -----------------------------------------------------------------------------------------------------------#
# List comprehension demo

# numbers = [1, 2, 3]
# new_numbers = [n+1 for n in numbers]
# print(new_numbers)

# nums2 = [2*n for n in range(1, 5)]
# print(nums2)

# names = ["Adarsh", "Ankit", "Sahil", "Shubham", "Krunal"]
# big_names = [name.upper() for name in names if len(name) > 5]
# print(big_names)
# -----------------------------------------------------------------------------------------------------------#


# -----------------------------------------------------------------------------------------------------------#
# Challenge1: make a list which is square of a given list
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = [n**2 for n in numbers]
# print(squared_numbers)


# Challenge2: make a list of even numbers from a given list
# numbers = [1, 2, 3, 4, 5]
# even_numbers = [num for num in numbers if num % 2 == 0]
# print(even_numbers)


# Challenge3: make a list of numbers which are common in file1.txt and file2.txt
# with open("file1.txt") as f1:
#     f1_nums = f1.readlines()
#
#     # for i in range(0, len(f1_nums)):
#     #     f1_nums[i] = int(f1_nums[i].strip())
#
# with open("file2.txt") as f2:
#     f2_nums = f2.readlines()
#
#     # for i in range(0, len(f2_nums)):
#     #     f2_nums[i] = int(f2_nums[i].strip())
#
# print(f1_nums)
# print(f2_nums)
#
# common_nums = [int(num) for num in f1_nums if num in f2_nums]
# print(common_nums)
# -----------------------------------------------------------------------------------------------------------#


# -----------------------------------------------------------------------------------------------------------#
# Dictionary comprehension demo

# student_scores = {
#     "Adarsh": 60,
#     "Ankit": 76,
#     "Sahil": 47,
#     "Om": 45
# }
#
# passed_students = {name: score for (name, score) in student_scores.items() if score > 50}
# print(passed_students)
# -----------------------------------------------------------------------------------------------------------------#


# -----------------------------------------------------------------------------------------------------------#
# Challenge1: create a dictionary of words as key and number of letters as value from given sentance
# sentence = "What is the airspeed velocity of an unladen Swallow?"
# # list_of_words = sentence.split()
# # print(list_of_words)
#
# words_dict = {word: len(word) for word in sentence.split()}     # we can use split() directly over here as well
# print(words_dict)


# Challenge2: create a dictionary weather_F(temp in ℉) from existing dictionary of weather_C(temp in ℃)
# weather_C = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24
# }
#
# weather_F = {key: (value * 1.8 + 32) for (key, value) in weather_C.items()}  # .items() is must to iterate thru dict
# print(weather_F)

# ---------------------------------------------------------------------------------------------------------------------#


# -----------------------------------------------------------------------------------------------------------#
# Iterating over pandas DataFrame
# students_dict = {
#     "student": ["Adarsh", "Ankit", "Sahil"],
#     "score": [56, 87, 71]
# }

# looping thru dictionaries: (This method is not very useful)
# for (key, value) in students_dict.items():
#     print(value)


# import pandas
#
# students_data_frame = pandas.DataFrame(students_dict)
# print(students_data_frame)

# looping thru dataframe METHOD1:
# for (key, value) in students_data_frame.items():
#     print(value)


# looping thru dataframe METHOD2:
# for (index, row) in students_data_frame.iterrows():
#     print(row.score)
#     print(row.score)
