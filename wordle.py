from colors_lib import bcolors
import random

lista_de_palavras = []
l = open("Lista-de-Palavras.txt", "r")
for i in range(len(l)):
    # if(len(l.readline(i)) == 5):
    lista_de_palavras.append(l.readline(i))

lista = ["navio", "tenis", "mesmo", "carro"]
word = lista_de_palavras[random.randint(0, len(lista_de_palavras))]
def wordle():
    word_input = input('Digite uma palavra: ')

    if len(word_input) == 5:
        for i in range(len(word_input)):
            if word_input[i] == word[i]:
                print(f"{bcolors.OKGREEN}" + word_input[i] + bcolors.ENDC)
            elif word_input[i] in word:
                print(f"{bcolors.WARNING}" + word_input[i] + bcolors.ENDC)
            else:
                print(f"{bcolors.RED}" + word_input[i] + bcolors.ENDC)
    else:
        print(f"{bcolors.WARNING}" + "palavra precisa conter 5 letras" + bcolors.ENDC)
# wordle()

tentativas = 0

while(tentativas < 6):
    wordle()
    tentativas += 1
