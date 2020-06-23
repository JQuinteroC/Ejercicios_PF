"""
Armar una lista de listas con los enteros formados por los múltiplos de 3 de los 
dígitos de los enteros de una lista
"""

def primero(numero):
    if numero >= 10:
        return primero(numero//10) + [3*(numero%10)]
    return [3*numero]

def listaX3(lista, res):
    if lista != []:
        return listaX3(lista[1:],res + [primero(lista[0])])
    return res
def main(lista):
    return listaX3(lista,[])

print(main([123, 456]))
