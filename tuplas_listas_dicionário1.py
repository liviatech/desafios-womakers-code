'''1. Utilizando listas faça um programa que faça 5 perguntas para uma
pessoa sobre um crime. As perguntas são:
""Telefonou para a vítima?""
""Esteve no local do crime?""
""Mora perto da vítima?""
""Devia para a vítima?""
""Já trabalhou com a vítima?""
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser
classificada como ""Suspeita"", entre 3 e 4 como ""Cúmplice"" e 5 como
""Assassino"".
Caso contrário,ele será classificado como""Inocente"". '''

perguntas = []

pergunta_telefone = input('Telefonou para a vítima?')
perguntas.append(pergunta_telefone.upper())

pergunta_local = input('Esteve no local do crime?')
perguntas.append(pergunta_local.upper())

pergunta_moradia = input('Mora perto da vítima?')
perguntas.append(pergunta_moradia.upper())

pergunta_divida = input('Devia para a vítima?')
perguntas.append(pergunta_divida.upper())

pergunta_trabalho = input('Já trabalhou com a vítima?')
perguntas.append(pergunta_trabalho.upper())

perguntas_onderm = perguntas.sort()

numero_sim = perguntas.count('SIM')#contar os sim

if numero_sim == 2:
    print('Suspeita')
elif 3 <= numero_sim <= 4:
    print('Cumplice')
elif numero_sim == 5:
    print('Culpado')
else: 
    print('Inocente')