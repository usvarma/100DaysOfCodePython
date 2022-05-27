from constants import MENU, resources

initial_prompt_msg = "What would you like? (espresso/latte/cappuccino):\n"
invalid_option_msg = "We don't serve the selected coffee type"
select_again_msg = "Do you want to select again? Type 'y' or 'n': "
machine_empty_msg = "Machine is totally empty. Please refill to continue..."
insufficient_resources_msg = "Machine doesn't have enough stuff to make any coffee. Please refill to continue.."
insert_coins_msg = "Please insert coins \n"
insert_quarters_msg = "How many quarters?: "
insert_dimes_msg = "How many dimes?: "
insert_nickels_msg = "How many nickels?: "
insert_pennies_msg = "How many pennies?: "
not_enough_msg = "Sorry there is not enough"
money_refunded_msg = "Money refunded."
lower_amount_inserted_msg = "Sorry that's not enough money."
dispense_change_msg = "Here is your change amount $"
enjoy_coffee_msg = "Here is your"
enjoy_msg = "Enjoy!"
machine_turned_off_msg = "Machine turned off!!"
coffee_list = ["espresso", "latte", "cappuccino"]
ingredients_key = "ingredients"
cost_key = "cost"
money_key = "money"
option_turn_off = "off"
option_fetch_report = "report"
units = {
    "water": "ml",
    "milk": "ml",
    "coffee": "g",
    "money": "$"
}


def is_machine_empty():
    ran_out_of_stuff = True
    for values in resources.values():
        ran_out_of_stuff = values == 0 and ran_out_of_stuff
    return ran_out_of_stuff


def cant_make_any_coffee():
    espresso = "espresso"
    ingredients_required = MENU[espresso][ingredients_key].keys()
    for ingredient in ingredients_required:
        if resources[ingredient] < MENU[espresso][ingredients_key][ingredient]:
            return True
    return False


def check_resources():
    if is_machine_empty():
        return machine_empty_msg
    if cant_make_any_coffee():
        return insufficient_resources_msg
    return ""


def calc_inserted_amount(quarters, dimes, nickels, pennies):
    amount = 0
    if quarters > 0:
        amount += quarters * 0.25
    if dimes > 0:
        amount += dimes * 0.10
    if nickels > 0:
        amount += nickels * 0.05
    if pennies > 0:
        amount += pennies * 0.01
    return amount


def make_coffee(selected_coffee):
    ingredients_required = MENU[selected_coffee][ingredients_key].keys()
    for ingredient in ingredients_required:
        if resources[ingredient] < MENU[selected_coffee][ingredients_key][ingredient]:
            print(f"{not_enough_msg} {ingredient}. {money_refunded_msg}")
            return False
    for ingredient in ingredients_required:
        resources[ingredient] -= MENU[selected_coffee][ingredients_key][ingredient]
    print(f"{enjoy_coffee_msg} {selected_coffee}. {enjoy_msg}")
    return True


def return_change(change_to_return):
    if change_to_return > 0:
        print(f"{dispense_change_msg}{change_to_return}.")
    return


def print_resources():
    for key, value in resources.items():
        if key != money_key:
            print(f"{key.capitalize()}: {value}{units[key]}")
        else:
            print(f"{key.capitalize()}: {units[key]}{value}")


def update_money(coffee_charge):
    resources["money"] += coffee_charge
    return


def coffee_machine():
    ran_out_of_stuff = False

    while not ran_out_of_stuff:
        no_resources_msg = check_resources()
        ran_out_of_stuff = len(no_resources_msg) > 0
        if ran_out_of_stuff:
            print(no_resources_msg)
            return

        coffee_selected = input(initial_prompt_msg).lower()
        if coffee_selected in coffee_list:
            print(insert_coins_msg)
            quarters = int(input(insert_quarters_msg))
            dimes = int(input(insert_dimes_msg))
            nickels = int(input(insert_nickels_msg))
            pennies = int(input(insert_pennies_msg))

            inserted_amount = calc_inserted_amount(quarters, dimes, nickels, pennies)
            coffee_charge = MENU[coffee_selected][cost_key]

            if inserted_amount < coffee_charge:
                print(f"{lower_amount_inserted_msg} {money_refunded_msg}")
                return
            else:
                change_to_return = inserted_amount - coffee_charge
                coffee_result = make_coffee(coffee_selected)
                if coffee_result:
                    return_change(change_to_return)
                    update_money(coffee_charge)
                else:
                    pass
            # take payment and check if user has paid correct amount
            # check if we have resources and show an error message
            # dispense coffee and return change if user has paid more
        elif coffee_selected == option_fetch_report:
            print_resources()
        elif coffee_selected == option_turn_off:
            print(machine_turned_off_msg)
            return
        else:
            print(f"{invalid_option_msg} {coffee_selected}. {select_again_msg}")
        pass


if __name__ == '__main__':
    coffee_machine()
