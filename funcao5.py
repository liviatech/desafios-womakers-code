'''5. Crie uma função chamada contar_vogais que recebe uma string
como parâmetro. Implemente a lógica para contar o número de vogais
na string e retorne o total de vogais. Solicite ao usuário para inserir uma
frase e utilize a função para contar as vogais.
'''

def contar_vogais():
    vogais = ['a', 'e', 'i', 'o', 'u']
    frase = input('Digite uma frase: ')
    frase_minuscula = frase.lower()  # tudo minusculo
    
    contagem_vogais = 0

    # Conta as vogais na frase
    for letra in frase_minuscula:
        if letra in vogais:
            contagem_vogais += 1


    print('A frase contém', contagem_vogais, 'vogais.')

contar_vogais()

    