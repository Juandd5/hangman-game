import os #To clean the screen
from random import randint

DATA = []

def print_on_screen(word):
    underscore = '_'
    underscore_list = [underscore for i in range(1, len(word))]
    
    print('|', end=' ')
    for i in underscore_list:
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
    word = normalize(read_data())
    print(f'{word}\n')
    print_on_screen(word)


if __name__=='__main__':
    run()