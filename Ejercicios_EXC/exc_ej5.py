while True:
    try:
        escrito = input("Ingresar string: ")
        f = open('./Ejercicios_EXC/texto.txt', 'a')

        if escrito.isnumeric():
            f.write(int(escrito))
        else:
            f.write('\n' + escrito)
        while True:
            print("Quiere seguir escribiendo: ")
            option=input("ingrese opción Yes=s // No=n: ")
            if option == "s" or option == "n":
                break;
        if option=="n":
            break  
    except TypeError:
        print("No intente ingresar numeros")