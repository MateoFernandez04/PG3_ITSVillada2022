
while True:
    try:
        num = int(input("Please enter a number: "))
        num2= int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

    int (input("Coloque una opción 1=no 2=si"))
