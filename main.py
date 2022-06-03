import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


game_over = False

word_list = ['aardvark', 'baboon', 'camel']

chosen_word = list(random.choice(word_list))

# print(chosen_word)
print(''.join('_' * len(chosen_word)))

display = []
lives = 6

guess = input('Guess a letter: ')

for index in range(len(chosen_word)):

    if chosen_word[index] == guess:
        display.append(guess)
    else:
        display.append('_')

print(''.join(display))

while not game_over:
    guess = input('Guess a letter: ')

    for index in range(len(display)):
        if chosen_word[index] == guess:
            display[index] = guess

    if '_' not in display or lives == 0:
        game_over = True
        print("You win!")

    print(''.join(display))

