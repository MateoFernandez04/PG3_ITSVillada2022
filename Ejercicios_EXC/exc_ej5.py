while True:
    try:
        ingreso = input("Ingresar string: ")
        datos = open('./Ejercicios_EXC/texto.txt', 'a')

        if ingreso.isnumeric():
            datos.write(int(ingreso))
        else:
            datos.write(ingreso)
        while True:
            print("Quiere seguir escribiendo: /n")
            ans=input("ingrese opción Yes=s // No=n: ")
            if ans == "s" or ans == "n":
                break;
        if ans=="n":
            break  
    except TypeError:
        print("No intente ingresar numeros")