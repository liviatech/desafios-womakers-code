'''3. Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para cada opção, crie uma função.
Extra: Crie uma terceira, que é um menu para o usuário escolher a  opção desejada, onde esse menu chama a função de conversão correta. '''

def celsius_fahrenheit(celsius):
    return celsius * 9.0 / 5.0 + 32

def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0 / 9.0

def menu():
    opcao = input('Converter a temperatura de Celsius para Fahrenheit (digite "s")sim ou de Fahrenheit para Celsius (digite "n") não: ').strip().lower()
    
    if opcao == 's':
        temperatura_celsius = float(input('Digite a temperatura em Celsius: '))
        fahrenheit = celsius_fahrenheit(temperatura_celsius)
        print(f'A temperatura em Fahrenheit é {fahrenheit:.2f}')
    elif opcao == 'n':
        temperatura_fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))
        celsius = fahrenheit_celsius(temperatura_fahrenheit)
        print(f'A temperatura em Celsius é {celsius:.2f}')
    else:
        print('Opção inválida. Por favor, digite "sim" ou "nao".')

menu()

