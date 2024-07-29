''' Crie um dicionário representando um carrinho de compras.
Adicione produtos (chaves) e quantidades (valores) ao carrinho.
Calcule o total do carrinho de compra.'''
carrinho_compras = {} 
carrinho_compras ['bala'] = 5.00
carrinho_compras ['carne'] = 30.00
carrinho_compras [ 'feijão'] = 25.00
carrinho_compras ['alho'] = 10.00

total = sum(carrinho_compras.values())

print(f'O total é :   {total:.2f} reais')
