"""
#Investigar acerca del Menu y las ventanas Modales en CustomTkinter

"""
#Librerias
import tkinter as tk
import customtkinter as ctk

#Configurar CustomTkinter
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk): #Clase hija de CTk
    def __init__(self):
        super().__init__()

        self.title("Menú en CustomTkinter")
        self.geometry("500x300")

        """
        Syntax 
        w = menu (master,option, ... ) 
        
        """
        # Configurar el menú en la barra superior
        menu_bar = tk.Menu(self)

        # Menú Archivo
        #Crea el primer apartado 
        file_menu = tk.Menu(menu_bar, tearoff=0)
        #Se agrega el .add_command seguido del label y el command como parametros
        file_menu.add_command(label="Abrir", command=self.abrir_archivo)
        file_menu.add_command(label="Guardar", command=self.guardar_archivo)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.quit)

        # Menú Ayuda
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="Acerca de", command=self.mostrar_acerca_de)

        # Agregar menús a la barra
        menu_bar.add_cascade(label="Archivo", menu=file_menu)
        menu_bar.add_cascade(label="Ayuda", menu=help_menu)

        # Establecer la barra de menú
        self.config(menu=menu_bar)

    def abrir_archivo(self):
        print("Abrir archivo")

    def guardar_archivo(self):
        print("Guardar archivo")

    def mostrar_acerca_de(self):
        Modal(self, "Acerca de", "Este es un ejemplo de CustomTkinter.")

# 🔹 **Ventana Modal en CustomTkinter**
class Modal(ctk.CTkToplevel):
    def __init__(self, parent, title, mensaje):
        super().__init__(parent)
        self.title(title)
        self.geometry("300x150")
        self.grab_set()  # Hace que la ventana sea modal (bloquea la principal)

        # Widgets de la ventana modal
        label = ctk.CTkLabel(self, text=mensaje)
        label.pack(pady=20)

        boton_cerrar = ctk.CTkButton(self, text="Cerrar", command=self.destroy)
        boton_cerrar.pack(pady=10)

app = App()
app.mainloop()