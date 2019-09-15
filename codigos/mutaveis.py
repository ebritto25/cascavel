def adicionar_lista(lista):
    '''
    Concatena um elemento em uma lista
    '''
    print(f'Endereço da Lista dentro da Função: {id(lista)}')
    lista += [99]

def adicionar_tupla(tupla):
    '''
    Tenta concatenar um elemento em uma tupla
    '''
    print(f'Endereço da Tupla dentro da Função: {id(tupla)}')
    tupla += (99)

'''
Declaração e inicialização de um tipo mutável(lista)
e um tipo não-mutável(tupla)
'''
lista = [1,2,3,4] 
tupla = (1,2,3,4)

print(f'Endereço da Lista fora da Função: {id(lista)}')
print(f'Endereço da Tupla fora da Função: {id(tupla)}')

print(f'Lista antes da Execução da Função: {lista}')
print(f'Tupla antes da Execução da Função: {tupla}')

adicionar_lista(lista)
print(f'Lista depois da Execução da Função: {lista}')

adicionar_tupla(tupla)
print(f'Tupla depois da Execução da Função: {tupla}')
