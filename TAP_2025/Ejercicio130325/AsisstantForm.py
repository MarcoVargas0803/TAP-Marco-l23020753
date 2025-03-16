import customtkinter as ct

class Assistant(ct.CTk):
    def __init__(self):
        super().__init__()

        self.title("Assistant Form")
        self.geometry("600x650")
        self.minsize(500,500)
        self.resizable(True, True)

        self.foto_path = "usuario.png"

        self.configurar_grid()
        self.frame_creation()
        self.frame_creation()
        self.entry_creation()
        self.button_creation()
        self.label_creation()
        self.bind_creation()

    def configurar_grid(self):
        self.grid_columnconfigure(0, weight=1)
        for i in range(8):
            self.grid_rowconfigure(i, weight=1)

    def frame_creation(self):

        self.frame_title = ct.CTkFrame(self, border_width=2)
        self.id_frame = ct.CTkFrame(self, border_width=2)
        self.name_frame = ct.CTkFrame(self, border_width=2)
        self.first_lastn_frame = ct.CTkFrame(self, border_width=2)
        self.sec_lastn_frame = ct.CTkFrame(self, border_width=2)
        self.curp_frame = ct.CTkFrame(self, border_width=2)
        self.phone_frame = ct.CTkFrame(self, border_width=2)
        self.submit_frame = ct.CTkFrame(self, border_width=2)

        self.frame_title.grid(row=0, column=0, sticky="nsew", pady=5, padx=5)
        self.id_frame.grid(row=1, column=0, sticky="nsew", pady=5, padx=5)
        self.name_frame.grid(row=2, column=0, sticky="nsew", pady=5, padx=5)
        self.first_lastn_frame.grid(row=3, column=0, sticky="nsew", pady=5, padx=5)
        self.sec_lastn_frame.grid(row=4, column=0, sticky="nsew", pady=5, padx=5)
        self.curp_frame.grid(row=5, column=0, sticky="nsew", pady=5, padx=5)
        self.phone_frame.grid(row=6, column=0, sticky="nsew", pady=5, padx=5)
        self.submit_frame.grid(row=7, column=0, sticky="nsew", pady=5, padx=5)

    def entry_creation(self):

        # Entradas de texto
        self.id_assistant_entry = ct.CTkEntry(self.id_frame, placeholder_text="Fulanito Alberto", width=400)
        self.id_assistant_entry.pack(padx=20, pady=5, fill="x", expand=True)
        self.id_assistant_entry.bind("<FocusIn>")

        self.name_entry = ct.CTkEntry(self.name_frame, placeholder_text="Alimaña Rodriguez", width=400)
        self.name_entry.pack(padx=20, pady=5, fill="x", expand=True)

        self.first_lastname_entry = ct.CTkEntry(self.first_lastn_frame, placeholder_text="Correo", width=400)
        self.first_lastname_entry.pack(padx=20, pady=5, fill="x", expand=True)

        self.second_lastname_entry = ct.CTkEntry(self.sec_lastn_frame, placeholder_text="Juanito123@", show="*", width=400)
        self.second_lastname_entry.pack(padx=20, pady=5, fill="x", expand=True)

        self.curp_entry = ct.CTkEntry(self.curp_frame, show="*", placeholder_text="Juanito123@", width=400)
        self.curp_entry.pack(padx=20, pady=5, fill="x", expand=True)

        self.phone_entry = ct.CTkEntry(self.phone_frame, placeholder_text="Juanito1", width=400)
        self.phone_entry.pack(padx=20, pady=5, fill="x", expand=True)

    def button_creation(self):
        # Botón de Registro
        self.boton_registrar = ct.CTkButton(self.submit_frame, text="Registrar", command=self.register_user,
                                            fg_color="gray", hover_color="#438713", text_color="black")
        self.boton_registrar.pack(pady=10)

    def label_creation(self):
        # Error label
        self.title = ct.CTkLabel(self.frame_title, text="Asistente", font=("Helvetica",50),corner_radius=20)
        self.title.pack(side="left", padx=10, pady=10)

        self.label_message = ct.CTkLabel(self.frame_title, text=" ", font=("Helvetica", 15), corner_radius=20)
        self.label_message.pack(side="right", padx=10, pady=10)

    def bind_creation(self):
        # Eventos bind
        self.id_assistant_entry.bind("<FocusIn>", lambda e: self.on_focus_in(self.id_assistant_entry, " Nombre de pila "))
        self.id_assistant_entry.bind("<FocusOut>", lambda e: self.on_focus_out(self.id_assistant_entry))

        self.name_entry.bind("<FocusIn>", lambda e: self.on_focus_in(self.name_entry, " 1er y 2ndo Apellido "))
        self.name_entry.bind("<FocusOut>", lambda e: self.on_focus_out(self.name_entry))

        self.second_lastname_entry.bind("<FocusIn>", lambda e: self.on_focus_in(self.second_lastname_entry,
                                                                                " Al menos un caracter especial "))
        self.second_lastname_entry.bind("<FocusOut>", lambda e: self.on_focus_out(self.second_lastname_entry))

        self.curp_entry.bind("<FocusIn>", lambda e: self.on_focus_in(self.curp_entry, " Verificar contraseña "))
        self.curp_entry.bind("<FocusOut>", lambda e: self.on_focus_out(self.curp_entry))

        self.first_lastname_entry.bind("<FocusIn>", lambda e: self.on_focus_in(self.first_lastname_entry,
                                                                               " Correo personal u institucional "))
        self.first_lastname_entry.bind("<FocusOut>", lambda e: self.on_focus_out(self.first_lastname_entry))

        self.phone_entry.bind("<FocusIn>", lambda e: self.on_focus_in(self.phone_entry, " Nombre de usuario "))
        self.phone_entry.bind("<FocusOut>", lambda e: self.on_focus_out(self.phone_entry))

        #KeyRealease user
        self.phone_entry.bind("<KeyRelease>", self.validate_user)


        self.bind("<Return>", self.register_user)

    def progress_bar_creation(self):
        # Barra de progreso (oculta al inicio)
        self.progress = ct.CTkProgressBar(self)
        self.progress.grid(row=8, column=0, padx=10, pady=10, sticky="ew")
        self.progress.set(0)  # Iniciar en 0

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
        self.label_message.configure(text=message, text_color=text_color, fg_color=fg_color, corner_radius=20)

    def hide_label(self):
        self.label_message.configure(text="", fg_color="transparent") # Oculta el Label

    def on_focus_in(self, entry, message):
        entry.configure(text_color="white")
        self.label_message.configure(text=message, fg_color="#9197a1", text_color="black")
        self.after(1500, self.hide_label)

    def on_focus_out(self, entry):
        entry.configure(text_color="gray")

    def validate_user(self, event):
        #Verificar en tiempo real si el usuario existe.
        user = self.phone_entry.get().strip()

        #usuarios = self.db.obtain_user()
        """if any(user == u[0] for u in usuarios):
            self.label_message.configure(text="Usuario ya registrado", text_color="white", fg_color="#f04735")
        else:
            self.label_message.configure(text="Disponible para registrar", text_color="white", fg_color="green")
"""
    def register_user(self, event=None):
        nombre = self.id_assistant_entry.get()
        apellido = self.name_entry.get()
        password = self.second_lastname_entry.get()
        email = self.first_lastname_entry.get()
        usuario = self.phone_entry.get()
        verify_password = self.curp_entry.get()

        # Validaciones
        if not usuario or not password or not verify_password:
            self.on_log_error_entry()
            return

        if password != verify_password:
            self.on_log_error_entry(message="Las contraseñas no coinciden.",fg_color="#c9d134",text_color="black")
            self.after(1500,self.hide_label)
            return

        # Verificar si el usuario ya existe
        """for u in self.db.get_users():
            if self.db.user_exists(u) == usuario:
                self.on_log_error_entry(message="El usuario ya existe.")
                self.after(1500, self.hide_label)
                return"""

        # Agregar usuario a la base de datos
        #self.db.insert_user(nombre,apellido,email,usuario,password,foto=foto_pefil)
        self.on_log_error_entry(message=f" usuario {usuario} registrado correctamente.",fg_color="#5ccc58")
        self.start_loading()  # Cierra la ventana de registro

app = Assistant()
app.mainloop()
