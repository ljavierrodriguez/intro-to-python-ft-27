# Object Oriented Programming (Programacion Orientada a Objetos)

persona = {
    "nombre": "",
    "apellido": ""
}

class Persona:
    nombre = ""
    apellido = ""
    edad = ""

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludar(self):
        pass

    def comer(self):
        pass

    def hablar(self):
        pass


persona1 = Persona("John", "Doe")
persona2 = Persona("Jane", "Doe")
persona3 = Persona("Mickey", "Mouse")

class Estudiante(Persona):
    pass

estudiante1 = Estudiante()
print(estudiante1.hablar())