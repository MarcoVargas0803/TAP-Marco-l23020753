import customtkinter as ct
import json
import os

class Registro(ct.CTk):
    def __init__(self):
        super().__init__()

        self.title("Registro")
        self.geometry("600x450")
        self.resizable(False, False)

        self.configurar_grid()
        self.crear_frames()
        self.crear_widgets()

    def configurar_grid(self):
        self.grid_columnconfigure(0, weight=1)
        for i in range(8):
            self.grid_rowconfigure(i, weight=1)

    def crear_frames(self):
        self.titulo = ct.CTkFrame(self, border_width=2)
        self.f1 = ct.CTkFrame(self, border_width=2)
        self.f2 = ct.CTkFrame(self, border_width=2)
        self.f3 = ct.CTkFrame(self, border_width=2)
        self.f4 = ct.CTkFrame(self, border_width=2)
        self.f5 = ct.CTkFrame(self, border_width=2)
        self.f6 = ct.CTkFrame(self, border_width=2)
        self.f7 = ct.CTkFrame(self, border_width=2)

        self.titulo.grid(row=0, column=0, sticky="nsew", pady=5, padx=5)
        self.f1.grid(row=1, column=0, sticky="nsew", pady=5, padx=5)
        self.f2.grid(row=2, column=0, sticky="nsew", pady=5, padx=5)
        self.f3.grid(row=3, column=0, sticky="nsew", pady=5, padx=5)
        self.f4.grid(row=4, column=0, sticky="nsew", pady=5, padx=5)
        self.f5.grid(row=5, column=0, sticky="nsew", pady=5, padx=5)
        self.f6.grid(row=6, column=0, sticky="nsew", pady=5, padx=5)
        self.f7.grid(row=7, column=0, sticky="nsew", pady=5, padx=5)

    def crear_widgets(self):
        # Labels
        ct.CTkLabel(self.titulo, text="registro de usuario", text_color="White", font=("Helvetica", 25)).pack(padx=10, pady=10,side="left")
        ct.CTkLabel(self.f1, text="Nombre:", text_color="White").pack(side="left", padx=10, pady=10)
        ct.CTkLabel(self.f2, text="Apellido:", text_color="White").pack(side="left", padx=10, pady=10)
        ct.CTkLabel(self.f3, text="Email:", text_color="White").pack(side="left", padx=10, pady=10)
        ct.CTkLabel(self.f4, text="Password:", text_color="White").pack(side="left", padx=10, pady=10)
        ct.CTkLabel(self.f5, text="Verify Password:", text_color="White").pack(side="left", padx=10, pady=10)
        ct.CTkLabel(self.f6, text="Usuario:", text_color="White").pack(side="left", padx=10, pady=10)
        ct.CTkLabel(self.titulo, text=" " , text_color="White", font=("Helvetica", 10)).pack(padx=10, pady=10,side="right")


        # Entradas de texto
        self.entrada_nombre = ct.CTkEntry(self.f1)
        self.entrada_nombre.pack(padx=20, pady=5, fill="x", expand=True)
        self.entrada_nombre.bind("<FocusIn>")

        self.entrada_apellido = ct.CTkEntry(self.f2)
        self.entrada_apellido.pack(padx=20, pady=5, fill="x", expand=True)

        self.entrada_email = ct.CTkEntry(self.f3)
        self.entrada_email.pack(padx=20, pady=5, fill="x", expand=True)

        self.entrada_password = ct.CTkEntry(self.f4, show="*")
        self.entrada_password.pack(padx=20, pady=5, fill="x", expand=True)

        self.entrada_verify_password = ct.CTkEntry(self.f5, show="*")
        self.entrada_verify_password.pack(padx=20, pady=5, fill="x", expand=True)

        self.entrada_usuario = ct.CTkEntry(self.f6)
        self.entrada_usuario.pack(padx=20, pady=5, fill="x", expand=True)

        # Botón de Registro
        self.boton_registrar = ct.CTkButton(self.f7, text="Registrar", command=self.registrar_usuario)
        self.boton_registrar.pack(pady=10)



        # Eventos bind
        self.entrada_nombre.bind("<FocusIn>", self.on_focus_in_name)
        self.entrada_nombre.bind("<FocusOut>", self.on_focus_out_name)
        self.entrada_apellido.bind("<FocusIn>", self.on_focus_in_lastname)
        self.entrada_apellido.bind("<FocusOut>", self.on_focus_out_lastname)
        self.entrada_email.bind("<FocusIn>", self.on_focus_in_email)
        self.entrada_email.bind("<FocusOut>", self.on_focus_out_email)
        self.entrada_password.bind("<FocusIn>", self.on_focus_in_password)
        self.entrada_password.bind("<FocusOut>", self.on_focus_out_password)
        self.entrada_verify_password.bind("<FocusIn>", self.on_focus_in_password_v)
        self.entrada_verify_password.bind("<FocusOut>", self.on_focus_out_password_v)
        self.entrada_usuario.bind("<FocusIn>", self.on_focus_in_user)
        self.entrada_usuario.bind("<FocusOut>", self.on_focus_out_user)


    def on_log_error_entry(self,message,text_color,fg_color):
        self.error_label.configure(text=message,text_color=text_color,fg_color=fg_color,corner_radius=10)


    def on_focus_in_name(self, e):
        self.entrada_nombre.configure(text_color="white")

    def on_focus_out_name(self, e):
        self.entrada_nombre.configure(text_color="gray")

    def on_focus_in_lastname(self, e):
        self.entrada_apellido.configure(text_color="white")

    def on_focus_out_lastname(self, e):
        self.entrada_apellido.configure(text_color="gray")

    def on_focus_in_password(self, e):
        self.entrada_password.configure(text_color="white")

    def on_focus_out_password(self, e):
        self.entrada_password.configure(text_color="gray")

    def on_focus_in_password_v(self, e):
        self.entrada_verify_password.configure(text_color="white")

    def on_focus_out_password_v(self, e):
        self.entrada_verify_password.configure(text_color="gray")

    def on_focus_in_email(self, e):
        self.entrada_email.configure(text_color="white")

    def on_focus_out_email(self, e):
        self.entrada_email.configure(text_color="gray")

    def on_focus_in_user(self, e):
        self.entrada_usuario.configure(text_color="gray")

    def on_focus_out_user(self, e):
        self.entrada_usuario.configure(text_color="gray")



    def on_button_register(self, event):
        self.registro_win = Registro()
        self.registro_win.mainloop()

    def on_enter_register(self, event):
        self.register_me.configure(text_color="#2641de")

    def on_leave_register(self, event):
        self.register_me.configure(text_color="#cacfed")

    def registrar_usuario(self):
        """Registra al usuario y guarda en JSON"""
        nombre = self.entrada_nombre.get()
        apellido = self.entrada_apellido.get()
        email = self.entrada_email.get()
        usuario = self.entrada_usuario.get()
        password = self.entrada_password.get()
        verify_password = self.entrada_verify_password.get()

        # Validaciones
        if not all([nombre, apellido, email, usuario, password, verify_password]):
            print("Todos los campos son obligatorios.")
            return

        if password != verify_password:
            print("Las contraseñas no coinciden.")
            return

        # Cargar usuarios existentes
        usuarios = self.cargar_usuarios()

        if usuario in usuarios:
            print(f"El usuario '{usuario}' ya existe.")
            return

        # Guardar usuario
        usuarios[usuario] = {
            "nombre": nombre,
            "apellido": apellido,
            "email": email,
            "password": password
        }

        self.guardar_usuarios(usuarios)
        print(f"Usuario '{usuario}' registrado exitosamente.")
        self.destroy()  # Cierra la ventana de registro

    def cargar_usuarios(self):
        """Carga los usuarios desde un archivo JSON."""
        if os.path.exists("usuarios.json"):
            with open("usuarios.json", "r") as file:
                return json.load(file)
        return {}  # Si no existe el archivo, devuelve un diccionario vacío

    def guardar_usuarios(self, usuarios):
        """Guarda los usuarios en un archivo JSON."""
        with open("usuarios.json", "w") as file:
            json.dump(usuarios, file, indent=4)
