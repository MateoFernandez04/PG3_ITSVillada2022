
while True:
    try:
        num = int(input("Please enter a number: "))
        num2= int(input("Please enter a number: "))
    except ValueError:
        print("Los números colocados no son enteros")
    else:
        result=num+num2
        print(result)
    print("Quiere seguir colocando números\n 1=no  2=si")
    option=int(input())
    if option==1:
        break
