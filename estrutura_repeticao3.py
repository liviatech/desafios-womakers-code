'''Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.'''


nota = -1
while nota < 0 or nota >10:
    nota = int(input('Digite uma nota de Zero a Dez : '))
    if nota < 0 or nota > 10:
       print('Digite um valor Válido !')
       
    
print('Valor informado é válido !')
    
    

