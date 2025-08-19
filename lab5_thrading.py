import threading
import time
import random

class GrupoBorrachos:
    def __init__(self, nombre, rockola, mesa_billar, bano):
        self.nombre = nombre
        self.rockola = rockola
        self.mesa_billar = mesa_billar
        self.bano = bano
        self.borrachos = [f"{nombre}-1", f"{nombre}-2", f"{nombre}-3"]
        self.ciclos_completados = 0
        
    def usar_rockola(self):
        with self.rockola:
            print(f"🎵 {self.nombre} está usando la ROCKOLA")
            time.sleep(random.uniform(0.5, 1.5))
            print(f"🎵 {self.nombre} terminó de usar la ROCKOLA")
            
    def usar_mesa_billar(self):
        with self.mesa_billar:
            print(f"🎱 {self.nombre} está usando la MESA DE BILLAR")
            time.sleep(random.uniform(0.7, 2.0))
            print(f"🎱 {self.nombre} terminó de usar la MESA DE BILLAR")
            
    def usar_bano(self, borracho):
        with self.bano:
            print(f"🚽 {borracho} está usando el BAÑO")
            time.sleep(random.uniform(0.3, 1.0))
            print(f"🚽 {borracho} terminó de usar el BAÑO")
            
    def ciclo_borracho(self):
        # Cada borracho del grupo debe usar el baño individualmente.
        for borracho in self.borrachos:
            self.usar_bano(borracho)
            
        # El grupo usa recursos compartidos
        if random.choice([True, False]):
            self.usar_rockola()
            self.usar_mesa_billar()
        else:
            self.usar_mesa_billar()
            self.usar_rockola()
            
        self.ciclos_completados += 1
        print(f"✅ {self.nombre} completó ciclo {self.ciclos_completados}")
        
    def ejecutar(self):
        while self.ciclos_completados < 5:
            try:
                self.ciclo_borracho()
                time.sleep(random.uniform(0.1, 0.5))
            except Exception as e:
                print(f"❌ Error en {self.nombre}: {e}")

def main():
    # Crear semáforos para los recursos compartidos
    rockola = threading.Semaphore(1)      # Solo 1 grupo a la vez
    mesa_billar = threading.Semaphore(1)  # Solo 1 grupo a la vez
    bano = threading.Semaphore(1)         # Solo 1 persona a la vez
    
    # Crear Lock adicional para controlar acceso a recursos críticos.
    lock_contador = threading.Lock()
    
    # Crear los grupos de borrachos
    grupo_a = GrupoBorrachos("GrupoA", rockola, mesa_billar, bano)
    grupo_b = GrupoBorrachos("GrupoB", rockola, mesa_billar, bano)
    grupo_c = GrupoBorrachos("GrupoC", rockola, mesa_billar, bano)
    
    # Crear e iniciar los hilos
    hilos = []
    for grupo in [grupo_a, grupo_b, grupo_c]:
        hilo = threading.Thread(target=grupo.ejecutar, name=grupo.nombre)
        hilos.append(hilo)
        hilo.start()
    
    # Esperar a que todos los hilos terminen.
    for hilo in hilos:
        hilo.join()
    
    print("\n" + "="*50)
    print("SIMULACIÓN COMPLETADA")
    print("="*50)
    print(f"GrupoA completó {grupo_a.ciclos_completados} ciclos")
    print(f"GrupoB completó {grupo_b.ciclos_completados} ciclos")
    print(f"GrupoC completó {grupo_c.ciclos_completados} ciclos")

if __name__ == "__main__":
    main()
