pedidos = [
	{
		'nome': 'Mario',
		'sabor': 'portuguesa'
	},
	{
		'nome' : 'Marco',
		'sabor' : 'presunto'
	}
]
for pedido in pedidos:
	print('Nome: {0}\n Sabor {1}'.format(pedido['nome'],pedido['sabor']))
