from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


while True:
    user_input = input("What would you like (Espresso/ Latte/ Cappuccino) ? ").lower()
    if user_input == "report":
        my_money = CoffeeMaker()
        my_money.report()
    elif user_input == "off":
        exit()
    elif user_input == "espresso":
        c1 = Menu()
        print(c1.menu)
        c2 = CoffeeMaker()
        # print(c2.is_resource_sufficient(espresso))
    elif user_input == "latte":
        print("hello")
    elif user_input == "cappuccino":
        print("hello")
    else :
        print("Invalid input")
        exit()