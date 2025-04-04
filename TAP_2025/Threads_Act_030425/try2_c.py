import customtkinter as ctk
import tkinter as tk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Movimiento en Canvas")
        self.geometry("600x400")

        # Crear un marco para contener el Canvas
        frame = ctk.CTkFrame(self, width=500, height=300)
        frame.pack(pady=20, padx=20)

        # Crear el Canvas
        self.canvas = tk.Canvas(frame, bg="white", width=480, height=280)
        self.canvas.pack()

        # Dibujar un rectángulo en el Canvas
        self.rect = self.canvas.create_rectangle(50, 50, 100, 100, fill="blue")

        # Botón para iniciar el movimiento
        self.button = ctk.CTkButton(self, text="Mover", command=self.mover_rectangulo)
        self.button.pack(pady=10)

    def mover_rectangulo(self):
        """ Mueve el rectángulo del punto A al punto B con animación """
        self.mover_objeto(self.rect, 5, 2)  # Desplazamiento en X e Y

    def mover_objeto(self, objeto_id, dx, dy):
        """ Mueve un objeto paso a paso hasta alcanzar el destino """
        x1, y1, x2, y2 = self.canvas.coords(objeto_id)  # Obtener coordenadas actuales

        if x2 < 300:  # Verificar si aún no llega al punto B
            self.canvas.move(objeto_id, dx, dy)  # Mover el objeto
            self.after(50, self.mover_objeto, objeto_id, dx, dy)  # Repetir el movimiento


if __name__ == "__main__":
    app = App()
    app.mainloop()
