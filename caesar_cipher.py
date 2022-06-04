from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', ' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print(logo)

user_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
user_text = input("Type your message:\n").lower()
user_shift = int(input("Type the shift number:\n"))


def cesar(text, shift, direction):
    result_text = ''
    new_position = 0
    for letter in text:
        position = alphabet.index(letter)
        if direction == 'encode':
            new_position = position - shift
            while new_position < 0:
                new_position += len(alphabet)
        if direction == 'decode':
            new_position = position + shift
            if new_position > len(alphabet) - 1:
                new_position %= len(alphabet)
        new_letter = alphabet[new_position]
        result_text += new_letter
    result_text = f'The {direction}d text is {result_text}'
    print(result_text)


cesar(user_text, user_shift, user_direction)