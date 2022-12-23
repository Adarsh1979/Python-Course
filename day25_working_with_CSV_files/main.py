# In this list&dict_compre_demo.py, we are seeing different methods to read the CSV file


# Method 1: to get the data from the CSV file
# with open("weather_data.csv") as file:
#     data = file.readlines()
#
# for i in range(0, len(data)):
#     new_item = data[i].strip()
#     data[i] = new_item


# ------------------------------------------------------------------------------#


# Method 2: Using in-built library CSV
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#             print(row)
#     print(temperature)


# ------------------------------------------------------------------------------#


# Method 3: Using pandas library
# import pandas
# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["day"])


# ------------------------------------------------------------------------------#


# now exploring pandas library

import pandas
data = pandas.read_csv("weather_data.csv")

# print(type(data))       # here data is Dataframe object (representing whole table)
# print(type(data["temp"]))       # data["temp"] is Series object (representing particular column of table)

# data_dict = data.to_dict()        # converting our data from DataFrame object to dictionary
# print(data_dict)

# temp_list = data["temp"].to_list()    # converting our data from DataFrame object to list
# print(temp_list)


# Challenge: how to calculate the average of all temperatures from above list obtained
# Method1: using traditional way
# average = sum(temp_list) / len(temp_list)
# print(average)


# Method2: using method of Series class in pandas library
# print(data["temp"].mean())

# print(data)
# print(data["temp"].max())   #data["temp"] canbe used to run methods of Series class bcoz data["temp"] returns a column


# Extracting columns: (Both methods given below are valid to get hold of a column from table)
# print(data["temp"])
# print(data.temp)      # It's like accessing variable of struct in c language

# Extracting row/rows:
monday_data = data[data.day == "Monday"]
print(monday_data.condition)    # we can use "." to get hold of further data like ROW.condition or ROW.temp or ROW.day

# print(data[data.temp == data.temp.max()])       # getting the row having maximum temperature

# creating a dataframe from dictionary
# data_dict = {
#     "students": ["Adarsh", "Sahil", "Ankit"],
#     "scores": [98, 75, 80]
# }
#
# converted_data = pandas.DataFrame(data_dict)
# print(converted_data)

# converted_data.to_csv("new_csv")
