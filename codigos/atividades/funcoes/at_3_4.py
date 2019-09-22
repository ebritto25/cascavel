'''
    Funcao possui valores padrões para os parametros
    Se nenhum valor for fornecido a 'num1' seu valor sera 10
    o mesmo acontece com 'num2' seu valor padrão é 30
'''
def soma(num1 = 10, num2 = 30):
    return num1 + num2


num1 = 40
num2 = 20

# Imprime a soma usando parametros nomeaveis
print(soma(num1,num2)) 
# Resultado: 60


'''
    Nenhum valor foi fornecido, dessa forma os valores padroes serao utilizados
    num1 = 10
    num2 = 30
'''
print(soma())
# Resultado: 40
