class Actividad:
    def __init__(self, nombre, hora, prioridad, esfuerzo_requerido):
        self.nombre = nombre
        self.hora = hora
        self.prioridad = prioridad
        self.esfuerzo_requerido = esfuerzo_requerido #Nuevo atributo

    def mostrar_info(self):
        print("Actividad:", self.nombre)
        print("Hora:", self.hora)
        print("Prioridad:", self.prioridad)
        print("Esfuerzo Requerido (1-10)", self.esfuerzo_requerido)
        self.evaluar_valoracion() #Llamamos el nuevo método
        print("-------------------------")

    #Nuevo método: Evalúa si la actividad será valorada
    def evaluar_valoracion(self):
        if self.esfuerzo_requerido >= 7:
            print("Esta actividad requiere un esfuerzo ALTO y será MUY VALORADA")
        elif self.esfuerzo_requerido >=4:
            print("Esta actividad requiere un esfuerzo MODERADO y será VALORADA")
        else:
            print("Esta actividad requiere un esfuerzo BAJO")



# Crear un objeto
print("---Actividad 1---")
actividad1 = Actividad("Diseñar UI/UX", "09:00", "Alta", 8)
# Usar el método
actividad1.mostrar_info()

# Crear un objeto
print("---Actividad 2---")
actividad2 = Actividad("Revisar correos", "10:00", "Media", 3)
# Usar el método
actividad2.mostrar_info()

# Crear un objeto
print("---Actividad 3---")
actividad3 = Actividad("Aprender programación orientada a objetos", "14:00", "Alta", 7)
# Usar el método
actividad3.mostrar_info()

