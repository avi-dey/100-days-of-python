import os

# constant
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

# would be updated
resources = {
    "water": 400,
    "milk": 200,
    "coffee": 100
}


# TODO: print report
def get_report():
    """returns the resources that are left"""
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    return f"Here's your report: 📄\nwater : {water}\nmilk: {milk}\ncoffee: {coffee}"


# TODO: check resources availability
def is_resources_sufficient(order):
    for ingredients in order:
        if resources[ingredients] < order[ingredients]:
            print("sorry there is not enough resources to process your coffee request")
            return False
    return True


def get_payment():
    """ask for the quarters, dimes, nickels, pennies and return the total value"""
    print("💲 Please insert coins. 💲")
    # quarter: $0.25, dime: $0.10, nickel: $0.05, penny: $0.01
    quarter_qty = int(input("how many quarters?: "))
    dime_qty = int(input("how many dimes?: "))
    nickel_qty = int(input("how many nickels?: "))
    penny_qty = int(input("how many pennies?: "))

    quarter_value = quarter_qty * 0.25
    dime_value = dime_qty * 0.10
    nickel_value = nickel_qty * 0.05
    penny_value = penny_qty * 0.01

    return quarter_value + dime_value + nickel_value + penny_value  # total value


# TODO: process coins : insufficient balance or return change
def is_money_sufficient(cost, total_paid):
    if cost <= total_paid:
        print(f"Order successful. Here's your change : {round(total_paid - cost, 2)} 👛")
        return True
    else:
        print(f"Order declined by {round(cost - total_paid, 2)} amount")
        return False


# TODO: deduct the resources that were used to make up the coffee
def deduct_resources(resources, order_ingredients):
    """deducts the ingredients used to prepare the order from the resources remember: is resources sufficient is
    already checked and ensured so, we are confident that: resources[x] - order_ingredients[x] can never give
    negative values"""
    for ingredients in order_ingredients:
        resources[ingredients] -= order_ingredients[ingredients]


def refill_machine():
    print("Enter refill amounts: ")
    water_refill = int(input("enter the amount of water you want refill: "))
    milk_refill = int(input("enter the amount of coffee you want refill: "))
    coffee_refill = int(input("enter the amount of coffee you want refill: "))
    resources["water"] += water_refill
    resources["milk"] += milk_refill
    resources["coffee"] += coffee_refill


def coffe_machine():
    switch_off = False

    while not switch_off:
        print("\nwhat would you like?(espresso/latte/cappuccino) ☕")
        order = input("(report/off for 'get report'/'turn off machine'): ").lower().strip()

        valid_options = ["cappuccino", "espresso", "latte", "off", "report"]
        while order not in valid_options:
            print("❌ INVALID INPUT ❌")
            order = input("what would you like? (espresso/latte/cappuccino)").lower().strip()

        if order == "report":
            print(get_report())
        elif order == "off":
            switch_off = True
        else:  # i.e. we have order = cappuccino/ latte/ espresso
            order_ingredients = MENU[order]["ingredients"]
            order_cost = MENU[order]["cost"]
            if is_resources_sufficient(order_ingredients):
                total_payment = get_payment()
                if is_money_sufficient(order_cost, total_payment):
                    deduct_resources(resources, order_ingredients)
                    print(f"Here's your {order} ☕")
                else:
                    print("money not sufficient ❌")
            else:
                print("machine doesn't have enough resources at the moment: 😢")
                print("do you want to refill? :")
                refill_machine()


coffe_machine()
