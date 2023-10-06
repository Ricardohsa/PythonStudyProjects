import Coffee_Machine
quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01
off = False


def print_machine_report():
    """
returns the current resource values
    """
    print(f"Water: {Coffee_Machine.resources['water']} ml\n"
          f"Milk: {Coffee_Machine.resources['milk']} ml\n"
          f"Coffee: {Coffee_Machine.resources['coffee']} ml\n"
          f"Money: $ {Coffee_Machine.profit}\n")


def buy_coffee(coffee_option):

    if coffee_option == "report":
        print_machine_report()
    else:
        print("Please insert coins.")
        user_quarters = float(input(f"how many quarters?: "))
        user_dimes = float(input(f"how many dimes?: "))
        user_nickles = float(input(f"how many nickles?: "))
        user_pennies = float(input(f"how many pennies?: "))

        total = (user_quarters * quarters) + (user_dimes * dimes) + (user_nickles * nickles) + (user_pennies * pennies)

        coffee_cost = Coffee_Machine.MENU[coffee_option]['cost']

        if total < coffee_cost or not check_resource(coffee_option):
            global off
            off = True
            print("Sorry that's not enough money. Money refunded.")
            return False
        else:
            make_coffee(coffee_option)
            change = total - coffee_cost
            Coffee_Machine.profit += coffee_cost
            print(f"Here is ${change} in change\nHere is your {coffee_option}. Enjoy!")
            return True


def check_resource(user_option):
    """
    check if the Machine has enough resource, if has will deduct the amount needed.

    @param user_option:
    @return:
    """
    machine_water = int(Coffee_Machine.resources['water'])
    machine_milk = int(Coffee_Machine.resources['milk'])
    machine_coffee = int(Coffee_Machine.resources['coffee'])

    if user_option == 'espresso':
        water_needed = int(Coffee_Machine.MENU[user_option]['ingredients']['water'])
        coffee_needed = int(Coffee_Machine.MENU[user_option]['ingredients']['coffee'])

        if machine_water > water_needed and machine_coffee > coffee_needed:
            return True
        else:
            print("Sorry there is not enough water")
            return False
    else:
        water_needed = int(Coffee_Machine.MENU[user_option]['ingredients']['water'])
        milk_needed = int(Coffee_Machine.MENU[user_option]['ingredients']['milk'])
        coffee_needed = int(Coffee_Machine.MENU[user_option]['ingredients']['coffee'])

        if machine_water > water_needed and machine_coffee > coffee_needed and machine_milk > milk_needed:
            return True
        else:
            return False


def make_coffee(user_option):
    if user_option == 'espresso':
        water_needed = int(Coffee_Machine.MENU[user_option]['ingredients']['water'])
        coffee_needed = int(Coffee_Machine.MENU[user_option]['ingredients']['coffee'])

        Coffee_Machine.resources['water'] -= water_needed
        Coffee_Machine.resources['coffee'] -= coffee_needed
    else:
        water_needed = int(Coffee_Machine.MENU[user_option]['ingredients']['water'])
        milk_needed = int(Coffee_Machine.MENU[user_option]['ingredients']['milk'])
        coffee_needed = int(Coffee_Machine.MENU[user_option]['ingredients']['coffee'])

        Coffee_Machine.resources['water'] -= water_needed
        Coffee_Machine.resources['coffee'] -= coffee_needed
        Coffee_Machine.resources['milk'] -= milk_needed


while not off:
    user_choice = input("What would you like? (espresso/latte/cappuccino):")
    buy_coffee(user_choice)




