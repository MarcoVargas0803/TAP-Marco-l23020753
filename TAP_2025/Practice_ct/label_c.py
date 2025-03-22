import tkinter as tk

class FloatingLabelApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x300")

        self.button = tk.Button(root, text="Haz clic aquí", command=self.show_floating_label)
        self.button.pack(pady=50)

    def show_floating_label(self):
        # Crear una ventana emergente
        popup = tk.Toplevel(self.root)
        popup.overrideredirect(True)  # Quitar bordes de la ventana
        popup.geometry("120x40+500+300")  # Ajustar posición y tamaño

        label = tk.Label(popup, text="Mensaje flotante", bg="yellow", font=("Arial", 12))
        label.pack()

        # Cerrar después de 2 segundos
        self.root.after(2000, popup.destroy)

root = tk.Tk()
app = FloatingLabelApp(root)
root.mainloop()





"""
import customtkinter as ct

class App(ct.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("400x300")
        self.title("Ejemplo de Texto Bajo Entry")

        # Crear un Entry
        self.entry = ct.CTkEntry(self, placeholder_text="Escribe aquí")
        self.entry.pack(pady=20)

        # Crear un Label (Inicialmente vacío)
        self.label_info = ct.CTkLabel(self, text="", text_color="gray")
        self.label_info.pack()

        # Vincular eventos
        self.entry.bind("<FocusIn>", self.mostrar_texto)
        self.entry.bind("<FocusOut>", self.ocultar_texto)

    def mostrar_texto(self, event):
        self.label_info.configure(text="Escribe tu información aquí.")

    def ocultar_texto(self, event):

        self.label_info.configure(text="")


if __name__ == "__main__":
    app = App()
    app.mainloop()
"""