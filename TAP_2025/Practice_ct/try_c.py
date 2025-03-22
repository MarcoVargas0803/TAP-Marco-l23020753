import customtkinter as ct
from PIL import Image
from Excercise_250225_register import Registro
from MainApp import MainApp
import time

class LoginApp(ct.CTk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.geometry("400x500")
        self.resizable(False, False)
        self.title("Login Page")

        # Variables para intentos de login
        self.intentos_fallidos = 0
        self.bloqueado_hasta = 0

        # Cargar usuarios desde el archivo JSON
        self.usuarios = Registro.users

        self.configure_grid()
        self.create_widgets()

    def configure_grid(self):
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        self.grid_columnconfigure(0, weight=1)

    def create_widgets(self):
        # Entrada de usuario
        self.entry_user = ct.CTkEntry(self, text_color="white", placeholder_text="User Name")
        self.entry_user.grid(row=1, column=0, sticky="ew", padx=10)
        self.entry_user.bind("<KeyRelease>", self.validar_usuario)

        # Entrada de contraseña
        self.entry_password = ct.CTkEntry(self, text_color="white", placeholder_text="Password", show="*")
        self.entry_password.grid(row=2, column=0, sticky="ew", padx=10)

        # Botón para mostrar/ocultar contraseña
        self.toggle_password_btn = ct.CTkButton(self, text="👁", width=30, command=self.toggle_password)
        self.toggle_password_btn.grid(row=2, column=1, padx=5)

        # Botón de login
        self.button_login = ct.CTkButton(self, text="Login", command=self.submit_login)
        self.button_login.grid(row=3, column=0, pady=10)

        self.error_label = ct.CTkLabel(self, text="", text_color="red")
        self.error_label.grid(row=4, column=0, pady=5)

    def toggle_password(self):
        """Alternar la visibilidad de la contraseña."""
        if self.entry_password.cget("show") == "*":
            self.entry_password.configure(show="")
        else:
            self.entry_password.configure(show="*")

    def validar_usuario(self, event):
        """Verificar en tiempo real si el usuario existe."""
        user = self.entry_user.get()
        if any(u["usuario"] == user for u in Registro.users):
            self.error_label.configure(text="Usuario encontrado", text_color="green")
        else:
            self.error_label.configure(text="Usuario no existe", text_color="red")

    def submit_login(self):
        """Verifica usuario y contraseña, con intentos limitados."""
        user = self.entry_user.get()
        password = self.entry_password.get()

        # Verificar bloqueo
        if time.time() < self.bloqueado_hasta:
            self.error_label.configure(text="Cuenta bloqueada. Intenta más tarde.", text_color="red")
            return

        for u in Registro.users:
            if u["usuario"] == user and u["password"] == password:
                self.error_label.configure(text="Login exitoso", text_color="green")
                self.destroy()
                MainApp().mainloop()
                return

        # Si el login falla
        self.intentos_fallidos += 1
        self.error_label.configure(text=f"Intento fallido {self.intentos_fallidos}/3", text_color="red")

        # Bloquear si fallan 3 veces
        if self.intentos_fallidos >= 3:
            self.bloqueado_hasta = time.time() + 10  # Bloqueo por 10 segundos
            self.error_label.configure(text="Cuenta bloqueada por 10 segundos.", text_color="red")
            self.intentos_fallidos = 0  # Reiniciar intentos


if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()
