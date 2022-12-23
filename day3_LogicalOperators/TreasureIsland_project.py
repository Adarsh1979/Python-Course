# Treasure island game project
print("___________________Treasure Island Game___________________")
print("Your mission is to find the Treasure by making your decisions wisely !!!")
first = input('You have two options "Left" or "Right". What will you select? \n').lower()
if first == "right":
    print("You entered a place full of Pythons.\nThey will now enjoy you.\nGame Over!!!")
elif first == "left":
    print("Okay you proceeded")
    second = input('What would you like to "Swim" or "Wait" ?\n').lower()
    if second == "swim":
        print("You can swim only in gutter nearby.\nSo go again and try to come after bathing up\nGame over !!")
    elif second == "wait":
        print("You are smart enough to win the game\nLet us see if you can or not\n")
        third = input('You have now three doors "Red" "Blue" or "Yellow", which one will you prefer? ').lower()
        if third == "red" or third == "blue" :
            print("Game over\n")
        elif third == "yellow" :
            print("You win the treasure game\n")
        else:
            print("Better luck next time\nGame over!!!\n")
    else:
        print("Please type correctly\n")
else :
    print("You should enroll yourself in typing course !!!")
            