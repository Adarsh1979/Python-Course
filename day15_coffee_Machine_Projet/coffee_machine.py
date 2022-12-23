MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money" : 0
}


def areResoAvail(coffeeType):
    '''This function will take the coffee type and return True if resources for that coffee are available.'''
    water_avail = resources["water"]
    milk_avail = resources["milk"]
    coffee_avail = resources["coffee"]

    water_req = MENU[coffeeType]["ingredients"]["water"]
    milk_req = MENU[coffeeType]["ingredients"]["milk"]
    coffee_req = MENU[coffeeType]["ingredients"]["coffee"]

    if water_req <= water_avail and milk_req <= milk_avail and coffee_req <= coffee_avail:
        return True
    else:
        return False
    

def coinCalc():
    '''This function will perform inputting user coins and return the equivalent dollar amount of coins'''
    print("Please insert coins")
    quarters = int(input("How many quarters ?: "))
    dimes = int(input("How many dimes ?: "))
    nickles = int(input("How many nickles ?: "))
    pennies = int(input("How many pennies ?: "))
    total_dollar = (quarters*0.25) + (dimes*0.1) + (nickles*0.05) + (pennies*0.01)
    return total_dollar


def resourceModifier(coffee_type):
    '''This function will modify the resources of coffee machine as per coffee made'''
    resources["water"] = resources["water"] - MENU[coffee_type]["ingredients"]["water"]
    resources["milk"] = resources["milk"] - MENU[coffee_type]["ingredients"]["milk"]
    resources["coffee"] = resources["coffee"] - MENU[coffee_type]["ingredients"]["coffee"]
    resources["money"] += MENU[coffee_type]["cost"]

    
def coffee_machine(coffee_type):
    '''This will run all functions to serve coffee once for the given coffee type'''
    if areResoAvail(coffee_type):
        cost = MENU[coffee_type]["cost"]
        total_dollar = coinCalc()
        if cost <= total_dollar:
            print(f"Here is ${total_dollar-cost} in change")
            print("Here is your", coffee_type.title(), "☕ Enjoy!!")
            resourceModifier(coffee_type)
        else:
            print("Sorry that's not enough money. Money refunded. ")
    else:
        print("Coffee machine has been ran out of resources !!!")
        exit()


while True:
    user_input = input("What would you like (Espresso/ Latte/ Cappuccino) ? ").lower()
    if user_input == "report":
        for key in resources:
            print(key,":",resources[key])
    elif user_input == "off":
        exit()
    elif user_input == "espresso":
        coffee_machine("espresso")
    elif user_input == "latte":
        coffee_machine("latte")
    elif user_input == "cappuccino":
        coffee_machine("cappuccino")
    else :
        print("Invalid input")
        exit()