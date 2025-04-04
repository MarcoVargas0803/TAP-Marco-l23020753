import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk

# Configuración de la ventana principal
root = ctk.CTk()
root.geometry("500x400")
root.title("Animación con ProgressBar")

# Crear un marco para contener el Canvas
frame = ctk.CTkFrame(root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Crear un Canvas dentro del frame
canvas = tk.Canvas(frame, width=400, height=200, bg="white")
canvas.pack()

# Cargar la imagen
img = Image.open("imagen1.png")  # Reemplaza con tu imagen
img = img.resize((50, 50))  # Ajustar tamaño si es necesario
img = ImageTk.PhotoImage(img)

# Agregar la imagen al canvas en el punto A
image_id = canvas.create_image(50, 100, anchor=tk.CENTER, image=img)

# Crear ProgressBar
progress_bar = ctk.CTkProgressBar(root, width=400)
progress_bar.pack(pady=20)
progress_bar.set(0)  # Inicializar en 0

def move_image(x_pos=50, progress=0):
    """ Mueve la imagen en el Canvas y actualiza la barra de progreso """
    if x_pos < 350:  # Punto B (final de la animación)
        x_pos += 5   # Incremento en la posición
        progress += 0.02  # Incremento del progreso

        # Mover la imagen en el Canvas
        canvas.coords(image_id, x_pos, 100)

        # Actualizar la ProgressBar
        progress_bar.set(progress)

        # Llamar a la función de nuevo después de 50ms
        root.after(50, move_image, x_pos, progress)

# Botón para iniciar la animación
start_button = ctk.CTkButton(root, text="Iniciar Animación", command=lambda: move_image())
start_button.pack(pady=10)

root.mainloop()
