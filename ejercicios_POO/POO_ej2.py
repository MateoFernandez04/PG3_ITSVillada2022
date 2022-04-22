class Alumno:

    def inicializar(self,nombre,calificacion):
        self.nombre=nombre
        self.nota=calificacion

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Nota:",self.nota)

    def estado(self):
        if self.nota>=4:
            print("Estado: Regular\n")
        else:
            print("Libre\n")


# principal

alumno1=Alumno()
alumno1.inicializar("Mateo",2)
alumno1.imprimir()
alumno1.estado()

alumno2=Alumno()
alumno2.inicializar("Agustín",5)
alumno2.imprimir()
alumno2.estado()

alumno3=Alumno()
alumno3.inicializar("Alonso",4)
alumno3.imprimir()
alumno3.estado()