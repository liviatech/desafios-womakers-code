'''Faça um Programa que peça a quantidade de quilômetros, transforme
em metros, centímetros e milímetros.'''

quilometro = float(input('Qual a quantidade de qulometros? '))
metro = quilometro * 1000
centimetro = quilometro * 10000
milimetro = quilometro * 100000

print(f'A quantidade de quilometros fornecida equivale a {metro:,.2f} metros, {centimetro:,.2f} centimetros, {milimetro:,.2f} milimetros . ')