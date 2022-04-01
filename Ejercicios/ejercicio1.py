from typing import List

listavalores: List[int]=[10, 56, 23, 120, 94]
print(listavalores)
print("Escriba el valor a  buscar")
numero: int =int(input())
def buscar(lista: List[int] , num: int):
    print(lista)
    print(num)
    if num in lista: 
         indice=(lista.index(num))
    else:
        indice=("No hay")
    return indice 


print("Índice:", buscar(listavalores,numero))