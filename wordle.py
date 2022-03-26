from colors_lib import bcolors
import random

lista = ["navio", "tenis", "mesmo", "carro"]
wor = lista[random.randint(0, len(lista) -1)]
word = wor.lower()

def wordle():
    tentativas = 0
    while True:
        palavra = ""
        if tentativas > 6:
            print("Numero de tentativas excedido. A palavra era", word)
            break
        word_input_before = input("Digite uma palavra: ")
        word_input = word_input_before.lower()
        if len(word_input) == 5:
            if word_input in lista:
                for i in range(len(word_input)):
                    if word_input[i].upper() == word[i].upper():
                        palavra = palavra + f"{bcolors.GREEN}" + word_input[i].lower() + bcolors.ENDC
                    elif word_input[i] in word:
                        palavra = palavra + f"{bcolors.YELLOW}" + word_input[i].lower() + bcolors.ENDC
                    else:
                        palavra = palavra + f"{bcolors.RED}" + word_input[i].lower() + bcolors.ENDC
                print(palavra)
                tentativas+=1
                if word_input == word:
                    print("Você acertou")
                    break
            else:
                print(f"{bcolors.YELLOW}" + "Essa palavra não é aceita" + bcolors.ENDC)
            
        else:
            print(f"{bcolors.YELLOW}" + "palavra precisa conter 5 letras" + bcolors.ENDC)

wordle()
