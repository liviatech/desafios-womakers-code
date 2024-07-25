'''Desenvolva um programa que solicite ao usuário os comprimentos dos três lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno.
equilátero: todos os lados com o mesmo valor
isósceles: dois lados com o mesmo valor
escaleno: todos os lados com medidas distintas.'''


numero1 = float(input('Digite o valor do comprimento : '))
numero2 = float(input('Digite o valor do comprimento : '))
numero3 = float(input('Digite o valor do comprimento : '))

if numero1 == numero2 == numero3:
    print('É um triângulo equilátero !')
elif numero1 == numero2 and numero1 != numero3:
    print('È um triângulo isósceles ! ')
else:
    print('È um triângulo escaleno ! ')
    