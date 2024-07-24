''''Faça um Programa que utilize 4 variáveis como preferir e no final print
uma mensagem amigável utilizando as variáveis criadas.
Exemplos de variáveis: nome, idade, lugar, profissão ....
Exemplo de retorno: Olá Maria, prazer te conhecer. Sou de São Paulo também e estou migrando de área.
Lembrando que para o retorno vamos usar print com as variáveis criadas e este texto é somente um exemplo, utilizem a criatividade'''
nome_input = input('Digite seu nome: ')
nome_maiusculo = nome_input.upper()

emprego_atual_input = input('Digite sua ocupação profissional atual: ')
emprego_atual_maiusculo = emprego_atual_input.upper()

curso_atual_input = input('Digite o curso em andamento: ')
curso_atual = curso_atual_input.upper()

expectativa_profissional_input = input('Digite qual sua expectativa para seu futuro profissional:')
expectativa_profissional = emprego_atual_input.upper()

print(f'Olá {nome_maiusculo} atuando em {emprego_atual_maiusculo} suas chances de crescimento e sucesso são enormes, parabéns ao concluir seus estudos em  {curso_atual} você  está mais perto de seu objetivo {expectativa_profissional} ')