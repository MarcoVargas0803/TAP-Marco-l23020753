import customtkinter as ct

# Configurar la aplicación
app = ct.CTk()
app.title("Calculadora")
app.geometry("350x500")
app.resizable(False, False)

# Variable para almacenar la expresión
expresion = ""


def agregar(valor):
    global expresion
    expresion += str(valor)
    entrada_var.set(expresion)


def limpiar():
    global expresion
    expresion = ""
    entrada_var.set("")


def calcular():
    global expresion
    try:
        resultado = eval(expresion)
        entrada_var.set(resultado)
        expresion = str(resultado)
    except:
        entrada_var.set("Error")
        expresion = ""


# Estilo de la interfaz
ct.set_appearance_mode("light")  # Tema claro
ct.set_default_color_theme("blue")

# Marco principal
frame = ct.CTkFrame(app)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Pantalla de entrada
entrada_var = ct.StringVar()
entrada = ct.CTkEntry(frame, textvariable=entrada_var, font=("Arial", 24), justify="right", height=50)
entrada.pack(pady=10, fill="both")

# Botones
botones = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for (texto, fila, columna) in botones:
    if texto == "C":
        bt = ct.CTkButton(frame, text=texto, command=limpiar, fg_color="red")
    elif texto == "=":
        bt = ct.CTkButton(frame, text=texto, command=calcular, fg_color="green")
    else:
        bt = ct.CTkButton(frame, text=texto, command=lambda t=texto: agregar(t))

    bt.grid(row=fila, column=columna, padx=5, pady=5, sticky="nsew")

# Ajustar columnas y filas
for i in range(5):
    frame.rowconfigure(i, weight=1)
    frame.columnconfigure(i, weight=1)

app.mainloop()




