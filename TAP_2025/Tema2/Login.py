#Diseñar una clase Login, donde podamos instanciar las ventanas de login que queramos y podamos
#Pasar: Foto , fondo , textos:
#from PIL import Image
import customtkinter as ct

class Login:
    text_entry_name = " "
    text_entry_password = " "
    text_entry_button_login = " "
    text_entry_button_cancel = " "

    def __init__(self,text_entry_name,text_entry_password,text_entry_button_login,text_entry_button_cancel):
        self.text_entry_name = text_entry_name
        self.text_entry_password = text_entry_password
        self.text_entry_button_login = text_entry_button_login
        self.text_entry_button_cancel = text_entry_button_cancel

    def init_window(self):
        import customtkinter as ct
        app.ct.Ctk()
        app.title("Login")

        # Tamaño y configuración de la ventana
        app.geometry("900x450")
        app.resizable(False, False)

        # Configuración de apariencia
        ct.set_appearance_mode("System")
        ct.set_default_color_theme("blue")

        # Configuración de columnas y filas
        app.grid_columnconfigure(0, weight=1)
        for i in range(5):
            app.grid_rowconfigure(i, weight=1)
    def Frame_creation(self):
        # Creación de Frames
        titulo = ct.CTkFrame(app, fg_color="gray", border_width=2)
        f1 = ct.CTkFrame(app, fg_color="gray", height=100, width=200, border_width=2)
        f2 = ct.CTkFrame(app, fg_color="gray", border_width=2)
        f3 = ct.CTkFrame(app, fg_color="gray", border_width=2)
        f4 = ct.CTkFrame(app, fg_color="gray", border_width=2)
        # f5 = ct.CTkFrame(app, fg_color="gray",border_width=2)

        # Posicionamiento de los Frames
        titulo.grid(row=0, column=0, sticky="nsew", pady=5, padx=5)
        f1.grid(row=1, column=0, sticky="nsew", pady=5, padx=5)
        f2.grid(row=2, column=0, sticky="nsew", pady=5, padx=5)
        f3.grid(row=3, column=0, sticky="nsew", pady=5, padx=5)
        f4.grid(row=4, column=0, sticky="nsew", pady=5, padx=5)
    def labels_creation(self):
        P_titulo = ct.CTkLabel(titulo, text="REGISTRO", text_color="Red", anchor="w", font=("Arial", 50))

        # Posicionamiento de Labels
        P_titulo.pack(padx=10, pady=10, side="left")
    def entry_creation(self):
        entrada_nombre = ct.CTkEntry(f1, width=40, placeholder_text="Usuario")
        entrada_nombre.pack(padx=20, pady=5, fill="x", expand=True)

        entrada_apellido = ct.CTkEntry(f2, width=40, placeholder_text="Contraseña")
        entrada_apellido.pack(padx=20, pady=5, fill="x", expand=True)

    def button_creation(self):
        login_botton = ct.CTkButton(f3, text="Login", fg_color="white", text_color="black", hover_color="grey",
                                    command=submit())
        login_botton.pack(padx=5, pady=5, side="left")

        cancel_botton = ct.CTkButton(f3, text="Cancel", fg_color="white", text_color="black", hover_color="grey")
        cancel_botton.pack(padx=5, pady=5, side="left")
    def checkbox_creation(self):
        checkbox4_1 = ct.CTkCheckBox(f4, text="Recordarme", variable=check_var1)
        checkbox4_1.pack(side="left", padx=20)

    def ejecution(self):
        app.mainloop()

# Configuración de apariencia
ct.set_appearance_mode("System")
ct.set_default_color_theme("blue")

# Creación de la ventana principal
app = ct.CTk()
app.title("Login")

# Tamaño y configuración de la ventana
app.geometry("900x450")
app.resizable(False, False)

# Configuración de columnas y filas
app.grid_columnconfigure(0, weight=1)
for i in range(5):
    app.grid_rowconfigure(i, weight=1)

# Creación de Frames
titulo = ct.CTkFrame(app, fg_color="gray",border_width=2)
f1 = ct.CTkFrame(app, fg_color="gray", height=100, width=200,border_width=2)
f2 = ct.CTkFrame(app, fg_color="gray",border_width=2)
f3 = ct.CTkFrame(app, fg_color="gray",border_width=2)
f4 = ct.CTkFrame(app, fg_color="gray",border_width=2)
#f5 = ct.CTkFrame(app, fg_color="gray",border_width=2)

# Posicionamiento de los Frames
titulo.grid(row=0, column=0, sticky="nsew", pady=5, padx=5)
f1.grid(row=1, column=0, sticky="nsew", pady=5, padx=5)
f2.grid(row=2, column=0, sticky="nsew", pady=5, padx=5)
f3.grid(row=3, column=0, sticky="nsew", pady=5, padx=5)
f4.grid(row=4, column=0, sticky="nsew", pady=5, padx=5)
#f5.grid(row=5, column=0, sticky="nsew", pady=5, padx=5)

#Image


#my_image = ct.CTkImage(light_image=Image.open("<path to light mode image>"),
                                  #dark_image=Image.open("<path to dark mode image>"),
                                  #size=(30, 30))

#image_label = ct.CTkLabel(app, image=my_image, text="")  # display image with a CTkLabel


# Labels
P_titulo = ct.CTkLabel(titulo, text="REGISTRO", text_color="Red", anchor="w", font=("Arial",50))
#P1 = ct.CTkLabel(f1, text="Nombre: ", text_color="Red", anchor="w")
#P2 = ct.CTkLabel(f2, text="Apellido", text_color="Red", anchor="w")
#P3 = ct.CTkLabel(f3, text="Género: ", text_color="Red", anchor="w")
#P4 = ct.CTkLabel(f4, text="Perteneces a: ", text_color="Red", anchor="w")

# Posicionamiento de Labels
P_titulo.pack(padx=10, pady=10,side="left")
#P1.pack( padx=10, pady=10)
#P2.pack( padx=10, pady=10)
#P3.pack( padx=10, pady=10)
#4.pack( padx=10, pady=10)

# Variables para los CheckBox y RadioButtons
check_var1 = ct.BooleanVar()
check_var2 = ct.BooleanVar()
check_var3 = ct.BooleanVar()
radio_var = ct.StringVar(value="")

# Entradas de texto
entrada_nombre = ct.CTkEntry(f1,width= 40,placeholder_text="Usuario")
entrada_nombre.pack(padx=20,pady=5,fill="x",expand=True)

entrada_apellido = ct.CTkEntry(f2,width= 40,placeholder_text="Contraseña")
entrada_apellido.pack(padx=20, pady=5,fill="x",expand=True)

#Combobox
#def combobox_callback(choice):
    #print("combobox dropdown clicked:", choice)

#combobox = ct.CTkComboBox(f3, values=["Hombre", "Mujer"], command=combobox_callback)
#combobox.set("Genero")

def submit():
    nombre = entrada_nombre.get()
    apellido = entrada_apellido.get()
    #genero = radio_var.get()
    pertenece_a = []

    if check_var1.get():
        pertenece_a.append("Recordarme")

    print(f"Nombre: {nombre}")
    print(f"Apellido: {apellido}")
    #print(f"Género: {genero}")
    #print(f"Perteneces a: {', '.join(pertenece_a) if pertenece_a else 'Ninguno'}")

#Bottons Login y Cancel

login_botton = ct.CTkButton(f3,text="Login",fg_color="white",text_color="black",hover_color="grey",command=submit())
login_botton.pack(padx=5,pady=5,side="left")

cancel_botton = ct.CTkButton(f3,text="Cancel",fg_color="white",text_color="black",hover_color="grey")
cancel_botton.pack(padx=5,pady=5,side="left")




# RadioButtons
#radio3_1 = ct.CTkRadioButton(f3, text="Masculino", variable=radio_var, value="Masculino")
#radio3_2 = ct.CTkRadioButton(f3, text="Femenino", variable=radio_var, value="Femenino")

# CheckButtons
checkbox4_1 = ct.CTkCheckBox(f4, text="Recordarme", variable=check_var1)
#checkbox4_2 = ct.CTkCheckBox(f4, text="Artes", variable=check_var2)
#checkbox4_3 = ct.CTkCheckBox(f4, text="Entretenimiento", variable=check_var3)


# Función para capturar los datos e imprimirlos en la terminal




# Botón para enviar los datos
#button_send = ct.CTkButton(f5, text="Enviar", text_color="black", corner_radius=20, fg_color="grey", command=submit)

# Posicionamiento de elementos
#radio3_1.pack(side="right", padx=5)
#radio3_2.pack(side="right", padx=5)

#combobox.pack(side="right", padx=20, pady=5,fill="x",expand=True)


checkbox4_1.pack(side="left", padx=20)
#checkbox4_2.pack(side="right", padx=20)
#checkbox4_3.pack(side="right", padx=20)


#button_send.pack(padx=5, pady=5)

# Ejecución de la ventana
app.mainloop()