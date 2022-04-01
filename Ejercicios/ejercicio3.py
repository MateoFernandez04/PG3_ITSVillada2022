anchura = int(input("Anchura del rectángulo: "))
altura = int(input("Altura del rectángulo: "))
caracter =input("Caracter a escribir: ")
for i in range(altura):
    for j in range(anchura):
        print(caracter," ",end="")
    print()
