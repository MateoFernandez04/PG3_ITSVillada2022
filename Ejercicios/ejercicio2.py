print("Coloque un año")
anio=int(input())


def bisiest(num):
    if num % 400 == 0:
        return True
    elif num % 100 == 0:
        return False
    elif num % 4 == 0:
        return True
    else:
        return False

print("¿El año es bisiesto?:", bisiest(anio))