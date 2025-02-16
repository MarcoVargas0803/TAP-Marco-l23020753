import customtkinter as ct

# Configuración de apariencia
ct.set_appearance_mode("System")
ct.set_default_color_theme("blue")

# Creación de la ventana principal
app = ct.CTk()
app.title("Registro")

# Tamaño y configuración de la ventana
app.geometry("900x450")
app.resizable(False, False)

# Configuración de columnas y filas
app.grid_columnconfigure(0, weight=1)
for i in range(5):
    app.grid_rowconfigure(i, weight=1)

# Creación de Frames
titulo = ct.CTkFrame(app, fg_color="black")
f1 = ct.CTkFrame(app, fg_color="black", height=100, width=200)
f2 = ct.CTkFrame(app, fg_color="black")
f3 = ct.CTkFrame(app, fg_color="black")
f4 = ct.CTkFrame(app, fg_color="black")
f5 = ct.CTkFrame(app, fg_color="black")

# Posicionamiento de los Frames
titulo.grid(row=0, column=0, sticky="nsew", pady=5, padx=5)
f1.grid(row=1, column=0, sticky="nsew", pady=5, padx=5)
f2.grid(row=2, column=0, sticky="nsew", pady=5, padx=5)
f3.grid(row=3, column=0, sticky="nsew", pady=5, padx=5)
f4.grid(row=4, column=0, sticky="nsew", pady=5, padx=5)
f5.grid(row=5, column=0, sticky="nsew", pady=5, padx=5)

# Labels
P_titulo = ct.CTkLabel(titulo, text="R E G I S T R O ", text_color="Red", anchor="w")
P1 = ct.CTkLabel(f1, text="Nombre: ", text_color="Red", anchor="w")
P2 = ct.CTkLabel(f2, text="Apellido", text_color="Red", anchor="w")
P3 = ct.CTkLabel(f3, text="Género: ", text_color="Red", anchor="w")
P4 = ct.CTkLabel(f4, text="Perteneces a: ", text_color="Red", anchor="w")

# Posicionamiento de Labels
P_titulo.pack(padx=10, pady=10)
P1.pack(side="left", padx=10, pady=10)
P2.pack(side="left", padx=10, pady=10)
P3.pack(side="left", padx=10, pady=10)
P4.pack(side="left", padx=10, pady=10)

# Variables para los CheckBox y RadioButtons
check_var1 = ct.BooleanVar()
check_var2 = ct.BooleanVar()
check_var3 = ct.BooleanVar()
radio_var = ct.StringVar(value="")

# Entradas de texto
entrada_nombre = ct.CTkEntry(f1)
entrada_nombre.pack(padx=5, pady=5)

entrada_apellido = ct.CTkEntry(f2)
entrada_apellido.pack(padx=5, pady=5)

# RadioButtons
radio3_1 = ct.CTkRadioButton(f3, text="Masculino", variable=radio_var, value="Masculino")
radio3_2 = ct.CTkRadioButton(f3, text="Femenino", variable=radio_var, value="Femenino")

# CheckButtons
checkbox4_1 = ct.CTkCheckBox(f4, text="Deportes", variable=check_var1)
checkbox4_2 = ct.CTkCheckBox(f4, text="Artes", variable=check_var2)
checkbox4_3 = ct.CTkCheckBox(f4, text="Entretenimiento", variable=check_var3)


# Función para capturar los datos e imprimirlos en la terminal
def submit():
    nombre = entrada_nombre.get()
    apellido = entrada_apellido.get()
    genero = radio_var.get()
    pertenece_a = []

    if check_var1.get():
        pertenece_a.append("Deportes")
    if check_var2.get():
        pertenece_a.append("Artes")
    if check_var3.get():
        pertenece_a.append("Entretenimiento")

    print(f"Nombre: {nombre}")
    print(f"Apellido: {apellido}")
    print(f"Género: {genero}")
    print(f"Perteneces a: {', '.join(pertenece_a) if pertenece_a else 'Ninguno'}")


# Botón para enviar los datos
button_send = ct.CTkButton(f5, text="Enviar", text_color="black", corner_radius=20, fg_color="grey", command=submit)

# Posicionamiento de elementos
radio3_1.pack(side="right", padx=5)
radio3_2.pack(side="right", padx=5)

checkbox4_1.pack(side="right", padx=5)
checkbox4_2.pack(side="right", padx=5)
checkbox4_3.pack(side="right", padx=5)

button_send.pack(padx=5, pady=5)

# Ejecución de la ventana
app.mainloop()
