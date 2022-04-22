
class Persona:

    def __init__(self):
        self.nombre=input("Ingrese el nombre:")
        self.edad=int(input("Ingrese la edad:"))

    def imprimir(self):
        print ( f"Nombre: { self . nombre } || Edad: { self . edad } " )

class Empleado(Persona):

    def __init__(self):
        super().__init__()
        self.sueldo=float(input("Ingrese el sueldo:"))
        print("")

    def imprimir(self):
        super().imprimir()
        print("Sueldo:",self.sueldo)

    def estado_impuestos(self):
        if self.sueldo.is_integer():
            return True
        if self.sueldo>3000:
            print(f"{self.sueldo} mayor a 3000: Debe paga impuestos.")
        else:
            print(f"{self.sueldo} menor a 3000: No debe paga impuestos.")


# bloque principal

persona1=Persona()
persona1.imprimir()
print("////////////////////////////")
empleado1=Empleado()
empleado1.imprimir()
empleado1.estado_impuestos()
print("////////////////////////////")
empleado2=Empleado()
empleado2.imprimir()
empleado2.estado_impuestos()