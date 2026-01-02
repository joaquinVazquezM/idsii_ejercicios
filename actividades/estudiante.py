class Estudiante:
    def __init__(self, nombre, matricula, carrera, promedio):
        self.nombre = nombre
        self.matricula = matricula
        self.carrera = carrera
        self.promedio = promedio

    def mostrarDatos(self):
        print("Nombre: ", self.nombre)
        print("Matrícula: ", self.matricula)
        print("Carrera: ", self.carrera)
        print("Promedio: ", self.promedio)

    def inscribirseCurso(self, curso):
        print(f"{self.nombre} se ha inscrito al curso de {curso}")

estudiante1 = Estudiante("Juan Pérez", "20260001", "Ingeniería en Sistemas", 8.7)

estudiante1.mostrarDatos()
estudiante1.inscribirseCurso("Ingeniería de Software")