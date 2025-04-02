# Clase del Producto (Objeto a construir)
class Computadora:
    def __init__(self):
        self.procesador = None # Inicializa los atributos a None
        self.ram = None
        self.almacenamiento = None
        self.tarjeta_grafica = None

    def __str__(self):
        return (f"Computadora: {self.procesador},"
                f" {self.ram}GB RAM,"
                f" {self.almacenamiento}GB,"
                f" GPU: {self.tarjeta_grafica}")

# Clase Builder (Define los métodos para construir paso a paso)
class ComputadoraBuilder:
    def __init__(self):
        self.computadora = Computadora()

    def set_procesador(self, procesador):
        self.computadora.procesador = procesador
        return self  # Retorna el builder para permitir encadenamiento

    def set_ram(self, ram):
        self.computadora.ram = ram
        return self

    def set_almacenamiento(self, almacenamiento):
        self.computadora.almacenamiento = almacenamiento
        return self

    def set_tarjeta_grafica(self, tarjeta_grafica):
        self.computadora.tarjeta_grafica = tarjeta_grafica
        return self

    def build(self):
        return self.computadora  # Devuelve el objeto construido

builder = ComputadoraBuilder()
computadora_gamer = (builder.set_procesador("Intel i9")
                          .set_ram(32)
                          .set_almacenamiento(1000)
                          .set_tarjeta_grafica("RTX 4090")
                          .build())

print(computadora_gamer)

