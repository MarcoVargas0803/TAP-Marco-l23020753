import customtkinter as ct
import time


class App(ct.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("400x300")
        self.title("Login con Pantalla de Carga")

        # Crear un Entry para usuario
        self.entry_user = ct.CTkEntry(self, placeholder_text="Usuario")
        self.entry_user.pack(pady=10)

        # Crear un Entry para contraseña
        self.entry_pass = ct.CTkEntry(self, placeholder_text="Contraseña", show="*")
        self.entry_pass.pack(pady=10)

        # Botón de inicio de sesión
        self.btn_login = ct.CTkButton(self, text="Iniciar Sesión", command=self.login)
        self.btn_login.pack(pady=10)

        # Etiqueta de mensaje
        self.label_info = ct.CTkLabel(self, text="")
        self.label_info.pack()

        # Vincular evento de teclado (Enter)
        self.bind("<Return>", self.login)

    def login(self, event=None):
        """Función de inicio de sesión."""
        usuario = self.entry_user.get()
        contraseña = self.entry_pass.get()

        if usuario == "admin" and contraseña == "1234":
            self.label_info.configure(text="¡Inicio de sesión exitoso!", text_color="green")
            self.after(500, self.show_loading_screen)  # Mostrar pantalla de carga después de 0.5s
        else:
            self.label_info.configure(text="Usuario o contraseña incorrectos", text_color="red")

    def show_loading_screen(self):
        """Muestra una pantalla de carga antes de abrir la ventana principal."""
        self.withdraw()  # Oculta la ventana de login

        loading_window = ct.CTkToplevel(self)
        loading_window.geometry("300x200")
        loading_window.title("Cargando...")

        label_loading = ct.CTkLabel(loading_window, text="Cargando, por favor espere...")
        label_loading.pack(pady=50)

        self.after(2000, lambda: self.show_main_window(loading_window))  # Simula 2s de carga

    def show_main_window(self, loading_window):
        """Cierra la pantalla de carga y abre la ventana principal."""
        loading_window.destroy()  # Cierra la pantalla de carga
        main_window = ct.CTkToplevel(self)
        main_window.geometry("500x400")
        main_window.title("Panel Principal")

        label_welcome = ct.CTkLabel(main_window, text="¡Bienvenido al sistema!")
        label_welcome.pack(pady=50)

        btn_logout = ct.CTkButton(main_window, text="Cerrar Sesión", command=lambda: self.logout(main_window))
        btn_logout.pack()

    def logout(self, main_window):
        """Cierra la ventana principal y muestra nuevamente la ventana de login."""
        main_window.destroy()
        self.deiconify()  # Vuelve a mostrar la ventana de login


if __name__ == "__main__":
    app = App()
    app.mainloop()
