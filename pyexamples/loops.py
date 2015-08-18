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
	s = 'Nome: {0}\n Sabor {1}'
	print(s.format(pedido['nome'],pedido['sabor']))
