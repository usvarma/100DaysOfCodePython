# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

chars_list = [letters, numbers, symbols]
is_chosen = [False, False, False]


# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
def generate_random_index(length_list):
    return random.randint(0, length_list - 1)


def pick_chars(chars_length, pick_from_list):
    letter = ''
    length = len(pick_from_list)
    for i in range(chars_length):
        letter += pick_from_list[generate_random_index(length)]
    return letter


def generate_password(letters_length, numbers_length, symbols_length, is_randomized):
    passwd = ''
    length_list = [letters_length, numbers_length, symbols_length]
    if not is_randomized:
        passwd += pick_chars(letters_length, letters)
        passwd += pick_chars(symbols_length, symbols)
        passwd += pick_chars(numbers_length, numbers)
    else:
        password_generated = False
        while not password_generated:
            index = generate_random_index(len(chars_list))
            if not is_chosen[index]:
                passwd += pick_chars(length_list[index], chars_list[index])
                is_chosen[index] = True
                password_generated = not (False in is_chosen)

    return passwd


if __name__ == '__main__':
    print("Welcome to the PyPassword Generator!")
    num_letters = int(input("How many letters would you like in your password?\n"))
    num_symbols = int(input(f"How many symbols would you like?\n"))
    num_numbers = int(input(f"How many numbers would you like?\n"))

    print("Randomized password")
    password = generate_password(num_letters, num_numbers, num_symbols, True)
    print(password)
    print("Non-Randomized password")
    password = generate_password(num_letters, num_numbers, num_symbols, False)
    print(password)