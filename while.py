# laços de repetição

import random

numero_aleatorio = random.randint(0, 100)
# print(numero_aleatorio)

tentativas_restantes= 5
acertou = False

while tentativas_restantes > 0:
    
    chute = int(input('Chute um número inteiro de 0 a 100: '))

    if chute == numero_aleatorio:
            print('Você acertou! O número correto era', chute)
            acertou = True
            tentativas_restantes = 0
    
    else:
        tentativas_restantes = tentativas_restantes - 1
        print('Erroooou!')
        
        if chute < numero_aleatorio and tentativas_restantes > 0:
            print('O número correto é maior do que', chute)
        elif chute > numero_aleatorio and tentativas_restantes > 0:
            print('O número correto é menor do que', chute)
    
    if tentativas_restantes <= 0 and acertou == False:
         print('Você esgotou as tentativas. O número correto era ', numero_aleatorio)