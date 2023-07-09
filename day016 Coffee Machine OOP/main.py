from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
machine = MoneyMachine()
menu = Menu()

# print report

# check resources sufficient

# check money sufficient

# make coffee

turn_off = False

while not turn_off:
    print(f"what would you like? {menu.get_items()}")
    order = input("report/off for getting report/turn off machine: ").lower().strip()

    while order != "cappuccino" and order != "latte" and order != "espresso" and order != "off" and order != "report":
        print("❎ INVALID INPUT ❎")
        order = input(f"what would you like? {menu.get_items()}").lower().strip()

    if order == "off":
        turn_off = True
    elif order == "report":
        coffee_maker.report()
    else:  # we have cappuccino/espresso/latte
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink):
            if machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
