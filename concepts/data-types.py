# Data Types
""" 
String
Int
Float

None

Array
    List
    Tuples
    Set

Dict

"""
""" 
var_name = value
"""

nombre = "John"
apellido = 'Doe'
nombre_completo = f"{nombre} {apellido}"

edad = 42
precio = 10.50
temp = -10.5

users = None
posts = None

# Lista

numeros = [1, 2, 3, 4]
nombres = list()
nombres.append("Hugo")
nombres.append("Paco")
nombres.append("Luis")

nombres[0]
numeros.append(5)
numeros.pop()

# Tuples
status = ("active", "inactive", "suspended", "canceled", "completed")
status[0]

# Sets
frutas = {"Pera", "Manzana", "Uva", "Banana", "Kiwi", "Durazno"}

print(nombres)

print(dir(numeros))

# Dict

persona = {
    "nombre": "John",
    "apellido": "Doe"
}

print(persona["nombre"])

persona["edad"] = 10

print(persona)