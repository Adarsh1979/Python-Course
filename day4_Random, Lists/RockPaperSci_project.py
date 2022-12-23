# Rock paper and scissors game
import random
you = int(input("Press 0 for Rock, 1 for Scissor, 2 for Paper : "))
comp = random.randint(0,2)
# var = "variable"   -->  This is the logic to print Rock, Scissor, paper by 0, 1, 2
# if you == 0 :
#     var = "Rock"
# elif you == 1 :
#     var = "Paper"
# else :
#     var = "Scissor"
game_options = ["Rock","Scissor","Paper"]     # This is also the logic to print Rock, Scissor, paper by 0, 1, 2
print(f"You chosen {game_options[you]}\n")
print(f"Computer chosen {game_options[comp]}\n")
if (you == 0 and comp == 1) or (you == 1 and comp == 2) or (you == 2 and comp == 0): 
    print("You win !!!")
elif you == comp :
    print("Draw")
else :
    print("Computer wins !!!")