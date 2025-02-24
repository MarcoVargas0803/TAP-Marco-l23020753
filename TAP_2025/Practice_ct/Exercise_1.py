#Exercise 1: Involving in CustomTkinter

"""
Primer desarrollo:
Crear una pagina de login con un logo en el centro, labels de entrada y contraseña , y un botton de login.

Segundo desarrollo:
Al dar el boton de login, nos abrirá una pantalla con los datos del usuario, y asi como un menu basico
para enviar correo por smtplib.

Tercer desarrollo:
Aplicar de los principios de SOLID
"""

import customtkinter as ct
from PIL import Image


app = ct.CTk()

#Appareance Mode
ct.set_appearance_mode("System")
ct.set_default_color_theme("blue")

#Window config

app.geometry("400x500")
app.resizable(False,False)

#row, column config

app.grid_rowconfigure(0,weight=1)
app.grid_rowconfigure(1,weight=1)
app.grid_rowconfigure(2,weight=1)
app.grid_rowconfigure(3,weight=1)

app.grid_columnconfigure(0,weight=1)

#Image

image_login = ct.CTkImage(light_image=Image.open("login_logo_dark_mode.png"),
                          dark_image=Image.open("login_logo_dark_mode.png"),
                          size=(200,200))

image_label = ct.CTkLabel(app,image=image_login,text="")
image_label.grid(row=0,column=0,padx=5)

def image_message(e):
    print("Estas viendo la imagen")

#Entry

entry_user = ct.CTkEntry(app,text_color="white",placeholder_text="user name")
entry_user.grid(row=1,column=0,sticky="ew",padx=10)

entry_password = ct.CTkEntry(app,text_color="white",placeholder_text="password")
entry_password.grid(row=2,column=0,sticky="ew",padx=10)

#Button


def submit_login():
    user = entry_user.get()
    password = entry_password.get()


    print("user: ",user)
    print("password:",password)


button_login1 = ct.CTkButton(app,text_color="black",fg_color="gray",hover_color="green",corner_radius=6,width=175,height=50,command=submit_login).grid(row=3,column=0)

image_label.bind("<Double-Button-1>",image_message)
app.mainloop()
