#Ejercicio 16

class Pila:
    def __init__(self):
        self.items = []
    
    def esta_vacia(self):
        return self.items == []
    
    def apilar(self, item):
        self.items.append(item)
    
    def desapilar(self):
        return self.items.pop()
    
    def ver_tope(self):
        return self.items[-1]
    
    def tamano(self):
        return len(self.items)

# Función para encontrar la intersección de dos pilas
def interseccion_pilas(pila1, pila2):
    conjunto1 = set()
    while not pila1.esta_vacia():
        conjunto1.add(pila1.desapilar())
    
    conjunto2 = set()
    while not pila2.esta_vacia():
        conjunto2.add(pila2.desapilar())
    interseccion = conjunto1.intersection(conjunto2)
    for item in conjunto1:
        pila1.apilar(item)
    for item in conjunto2:
        pila2.apilar(item)
    return interseccion

# Ejemplo de uso
pila_ep5 = Pila()
pila_ep7 = Pila()

# Agregar personajes del episodio V
pila_ep5.apilar("Luke Skywalker")
pila_ep5.apilar("Han Solo")
pila_ep5.apilar("Leia Organa")
pila_ep5.apilar("Darth Vader")
pila_ep5.apilar("Yoda")

# Agregar personajes del episodio VII
pila_ep7.apilar("Luke Skywalker")
pila_ep7.apilar("Han Solo")
pila_ep7.apilar("Leia Organa")
pila_ep7.apilar("Kylo Ren")
pila_ep7.apilar("Rey")

# Encontrar la intersección de ambas pilas
personajes_comunes = interseccion_pilas(pila_ep5, pila_ep7)
print("Personajes que aparecen en ambos episodios:", personajes_comunes)
