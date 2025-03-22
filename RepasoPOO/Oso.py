class Oso:
    tipo_oso = " "

    def comer(self):
        print("Esta comiendo...")

    def inviernar(self):
        print("Esta inviernando...")

oso1 = Oso()
oso1.tipo_oso = "Oso Mexicano"
print(oso1.tipo_oso)
print(oso1.comer())
print(oso1.inviernar())



#Cadena formateada
# msg = f"Esto es un mensaje para {nombre}"