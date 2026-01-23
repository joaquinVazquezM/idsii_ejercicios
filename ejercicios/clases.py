class Estudiante:
    # Constructor
    def __init__(self, nombre, matricula):
        self.__nombre = nombre          # Privado
        self.__matricula = matricula    # Privado
        self.__edad = 0                 # Privado
        self.__promedio = 0.0           # Privado
        self.__activo = True            # Privado
    
    # Getters (métodos públicos para obtener valores)
    def get_nombre(self):
        return self.__nombre
    
    def get_edad(self):
        return self.__edad
    
    def get_promedio(self):
        return self.__promedio
    
    # Setters (métodos públicos para modificar con validación)
    def set_nombre(self, nombre):
        if len(nombre) > 0:
            self.__nombre = nombre
        else:
            print("Error: Nombre no puede estar vacío")
    
    def set_edad(self, edad):
        if 15 <= edad <= 100:
            self.__edad = edad
        else:
            print("Error: Edad debe estar entre 15 y 100")
    
    # Métodos de negocio
    def calcular_promedio(self, calificaciones):
        if len(calificaciones) > 0:
            self.__promedio = sum(calificaciones) / len(calificaciones)
        return self.__promedio
    
    def esta_aprobado(self):
        return self.__promedio >= 6.0
    
    # Método privado (solo para uso interno)
    def __validar_matricula(self):
        return len(self.__matricula) == 10
    
    # Representación en texto
    def __str__(self):
        return f"Estudiante: {self.__nombre} ({self.__matricula})"

# Uso:
estudiante = Estudiante("Ana García", "2024001234")
estudiante.set_edad(20)
estudiante.calcular_promedio([8.5, 9.0, 7.5, 8.0])

print(estudiante)  # Estudiante: Ana García (2024001234)
print(f"Promedio: {estudiante.get_promedio()}")  # 8.25
print(f"¿Aprobado? {estudiante.esta_aprobado()}")  # True