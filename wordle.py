from colors_lib import bcolors
import random

lista = ["navio", "tenis", "mesmo", "carro"]
word = lista[random.randint(0, len(lista) -1)]

def wordle():
    word_input = input("Digite uma palavra: ")
    if len(word_input) == 5:
        tentativas = 0
        palavra = ""
        for i in range(len(word_input)):
            if word_input[i] == word[i]:
                palavra = palavra + f"{bcolors.OKGREEN}" + word_input[i] + bcolors.ENDC
            elif word_input[i] in word:
                palavra = palavra + f"{bcolors.WARNING}" + word_input[i] + bcolors.ENDC
            else:
                palavra = palavra + f"{bcolors.RED}" + word_input[i] + bcolors.ENDC
            tentativas+=1
        print(palavra)
        if word_input == word:
            print("Voce acertou")

    else:
        print(f"{bcolors.WARNING}" + "palavra precisa conter 5 letras" + bcolors.ENDC)

tentativas = 0


while(True):
    wordle()
    tentativas +=1
    if tentativas == 6:
        print("Voce falhou")
        break