import random
import game_data
import highLowLogo
from os import name, system
import time

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def printDictionary(dict):
    for key in dict:
        if key == 'Follower_count':
            continue
        print(key,":", end=' ')
        print(dict[key])

score = 0
first = random.choice(game_data.data)
while True:
    print(highLowLogo.new_logo)
    second = random.choice(game_data.data)
    print("A: ")
    print(printDictionary(first))
    print(highLowLogo.vs)
    print("B: ")
    print(printDictionary(second))

    ch = input("Choose from 'A' and 'B' : ")
    if ch == 'A' and first['Follower_count'] > second['Follower_count']:
        score +=1
        print("Yes correct!! Your current score is : ", score)
        first = second
        time.sleep(3)
        clear()
    elif ch == 'B' and first['Follower_count'] < second['Follower_count']:
        score +=1
        print("Yes correct!! Your current score is : ", score)
        first = second
        time.sleep(3)
        clear()
    elif first['Follower_count'] == second['Follower_count']:
        score +=1
        print("Followers are equal!! Your current score is : ", score)
        first = second
        time.sleep(3)
        clear()
    else:
        print("You got wrong")
        print(f"Your score is {score}")
        break