import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

intro_msg = 'Welcome to Rock, Paper and Scissors game.'
choice_msg = 'To play you have to choose an option. Type "rock", "paper" or "scissors" to choose.\n'
invalid_user_choice_msg = 'You have selected an invalid choice. Game over!'
invalid_comp_choice_msg = 'Computer has selected an invalid choice. Game over!'
same_selection_msg = 'Both of you selected'
game_drawn_msg = 'It\'s a draw.'
rock_crushes_scissor_msg = 'Rock crushes scissor. Rock wins!'
scissor_cuts_paper_msg = 'Scissor cuts paper. Scissor wins!'
paper_covers_rock_msg = 'Paper covers rock. Paper wins!'
you_win_msg = "You win!"
you_lose_msg = "You lose!"

choice_list_ascii = [rock, paper, scissors]
choice_list = ["rock", "paper", "scissors"]
choice_msg_list = [rock_crushes_scissor_msg, paper_covers_rock_msg, scissor_cuts_paper_msg]


def print_choice(choice):
    if choice not in choice_list:
        print(invalid_user_choice_msg)
        return

    choice_index = choice_list.index(choice)
    print(choice_list_ascii[choice_index])


def computer_choice():
    random.seed(random.randint(1, 100));
    choice = random.randint(0, len(choice_list) - 1)
    return choice_list[choice]


def compute_winner(user_choice, comp_choice):
    if user_choice not in choice_list:
        print(invalid_user_choice_msg)
        return
    elif comp_choice not in choice_list:
        print(invalid_comp_choice_msg)
        return

    if user_choice == comp_choice:
        print(f"{same_selection_msg} {user_choice}. {game_drawn_msg}")
        return
    elif user_choice == 'rock' and comp_choice == 'scissors':
        print(rock_crushes_scissor_msg)
        print(you_win_msg)
    elif user_choice == 'paper' and comp_choice == 'rock':
        print(paper_covers_rock_msg)
        print(you_win_msg)
    elif user_choice == 'scissors' and comp_choice == 'paper':
        print(scissor_cuts_paper_msg)
        print(you_win_msg)
    else:
        msg_index = choice_list.index(comp_choice)
        print(choice_msg_list[msg_index])
        print(you_lose_msg)


def play_rock_paper_scissors():
    print(intro_msg)
    user_choice = input(choice_msg)
    print(f"You have chosen {user_choice}: ")
    print_choice(user_choice)
    # print()
    comp_choice = computer_choice()
    print(f"Computer has chosen {comp_choice}: ")
    print_choice(comp_choice)
    compute_winner(user_choice, comp_choice)
    return


if __name__ == '__main__':
    play_rock_paper_scissors()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
