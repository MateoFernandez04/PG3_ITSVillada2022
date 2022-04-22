class Operacion:

    def __init__(self):
        self.valor1=int(input("Ingresar numero:"))
        self.valor2=int(input("Ingresar sgundo numero:"))
        self.sumar()
        self.restar()
        self.multiplicar()
        self.dividir()

    def sumar(self):
        suma=self.valor1+self.valor2
        print("La suma es",suma)

    def restar(self):
        resta=self.valor1-self.valor2
        print("La resta es:",resta)

    def multiplicar(self):
        multiplicacion=self.valor1*self.valor2
        print("El producto es",multiplicacion)

    def dividir(self):
        if self.valor2 == 0:
            print("No se puede realizar la división")
        else:
            division=self.valor1/self.valor2
            print("La division es",division)


# bloque principal

operacion1=Operacion()