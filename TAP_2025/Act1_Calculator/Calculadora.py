import customtkinter as ct

# Configuración de la aplicación
app = ct.CTk()
app.title("Act1_Calculator")
app.geometry("600x250")
app.resizable(False, False)

# Campo de entrada
entry = ct.CTkEntry(app, font=("Arial", 24), justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, pady=10, padx=10, sticky="nsew")

# Contenedor de botones
button_frame = ct.CTkFrame(app)
button_frame.grid(row=1, column=0, columnspan=4, sticky="nsew")

# Definición de los botones
buttons = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
    ("0", 3, 0), ("C", 3, 1), ("=", 3, 2), ("+", 3, 3)
]

# Creación de botones en el grid
for text, row, col in buttons:
    btn = ct.CTkButton(button_frame, text=text, font=("Arial", 20))
    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Ajustar las filas y columnas para que los botones sean responsivos
for i in range(4):
    button_frame.rowconfigure(i, weight=1)
    button_frame.columnconfigure(i, weight=2)

# Ejecutar la aplicación
app.mainloop()
