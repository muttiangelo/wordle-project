from colors_lib import bcolors
import random

lista = ["navio", "tenis", "mesmo", "carro"]
word = lista[random.randint(0, len(lista) -1)]

def wordle():
    tentativas = 0
    while True:
        palavra = ""
        if tentativas > 6:
            print("Numero de tentativas excedido. A palavra era", word)
            break
        word_input = input("Digite uma palavra: ")
        if len(word_input) == 5:
            for i in range(len(word_input)):
                if word_input[i] == word[i]:
                    palavra = palavra + f"{bcolors.GREEN}" + word_input[i] + bcolors.ENDC
                elif word_input[i] in word:
                    palavra = palavra + f"{bcolors.YELLOW}" + word_input[i] + bcolors.ENDC
                else:
                    palavra = palavra + f"{bcolors.RED}" + word_input[i] + bcolors.ENDC
            print(palavra)
            tentativas+=1
            if word_input == word:
                print("Você acertou")
                break
            
        else:
            print(f"{bcolors.YELLOW}" + "palavra precisa conter 5 letras" + bcolors.ENDC)

wordle()
