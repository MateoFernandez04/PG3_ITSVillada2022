meses=("enero","febrero","marzo","abril","mayo","junio",
       "julio","agosto","septiembre","octubre","noviembre","diciembre")
try:
    indice=int(input("Ingrese un número de mes:"))
    print(meses[indice-1])
except IndexError:
    print("No es un índice de un mes")