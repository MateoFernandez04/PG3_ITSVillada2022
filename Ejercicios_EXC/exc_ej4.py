try:
    num1=int(input("Ingrese primer numero:"))
    num2=int(input("Ingrese segundo numero:"))
except ZeroDivisionError:
    print("No se puede dividir por cero.")
except ValueError:
    print("Los valores a ingresar deben ser enteros")
else:
    division=num1/num2
    print("El resultado de la división es", division)