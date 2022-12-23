import random
from name_logo import logo
random_number = random.randint(1,100)
print(logo)
guessed_number = 0
level = input("Choose a difficulty level between 'easy' and 'hard' : ")
if level == "easy" :
    no_of_attempts = 10
else:
    no_of_attempts = 5

print(f"You have {no_of_attempts} attempts remaining")

while not no_of_attempts < 1:
    guessed_number = int(input("Guess a number between 1 and 100 : "))
    if guessed_number == random_number :
        print("You win😎")
        break
    elif guessed_number < random_number :
        print("Too low Guess again")
    else :
        print("Too high Guess again")

    no_of_attempts -= 1
    print(f"You have {no_of_attempts} attempts remaining\n")

print("You lose😭")