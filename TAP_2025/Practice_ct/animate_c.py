import customtkinter as ct

class LoginApp(ct.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("400x300")
        self.title("Inicio de Sesión")

        # Campo de usuario
        self.user_entry = ct.CTkEntry(self, placeholder_text="Usuario")
        self.user_entry.pack(pady=10)

        # Campo de contraseña
        self.pass_entry = ct.CTkEntry(self, placeholder_text="Contraseña", show="*")
        self.pass_entry.pack(pady=10)

        # Botón de inicio de sesión
        self.login_button = ct.CTkButton(self, text="Iniciar Sesión", command=self.start_loading)
        self.login_button.pack(pady=20)

        # Barra de progreso (oculta al inicio)
        self.progress = ct.CTkProgressBar(self)
        self.progress.pack(pady=10, fill="x")
        self.progress.set(0)  # Iniciar en 0

    def start_loading(self):
        """Inicia la simulación de carga al iniciar sesión"""
        self.login_button.configure(state="disabled")  # Deshabilitar botón
        self.progress.set(0)  # Reiniciar barra de progreso
        self.update_progress(0)  # Iniciar progreso

    def update_progress(self, value):
        """Simula el progreso y carga la nueva ventana"""
        if value < 1:
            value += 0.1  # Incremento del progreso
            self.progress.set(value)
            self.after(300, self.update_progress, value)  # Esperar 300ms y actualizar
        else:
            self.open_main_window()  # Abrir nueva ventana al llegar a 100%

    def open_main_window(self):
        """Abre la nueva ventana después de la carga"""
        self.destroy()  # Cierra la ventana de login
        MainApp()  # Abre la ventana principal

class MainApp(ct.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("400x200")
        self.title("Ventana Principal")

        label = ct.CTkLabel(self, text="Bienvenido a la Aplicación!")
        label.pack(pady=50)

        self.mainloop()

if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()
