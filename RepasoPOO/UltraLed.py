class UltraLed:
    #Creamos el constructor usando __init__
    def __init__(self,color,intensidad,status="off",tamaño="mediano"):
        self.color = color
        self.intesidad = intensidad
        self.status = status
        self.tamaño = tamaño

    def __str__(self):
        return f"color:{self.color},intesidad:{self.intesidad},estatus:{self.status}, tamaño: {self.tamaño}"

u1 = UltraLed("verde",1,"on","chico")
print(u1)

u2 = UltraLed("rojo",0.5,"on")
print(u2)

u3 = UltraLed("Azul",0.8)
print(u3)

#Si lo hacemos asi, se pondrá de acuerdo al orden
u4 = UltraLed("rojo",1,"Jumbo")
print(u4)

u5 = UltraLed(status="on",color="amarillo",tamaño="pequeño",intensidad=0.5)
print(u5)

#Función eval(expresión)
#Si expresión = "print("juan")"
#==> eval(exp)