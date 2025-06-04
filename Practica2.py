import time
import random

baño_ocupado = False
llamada_ocupada = False
cervezas_servidas = {}  # Contador de cervezas por Drunkard

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
        # Verificar si ha tomado al menos 1 cerveza
        if self.nombre in cervezas_servidas and cervezas_servidas[self.nombre] >= 1:
            if not baño_ocupado:
                baño_ocupado = True
                print(f"{self.nombre} está usando el baño...")
                time.sleep(1)
                print(f"{self.nombre} terminó de usar el baño...")
                print("¡Baño Libre!")
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

# Crear personajes
bartender = Bartender("Bartender")
drunkards = [Drunkard("Carlos"), Drunkard("Brayan"), Drunkard("Zuñiga"), Drunkard("Antuna"), Drunkard("Pancho")]

# Inicializar contador de cervezas
for drunkard in drunkards:
    cervezas_servidas[drunkard.nombre] = 0

# Función para asignar acciones asegurando que todos participen
def asignar_acciones(drunkards):
    # Hacer copia de la lista para no modificar la original
    drunkards_disponibles = drunkards.copy()
    random.shuffle(drunkards_disponibles)
    
    # Asignar acciones prioritarias primero
    acciones_asignadas = []
    acciones_prioritarias = ["llamar_ex", "usar_baño"]
    
    # Asignar acciones prioritarias a drunkards aleatorios
    for accion in acciones_prioritarias:
        if drunkards_disponibles:
            drunkard = drunkards_disponibles.pop()
            acciones_asignadas.append((drunkard, accion))
    
    # Asignar el resto de acciones a los drunkards restantes
    for drunkard in drunkards_disponibles:
        accion = random.choice(["sirviendo_cerveza", "cantar"])
        acciones_asignadas.append((drunkard, accion))
    
    return acciones_asignadas

# Ejecución del programa
for ciclo in range(4):
    print(f"\n-- Ciclo {ciclo + 1} --")
    
    # Asignar acciones asegurando que todos participen
    acciones_asignadas = asignar_acciones(drunkards)
    
    # Ejecutar acciones en orden aleatorio
    random.shuffle(acciones_asignadas)
    for drunkard, accion in acciones_asignadas:
        drunkard.realizar_accion(accion, bartender)

