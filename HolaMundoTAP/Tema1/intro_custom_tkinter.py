import customtkinter as ct
#podemos agregar un alias a customtkinter como "ct" para llamar más a la paqueteria.
#Creamos un objeto con la clase CTK, con el cual lo llamamos desde el paquete customtkinter.

def funcion():
    print("Hola mundo")

app = ct.CTk()
#Titulo
app.title("Mi primera aplicación")

#Tamaño de la ventana
app.geometry("700x480")

#Creando botón
#Primero se pasa el parametro del contenedor en donde estará el contenedor, en este caso "app"
boton = ct.CTkButton(app,text="Soy un boton")

#Despliega el botón en pantalla
boton.pack()

#Otra forma de desplegar el botón
#Grid ve a la ventana como una matriz, teniendo que agregar la posición row y column.
#padX y padY agrega un margen entre los elementos , se pasa el parametro en pixeles
#con command podemos agregar una funcionalidad
#el command , y asi como otros se les llama función callBack.
#callBack : Funciones que responden a un evento.

boton.grid(row=0,column=0,padx=20,pady=20,command=funcion())

#Corriendo ventana
app.mainloop()


