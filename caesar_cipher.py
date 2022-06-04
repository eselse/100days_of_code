alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', ' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):

    cipher_text = ''
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        if new_position > len(alphabet)-1:
            new_position %= len(alphabet)
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f'The encoded text is "{cipher_text}"')

def decrypt(text, shift):

    initial_text = ''
    for letter in text:
        position = alphabet.index(letter)
        new_position = position - shift
        while new_position < 0:
            new_position += len(alphabet)
        new_letter = alphabet[new_position]
        initial_text += new_letter
    print(f'The decoded text is {initial_text}')

encrypt(plain_text=text, shift_amount=shift)

new_text = input("Type your message:\n").lower()
same_shift = int(input("Type the shift number:\n"))

decrypt(text=new_text, shift=same_shift)
