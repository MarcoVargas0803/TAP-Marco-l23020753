import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk


def seleccionar_imagen():
    # Abrir el cuadro de diálogo para seleccionar un archivo
    ruta_imagen = filedialog.askopenfilename(filetypes=[("Archivos de imagen", "*.jpg;*.jpeg;*.png;*.gif")])

    # Verificar si se seleccionó un archivo
    if ruta_imagen:
        label_ruta.configure(text=f"Ruta seleccionada: {ruta_imagen}")


# Configuración de la ventana principal
ventana = ctk.CTk()

# Título de la ventana
ventana.title("Seleccionar imagen")

# Crear un botón para abrir el cuadro de diálogo
boton_seleccionar = ctk.CTkButton(ventana, text="Seleccionar imagen", command=seleccionar_imagen)
boton_seleccionar.pack(pady=20)

# Crear una etiqueta para mostrar la ruta de la imagen seleccionada
label_ruta = ctk.CTkLabel(ventana, text="Ruta seleccionada: Ninguna")
label_ruta.pack(pady=10)

# Iniciar el bucle principal
ventana.mainloop()
