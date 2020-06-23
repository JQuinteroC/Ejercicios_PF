"""
Dado un árbol binario ordenado, retornar una lista de listas con los dígitos
de cada número en el árbol, manteniendo el orden de los elementos
"""

class Nodo():
    def __init__(self,valor,izquierda = None, derecha = None):
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha

def en_orden(arbol):
    if arbol == None:
        return []
    return en_orden(arbol.izquierda) + [[arbol.valor]] + en_orden(arbol.derecha)

print(en_orden(Nodo(15,Nodo(10,None,Nodo(12)),Nodo(25))))