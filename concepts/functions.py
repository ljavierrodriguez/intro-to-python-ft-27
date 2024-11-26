# Functions

""" 
Function Declarativa
"""
def saludar():
    print("Hola")

""" 
Funcion Anidada
"""
def exterior():
    nombre = "John Doe"

    def interior():
        print(f"Hola {nombre}")

    interior()

exterior()

""" 
Function Lambda
"""
sumar = lambda a, b: a + b 

sumar(5, 5)


def sumar(a, b = 5):
    return a + b


""" 
Parametros Keywords
"""

def nombre_completo(nombre, apellido):
    return f"{nombre} {apellido}"

nombre_completo(apellido="Doe", nombre="John")

""" 
Empaquetamiento de Parametros
"""

def totalizar(*args): # *args = tuple
    return sum(args)

totalizar(1, 2, 3, 4, 5)

""" 
Empaquetamiento de Parametros Keywords
"""

def informacion(**kwargs): # **kwargs = dict
    return f"Nombre: {kwargs["nombre"]}, Apellido: {kwargs["apellido"]}"


informacion(nombre="John", apellido="Doe")