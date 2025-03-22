#Herencia en Python
class ClaseBase:
    data = "123"

class ClaseDerivada(ClaseBase):
    pass
obj = ClaseDerivada()
print(obj.data)

class Fruta:
    def __init__(self,color):
        self.color = color

    def show(self):
        return f"soy una fruta de color {self.color}"

class Verdura:
    def __init__(self,color):
        self.color = color
    def show(self):
        return f"soy una verdura de color {self.color}"

#LLamando a constructor padre
class Manzana(Fruta):
    def __init__(self,color):
        self.familia = " Americana "

        Fruta.__init__(self,color)
        #Solo si es una unica herencia, se puede llamar como super()
        #Super().__init__(self,color)

#Herencia Multiple
#Pasamos Fruta y Verdura
class Aguacate(Fruta,Verdura):
    def __init__(self,color):

        #LLamando a los dos constructores y pasandoles los mismos datos
        Fruta.__init__(self,color)
        Verdura.__init__(self,color)
        self.familia = "Hass"

        #Llamando a los metodos de las clases.
        def show(self):
            return Fruta.show(self) + "o bien" + Verdura.show(self)

