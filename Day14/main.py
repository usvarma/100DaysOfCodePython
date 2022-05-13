from art import logo, vs
from game_data import data
from random import randint

data_length = len(data)


def get_random_index():
    return randint(0, data_length - 1)


def print_term(term):
    print(f"{term['name']}, an {term['description']} from {term['country']} has {term['follower_count']} followers.")


# Returns true if term2 has higher or equal follower count, false otherwise
def compare_terms(term1, term2):
    return term2['follower_count'] >= term1['follower_count']


def higher_lower():
    game_over = False
    user_score = 0
    current_term = data[get_random_index()]

    while not game_over:

        next_term = data[get_random_index()]
        # get another search term in case it is same as current term
        if current_term == next_term:
            next_term = data[get_random_index()]

        print_term(current_term)
        print(vs)
        user_choice = input(f"Do you think {next_term['name']} has more followers? Type 'y' or 'n'.").lower()

        compare_result = compare_terms(current_term, next_term)

        # compare followers and swap if second term has greater followers as user has guessed correctly
        if user_choice == 'y' and compare_result:
            user_score += 1
            current_term = next_term
            print("You guessed correctly.")
            print(f"Current score: {user_score}")
            continue
        # compare followers and increment score if user guess is correct. No need to swap as current term has more
        # followers
        elif user_choice == 'n' and not compare_result:
            user_score += 1
            print("You guessed correctly.")
            print(f"Current score: {user_score}")
            continue
        else:
            print("Incorrect guess.")
            print_term(next_term)
            print("Game over!!")
            game_over = True


def play_game():
    continue_playing = True
    while continue_playing:
        user_choice = input("Do you want to play the game? Type 'y' to play or 'n' to quit: \n").lower()

        if user_choice == 'y':
            print(logo)
            higher_lower()
        else:
            continue_playing = False


if __name__ == '__main__':
    play_game()