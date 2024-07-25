'''Criar um programa em Python que solicite três números ao usuário, utilize estruturas condicionais para determinar o maior entre eles e apresente o
resultado.'''


numeros = []
while len(numeros) < 3:
    numero = int(input('Digite um numero: '))
    numeros.append(numero)
numeros.sort()
print(numeros[-1])
    






    
    
 