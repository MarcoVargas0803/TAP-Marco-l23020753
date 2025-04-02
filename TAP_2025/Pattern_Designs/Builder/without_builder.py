# Clase con un constructor tradicional
class Computadora:
    def __init__(self, procesador, ram, almacenamiento, tarjeta_grafica):
        self.procesador = procesador
        self.ram = ram
        self.almacenamiento = almacenamiento
        self.tarjeta_grafica = tarjeta_grafica

    def __str__(self):
        return (f"Computadora: {self.procesador},"
                f" {self.ram}GB RAM,"
                f" {self.almacenamiento}GB,"
                f" GPU: {self.tarjeta_grafica}")

# Creando una computadora sin builder
computadora_gamer = Computadora("Intel i9", 32, 1000,
                                "RTX 4090")

print(computadora_gamer)
