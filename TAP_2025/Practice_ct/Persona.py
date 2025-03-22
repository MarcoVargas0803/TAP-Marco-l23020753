class Persona:
    def __init__(self,user,name,lastname,email,password,photo):
        self.user = user
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password
        self.photo = photo

    def __str__(self):
        return f"Usuario: {self.user},Nombre: {self.name},Apellido: {self.lastname}, Email: {self.email}, Contraseña: {self.password}"

class Lista_Persona:
    def __init__(self):
        self.lista = []

    def add_user(self,persona):
        self.lista.append(persona)


#Test
persona1 = Persona("user1","Marco","Vargas","marcocontacto","1234")
lista1 = Lista_Persona()

lista1.add_user(persona1)

persona1_t = lista1.lista[0]
print(persona1_t)
