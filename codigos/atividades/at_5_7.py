lista = [58,14,2,69,87,68,45,21,0]

lista += [58,69,45,2,-1,-2,-3]

print(f'Nova lista: {lista}')

conjunto = set(lista) #Transforma a lista em um conjunto, retirando itens repetidos
print(f'Set com números repetidos removidos: {conjunto}')
