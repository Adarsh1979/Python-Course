# try:
#     file = open("a.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
#
# except FileNotFoundError:
#     file = open("a.txt", "w")
#     file.write("something")
# 
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
#
# else:
#     content = file.read()
#     print(content)
#
# finally:
#     file.close()
#     print("File was closed.")
#
#
# height = float(input("Height: "))
# weight = float(input("Weight: "))
#
# if height > 3:
#     raise  ValueError("Human height cannot be more than 3 metre")
#
# bmi = weight / height ** 2
# print(bmi)
