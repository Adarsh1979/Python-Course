import random
letters = ['a','b','c','d','e','f']
numbers = ['1','2','3','4','5','6']
symbols = ['!','#','$','&']
print("Welcome to PyPassword generator!!")
nr_letters = int(input("How many letters do you want in your password ?\n"))
nr_numbers = int(input("How many numbers do you want in your password ?\n"))
nr_symbols = int(input("How many symbols do you want in your password ?\n"))

password_list = []

for char in range (0,nr_letters) :
    password_list.append(random.choice(letters))

for i in range (0,nr_numbers) :
    password_list.append(random.choice(numbers))

for i in range (0,nr_symbols) :
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ""
for char in password_list :
    password += char
print(f"Your password is {password}")