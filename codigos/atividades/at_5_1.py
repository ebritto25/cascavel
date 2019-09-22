lista = [58,14,2,69,87,68,45,21,0]

'''
    A função enumerate() aceita um iterável e retorna 
    uma lista de tuplas em que na primeira posição está
    um número em uma sequência e na segunda posição está
    o item do iterável
'''
for posicao, item in enumerate(lista,1):
    print(f'{posicao} - {item}')
