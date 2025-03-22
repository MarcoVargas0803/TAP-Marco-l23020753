import customtkinter as ct
from PIL import Image

from register import Registro
from mainApp import MainApp

class LoginApp(ct.CTk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.geometry("400x500")
        self.resizable(False, False)
        self.title("Login Page")

        # Modo de apariencia
        ct.set_appearance_mode("System")
        ct.set_default_color_theme("blue")

        # Cargar usuarios desde el archivo JSON
        self.usuarios = Registro.users

        self.configure_grid()
        self.create_widgets()

    def configure_grid(self):
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        self.grid_columnconfigure(0, weight=1)

    def create_widgets(self):
        # Imagen de logo con manejo de errores
        try:
            self.image_login = ct.CTkImage(
                light_image=Image.open(f"usuario.png"),
                dark_image=Image.open("usuario.png"),
                size=(200, 200)
            )
        except FileNotFoundError:
            print("Imagen 'usuario.png' no encontrada.")
            self.image_login = None

        self.image_label = ct.CTkLabel(self, image=self.image_login, text="") if self.image_login else ct.CTkLabel(self, text="Sin imagen")
        self.image_label.grid(row=0, column=0, padx=5)

        # Entradas de usuario y contraseña
        self.entry_user = ct.CTkEntry(self, text_color="white", placeholder_text="User Name")
        self.entry_user.grid(row=1, column=0, sticky="ew", padx=10)

        self.entry_password = ct.CTkEntry(self, text_color="white", placeholder_text="Password", show="*")
        self.entry_password.grid(row=2, column=0, sticky="ew", padx=10)

        # Botón de login
        self.button_login = ct.CTkButton(self, text="Login", text_color="black", fg_color="gray",
                                         hover_color="green", corner_radius=6, width=100, height=35,
                                         command=self.submit_login)
        self.button_login.grid(row=3, column=0,pady=10,padx=10,sticky="w")

        # Label de registro
        self.register_me = ct.CTkLabel(self, text="¿Sin usuario? Registrate!", text_color="#cacfed",
                                       font=("Helvetica", 15, "underline"))
        self.register_me.grid(row=3, column=0, sticky="es", padx=5, pady=10)

        self.error_label = ct.CTkLabel(self,font=("Helvetica", 20),text=" ")
        self.error_label.grid(row=4, column=0, sticky="nsew", padx=5, pady=5)

        # Eventos bind
        self.entry_user.bind("<FocusIn>", self.on_focus_in_user)
        self.entry_password.bind("<FocusIn>", self.on_focus_in_password)
        self.entry_user.bind("<FocusOut>", self.on_focus_out_user)
        self.entry_password.bind("<FocusOut>", self.on_focus_out_password)

    def on_log_error_entry(self,message,text_color,fg_color):
        self.error_label.configure(text=message,text_color=text_color,fg_color=fg_color,corner_radius=10)

        # Eventos para cambiar el color del label
        self.register_me.bind("<Enter>", self.on_enter_register)
        self.register_me.bind("<Leave>", self.on_leave_register)
        self.register_me.bind("<Button-1>", self.on_button_register)

        #Event Test

    def on_show_in_password(self):
        self.entry_password.configure(show="")

    def on_show_out_password(self):
        self.entry_password.configure(show="*")

    def on_focus_in_user(self, event):
        self.entry_user.configure(text_color="white")
        self.error_label.configure(text="",fg_color="transparent")

    def on_focus_out_user(self, event):
        self.entry_user.configure(text_color="gray")

    def on_focus_in_password(self, event):
        self.entry_password.configure(text_color="white")
        self.error_label.configure(text="",fg_color="transparent")

    def on_focus_out_password(self, event):
        self.entry_password.configure(text_color="gray")
        self.error_label.configure(text="",fg_color="transparent")

    def on_button_register(self, event):
        self.registro_win = Registro()
        self.registro_win.mainloop()

    def on_enter_register(self, event):
        self.register_me.configure(text_color="#2641de")

    def on_leave_register(self, event):
        self.register_me.configure(text_color="#cacfed")

    def submit_login(self):
        user = self.entry_user.get()
        password = self.entry_password.get()

        # Verificar si hay usuarios registrados
        if not Registro.users:
            self.on_log_error_entry("No hay usuarios registrados", "white", "#f04735")
            return

        # Buscar el usuario en la lista
        for u in Registro.users:
            if u["usuario"] == user and u["password"] == password:
                self.open_main_window()
                return
        self.on_log_error_entry("Usuario y/o contraseña incorrectos", "white", "#f04735",)

    def open_main_window(self):
        self.destroy()  # Cierra la ventana actual
        main = MainApp()  # Crea la nueva ventana
        main.mainloop()  # Ejecuta la ventana principal


app = LoginApp()
app.mainloop()


