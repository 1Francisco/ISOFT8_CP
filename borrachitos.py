import time
import random

baño_ocupado = False
llamada_ocupada = False

acciones = ["tomar", "cantar", "llamar_ex", "usar_baño"]

class Borracho:
    def __init__(self, nombre):
        self.nombre = nombre
        

    def tomar(self):
        print(f"{self.nombre} esta tomando cerveza...")
        time.sleep(1)

    def cantar(self):
        print(f"{self.nombre} esta cantando...")
        time.sleep(1)

    def llamar_ex(self):
        global llamada_ocupada
        
        if not llamada_ocupada:
            llamada_ocupada = True
            print(f"{self.nombre} esta llamando a su ex...")
            time.sleep(1)
            print(f"{self.nombre} termino de llamar a su ex...")
            llamada_ocupada = False
        else:
            print(f"{self.nombre} esta ocupado, no puede llamar a su ex...")
            self.cantar()

    def usar_baño(self):
        global baño_ocupado
        if not baño_ocupado:
            baño_ocupado = True
            print(f"{self.nombre} esta usando el baño...")
            time.sleep(1)
            print(f"{self.nombre} termino de usar el baño...")
            baño_ocupado = False
        else:
            print(f"{self.nombre} esta ocupado, no puede usar el baño...")
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

borrachos = [Borracho("Carlos"), Borracho("Brayan"), Borracho("Zuñiga"), Borracho("Antuna"), Borracho("Pancho")]

for ciclo in range(4):
    print(f" --Ciclo {ciclo +1}--")
    random.shuffle(borrachos)
    for borrachines in borrachos:
        accion = random.choice(acciones)
        borrachines.realizar_accion(accion)
