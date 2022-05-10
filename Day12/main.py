from art import logo
import random

difficulty_hard_lives = 5
difficulty_easy_lives = 10


def set_lives(difficulty):
    if difficulty == 'easy':
        return difficulty_easy_lives
    else:
        return difficulty_hard_lives


def guess_number():
    print(logo)
    difficulty_level = input("Choose difficulty level. Type 'easy' or 'hard': \n").lower()
    num_lives = set_lives(difficulty_level)

    computer_guess = random.randint(1, 100)

    while num_lives > 0:
        user_guess = int(input("Guess a number between 1 and 100: \n"))

        if user_guess == computer_guess:
            print(f"You guessed the number as {user_guess} correctly! You win!")
            break
        elif user_guess > computer_guess:
            num_lives -= 1
            if num_lives != 0:
                print(f"Your guess is too high! You have {num_lives} lives left!")
            else:
                print(f"You lost the game. Actual number was {computer_guess}")
        elif user_guess < computer_guess:
            num_lives -= 1
            if num_lives != 0:
                print(f"Your guess is too low! You have {num_lives} lives left!")
            else:
                print(f"You lost the game. Actual number was {computer_guess}")


if __name__ == '__main__':
    guess_number()
