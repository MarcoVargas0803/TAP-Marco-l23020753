#Polimorfismo en Python
class Pato():
    def volar(self):
        print("vuelo como pato")

class Pinguino():
    def volar(self):
        print("vuelo caminando")

lucas = Pato()
pingui = Pinguino()

lista = [lucas, pingui]

#Como tal no hay un polimorfismo claro en Python, pero al momento de
#hacer referencias en un lista y que al momento que tengan el mismo metodo todos los objetos
#ya estariamos aplicando un polimoformismo

for objeto in lista:
    objeto.volar()

