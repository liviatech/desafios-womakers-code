'''Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês.Calcule e mostre o total do seu
salário no referido mês.'''

ganho_hora_input = input('Informe  o ganho por hora: ')
ganho_hora = float(ganho_hora_input.replace(',', '.'))#substituir a virgula por ponto

horas_trabalhadas_input = input('Informe o total de horas trabalhadas no mês: ')
horas_trabalhadas = float(horas_trabalhadas_input.replace(',', '.'))#substituir vírgula por ponto


salario = ganho_hora * horas_trabalhadas

print(f'O total do salario neste mês é {salario:.2f}')