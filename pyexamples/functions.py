pedidos = []


def adiciona_pedido(nome, sabor, observacao=None):
	pedido = {}
	pedido['nome'] = nome
	pedido['sabor'] = sabor
	pedido['observacao'] = observacao
	
	return pedido


pedidos.append(adiciona_pedido('mario', 'pepperoni'))
pedidos.append(adiciona_pedido('marco', 'presunto','xyz'))
for pedido in pedidos:
	template = 'Nome: {nome}\nSabor: {sabor}'
	print(template.format(**pedido))
	if pedido['observacao']:
		print('Observacao: {}'.format(pedido['observacao']))
	print('-'*20)
