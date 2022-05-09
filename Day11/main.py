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


def is_over_threshold(users_deck, computers_deck):
    user_score = calculate_score(users_deck)
    computer_score = calculate_score(computers_deck)

    if user_score == 'BlackJack':
        print(f"Your final hand is {users_deck}, final score: {user_score}")
        print(f"Computer's final hand is {computers_deck}, final score: {computer_score}")
        print("You win with a BlackJack")
        return True
    elif computer_score == 'BlackJack':
        print(f"Your final hand is {users_deck}, final score: {user_score}")
        print(f"Computer's final hand is {computers_deck}, final score: {computer_score}")
        print("Computer wins with a BlackJack")
        return True
    elif user_score > game_threshold:
        print(f"Your final hand is {users_deck}, final score: {user_score}")
        print(f"Computer's final hand is {computers_deck}, final score: {computer_score}")
        print("You went over! Computer wins :D")
        return True

    elif computer_score > game_threshold:
        print(f"Your final hand is {users_deck}, final score: {user_score}")
        print(f"Computer's final hand is {computers_deck}, final score: {computer_score}")
        print("Computer went over! You win :D")
        return True

    return False


def find_winner(users_deck, computers_deck):
    user_score = calculate_score(users_deck)
    computer_score = calculate_score(computers_deck)

    if user_score > game_threshold:
        print(f"Your final hand is {users_deck}, final score: {user_score}")
        print(f"Computer's final hand is {computers_deck}, final score: {computer_score}")
        print("You went over! Computer wins :D")
        return False

    elif computer_score > game_threshold:
        print(f"Your final hand is {users_deck}, final score: {user_score}")
        print(f"Computer's final hand is {computers_deck}, final score: {computer_score}")
        print("Computer went over! You win :D")
        return False
    elif user_score > computer_score:
        print(f"Your final hand is {users_deck}, final score: {user_score}")
        print(f"Computer's final hand is {computers_deck}, final score: {computer_score}")
        print("You win :D")
        return False
    elif computer_score > user_score:
        print(f"Your final hand is {users_deck}, final score: {user_score}")
        print(f"Computer's final hand is {computers_deck}, final score: {computer_score}")
        print("Computer wins :D")
        return False
    else:
        print(f"Your final hand is {users_deck}, final score: {user_score}")
        print(f"Computer's final hand is {computers_deck}, final score: {computer_score}")
        print("It\'s a draw :D")
        return False


def play_blackjack():
    print(logo)
    continue_playing = True

    while continue_playing:
        user_choice = input("Do you want to play blackjack? Type 'y' or 'n': \n").lower()
        user_deck = []
        computer_deck = []

        if user_choice == 'y':
            user_deck.append(deal_cards())
            computer_deck.append(deal_cards())
            user_deck.append(deal_cards())
            computer_deck.append(deal_cards())
        else:
            return

        user_score = calculate_score(user_deck)
        computer_score = calculate_score(computer_deck)
        print(f"Your cards are {user_deck}, current score: {user_score}")
        print(f"Computer\'s first card: {computer_deck[0]}")

        continue_game = True
        while continue_game:
            user_choice = input("Type 'y' to get another card or type 'n' to pass: \n").lower()
            if user_choice == 'y':
                user_deck.append(deal_cards())
                game_completed = is_over_threshold(user_deck, computer_deck)
                if game_completed:
                    break
                if not game_completed:
                    computer_deck.append(deal_cards())
                    user_score = calculate_score(user_deck)
                    computer_score = calculate_score(computer_deck)
                    print(f"Your cards are {user_deck}, current score: {user_score}")
                    print(f"Computer\'s first card: {computer_deck[0]}")
                    continue
            elif user_choice == 'n':
                game_completed = is_over_threshold(user_deck, computer_deck)
                if game_completed:
                    break
                while computer_score < 17:
                    computer_deck.append(deal_cards())
                    computer_score = calculate_score(computer_deck)
                continue_game = find_winner(user_deck, computer_deck)


if __name__ == '__main__':
    play_blackjack()
