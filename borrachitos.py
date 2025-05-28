import time
import random

baño_ocupado = False
llamada_ocupada = False

acciones_posibles = ["tomar", "cantar", "llamar_ex", "usar_baño"]

class Borracho:
    def __init__(self, nombre):
        self.nombre = nombre

    def tomar(self):
        print(f"{self.nombre} está tomando cerveza... ")
        time.sleep(1)

    def cantar(self):
        print(f"{self.nombre} está cantando...")
        time.sleep(1)

    def llamar_ex(self):
        global llamada_ocupada
        if not llamada_ocupada:
            llamada_ocupada = True
            print(f"{self.nombre} está llamando a su ex...")
            time.sleep(1)
            print(f"{self.nombre} terminó de llamar a su ex...")
            llamada_ocupada = False
        else:
            print(f"{self.nombre} no puede llamar a su ex, línea ocupada...")
            self.cantar()

    def usar_baño(self):
        global baño_ocupado
        if not baño_ocupado:
            baño_ocupado = True
            print(f"{self.nombre} está usando el baño...")
            time.sleep(1)
            print(f"{self.nombre} terminó de usar el baño...")
            baño_ocupado = False
        else:
            print(f"{self.nombre} no puede usar el baño, está ocupado...")
            self.tomar()

    def realizar_accion(self, accion):
        if accion == "tomar":
            self.tomar()
        elif accion == "cantar":
            self.cantar()
        elif accion == "llamar_ex":
            self.llamar_ex()
        elif accion == "usar_baño":
            self.usar_baño()

borrachos = [Borracho("Carlos "), Borracho("Brayan "), Borracho("Zuñiga "), Borracho("Antuna "), Borracho("Pancho ")]

#Se usan las dos acciones globales(llamar y el baño) y se rellenan las otras 3 de forma aleatoria.
for ciclo in range(4):
    print(f"\n-- Ciclo {ciclo + 1} --")
    random.shuffle(borrachos)

    acciones_disponibles = ["llamar_ex", "usar_baño"]
    acciones_asignadas = []

    for borracho in borrachos:
        if acciones_disponibles:
            accion = acciones_disponibles.pop()
        else:
            accion = random.choice(["tomar", "cantar"])
        acciones_asignadas.append((borracho, accion))

    for borracho, accion in acciones_asignadas:
        borracho.realizar_accion(accion)
