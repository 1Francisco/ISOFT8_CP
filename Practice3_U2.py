import time
import random

class DrunkardsSimulation:
    def __init__(self):
        self.current_cycle = 1
        self.max_cycles = 5
        self.drunkards_core1 = [f"Borrachito_{i}" for i in range(1, 7)]
        self.drunkards_core2 = [f"Borrachita_{i}" for i in range(1, 7)]
        
        self.stats = {
            'beer': {'Core1': 0, 'Core2': 0},
            'rockola': {'Core1': 0, 'Core2': 0},
            'sing': {'Core1': 0, 'Core2': 0},
            'dance': {'Core1': 0, 'Core2': 0}
        }

        self.log_recursos = []  # Para registrar quién usó cada recurso por ciclo

    def core_cerveza(self):
        return 'Core1' if self.current_cycle % 2 != 0 else 'Core2'

    def core_rockola(self):
        return 'Core2' if self.current_cycle % 2 != 0 else 'Core1'

    def pedir_cerveza(self, drunkard, core):
        print(f"Ciclo {self.current_cycle}: {drunkard} está pidiendo cervez.")
        self.stats['beer'][core] += 1
        time.sleep(0.1)

    def rockola(self, drunkard, core):
        print(f"Ciclo {self.current_cycle}: {drunkard} está usando la rockola.")
        self.stats['rockola'][core] += 1
        time.sleep(0.1)

    def cantar(self, drunkard, core):
        print(f"Ciclo {self.current_cycle}: {drunkard} está cantando.")
        self.stats['sing'][core] += 1
        time.sleep(0.1)

    def bailar(self, drunkard, core):
        print(f"Ciclo {self.current_cycle}: {drunkard} está bailando.")
        self.stats['dance'][core] += 1
        time.sleep(0.1)

    def simulate_cycle(self):
        print(f"\n=== Comenzando Ciclo {self.current_cycle} ===")
        
        cerveza_core = self.core_cerveza()
        rockola_core = self.core_rockola()

        core1 = [(d, 'Core1') for d in self.drunkards_core1]
        core2 = [(d, 'Core2') for d in self.drunkards_core2]
        all_drunkards = core1 + core2
        random.shuffle(all_drunkards)

        # Elegir candidatos válidos para cada recurso
        cerveza_candidates = [d for d in all_drunkards if d[1] == cerveza_core]
        rockola_candidates = [d for d in all_drunkards if d[1] == rockola_core]

        cerveza_user = random.choice(cerveza_candidates)
        rockola_user = random.choice([d for d in rockola_candidates if d != cerveza_user] or [cerveza_user])

        # Registrar los usuarios
        self.log_recursos.append({
            'ciclo': self.current_cycle,
            'cerveza': cerveza_user,
            'rockola': rockola_user
        })

        for drunkard, core in all_drunkards:
            if (drunkard, core) == cerveza_user:
                self.pedir_cerveza(drunkard, core)
            elif (drunkard, core) == rockola_user:
                self.rockola(drunkard, core)
            else:
                action = random.choice([self.cantar, self.bailar])
                action(drunkard, core)

        self.current_cycle += 1
        time.sleep(1)

    def run_simulation(self):
        print("Iniciando simulación de borrachos en paralelo.")
        print(f"Core1: {', '.join(self.drunkards_core1)}")
        print(f"Core2: {', '.join(self.drunkards_core2)}\n")

        while self.current_cycle <= self.max_cycles:
            self.simulate_cycle()
        
        self.print_stats()

    def print_stats(self):
        print("\n=== Estadísticas Finales ===")
        print("Accesos a Pedir Cerveza:")
        print(f"  Core1: {self.stats['beer']['Core1']}")
        print(f"  Core2: {self.stats['beer']['Core2']}")
        
        print("\nAccesos a Rockola:")
        print(f"  Core1: {self.stats['rockola']['Core1']}")
        print(f"  Core2: {self.stats['rockola']['Core2']}")
        
        print("\nVeces que cantaron:")
        print(f"  Core1: {self.stats['sing']['Core1']}")
        print(f"  Core2: {self.stats['sing']['Core2']}")
        
        print("\nVeces que bailaron:")
        print(f"  Core1: {self.stats['dance']['Core1']}")
        print(f"  Core2: {self.stats['dance']['Core2']}")


# Ejecutar la simulación
if __name__ == "__main__":
    simulation = DrunkardsSimulation()
    simulation.run_simulation()
