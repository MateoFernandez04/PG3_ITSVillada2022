print("Escriba el valor de la altura")
num: int =int(input())
caracter:str =input("Caracter a escribir: ")
print("1-triangulo Normal")

print("2-triangulo invertido")
option:int=int(input("Coloque opción a hacer: "))
aux:int=num
if option ==1:
    for i in range(num):
        print(" " *(num -i -1)+ caracter *(2 *i +1))
else:
    if option==2:
        for i in range(num):
            print(" " *(num +(i+num) -1)+ caracter *(2 *(i+aux) -1))
            aux=aux-2
    else:
        result1=[" "*(num-i)+"*"*(i+i-1) for i in range(1,num+1)]
        print("\n".join(result1+list(reversed(result1[:-1]))))