#!/usr/bin/env python
import random
# 1 dummy words and hangman ASCII pictures -> source: https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

# 2 randomly select a word from list, set initial values for variables
word = random.choice(words)
lives = len(HANGMANPICS) - 1
hangman_index = 0
blanks = '_' * len(word)
on_screen = (' ').join(list(blanks))


def loose_a_life(lives, hangman_pic_index):
    lives -= 1
    hangman_pic_index += 1
    print(f'guess: {guess} was not found.\nRemaining lives: {lives}')
    return lives, hangman_pic_index

def fill_a_blank(blanks, guess, matches, lives):
    blanks = list(blanks)
    for idx in matches:
        blanks[idx] = guess
    return ''.join(blanks)

def print_hangman(idx):
    print(HANGMANPICS[idx])

# hint:
# print(f'*** secret word: {word} ***')

# 3 ask for user input
print_hangman(hangman_index)
while '_' in blanks:
    guess = input('Please enter a guess (a single letter): ').lower()
    print(f'Your guess was: {guess}')

    # 4 check if guess was in the random word, get char indexes if yes
    matches = [i for i, letter in enumerate(word) if letter == guess]

    if len(matches) == 0:
        # no match, loose a life
        lives, hangman_index = loose_a_life(lives, hangman_index)
        print_hangman(hangman_index)
        print(on_screen)
        if lives == 0:
            print(f'You lost. Game Over. The word was: {word}')
            exit()
    else:
        # match, populate corresponding blanks
        blanks = fill_a_blank(blanks, guess, matches, lives)
        on_screen = (' ').join(list(blanks))
        print(f'Correct guess: {guess}, lives: {lives}')
        print(on_screen)
print()
print('*' * 20)
print('You won.')
