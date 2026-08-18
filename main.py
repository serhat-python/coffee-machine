from idlelib.mainmenu import menudefs

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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_on = True


def show_resources():
    for key in resources:
        print(f"{key}: {resources[key]}")

def check_resources(drink):
    for ingredient in MENU[drink]["ingredients"]:
        if resources[ingredient] < MENU[drink]["ingredients"][ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True

def process_coins():
    quarters = int(input("How many quarters: ")) / 4
    dimes = int(input("how many dimes:")) / 10
    nickels = int(input("how many nickels:")) / 20
    pennies = int(input("how many pennies:")) / 100

    return quarters + dimes + nickels + pennies

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if choice == "off":
        is_on = False
    if choice == "report":
        show_resources()
        print(f"Money: {profit}$")
    if choice in MENU:
        if check_resources(choice):
            coins = process_coins()
            if coins >= MENU[choice]["cost"]:
                coins -= MENU[choice]["cost"]
                profit += MENU[choice]["cost"]
                exchange = round(coins, 2)
                if exchange > 0:
                    print(f"Your exchange:{exchange} ")
            else:
                print("Sorry that's not enough money. Money refunded.")


