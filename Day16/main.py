from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

initial_prompt_msg = "What would you like?"
select_again_msg = "Do you want to select again? Type 'y' or 'n': "
insufficient_resources_msg = "Machine doesn't have enough stuff to make any coffee. Please refill to continue.."
machine_turned_off_msg = "Machine turned off!!"
option_turn_off = "off"
option_fetch_report = "report"


def run_coffee_machine():
    is_machine_on = True
    coffee_menu = Menu()
    coffee_maker_machine = CoffeeMaker()
    money_processor = MoneyMachine()
    menu_items = coffee_menu.get_items()
    min_coffee = coffee_menu.find_minimum_coffee()
    have_resources = not coffee_maker_machine.is_machine_empty() \
                     and coffee_maker_machine.can_make_min_coffee(min_coffee)

    while is_machine_on:
        coffee_selected = input(f"{initial_prompt_msg} ({menu_items}): ").lower()

        if coffee_selected == option_turn_off:
            print(machine_turned_off_msg)
            is_machine_on = False

        elif coffee_selected == option_fetch_report:
            coffee_maker_machine.report()
            money_processor.report()
            continue

        while is_machine_on and have_resources:
            is_drink_on_menu = coffee_menu.find_drink(coffee_selected)

            if is_drink_on_menu:
                can_make_coffee = coffee_maker_machine.is_resource_sufficient(is_drink_on_menu)
                if can_make_coffee:
                    payment_status = money_processor.make_payment(is_drink_on_menu.cost)
                    if payment_status:
                        coffee_maker_machine.make_coffee(is_drink_on_menu)
                else:
                    pass
            have_resources = not coffee_maker_machine.is_machine_empty() \
                             and coffee_maker_machine.can_make_min_coffee(min_coffee)
            break


if __name__ == '__main__':
    run_coffee_machine()
