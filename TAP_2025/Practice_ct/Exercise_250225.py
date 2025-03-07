import customtkinter as ct
from PIL import Image, ImageTk
from tkinter import filedialog
from Excercise_250225_register import Registro
from MainApp import MainApp

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
        self.entry_user.bind("<KeyRelease>", self.validar_usuario)


        self.entry_password = ct.CTkEntry(self, text_color="white", placeholder_text="Password", show="*",width=350)
        self.entry_password.grid(row=2, column=0, sticky="w", padx=10)

        # Botón para mostrar/ocultar contraseña
        self.toggle_password_btn = ct.CTkButton(self, text="👁", width=30, command=self.toggle_password,fg_color="gray",hover_color="green",text_color="black")
        self.toggle_password_btn.grid(row=2, column=0, padx=5,sticky="e")

        # Botón de login
        self.button_login = ct.CTkButton(self, text="Login", text_color="black", fg_color="gray",
                                         hover_color="#438713", corner_radius=6, width=100, height=35,
                                         command=self.submit_login)
        self.button_login.grid(row=3, column=0,pady=10,padx=10,sticky="w")

        # Label de registro
        self.register_me = ct.CTkLabel(self, text="¿Sin usuario? Registrate!", text_color="#cacfed",
                                       font=("Helvetica", 15, "underline"))
        self.register_me.grid(row=3, column=0, sticky="es", padx=5, pady=10)

        self.error_label = ct.CTkLabel(self,font=("Helvetica", 20),text=" ")
        self.error_label.grid(row=4, column=0, sticky="nsew", padx=10, pady=10)

        # Barra de progreso (oculta al inicio)
        self.progress = ct.CTkProgressBar(self,progress_color="#5ccc58")
        self.progress.grid(row=5, column=0, padx=10, pady=10, sticky="ew")
        self.progress.set(0)  # Iniciar en 0

        # Eventos bind
        self.image_label.bind("<Double-Button-1>",self.update_profile_picture)
        self.entry_user.bind("<FocusIn>", self.on_focus_in_user)
        self.entry_password.bind("<FocusIn>", self.on_focus_in_password)
        self.entry_user.bind("<FocusOut>", self.on_focus_out_user)
        self.entry_password.bind("<FocusOut>", self.on_focus_out_password)

        # Eventos para cambiar el color del label
        self.register_me.bind("<Enter>", self.on_enter_register)
        self.register_me.bind("<Leave>", self.on_leave_register)
        self.register_me.bind("<Button-1>", self.on_button_register)

        self.bind("<Return>", self.submit_login_e)
        self.bind("<Shift_L>", self.on_show_in_password)
        self.bind("<Shift_R>",self.on_show_in_password)

        self.bind("<KeyRelease-Shift_L>",self.on_show_out_password)
        self.bind("<KeyRelease-Shift_R>",self.on_show_out_password)

    def update_profile_picture(self, event):
        # Abrir explorador de archivos
        file_path = filedialog.askopenfilename(filetypes=[("Imágenes", "*.png;*.jpg;*.jpeg;*.gif")])
        if not file_path:
            return  # Si el usuario cancela, no hacer nada

        # Cargar la nueva imagen con PIL
        image = Image.open(file_path).resize((200, 200))  # Ajusta el tamaño según sea necesario
        self.image_login = ct.CTkImage(light_image=image, dark_image=image, size=(200, 200))

        # Actualizar la imagen en el Label
        self.image_label.configure(image=self.image_login)
        self.error_label.configure(text="Imagen Actualizada",text_color="black",fg_color="green")
        self.after(2000,self.hide_label)

    def hide_label(self):
        self.error_label.configure(text="",fg_color="transparent") # Oculta el Label

    def on_log_error_entry(self,message,text_color,fg_color):
        self.error_label.configure(text=message,text_color=text_color,fg_color=fg_color,corner_radius=30)

    def on_show_in_password(self,event):
        self.entry_password.configure(show="")

    def on_show_out_password(self,event):
        self.entry_password.configure(show="*")

    def on_focus_in_user(self, event):
        self.entry_user.configure(text_color="white")
        self.error_label.configure(text="Ingresa usuario",fg_color="gray",font=("Helvetica",20),text_color="black",corner_radius=40)
        self.after(1000,self.hide_label)

    def on_focus_out_user(self, event):
        self.entry_user.configure(text_color="gray")

    def on_focus_in_password(self, event):
        self.entry_password.configure(text_color="white")
        self.error_label.configure(text="",fg_color="transparent")
        self.error_label.configure(text="Ingresa contraseña", fg_color="gray", font=("Helvetica", 20),text_color="black",corner_radius=40)
        self.after(1000, self.hide_label)

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

    def start_loading(self):
        """Inicia la simulación de carga al iniciar sesión"""
        self.button_login.configure(state="disabled")  # Deshabilitar botón
        self.progress.set(0)  # Reiniciar barra de progreso
        self.update_progress(0)  # Iniciar progreso

    def update_progress(self, value):
        """Simula el progreso y carga la nueva ventana"""
        if value < 1:
            value += 0.1  # Incremento del progreso
            self.progress.set(value)  # Actualizar la barra de progreso
            self.after(300, self.update_progress, value)  # Esperar 300ms y actualizar
        else:
            self.open_main_window()  # Abrir nueva ventana al llegar a 100%

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
            self.error_label.configure(text="Usuario encontrado", text_color="white",fg_color="green")
        else:
            self.error_label.configure(text="Usuario no existe", text_color="white",fg_color="#f04735")

    def submit_login(self):
        user = self.entry_user.get()
        password = self.entry_password.get()

        # Verificar si hay usuarios registrados
        if not Registro.users:
            self.on_log_error_entry("No hay usuarios registrados", "white", "#f04735")
            self.after(1000, self.hide_label)
            return

        # Buscar el usuario en la lista
        for u in Registro.users:
            if u["usuario"] == user and u["password"] == password:
                self.error_label.configure(text="Cargando...",fg_color="#5ccc58")
                self.start_loading()  # Agrega esto
                return
        self.on_log_error_entry("Usuario y/o contraseña incorrectos", "white", "#f04735",)
        self.after(1000,self.hide_label)


    def submit_login_e(self,event):
        user = self.entry_user.get()
        password = self.entry_password.get()

        # Verificar si hay usuarios registrados
        if not Registro.users:
            self.on_log_error_entry("No hay usuarios registrados", "white", "#f04735")
            self.after(1000, self.hide_label)
            return

        # Buscar el usuario en la lista
        for u in Registro.users:
            if u["usuario"] == user and u["password"] == password:
                self.error_label.configure(text="Cargando...",fg_color="#5ccc58")
                self.start_loading()  # Agrega esto
                return
        self.on_log_error_entry("Usuario y/o contraseña incorrectos", "white", "#f04735",)
        self.after(1000,self.hide_label)

    def open_main_window(self):
        self.destroy()  # Cierra la ventana actual
        main = MainApp()  # Crea la nueva ventana
        main.mainloop()  # Ejecuta la ventana principal


app = LoginApp()
app.mainloop()


