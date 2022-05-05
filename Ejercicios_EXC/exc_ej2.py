def division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print('¡No se puede dividir por cero!')
    else:
        print(f"La division entre'{a}' y {b} da {result} ")

num = int(input("Coloque un numero: "))
num2 = int(input("Coloque otro numero: "))
division(num,num2)
