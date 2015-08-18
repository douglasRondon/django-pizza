pedidos = []


def adiciona_pedido(nome, sabor):
	pedido = {}
	pedido['nome'] = nome
	pedido['sabor'] = sabor	
	pedidos.append(pedido)

print(pedidos)
adiciona_pedido('mario', 'pepperoni')
adiciona_pedido('marco', 'presunto') 
print( pedidos )
