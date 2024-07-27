'''1. Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.'''


def soma():
    numero1 = int(input('Digite um numero inteiro : '))
    numero2 = int(input('Digite um numero inteiro : '))
    numero3 = int(input('Digite um numero inteiro : '))
    calculo = numero1 + numero2 + numero3
    print(f'O resultado da soma é {calculo} ')
    
soma()