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
#Para agregar color usamos fg_color, puede ser en nombre o hexadecimal
#boton = ct.CTkButton(app,text="Soy un boton",fg_color="red")

#Podemos intercambiar del color cuando este entre un modo claro o oscuro, pasando una tupla a fg_color
#boton = ct.CTkButton(app,text="Soy un boton",fg_color=("red","blue"))

#Corner_radius => realiza un redondeo al boton
#Hover_color => el color al pasar con el mouse
#Sticky es un atributo para estirar un boton, se acopla de acuerdo a la dirrección que le mandamos
boton = ct.CTkButton(app,text="Soy un boton",fg_color=("red","blue"),corner_radius=10,hover_color="orange")
boton1 = ct.CTkButton(app,text="Soy un boton 2",fg_color=("red","blue"),corner_radius=10,hover_color="orange")
boton2 = ct.CTkButton(app,text="Soy un boton 3",fg_color=("red","blue"),corner_radius=10,hover_color="orange")




#Despliega el botón en pantalla
boton.pack()


#Otra forma de desplegar el botón
#Grid ve a la ventana como una matriz, teniendo que agregar la posición row y column.
#padX y padY agrega un margen entre los elementos , se pasa el parametro en pixeles
#con command podemos agregar una funcionalidad
#el command , y asi como otros se les llama función callBack.
#callBack : Funciones que responden a un evento.

boton.grid(row=0,column=0,padx=20,pady=20,command=funcion())
boton1.grid(row=0,column=1,padx=20,pady=20,command=funcion())
boton2.grid(row=0,column=2,padx=20,pady=20,command=funcion())


#Agregar color al boton
#Puede ser tanto como nombre del color o hexadecimal


#Agregar el modo "dark" / "light" de la ventana
ct.set_appearance_mode("dark")

#Funcionalidades de GRID
#el index se refiere a la columna en donde se ubica y el peso al nivel de espacio que tendra un boton de otro

app.grid_columnconfigure(0,weight=1)
app.grid_columnconfigure(1,weight=1)
app.grid_columnconfigure(2,weight=1)



#Corriendo ventana
app.mainloop()


