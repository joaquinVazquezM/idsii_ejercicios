class Actividad:
    def __init__(self, nombre, hora, prioridad):
        self.nombre = nombre
        self.hora = hora
        self.prioridad = prioridad

    def mostrar_info(self):
        print("Actividad:", self.nombre)
        print("Hora:", self.hora)
        print("Prioridad:", self.prioridad)
        print("-------------------------")


# Crear un objeto
actividad1 = Actividad("Estudiar", "16:00", "Alta")

# Usar el método
actividad1.mostrar_info()
