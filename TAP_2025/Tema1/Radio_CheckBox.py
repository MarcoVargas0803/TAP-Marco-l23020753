import customtkinter as ct

# Configuración de apariencia
ct.set_appearance_mode("System")
ct.set_default_color_theme("blue")

# Creación de la ventana principal
app = ct.CTk()
app.title("Formulario")

# Tamaño y configuración de la ventana
app.geometry("900x450")
app.resizable(False, False)

# Configuración de columnas y filas
app.grid_columnconfigure(0, weight=1)
for i in range(5):
    app.grid_rowconfigure(i, weight=1)

# Creación de Frames
f1 = ct.CTkFrame(app, fg_color="black")
f2 = ct.CTkFrame(app, fg_color="black")
f3 = ct.CTkFrame(app, fg_color="black")
f4 = ct.CTkFrame(app, fg_color="black")
f5 = ct.CTkFrame(app, fg_color="black")

# Posicionamiento de los Frames
f1.grid(row=0, column=0, sticky="nsew", pady=5, padx=5)
f2.grid(row=1, column=0, sticky="nsew", pady=5, padx=5)
f3.grid(row=2, column=0, sticky="nsew", pady=5, padx=5)
f4.grid(row=3, column=0, sticky="nsew", pady=5, padx=5)
f5.grid(row=4, column=0, sticky="nsew", pady=5, padx=5)

# Labels
P1 = ct.CTkLabel(f1, text="Soy una pregunta", text_color="Red", anchor="w")
P2 = ct.CTkLabel(f2, text="Soy una pregunta 2", text_color="Red", anchor="w")
P3 = ct.CTkLabel(f3, text="Soy una pregunta 3", text_color="Red", anchor="w")
P4 = ct.CTkLabel(f4, text="Soy una pregunta 4", text_color="Red", anchor="w")
P5 = ct.CTkLabel(f5, text="Soy una pregunta 5", text_color="Red", anchor="w")

# Posicionamiento de Labels
P1.pack(side="left", padx=10, pady=10)
P2.pack(side="left", padx=10, pady=10)
P3.pack(side="left", padx=10, pady=10)
P4.pack(side="left", padx=10, pady=10)
P5.pack(side="left", padx=10, pady=10)

# Variables para los CheckBox y RadioButtons
check_var1 = ct.StringVar(value="off")
check_var2 = ct.StringVar(value="off")
check_var3 = ct.StringVar(value="off")
check_var4 = ct.StringVar(value="off")
check_var5 = ct.StringVar(value="off")
radio_var = ct.StringVar(value="")

# Función para los CheckBox
def checkbox_event():
    print("Checkbox toggled!")

# CheckBox y RadioButton en cada fila
checkbox1_1 = ct.CTkCheckBox(f1, text="Opción 1", variable=check_var1, command=checkbox_event)
checkbox1_2 = ct.CTkCheckBox(f1, text="Opción 2", variable=check_var1, command=checkbox_event)
radio1 = ct.CTkRadioButton(f1, text="Elegir", variable=radio_var, value="p1")

checkbox2_1 = ct.CTkCheckBox(f2, text="Opción 1", variable=check_var2, command=checkbox_event)
checkbox2_2 = ct.CTkCheckBox(f2, text="Opción 2", variable=check_var2, command=checkbox_event)
radio2 = ct.CTkRadioButton(f2, text="Elegir", variable=radio_var, value="p2")

checkbox3_1 = ct.CTkCheckBox(f3, text="Opción 1", variable=check_var3, command=checkbox_event)
checkbox3_2 = ct.CTkCheckBox(f3, text="Opción 2", variable=check_var3, command=checkbox_event)
radio3 = ct.CTkRadioButton(f3, text="Elegir", variable=radio_var, value="p3")

checkbox4_1 = ct.CTkCheckBox(f4, text="Opción 1", variable=check_var4, command=checkbox_event)
checkbox4_2 = ct.CTkCheckBox(f4, text="Opción 2", variable=check_var4, command=checkbox_event)
radio4 = ct.CTkRadioButton(f4, text="Elegir", variable=radio_var, value="p4")

checkbox5_1 = ct.CTkCheckBox(f5, text="Opción 1", variable=check_var5, command=checkbox_event)
checkbox5_2 = ct.CTkCheckBox(f5, text="Opción 2", variable=check_var5, command=checkbox_event)
radio5 = ct.CTkRadioButton(f5, text="Elegir", variable=radio_var, value="p5")

# Posicionamiento de CheckBox y RadioButtons
checkbox1_1.pack(side="right", padx=5)
checkbox1_2.pack(side="right", padx=5)
radio1.pack(side="right", padx=5)

checkbox2_1.pack(side="right", padx=5)
checkbox2_2.pack(side="right", padx=5)
radio2.pack(side="right", padx=5)

checkbox3_1.pack(side="right", padx=5)
checkbox3_2.pack(side="right", padx=5)
radio3.pack(side="right", padx=5)

checkbox4_1.pack(side="right", padx=5)
checkbox4_2.pack(side="right", padx=5)
radio4.pack(side="right", padx=5)

checkbox5_1.pack(side="right", padx=5)
checkbox5_2.pack(side="right", padx=5)
radio5.pack(side="right", padx=5)

# Ejecución de la ventana
app.mainloop()
