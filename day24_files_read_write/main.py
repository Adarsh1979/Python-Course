# # Method 1:  (Closing a file is necessary)
# my_file = open("file1.txt", mode="r")  # by default file is in read only mode
# contents = my_file.read()
# print(contents)
# my_file.close()

# # Method 2: (Closing a file is not required)
# with open("file1.txt") as my_file_2:
#     contents2 = my_file_2.read()
#     print(contents2)


# # example of writing new content in the file
# with open("file1.txt", mode="w") as my_file_2:
#     my_file_2.write("Good Morning")


# # Example of appending something in the file
# with open("file1.txt", mode="a") as my_file_2:
#     my_file_2.write("\nEveryone")


# # example of creating file if it doesn't exist
# with open("file2.txt", mode="w") as my_file3:
#     my_file3.write("New file created")


# with open("C:/Users/Adarsh/Desktop/file1.txt") as my_file_2:
#     contents2 = my_file_2.read()
#     print(contents2)

with open("../../../Notes and Programs/file1.txt") as my_file_2:
    contents2 = my_file_2.read()
    print(contents2)
