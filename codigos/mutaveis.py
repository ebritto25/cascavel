'''
Declaração e inicialização de um tipo mutável(lista)
e um tipo não-mutável(tupla)
'''
lista = [1,2,3,4] 
tupla = (1,2,3,4)

print(f'Endereço da lista antes da modificação: {id(lista)}')
print(f'Lista antes da modificação: {lista}')
print(f'Endereço da tupla antes da modificação: {id(tupla)}')
print(f'Tupla antes da modificação: {tupla}')

lista += [99]

print(f'Endereço da lista depois da modificação: {id(lista)}')
print(f'Lista depois da modificação: {lista}')

tupla += (99)
print(f'Endereço da tupla depois da modificação: {id(tupla)}')
print(f'Tupla depois da Execução da Função: {tupla}')
