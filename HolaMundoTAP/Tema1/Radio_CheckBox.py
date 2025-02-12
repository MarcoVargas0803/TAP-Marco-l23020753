#Radio botton y Checkbox button
import customtkinter as ct
app = ct.CTk()
#Titulo
app.title("Formulario")

#Tamaño de la ventana
app.geometry("700x480")
app.resizable(False,False)

app.grid_columnconfigure(0,weight=1)
app.grid_rowconfigure(0,weight=1)

#Frame
F1 = ct.CTkFrame(app,fg_color="gray")

#Grid Frame
F1.grid(row=0,column=0)

#Ejemplo

#Ejecución
app.mainloop()