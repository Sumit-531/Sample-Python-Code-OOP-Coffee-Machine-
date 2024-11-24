from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# an object from Menu class
menu = Menu()

# an object from MoneyMachine class
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


is_coffee_machine_on = True


while is_coffee_machine_on:
    choice = input(f"What would like? ({menu.get_items()}): ").lower()
    if choice == "off":
        is_coffee_machine_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:

        drink = menu.find_drink(choice)
        res = coffee_maker.is_resource_sufficient(drink)
        payment = money_machine.make_payment(drink.cost)

        if res and payment:
            coffee_maker.make_coffee(drink)




