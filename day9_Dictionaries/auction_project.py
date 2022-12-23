from os import name, system
# from time import sleep
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

auction = {}
flag = "yes"
while flag == "yes":
    bidder_name = input("What is your name ? ")
    bid_value = int(input("Enter your bid : $"))
    auction[bidder_name] = bid_value
    flag = input("Is there any other who wants to bid ? Type 'yes' or 'no' ").lower()
    clear()

highest_bid = 0   
highest_bidder = ""
for bidder in auction :
    if auction[bidder] > highest_bid :
        highest_bid = auction[bidder]
        highest_bidder = bidder

print(f"{highest_bidder} is the winner of auction with the highest bid of ${highest_bid}")