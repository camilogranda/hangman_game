import os
import random
import time
from unidecode import unidecode as unidc


def random_word():
    """ 
    Pick a random word from hangman list and remove accents, blank spaces and uppercase.

    Return:
    random_word: A random word from the list
    word_lines: The lines that represent the letters of the random word 
    """
    with open('files/data.txt', 'r', encoding='utf-8') as f:
        hangman_list = [l.strip() for l in f.readlines()]

    random_word = unidc(random.choice(hangman_list))

    word_lines = ''
    for idx in range(0, len(random_word)): 
        word_lines += random_word[idx].replace(random_word[idx], '_')
    
    return random_word, word_lines

def capture_letter():
    """
    Capture a letter from user to play hangman game
    
    Return:
    Letter selected from user.
    """
    letter = input('Please, enter a letter to guees the word: ')
    print()
    try:
        if not letter.isalpha():
            raise ValueError('Argument not valid. Please enter a letter.')
        if len(letter) == 1:
            return letter.lower()
        else:
            os.system('cls')
            print('ERROR: Please enter a single letter.')
            print()
            print(input('Press enter to continue.'))
    except ValueError as e:
        os.system('cls')
        print('ERROR: ', e)
        print()
        print(input('Press enter to continue.'))

    return letter


def string_index(string, s):
    """
    Find the indices in which a letter or letters appears in a word.

    Parameters:
    string = Word to find the letters.
    s = Letter to search in the word.

    Return:
    Indices in which the letter appears in the word. 
    """
    idxs = []
    string = unidc(string.lower())
    for i in range(len(string)):
        if string[i] == s:
            idxs.append(i)
    return idxs

def replace_chars_in_lines(string, idxs, s):
    new_string = list(string)
    for i in idxs:
        new_string[i] = s
    new_string = "".join(new_string)
    return new_string


def main():

    word, word_lines = random_word()

    while word != word_lines:
        os.system('cls')

        with open('files/hangman_2.txt', 'r')  as f:
            print(f.read())

        print('Welcome to hangman game!')
        print()

        print(word)
        print(word_lines)
        print()

        l = capture_letter()
        print()
        
        if l in word:
            idxs = string_index(word, l)
            word_lines = replace_chars_in_lines(word_lines, idxs, l)
            print(word_lines)
        else:
            print('Pick another letter.')
            print()

    os.system('cls')
    time.sleep(.5)

    with open('files/owl.txt', 'r')  as f:
        print(f.read())

    print(f'Congratulations!\nYou guessed the word {word.upper()}')
        
if __name__ == "__main__":
    main()