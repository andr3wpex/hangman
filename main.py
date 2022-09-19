#!/usr/bin/env python
import random
from words import words
from hangman_ascii import HANGMANPICS

# 2 randomly select a word from list, set initial values for variables
word = random.choice(words)


def loose_a_life(lives, hangman_pic_index, guess):
    lives -= 1
    hangman_pic_index += 1
    print(f'guess: {guess} was not found.\nRemaining lives: {lives}')
    return lives, hangman_pic_index


def fill_a_blank(blanks, guess, matches):
    blanks = list(blanks)
    for idx in matches:
        blanks[idx] = guess
    return ''.join(blanks)


def print_hangman(idx):
    print(HANGMANPICS[idx])


# hint:
print(f'*** secret word: {word} ***')

# 3 ask for user input


def main(word):
    blanks = '_' * len(word)
    on_screen = (' ').join(list(blanks))
    hangman_index, lives = 0, 6
    print_hangman(hangman_index)
    while '_' in blanks:
        guess = input('Please enter a guess (a single letter): ').lower()
        print(f'Your guess was: {guess}')

        # 4 check if guess was in the random word, get char indexes if yes
        matches = [i for i, letter in enumerate(word) if letter == guess]

        if len(matches) == 0:
            # no match, loose a life
            lives, hangman_index = loose_a_life(lives, hangman_index, guess)
            print_hangman(hangman_index)
            print(on_screen)
            if lives == 0:
                return True
        else:
            # match, populate corresponding blanks
            blanks = fill_a_blank(blanks, guess, matches)
            on_screen = (' ').join(list(blanks))
            print(f'Correct guess: {guess}, lives: {lives}')
            print(on_screen)

if __name__ == '__main__':
    if main(word):
        print()
        print(f'You lost. Game Over. The word was: {word}')
    else:
        print()
        print('*' * 20)
        print('You won.')