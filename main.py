import os #To clean the screen
from random import randint

DATA = []


def read_data():
    with open('./data.txt', 'r', encoding='utf-8') as l:
        DATA = [line for line in l]
    ramdon_word = randint(0, len(DATA))
    return DATA[ramdon_word]

def clear():
    os.system('clear')
    #os.system('cls') For windows

def run():
    word = read_data()
    print(word)


if __name__=='__main__':
    run()