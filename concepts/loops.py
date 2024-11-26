# Loops

""" 

for counter in range():
    codigo

for value in collection:
    codigo


"""

for x in range(1, 11):
    print(x)

""" 
range(start = 0, stop, step = 1)
"""
for x in range(40, 80, 5): # 40 - 75
    print(x)


numeros = [1, 2, 3, 4]

for x in range(len(numeros)):
    print(numeros[x])

for num in numeros:
    print(num)

i = 1
while i <= 10:
    print(i)
    i+=1 # i = i + 1

indice = 0
while indice < len(numeros):
    print(numeros[indice])
    indice += 1