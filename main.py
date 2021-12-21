import os #To clean the screen
from random import choice

DATA = []

def print_on_screen(list_word_underscores):
    """This function print on screen
    Args:
        list_word_underscores (list): It contains as underscores as len(word)
        and it changes every time a letter is hit.
    """
    print('********* Juego del ahorcado *********\n')
    print('|', end=' ')
    for i in list_word_underscores:
        print(i, end=' ')
    print('|')


def normalize(s):
    """Function to remove accenst from vowels
    Args: 
        s (function): This parameter is a function that get a random word from 'read_data()'
    Returns: 
        [string]: the word in lowercase and without accenst
    """   
    #print(s, len(s)) 
    replacements = (
        ("Á", "A"),
        ("É", "E"),
        ("Í", "I"),
        ("Ó", "O"),
        ("Ú", "U"),
    )
    for a, b in replacements:
        s = s.upper().replace(a, b)#.replace(a.upper(), b.upper())

    return s


def read_data():
    """ Get the words from data.txt and choose one of them at random
    Returns: 
        string: a random word
    """
    with open('./data.txt', 'r', encoding='utf-8') as f:
        for line in f:
            DATA.append(line.strip())
    
    return choice(DATA)


def clear():
    """This function clear the screen"""
    os.system('clear')
    #os.system('cls') For windows


def run():
    clear()
    word = normalize(read_data())
    list_word_underscores = ['_' for i in range(len(word))]
    dict_letter_index = {}
    lifes = 6

    # I create a dict with the letters of the word as keys, and the values are index lists 
    # Example: word='casa' / dict = {'c':[0], 'a':[1,3], 's':[2]}
    for i, letter in enumerate(word):
        if not dict_letter_index.get(letter):
            dict_letter_index[letter] = []
        dict_letter_index[letter].append(i)

    while True:
        clear()
        print(lifes)
        print_on_screen(list_word_underscores)
        letter = input("\n\nIngresa una letra: ")
        letter = letter.upper()

        if letter in word:
            for i in dict_letter_index[letter]:
                list_word_underscores[i] = letter
        else:
            lifes -= 1

        if ''.join(list_word_underscores) == word:
            clear()
            print(f'¡Ganaste! La palabra era: {word}')
            break
        
        if lifes == 0:
            clear()
            print("¡Perdiste! Se te acabaron las vidas")
            break


if __name__=='__main__':
    run()