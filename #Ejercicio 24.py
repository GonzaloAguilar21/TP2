#Ejercicio 24

class Personaje:
    def __init__(self, nombre, cantidad_peliculas):
        self.nombre = nombre
        self.cantidad_peliculas = cantidad_peliculas

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
    
    def obtener_elemento(self, posicion):
        return self.items[-posicion] if 1 <= posicion <= len(self.items) else None

def posicion_personaje(pila, nombre):
    for i in range(1, pila.tamano() + 1):
        if pila.obtener_elemento(i).nombre == nombre:
            return i
    return -1
def personajes_mas_de_5_peliculas(pila):
    personajes = []
    for i in range(1, pila.tamano() + 1):
        personaje = pila.obtener_elemento(i)
        if personaje.cantidad_peliculas > 5:
            personajes.append((personaje.nombre, personaje.cantidad_peliculas))
    return personajes
def peliculas_black_widow(pila):
    for i in range(1, pila.tamano() + 1):
        personaje = pila.obtener_elemento(i)
        if personaje.nombre == "Black Widow":
            return personaje.cantidad_peliculas
    return 0
def personajes_con_letras(pila, letras):
    personajes = []
    for i in range(1, pila.tamano() + 1):
        personaje = pila.obtener_elemento(i)
        if personaje.nombre[0].upper() in letras:
            personajes.append(personaje.nombre)
    return personajes
# Crear la pila y agregar personajes
pila_mcu = Pila()

# Agregar personajes a la pila
pila_mcu.apilar(Personaje("Iron Man", 10))
pila_mcu.apilar(Personaje("Captain America", 9))
pila_mcu.apilar(Personaje("Thor", 8))
pila_mcu.apilar(Personaje("Hulk", 7))
pila_mcu.apilar(Personaje("Black Widow", 8))
pila_mcu.apilar(Personaje("Hawkeye", 6))
pila_mcu.apilar(Personaje("Rocket Raccoon", 4))
pila_mcu.apilar(Personaje("Groot", 4))
pila_mcu.apilar(Personaje("Doctor Strange", 3))
pila_mcu.apilar(Personaje("Spider-Man", 5))
pila_mcu.apilar(Personaje("Black Panther", 4))

# a. Determinar la posición de Rocket Raccoon y Groot
pos_rocket = posicion_personaje(pila_mcu, "Rocket Raccoon")
pos_groot = posicion_personaje(pila_mcu, "Groot")
print(f"Rocket Raccoon está en la posición: {pos_rocket}")
print(f"Groot está en la posición: {pos_groot}")

# b. Determinar los personajes que participaron en más de 5 películas
personajes_5_peliculas = personajes_mas_de_5_peliculas(pila_mcu)
print("Personajes que participaron en más de 5 películas:")
for nombre, cantidad in personajes_5_peliculas:
    print(f"{nombre}: {cantidad} películas")

# c. Determinar en cuántas películas participó Black Widow
peliculas_black_widow = peliculas_black_widow(pila_mcu)
print(f"Black Widow participó en {peliculas_black_widow} películas")

# d. Mostrar personajes cuyos nombres empiezan con C, D y G
letras = {'C', 'D', 'G'}
personajes_letras = personajes_con_letras(pila_mcu, letras)
print("Personajes cuyos nombres empiezan con C, D y G:")
for nombre in personajes_letras:
    print(nombre)
