import time
import random

baño_ocupado = False
llamada_ocupada = False
cervezas_servidas = {}

acciones_posibles = ["sirviendo_cerveza", "cantar", "llamar_ex", "usar_baño"]

class Bartender:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def servir_cerveza(self, drunkard):
        
        if drunkard.nombre not in cervezas_servidas:
            cervezas_servidas[drunkard.nombre] = 0
        cervezas_servidas[drunkard.nombre] += 1
        print(f"{self.nombre} ha servido {cervezas_servidas[drunkard.nombre]} cerveza(s) a {drunkard.nombre}")

class Drunkard:
    def __init__(self, nombre):
        self.nombre = nombre
    
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
        if self.nombre in cervezas_servidas and cervezas_servidas[self.nombre] >= 1:
            if not baño_ocupado:
                baño_ocupado = True
                print(f"{self.nombre} está usando el baño...")
                time.sleep(1)
                print("Bartender: ¡Baño Libre!")
                baño_ocupado = False
            else:
                print(f"{self.nombre} no puede usar el baño, está ocupado...")
                self.cantar()
        else:
            
            self.cantar()
    
    def realizar_accion(self, accion, bartender):
        if accion == "sirviendo_cerveza":
            bartender.servir_cerveza(self)
        elif accion == "cantar":
            self.cantar()
        elif accion == "llamar_ex":
            self.llamar_ex()
        elif accion == "usar_baño":
            self.usar_baño()

bartender = Bartender("Bartender")
drunkards = [Drunkard("Carlos"), Drunkard("Brayan"), Drunkard("Zuñiga"), Drunkard("Antuna"), Drunkard("Pancho")]

for drunkard in drunkards:
    cervezas_servidas[drunkard.nombre] = 0

def asignar_acciones(drunkards):
    drunkards_disponibles = drunkards.copy()
    random.shuffle(drunkards_disponibles)
    
    acciones_asignadas = []
    acciones_prioritarias = ["llamar_ex", "usar_baño"]
    
    for accion in acciones_prioritarias:
        if drunkards_disponibles:
            drunkard = drunkards_disponibles.pop()
            acciones_asignadas.append((drunkard, accion))
    
    for drunkard in drunkards_disponibles:
        accion = random.choice(["sirviendo_cerveza", "cantar"])
        acciones_asignadas.append((drunkard, accion))
    
    return acciones_asignadas

for ciclo in range(4):
    print(f"\n-- Ciclo {ciclo + 1} --")
    
    acciones_asignadas = asignar_acciones(drunkards)
    
    random.shuffle(acciones_asignadas)
    for drunkard, accion in acciones_asignadas:
        drunkard.realizar_accion(accion, bartender)
