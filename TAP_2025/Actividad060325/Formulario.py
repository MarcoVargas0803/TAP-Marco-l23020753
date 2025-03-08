from tkinter import *
from tkinter.ttk import Treeview
from db_script import DataBase

import customtkinter as ct


class ControlMto(ct.CTk):

    """
    users = [("paquito", "paquito123"),
                ("tribilin", "tribilin123"),
                ("elbryan", "elbryan123"),
                ("mariacarey", "mariacarey123")
                ]
    """


    def __init__(self):
        super().__init__()

        self.db1 = DataBase()
        self.title("Control de Mantenimiento")
        self.geometry("900x750")
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
        #self.f7.grid(row=7, column=0, sticky="nsew", pady=5, padx=5)

    def crear_widgets(self):
        # Labels
        ct.CTkLabel(self.titulo, text="Control de Mantenimiento", text_color="White", font=("Helvetica", 25)).pack(padx=10, pady=10,side="left")
        ct.CTkLabel(self.f1, text="Nombre:", text_color="White").pack(side="left", padx=10, pady=10)
        ct.CTkLabel(self.f2, text="Fecha:", text_color="White").pack(side="left", padx=10, pady=10)
        ct.CTkLabel(self.f3, text="Clave:", text_color="White").pack(side="left", padx=10, pady=10)
        ct.CTkLabel(self.f4, text="Pago:", text_color="White").pack(side="left", padx=10, pady=10)

        # Entradas de texto
        self.entrada_nombre = ct.CTkEntry(self.f1,placeholder_text="Fulanito Alberto",width=400)
        self.entrada_nombre.pack(padx=20, pady=5, side="right")
        self.entrada_nombre.bind("<FocusIn>")

        self.entrada_fecha = ct.CTkEntry(self.f2, placeholder_text="07/03/25", width=400)
        self.entrada_fecha.pack(padx=20, pady=5, side="right")

        self.entrada_pago = ct.CTkEntry(self.f3, placeholder_text="1023", width=400)
        self.entrada_pago.pack(padx=20, pady=5, side="right")

        self.entrada_password = ct.CTkEntry(self.f4,placeholder_text="Juanito123@", show="*",width=400)
        self.entrada_password.pack(padx=20, pady=5, side="right")

        #Buttons en f6

        self.button_send = ct.CTkButton(self.f5,)
        self.button_send.pack(padx=10,pady=5,side="right")

        self.button_cancel = ct.CTkButton(self.f5)
        self.button_cancel.pack(padx=10,pady=5,side="right")

        #self.entrada_usuario = ct.CTkEntry(self.f6,placeholder_text="Juanito1",width=400)
        #self.entrada_usuario.pack(padx=20, pady=5, side="right")

        self.error_label = ct.CTkLabel(self.titulo,text=" ",font=("Helvetica",15),corner_radius=20)
        self.error_label.pack(side="right",padx=10,pady=10)


        # Botón de Registro
        self.boton_registrar = ct.CTkButton(self.f7, text="Registrar", command=self.registrar_usuario,fg_color="gray",hover_color="#438713",text_color="black")
        self.boton_registrar.pack(pady=10)

        # Barra de progreso (oculta al inicio)
        self.progress = ct.CTkProgressBar(self)
        self.progress.grid(row=8, column=0, padx=10, pady=10, sticky="ew")
        self.progress.set(0)  # Iniciar en 0

        # Style=Style()

        self.tv = Treeview(self.f6, columns=("Columna1", "Columna2"))
        # Style.configure("Treeview",rowheight=40)
        self.tv.heading("#0", text="No.")
        self.tv.heading("Columna1", text="Usuario")
        self.tv.heading("Columna2", text="Password")
        self.tv.column("#0", width=5, minwidth=5, stretch=True)
        # tv.configure()
        self.tv.tag_configure('par', background='lightyellow', font=("Arial", 15))
        self.tv.tag_configure('impar', background='lightgreen', font=("Arial", 15), foreground="blue")

        self.tv.pack(side="top", fill="x", padx=5, pady=5)
        self.llenarTreeview()

        # Eventos bind
        self.entrada_nombre.bind("<FocusIn>", self.on_focus_in_name)
        self.entrada_nombre.bind("<FocusOut>", self.on_focus_out_name)
        self.entrada_fecha.bind("<FocusIn>", self.on_focus_in_lastname)
        self.entrada_fecha.bind("<FocusOut>", self.on_focus_out_lastname)
        self.entrada_pago.bind("<FocusIn>", self.on_focus_in_email)
        self.entrada_pago.bind("<FocusOut>", self.on_focus_out_email)
        self.entrada_password.bind("<FocusIn>", self.on_focus_in_password)
        self.entrada_password.bind("<FocusOut>", self.on_focus_out_password)


        #self.bind("<Return>", self.registrar_)
        self.bind("<Shift_L>", self.on_show_in_password)
        self.bind("<Shift_R>", self.on_show_in_password)

        self.bind("<KeyRelease-Shift_L>", self.on_show_out_password)
        self.bind("<KeyRelease-Shift_R>", self.on_show_out_password)

    def llenarTreeview(self):
        users = self.db1.obtain_users()
        contador = 0
        for item in users:
            contador += 1
            if contador % 2 == 0:
                self.tv.insert("", END, text=contador, values=(item[0], item[1]), tags=("par",))
            else:
                self.tv.insert("", END, text=contador, values=(item[0], item[1]), tags=("impar",))
        return

    def start_loading(self):
        """Inicia la simulación de carga al iniciar sesión"""
        self.boton_registrar.configure(state="disabled")  # Deshabilitar botón
        self.progress.set(0)  # Reiniciar barra de progreso
        self.update_progress(0)  # Iniciar progreso

    def update_progress(self, value):
        """Simula el progreso y carga la nueva ventana"""
        if value < 1:
            value += 0.1  # Incremento del progreso
            self.progress.set(value)
            self.after(300, self.update_progress, value)  # Esperar 300ms y actualizar
        else:
            self.destroy()  # Abrir nueva ventana al llegar a 100%


    def on_log_error_entry(self,text_color="#d1cdcd",message="Todos los campos son obligatorios.",fg_color="#d94b43"):
        self.error_label.configure(text=message,text_color=text_color,fg_color=fg_color,corner_radius=20)

    def hide_label(self):
        self.error_label.configure(text="",fg_color="transparent") # Oculta el Label


    def on_focus_in_name(self, e):
        self.entrada_nombre.configure(text_color="white")
        self.error_label.configure(text=" Nombre de pila ",fg_color="#9197a1",text_color="black")
        self.after(1500,self.hide_label)

    def on_focus_out_name(self, e):
        self.entrada_nombre.configure(text_color="gray")

    def on_focus_in_lastname(self, e):
        self.entrada_fecha.configure(text_color="white")
        self.error_label.configure(text=" 1er y 2ndo Apellido ",fg_color="#9197a1",text_color="black")
        self.after(1500,self.hide_label)

    def on_focus_out_lastname(self, e):
        self.entrada_fecha.configure(text_color="gray")

    def on_focus_in_password(self, e):
        self.entrada_password.configure(text_color="white")
        self.error_label.configure(text=" Almenos un caracter especial ",fg_color="#9197a1",text_color="black")
        self.after(1500,self.hide_label)


    def on_focus_out_password(self, e):
        self.entrada_password.configure(text_color="gray")

    def on_focus_in_password_v(self, e):
        self.entrada_verify_password.configure(text_color="white")
        self.error_label.configure(text=" Verificar contraseña ",fg_color="#9197a1",text_color="black")
        self.after(1500,self.hide_label)


    def on_focus_out_password_v(self, e):
        self.entrada_verify_password.configure(text_color="gray")

    def on_show_in_password(self,event):
        self.entrada_password.configure(show="")
        self.entrada_verify_password.configure(show="")

    def on_show_out_password(self,event):
        self.entrada_password.configure(show="*")
        self.entrada_verify_password.configure(show="*")

    def on_focus_in_email(self, e):
        self.entrada_pago.configure(text_color="white")
        self.error_label.configure(text=" Correo personal u institucional ",fg_color="#9197a1",text_color="black")
        self.after(1500,self.hide_label)


    def on_focus_out_email(self, e):
        self.entrada_pago.configure(text_color="gray")

    def on_focus_in_user(self, e):
        self.entrada_usuario.configure(text_color="gray")
        self.error_label.configure(text=" Nombre de usuario ",fg_color="#9197a1",text_color="black")
        self.after(1500,self.hide_label)


    def on_focus_out_user(self, e):
        self.entrada_usuario.configure(text_color="gray")

    def on_button_register(self, event):
        self.registro_win = ControlMto()
        self.registro_win.mainloop()

    def validar_usuario(self, event):
        """Verificar en tiempo real si el usuario existe."""
        user = self.entrada_usuario.get()
        if any(u["usuario"] == user for u in ControlMto.users):
            self.error_label.configure(text="Usuario encontrado", text_color="white",fg_color="green")
        else:
            self.error_label.configure(text="Usuario no existe", text_color="white",fg_color="#f04735")

    def registrar_usuario(self):
        usuario = self.entrada_usuario.get()
        password = self.entrada_password.get()
        pago = self.entrada_pago()
        verify_password = self.entrada_verify_password.get()

        # Validaciones
        if not usuario or not password or not verify_password:
            self.on_log_error_entry("Todos los campos son obligatorios.")
            return

        if password != verify_password:
            self.on_log_error_entry("Las contraseñas no coinciden.", fg_color="#c9d134", text_color="black")
            self.after(1500, self.hide_label)
            return

        # Verificar si el usuario ya existe en la base de datos

        if self.db1.user_exists(usuario):
            self.on_log_error_entry("El usuario ya existe.")
            self.after(1500, self.hide_label)
            return

        # Insertar usuario en la base de datos
        if self.db1.insert(usuario,password,pago):
            self.on_log_error_entry(f"Usuario {usuario} registrado correctamente.", fg_color="#5ccc58")
            self.start_loading()
        else:
            self.on_log_error_entry("Error al registrar el usuario.")

"""
    def registrar_usuario(self):
        usuario = self.entrada_usuario.get()
        password = self.entrada_password.get()
        verify_password = self.entrada_verify_password.get()

        # Validaciones
        if not usuario or not password or not verify_password:
            self.on_log_error_entry()
            return

        if password != verify_password:
            self.on_log_error_entry(message="Las contraseñas no coinciden.",fg_color="#c9d134",text_color="black")
            self.after(1500,self.hide_label)
            return

        # Verificar si el usuario ya existe
        for u in ControlMto.users:
            if u["usuario"] == usuario:
                self.on_log_error_entry(message="El usuario ya existe.")
                self.after(1500, self.hide_label)
                return

        # Agregar usuario a la lista
        ControlMto.users.append({"usuario": usuario, "password": password})
        #self.after(2000,self.on_log_error_entry,show_loading_bar)
        self.on_log_error_entry(message=f" usuario {usuario} registrado correctamente.",fg_color="#5ccc58")


"""


def registrar_usuario_e(self, event):
    usuario = self.entrada_usuario.get()
    password = self.entrada_password.get()
    verify_password = self.entrada_verify_password.get()

    # Validaciones
    if not usuario or not password or not verify_password:
        self.on_log_error_entry("Todos los campos son obligatorios.")
        return

    if password != verify_password:
        self.on_log_error_entry("Las contraseñas no coinciden.", fg_color="#c9d134", text_color="black")
        self.after(1500, self.hide_label)
        return

    # Verificar si el usuario ya existe en la base de datos
    if self.db1.user_exists(usuario):
        self.on_log_error_entry("El usuario ya existe.")
        self.after(1500, self.hide_label)
        return

    # Insertar usuario en la base de datos
    if self.db1.insert(usuario, password,):
        self.on_log_error_entry(f"Usuario {usuario} registrado correctamente.", fg_color="#5ccc58")
        self.start_loading()
    else:
        self.on_log_error_entry("Error al registrar el usuario.")

app1 = ControlMto()
app1.mainloop()