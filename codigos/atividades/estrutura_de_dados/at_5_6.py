lista = [58,14,2,69,87,68,45,21,0]

tupla = tuple(lista)

tupla[1] = -1 #Essa linha vai dar erro pois tuplas são imutáveis

print(f'Tupla modificada: {tupla}')
