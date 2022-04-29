from typing import List

listavalores: List[int]=[10, 56, 23, 120, 94]
print(listavalores)
print("Escriba el valor a  buscar")
numero: int =int(input())
def BinarySearch(lys, val):
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val<lys[mid]:
                last = mid -1
            else:
                first = mid +1
    return index

print("Índice:", BinarySearch(listavalores,numero))