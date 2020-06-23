"""
Retornar un entero con los últimos dígitos de una lista de enteros
"""


def ultimo_dig(lista, valor):
    if lista == []:
        return valor
    return ultimo_dig(lista[1:], (valor*10)+(lista[0] % 10))

print(ultimo_dig([123, 234, 678], 0))