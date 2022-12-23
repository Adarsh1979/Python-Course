# num = int(input("Which number do you want to check ? "))
# if num%2 == 0:
#     print("Entered number is even.\n")
# else:
#     print("Entered number is odd.\n")






# weight = float(input("Enter your weight in kilograms : "))
# height = float(input("Enter your height in metres : "))
# bmi = round(weight/(height*height), 1)
# if bmi < 18.5:
#     print(f"Your BMI is {bmi} and you are Underwight\n")
# elif 18.5 <= bmi < 25:
#     print(f"Your BMI is {bmi} and you are Normal\n")
# elif 25 <= bmi < 30:
#     print(f"Your BMI is {bmi} and you are Overweight\n")
# elif 30 <= bmi < 35:
#     print(f"Your BMI is {bmi} and you are Obese\n")
# else:
#     print(f"Your BMI is {bmi} and you are Clinically Obese\n")







# year = int(input("Enter the year you want to check : "))
# if (year % 4 == 0):
#     if (year % 100 == 0):
#         if (year % 400 == 0):
#             print(f"The year {year} is a Leap year")
#         else:
#             print(f"The year {year} is not a Leap year")
#     else:
#         print(f"The year {year} is a Leap year")
# else:
#     print(f"The year {year} is not a Leap year")

# or we can also write it as
# if ((year%4 == 0 and year%100 != 0) or (year%400 == 0)):
#     print("This is leap year.")
# else:
#     print("This is not a leap year")







# Day 3 8/12 challenge
# print("Welcome to Python Pizza shop !!")
# size = input("What size pizza do you want? S for small, M for medium, L for large ")
# add_pepperoni = input("Do you want to add pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# bill = 0
# if size == "S" :
#     bill = 15
#     if add_pepperoni == "Y" :
#         bill += 2
# elif size == "M" :
#     bill = 20
#     if add_pepperoni == "Y" :
#         bill += 3
# else :
#     bill = 25
#     if add_pepperoni == "Y" :
#         bill += 3


# if extra_cheese == "Y" :
#     bill += 1

# print(f"Your final bill is {bill}")






# Day3 10/12 challenge
print("Welcome to love calculator !!")
your_name = input("What is your name? ").lower()
partner_name = input("What's your partner name? ").lower()
name = your_name + partner_name

true_count = name.count('t') + name.count('r') + name.count('u') + name.count('e')
love_count = name.count('l') + name.count('o') + name.count('v') + name.count('e')

score = int(str(true_count)+str(love_count))

if score<=10 and score>90:
    print(f"Your score is {score}, You go together like coke and mentos ")
elif score>=40 and score<50:
    print(f"Your score is {score}, You are alright together ")     
else:
    print(f"Your score is {score}")