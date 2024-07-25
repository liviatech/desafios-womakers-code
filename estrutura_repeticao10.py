''' Faça um programa que lê três números inteiros e os mostra em ordem
crescente.'''

numeros = []
while len(numeros) < 3: #solicitar numeros até que 
    numero = int(input('Digite um numero: '))
    numeros.append(numero)# adicionar numeros em uma lista
numeros.sort() # ordem crescente
print(numeros[0], numeros[1], numeros[2])
    