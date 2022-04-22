class Triangulo:

    def inicializar(self,lado1,lado2,lado3):
        self.lado1=lado1
        self.lado2=lado2
        self.lado3=lado3

    def imprimir_LMayor(self):
        if self.lado1 > self.lado2:
            if self.lado1 > self.lado3:
                print("Lado mayor: ",self.lado1)
            else:
                print("Lado mayor: ",self.lado3)
        elif self.lado2>self.lado3:
            print("Lado mayor: ",self.lado2)
        else:
            print("Lado mayor: ",self.lado3)

    def is_equilatero(self):
        if self.lado1 ==self.lado2 ==self.lado3:
            print("Es equilatero\n")
        else:
            print("No es equilatero\n")


# principal

triangulo1=Triangulo()
triangulo1.inicializar(5,5,5)
triangulo1.imprimir_LMayor()
triangulo1.is_equilatero()

triangulo2=Triangulo()
triangulo2.inicializar(5,3,4)
triangulo2.imprimir_LMayor()
triangulo2.is_equilatero()
