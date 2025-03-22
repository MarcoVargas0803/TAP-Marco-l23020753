#Poniendo en practica la cadena formateada

class Led:
    color = ""
    intesidad = 0
    status = "off"

    def encender(self):
        self.status = "on"
        return
    def mostrar_estado(self):
        print(f"estado:{self.color},{self.intesidad},{self.status}")

    # Para poder imprimir el objeto con un metodo definido.
    # todos los que incian con __ , son metodos ya definidos dentro del objeto.
    # el metodo __str__ equivale al metodo ToString de Java

    def __str__(self):
        return f"color:{self.color},{self.intesidad},{self.intesidad}"

led1 = Led()

led1.color = "rojo"
led1.intesidad = 0.5
led1.encender()
print(led1)
#No esta imprimiendo el __str__



