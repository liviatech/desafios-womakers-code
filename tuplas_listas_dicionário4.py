'''Crie um dicionário representando contatos (nome, telefone).
Permita ao usuário procurar por um contato pelo nome.'''

contatos = {}
contatos['MARIA'] = '1111-1111'
contatos['JOÃO'] = '2222-2222'
contatos['CARMEM'] = '3333-3333'
contatos['PAULO'] = '4444-4444'
contatos['DARCY'] = '5555-5555'

# Solicitar entrada do usuário e converter para maiúsculas
busca = input('Digite o nome: ').upper()

# Verificar se o nome buscado está nos contatos
if busca in contatos:
    print(f'O número de {busca} é: {contatos[busca]}')
else:
    print('Nome não encontrado.')
