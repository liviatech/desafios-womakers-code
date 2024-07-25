'''Desenvolver um programa que solicite a idade do usuário e identifique se ele é uma criança, um adolescente, adulto ou idoso.'''

idade = int (input('Digite sua idade: '))

if idade < 10:
    print('Você é uma criança !')
elif  10 <= idade <= 17:
    print('Você é um adolescente!')
elif 18 <= idade <= 59:
    print('Você é um adulto !')    
else:
    print('Você é um idoso !')
