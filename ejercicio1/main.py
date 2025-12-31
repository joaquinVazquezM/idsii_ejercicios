# 1. LA CLASE (El Molde)
class Libro:
    # 2. LOS ATRIBUTOS (Los datos que definen al objeto)
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    # 3. EL MÉTODO (La acción que el objeto puede realizar)
    def describir(self):
        return f"Este libro es '{self.titulo}' escrito por {self.autor}."

# 4. LAS INSTANCIAS (Los objetos reales creados con el molde)
libro_a = Libro("El Principito", "Saint-Exupéry")
libro_b = Libro("Hamlet", "Shakespeare")

# Usando los objetos
print(libro_a.describir())
print(libro_b.describir())