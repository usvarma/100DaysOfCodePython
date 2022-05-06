import caesar_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text_to_process, shift_amount, shift_direction):
    processed_text = ''
    alphabet_length = len(alphabet)

    if shift_direction == "encode":
        shift_amount *= 1
    elif shift_direction == "decode":
        shift_amount *= -1
    else:
        print(f"Invalid operation to perform: {shift_direction}")
        exit()

    # Calculate shift amount and if it exceeds, perform modulus to take reminder to wrap around
    new_shift = shift_amount % alphabet_length
    # Get a letter to substitute and create encrypted/decrypted string
    for letter in text_to_process:
        try:
            index_substitute = (alphabet.index(letter) + new_shift) % alphabet_length
        except ValueError:
            processed_text += letter
            continue
        processed_text += alphabet[index_substitute]

    print(f"The {shift_direction}d text is {processed_text}")


if __name__ == '__main__':
    print(caesar_art.logo)
    run_again = True
    while run_again:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(text, shift, direction)
        continue_running = input("Type 'yes' to continue running the program again, type 'no' to exit:\n").lower()

        if continue_running != 'yes':
            run_again = False
