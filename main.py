import os #To clean the screen
from random import randint, uniform

DATA = []

def print_on_screen(list_word):
    print('********* Juego del ahorcado *********\n')
    print('|', end=' ')
    for i in list_word:
        print(i, end=' ')
    print('|')


def normalize(s):
    """Function to remove accenst from vowels
    Args: 
        s (function): This parameter is a function that get a random word from 'read_data()'
    Returns: 
        [string]: the word in lowercase and without accenst
    """    
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s


def read_data():
    """ Get the words from data.txt and choose one of them at random
    Returns: 
        string: a random word
    """
    with open('./data.txt', 'r', encoding='utf-8') as l:
        DATA = [line for line in l]
    ramdon_word = randint(0, len(DATA))
    return DATA[ramdon_word]


def clear():
    """This function clear the screen"""
    os.system('clear')
    #os.system('cls') For windows


def run():
    clear()
    word = normalize(read_data())
    list_word = ['_' for i in range(1, len(word))]


    while True:
        print_on_screen(list_word)
        try:
            letter = input("\n\nIngresa una letra: ")
        except ValueError:
            print('¡Error! solo ingresa letras')
        
        clear()

        for l in range(len(word)):
            if word[l] == letter:
                list_word[l] = letter

        if letter == 'q':
            print('Ganaste ')
            break


if __name__=='__main__':
    run()