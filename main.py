from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
coffee_maker.report()
money_machine.report()
menu = Menu()
on = True

while on == True:
    options = menu.get_items()
    ask = input(f"Choose a coffee {options}:")
    if ask == 'off':
        on = False
    if ask == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(ask)
        print(f"You choose {ask}.")
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)