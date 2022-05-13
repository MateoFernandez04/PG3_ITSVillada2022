meses=("enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre")
while True:
    try:
        indice=int(input("Ingrese un número de mes:"))
        print(meses[indice-1])
    except IndexError:
        print("No es un índice de un mes")

    flag = input("¿Desea continuar? (S/N)")
    if flag == "N":
        break