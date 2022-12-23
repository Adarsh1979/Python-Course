# Day4: 3/9 challenge
# import random
# while (True) :
#     random.seed(input("Create a seed number : "))
#     random_int = random.randint(0,1)
#     if random_int == 0:
#         print("Heads")
#     else:
#         print("Tails")





# Day4: 5/9 challenge
# import random
# random.seed(input("Create a seed number : "))
# nameAsCSV = input('Give me everybody name seperated by a ", "\n')
# names = nameAsCSV.split(", ")
# random_int = random.randint(0,len(names)-1)
# print(f"{names[random_int]} is going to buy the meal today !!")





# Day4: 7/9 challenge
row1 = ["☠️","☠️","☠️"]
row2 = ["☠️","☠️","☠️"]
row3 = ["☠️","☠️","☠️"]
map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to store the treasure? (Enter column number and then row number)")
col_num = int(position[0])
row_num = int(position[1])
map[row_num-1][col_num-1] = "X"
print(f"{row1}\n{row2}\n{row3}")
