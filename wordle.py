from colors_lib import bcolors
import random


def wordle(word_input = input('Digite uma palavra: ')):
    lista = ["navio", "tenis", "mesmo", "carro"]

    word = lista[random.randint(0, 3)]

    if len(word_input) == 5:
        for i in range(len(word_input)):
            if word_input[i] == word[i]:
                print(f"{bcolors.OKGREEN}" + word_input[i] + bcolors.ENDC)
            else:
                print(f"{bcolors.RED}" + word_input[i] + bcolors.ENDC)
    else:
        print(f"{bcolors.WARNING}" + "palavra precisa conter 5 letras" + bcolors.ENDC)

    # if(word_input == word):
    #     print(f"{bcolors.OKGREEN}" + word + bcolors.ENDC)

wordle()