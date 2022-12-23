import random
word_list = ["ardvark","baboon","camel"]
chosen_word = random.choice(word_list).lower()
# print(f"Chosen word is {chosen_word}")
display = []
for i in range(len(chosen_word)) :
    display.append('_')

end_of_game = False
lives = 4
while (not end_of_game) and lives != 0:
    guess = input("Input a character : ")
    if guess not in chosen_word :
        lives -= 1
        print(f"Your guess {guess} is not in the word. ", end="")
        print(f"You have {lives} lives remaining !!")
    elif guess in display :
        print(f"You already guessed {guess} , Try something different !!")
    for position in range(0,len(chosen_word)) :     # This loop is for checking if the character is present in display list 
        if guess == chosen_word[position] :              # or not and if present then replacing the '_' with that character
            display[position] = guess
    

    for position in display :               # This loop is for printing the current values of display list
        print(position, end = ' ')
    print()
    
    if not '_' in display :
        end_of_game = True
        
if lives == 0:
    print("You lose")
else :
    print("You win",end='')