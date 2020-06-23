"""
Para una lista de listas retornar una lista de tuplas con el mayor, menor y la suma del
mayor y menor de cada sublista
"""


def max(lista, mayor):
    if lista == []:
        return mayor
    elif lista[0] > mayor:
        return max(lista[1:], lista[0])
    return max(lista[1:], mayor)


def min(lista, menor):
    if lista == []:
        return menor
    elif lista[0] < menor:
        return min(lista[1:], lista[0])
    return min(lista[1:], menor)


def suma(lista):
    return max(lista, 0)+min(lista, max(lista, 0))


def tuplas(lista, res):
    if lista != []:
        return tuplas(lista[1:], res + [[max(lista[0], 0), min(lista[0], max(lista[0], 0)), suma(lista[0])]])
    return res


def main(lista):
    return tuplas(lista, [])


print(main([[1, 2, 3, 7], [4, 5, 1]]))
