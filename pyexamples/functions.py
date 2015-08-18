pedidos = []


def adiciona_pedido(nome, sabor, observacao='sem obs'):
	pedido = {}
	pedido['nome'] = nome
	pedido['sabor'] = sabor
	pedido['observacao'] = observacao	
	return pedido

print(pedidos)
pedidos.append(adiciona_pedido('mario', 'pepperoni'))
pedidos.append(adiciona_pedido('marco', 'presunto'))
print( pedidos )
