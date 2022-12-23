import random
def sum(list_p):
    sum = 0
    for item in list_p:
        sum += item
    return sum

def comparison():
    print("Your final hand :",user_card, "and sum is",user_sum)
    print("Computer's final hand :",comp_card, "and sum is",comp_sum)
    if user_sum == 21 :
        print("BLACKJACK🤑 You win")
    elif comp_sum == 21 :
        print("Computer has BLACKJACK, you lose😭")
    elif user_sum > 21 :
        print("You went over!!! You lose😭")
    elif comp_sum > 21 :
        print("Computer went over!!! You win😎")
    elif user_sum == comp_sum :
        print("Draw")
    elif user_sum > comp_sum :
        print("You win😎")
    elif user_sum < comp_sum :
        print("You lose😭")
    elif comp_sum == 21 and user_sum == 21 :
        print("Draw")
    

print("*************** BLACKJACK GAME ****************")
card_list = [11,2,3,4,5,6,7,8,9,10,10,10,10]
user_card = []
comp_card = []
user_card.append(random.choice(card_list))
user_card.append(random.choice(card_list))
comp_card.append(random.choice(card_list))
comp_card.append(random.choice(card_list))
user_sum = sum(user_card)
comp_sum = sum(comp_card)
print("Your cards are :",user_card, "and sum is",user_sum)
print("Computer's first card is :",comp_card[0])

if 11 in user_card and sum(user_card) > 21 :
    user_sum = user_sum - 10
    # user_card.remove(11)
    user_card.insert(user_card.index(11),1)

while not comp_sum >= 17 :
    comp_card.append(random.choice(card_list))
    comp_sum = sum(comp_card)
    if 11 in comp_card and sum(comp_card) > 21 :
        comp_sum = comp_sum - 10
        # comp_card.remove(11)
        comp_card.insert(comp_card.index(11),1)
        comp_sum = sum(comp_card)

while (input("Do you want to 'hit' or 'stand' ? ") == "hit") :
    if 11 in user_card and sum(user_card) > 21 :
        # user_sum = user_sum - 10
        user_card.insert(user_card.index(11),1)
        user_card.remove(11)

    user_card.append(random.choice(card_list))
    user_sum = sum(user_card)
    print("Your cards are :",user_card, "and sum is",user_sum)


    if user_sum > 21 :
        break
comparison()

# OP WORK !!!
# Some bugs related to Ace card score are pending to be fixed