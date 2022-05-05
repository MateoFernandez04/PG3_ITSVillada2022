
while True:
    try:
        num = int(input("Por favor coloque un número: "))
        num2= int(input("Por favor coloque un número: "))
    except ValueError:
        print("Los números colocados no son enteros")
    else:
        result=num+num2
        print(result)
    while True:
        print("Quiere seguir colocando números\n 1=si  2=no")
        option=int(input())
        if option == 1 or option == 2:
            break;
    if option==2:
        break
