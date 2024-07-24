'''Escreva um programa que calcule o salário líquido. Lembrando de
declarar o salário bruto e o percentual de desconto do Imposto de
Renda.
● Renda até R$ 1.903,98: isento de imposto de renda;
● Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%;
● Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%;
● Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%;
● Renda acima de R$ 4.664,68: alíquota máxima de 27,5%.'''

renda = float(input('Digite o valor do salário bruto: '))

if renda <= 1903.98 :
    print(f'Renda até R$ 1.903,98: isento de imposto de renda. ')
    
elif renda >= 1903.99 and renda <= 2826.65:
    renda_liqueda = (7.5 / 100) * renda
    salario = renda - renda_liqueda
    print(f' Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%, salario liquido é de: {salario}')
    
elif renda >= 2826.66 and renda <= 3751.05:
     renda_liqueda = (15 / 100) * renda
     salario = renda - renda_liqueda
     print(f'Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%')

elif renda >= 3751.06 and renda <= 4664.68:
     renda_liqueda = (22.5 / 100) * renda
     salario = renda - renda_liqueda
     print(f'Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%')

else:
     renda_liqueda = (27.5 / 100) * renda
     salario = renda - renda_liqueda
     print(f'Renda acima de R$ 4.664,68: alíquota máxima de 27,5%')



