intro_msg = "Welcome to Treasure Island."
mission_msg = "Your mission is to find the treasure."

crossroad_msg = 'You have reached a cross road. Where do you want to go? Type "left" or "right".'
fell_into_hole_msg = "You fell into a hole. Game over!!!"
reached_river_msg = 'You have reached a river. What do you want to do? Type "swim" or "wait".'
trout_attack_msg = "A trout attacked you. Game over!!!"
intro_door_msg = "Three doors blue, red and a yellow colored ones have appeared in front of you."
select_door_msg = 'Which door do you choose? Type "blue", "red" or "yellow".'

door_colors = ["blue", "red", "yellow"]
winner_msg = "You win!"
invalid_door_msg = "Invalid door color selected. Game over!!!"
door_select_result_msg_blue = "You are eaten by beasts of the sea. Game over!!!"
door_select_result_msg_red = "You are burned by fire! Game over!!!"
door_select_result_msg_yellow = winner_msg


def treasure_island_game():
    user_choice = input(crossroad_msg)

    if user_choice != "left":
        print(fell_into_hole_msg)
        return
    else:
        user_choice = input(reached_river_msg)

    if user_choice != "wait":
        print(trout_attack_msg)
        return
    else:
        print(intro_door_msg)
        user_choice = input(select_door_msg)

    if user_choice not in door_colors:
        print(invalid_door_msg)
        return
    elif user_choice == "blue":
        print(door_select_result_msg_blue)
        return
    elif user_choice == "red":
        print(door_select_result_msg_red)
        return
    elif user_choice == "yellow":
        print(door_select_result_msg_yellow)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('''
    *******************************************************************************
              |                   |                  |                     |
     _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
              |                `"=._o`"=._      _`"=._                     |
     _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
              |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
     _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_____ /
    *******************************************************************************
    ''')
    print(intro_msg)
    print(mission_msg)

    # https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

    # Write your code below this line 👇
    treasure_island_game()
