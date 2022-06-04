import random
from hangman_art import stages
from hangman_art import logo
from hangman_words import word_list

game_over = False

print(logo)

chosen_word = list(random.choice(word_list))

# print(''.join('_' * len(chosen_word)))

display = ["_" for _ in range(len(chosen_word))]

lives = 6

tries = []
while not game_over:

    guess = input('Guess a letter: ').lower()

    if guess not in chosen_word or guess in tries:
        lives -= 1
        print(stages[lives])
    for index in range(len(display)):
        if chosen_word[index] == guess:
            display[index] = guess

    if lives == 0:
        game_over = True
        print("You lose.")

    if '_' not in display:
        game_over = True
        print("You win!")

    tries.append(guess)
    print(''.join(display))

