from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money = MoneyMachine()
machine = CoffeeMaker()
is_on = True

while is_on:
    option = input(f"What would you like ({menu.get_items()}):")

    if option == 'report':
        machine.report()
        money.report()
    else:
        drink = menu.find_drink(option)
        if money.make_payment(drink.cost) == True and machine.is_resource_sufficient(drink) == True:
            machine.make_coffee(drink)

