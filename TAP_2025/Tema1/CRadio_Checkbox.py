# Importación
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

# Configuración de filas y columnas
app.grid_columnconfigure(0, weight=1)
for i in range(5):
    app.grid_rowconfigure(i, weight=1)

# Creación de Frames
frames = [ct.CTkFrame(app, fg_color="gray") for _ in range(5)]

# Posicionamiento de los Frames en la cuadrícula
for i, frame in enumerate(frames):
    frame.grid(row=i, column=0, sticky="nsew", pady=5, padx=5)

# Creación y posicionamiento de Labels dentro de los Frames
labels = [
    ct.CTkLabel(frames[i], text=f"Soy una pregunta {i+1}", text_color="white")
    for i in range(5)
]

for label in labels:
    label.pack(pady=10)  # Usamos pack para centrar en cada frame

# Ejecución de la ventana
app.mainloop()
