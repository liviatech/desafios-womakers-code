'''Solicite ao usuário o número de horas de exercício físico por semana.
Calcule o total de calorias queimadas em um mês, considerando uma
média de 5 calorias por minuto de exercício.'''


horas_semana_input = input('Informe as horas de exercicios por semana: ')
horas_semana = float(horas_semana_input.replace(',','.'))
calorias = 5 * 60
calorias_queimadas = (horas_semana  * calorias) * 4

print(f' O total de calorias queimadas em um mês é {calorias_queimadas:.1f}')