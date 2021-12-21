import os #To clean the screen
from random import choice

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
    list_word = ['_' for i in range(len(word))]
    #list_word = '_' * len(word)

    #print(word)
    while True:
        clear()
        print_on_screen(list_word)
        try:
            letter = input("\n\nIngresa una letra: ")
            letter = letter.upper()
        except ValueError:
            print('¡Error! solo ingresa letras')

        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    list_word[i] = letter

        if ''.join(list_word) == word:
            clear()
            print('Ganaste ')
            break


if __name__=='__main__':
    run()