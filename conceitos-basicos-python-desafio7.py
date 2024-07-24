'''Solicite ao usuário o peso em kg e a altura em metros. Calcule e
imprima o Índice de Massa Corporal (IMC) usando a fórmula:
IMC = peso / (altura x altura).'''

peso_input = input('Digite seu peso em kg: ')
peso = float(peso_input.replace(',', '.'))#substituir a virgula por ponto

altura_input = input('Digite sua altura em metros: ')
altura = float(altura_input.replace(',', '.'))#substituir vírgula por ponto

imc = peso / (altura * altura)
print(f'O Índice de massa corporal (IMC) é : {imc:.1f}')