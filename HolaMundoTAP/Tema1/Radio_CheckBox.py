#Radio botton y Checkbox button
import customtkinter as ct

ct.set_appearance_mode("System")
ct.set_default_color_theme("blue")
app = ct.CTk()
#Titulo
app.title("Formulario")

#Tamaño de la ventana
app.geometry("400x250")
app.resizable(False,False)
app.minsize(900,450)
app.grid_columnconfigure(0,weight=1)
app.grid_rowconfigure(0,weight=1)



#Frame
f1 = ct.CTkFrame(app,fg_color="gray",height=300)
f2 = ct.CTkFrame(app,fg_color="gray")
f3 = ct.CTkFrame(app,fg_color="gray")
f4 = ct.CTkFrame(app,fg_color="gray")
f5 = ct.CTkFrame(app,fg_color="gray")



#Grid Frame
f1.grid(row=0,column=0,sticky="nsew",pady=5,padx=5)
f2.grid(row=1,column=0,sticky="nsew",pady=5,padx=5)
f3.grid(row=2,column=0,sticky="nsew",pady=5,padx=5)
f4.grid(row=3,column=0,sticky="nsew",pady=5,padx=5)
f5.grid(row=4,column=0,sticky="nsew",pady=5,padx=5)

#Column & row configure

app.rowconfigure(0,weight=2)
app.rowconfigure(1,weight=1)
app.rowconfigure(2,weight=1)
app.rowconfigure(3,weight=1)
app.rowconfigure(4,weight=1)


#Labels
P1 = ct.CTkLabel(f1,text="Soy una pregunta",fg_color="Red")
P2 = ct.CTkLabel(f2,text="Soy una pregunta 2",fg_color="Red")
P3 = ct.CTkLabel(f3,text="Soy una pregunta 3",fg_color="Red")
P4 = ct.CTkLabel(f4,text="Soy una pregunta 4",fg_color="Red")
P5 = ct.CTkLabel(f5,text="Soy una pregunta 5",fg_color="Red")

#Labels Grid
P1.grid(row=0,column=0,padx=5,pady=5,sticky="w")









#Ejemplo

#Ejecución
app.mainloop()