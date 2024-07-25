'''O programa deve calcular e apresentar a quantidade de números pares e
ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário
informar o valor zero. Certifique-se de incluir validações para garantir que
apenas números positivos sejam considerados na contagem e cálculos.'''


# Inicializa contadores de números pares e ímpares
pares = 0
impares = 0

# Loop para leitura dos números
while True:
    numero = int(input('Digite um numero (0 para encerrar): '))
    
    # Encerra o loop se o número for zero
    if numero == 0:
        break
    
    # Ignora números negativos
    if numero < 0:
        print("Por favor, digite apenas números positivos.")
        continue
    
    # Verifica se o número é par ou ímpar
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

# Imprime a quantidade de números pares e ímpares
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
