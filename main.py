import data

menu = data.MENU
resources = data.resources


def print_report():
    print("Water: ", resources["water"], "ml", sep="")
    print("Milk: ", resources["milk"], "ml", sep="")
    print("Coffee: ", resources["coffee"], "g", sep="")
    print("Money: $", resources["money"], sep="")


# Checks if there are sufficient resources to proceed with order
def handle_order(drink):
    if "water" in drink["ingredients"] and drink["ingredients"]["water"] > resources["water"]:
        print("Sorry, there is not enough water.")
    elif "milk" in drink["ingredients"] and drink["ingredients"]["milk"] > resources["milk"]:
        print("Sorry, there is not enough milk.")
    elif "coffee" in drink["ingredients"] and drink["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry, there is not enough coffee.")
    else:
        print("That'll be $", drink["cost"], sep="")


def main():
    while True:
        user_input = input("What would you like? (espresso/latte/cappuccino):").lower()

        if user_input == "off":
            return False
        elif user_input == "report":
            print_report()
        elif user_input == "espresso":
            handle_order(menu["espresso"])
        elif user_input == "latte":
            handle_order(menu["latte"])
        elif user_input == "cappuccino":
            handle_order(menu["cappuccino"])
        else:
            print("Invalid input, try again.")


main()
