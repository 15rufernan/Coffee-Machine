from data import menu
from data import resources



def print_report():
    print("Water: ", resources["water"], "ml", sep="")
    print("Milk: ", resources["milk"], "ml", sep="")
    print("Coffee: ", resources["coffee"], "g", sep="")
    print("Money: $", resources["money"], sep="")


# Updates the values of the resources
def update_resources(drink):
    ingredients = menu[drink]["ingredients"]
    if "water" in ingredients:
        resources["water"] -= ingredients["water"]
    if "milk" in ingredients:
        resources["milk"] -= ingredients["milk"]
    if "coffee" in ingredients:
        resources["coffee"] -= ingredients["coffee"]
    resources["money"] += menu[drink]["cost"]


# Counts user inputted money and gives change
def handle_payment(drink):
    cost = menu[drink]["cost"]
    try:
        dollars_from_quarters = int(input("How many quarters?: ")) * 0.25
        dollars_from_dimes = int(input("How many dimes?: ")) * 0.1
        dollars_from_nickles = int(input("How many nickles?: ")) * 0.05
        dollars_from_pennies = int(input("How many pennies?: ")) * 0.01
    except ValueError:
        print("Invalid input, try again.")
        return

    total = sum([dollars_from_quarters, dollars_from_dimes, dollars_from_nickles, dollars_from_pennies])
    if total < cost:
        print("Sorry that's not enough money. Money refunded.")
        return
    if total > cost:
        print(f"Here is ${round(total-cost, 2)} dollars in change.")
    print(f"Here is your {drink}. Enjoy!")
    update_resources(drink)


# Checks if there are sufficient resources to proceed with order
def handle_order(drink):
    drink_obj = menu[drink]
    ingredients = drink_obj["ingredients"]
    if "water" in ingredients and ingredients["water"] > resources["water"]:
        print("Sorry, there is not enough water.")
    elif "milk" in ingredients and ingredients["milk"] > resources["milk"]:
        print("Sorry, there is not enough milk.")
    elif "coffee" in ingredients and ingredients["coffee"] > resources["coffee"]:
        print("Sorry, there is not enough coffee.")
    else:
        print("That'll be $", drink_obj["cost"], sep="")
        handle_payment(drink)


def main():
    while True:
        user_input = input("What would you like? (espresso/latte/cappuccino):").lower()

        if user_input == "off":
            return False
        elif user_input == "report":
            print_report()
        elif user_input == "espresso":
            handle_order("espresso")
        elif user_input == "latte":
            handle_order("latte")
        elif user_input == "cappuccino":
            handle_order("cappuccino")
        else:
            print("Invalid input, try again.")


main()
