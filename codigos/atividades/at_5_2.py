lista = [58,14,2,69,87,68,45,21,0]

print(f'Ordenada: {sorted(lista)}') #Função sorted() retorna uma nova lista ordenada
print(f'Não ordenada: {lista}')

lista2 = [58,14,2,69,87,68,45,21,0]
lista2.sort() #Função sort() do objeto list faz a ordenação "in-place"

print(f'Ordenada in-place: {lista2}')
