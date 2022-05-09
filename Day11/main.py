import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_threshold = 21


def deal_cards():
    return random.choice(cards)


def calculate_score(deck):
    ace = 11
    sum_deck = sum(deck)
    if len(deck) == 2 and sum_deck == 21:
        return 'BlackJack'
    if ace in deck and sum(deck) > 21:
        deck.remove(ace)
        deck.append(1)
    return sum(deck)


def print_scores_decks(users_deck, computers_deck, user_score, computer_score):
    print(f"Your final hand is {users_deck}, final score: {user_score}")
    print(f"Computer's final hand is {computers_deck}, final score: {computer_score}")


def is_game_over(users_deck, computers_deck):
    user_score = calculate_score(users_deck)
    computer_score = calculate_score(computers_deck)
    win_msg = ''

    if user_score == 'BlackJack':
        win_msg = "You win with a BlackJack"
    elif computer_score == 'BlackJack':
        win_msg = "Computer wins with a BlackJack"
    elif user_score > game_threshold:
        win_msg = "You went over! Computer wins :D"
    elif computer_score > game_threshold:
        win_msg = "Computer went over! You win :D"

    if win_msg != '':
        print_scores_decks(users_deck, computers_deck, user_score, computer_score)
        print(win_msg)
        return True

    return False


def find_winner(users_deck, computers_deck):
    user_score = calculate_score(users_deck)
    computer_score = calculate_score(computers_deck)
    win_msg = ''

    if user_score > computer_score:
        win_msg = "You win :D"
    elif computer_score > user_score:
        win_msg = "Computer wins :D"
    else:
        win_msg = "It\'s a draw :D"

    if win_msg != '':
        print_scores_decks(users_deck, computers_deck, user_score, computer_score)
        print(win_msg)
        return True

    return False


def play_game():
    print(logo)
    user_deck = []
    computer_deck = []

    # Deal two cards for both computer and player initially
    user_deck.append(deal_cards())
    computer_deck.append(deal_cards())
    user_deck.append(deal_cards())
    computer_deck.append(deal_cards())

    # Continue the game dealing cards
    continue_game = True
    while continue_game:

        # Calculate and print scores
        user_score = calculate_score(user_deck)
        computer_score = calculate_score(computer_deck)
        print(f"Your cards are {user_deck}, current score: {user_score}")
        print(f"Computer\'s first card: {computer_deck[0]}")

        # Check if game is over, either due to player score being 21(BlackJack) or due to going over limit
        if is_game_over(user_deck, computer_deck):
            return
        else:
            user_choice = input("Type 'y' to get another card or type 'n' to pass: \n").lower()
            if user_choice == 'y':
                user_deck.append(deal_cards())
                continue
            elif user_choice == 'n':
                game_completed = is_game_over(user_deck, computer_deck)
                if game_completed:
                    return
                while computer_score < 17:
                    computer_deck.append(deal_cards())
                    computer_score = calculate_score(computer_deck)
        if is_game_over(user_deck, computer_deck):
            return
        find_winner(user_deck, computer_deck)
        return


def play_blackjack():
    continue_playing = True

    while continue_playing:
        user_choice = input("Do you want to play blackjack? Type 'y' or 'n': \n").lower()
        if user_choice == 'y':
            play_game()
        else:
            continue_playing = False


if __name__ == '__main__':
    play_blackjack()
