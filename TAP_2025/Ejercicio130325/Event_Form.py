import customtkinter as ct
import tkinter.font as tkfont
from ORM_classes import Event, engine
from PIL import Image
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from consult_AssistanceClasses import Event_consult


class EventForm(ct.CTkToplevel):
    def __init__(self):
        super().__init__()

        self.title("Event Form")
        self.geometry("850x500")
        self.resizable(False, False)
        self.grab_set()

        self.personalized_font = tkfont.Font(family="SF-Pro-Rounded-Regular",size=10)

        self.foto_path = "usuario.png"

        self.configurar_grid_main()
        self.frame_main_creation()
        self.configurar_grid_title()
        self.frametitle_creation()
        self.configurar_grid_widgets()
        self.framewidgets_creation()
        self.progress_bar_creation()
        self.bind_creation()
        self.in_focus_id_event_auto_define()

        """self.configurar_grid()
        self.frame_creation()
        self.frame_creation()
        self.entry_creation()
        self.button_creation()
        self.label_creation()
        self.bind_creation()
        """
    def configurar_grid_main(self):
        self.grid_columnconfigure(index=(0,1), weight=1)
        self.grid_rowconfigure(index=0,weight=1)

    def frame_main_creation(self):
        self.frameTitle = ct.CTkFrame(self,corner_radius=0)
        self.framewidgets = ct.CTkFrame(self,fg_color="#d54c4a",corner_radius=0)
        self.frameTitle.grid(column=0,row=0,sticky="nsew")
        self.framewidgets.grid(column=1,row=0,sticky="nsew")

    def configurar_grid_title(self):
        self.frameTitle.grid_columnconfigure(index=0,weight=1)
        self.frameTitle.grid_rowconfigure(index=(0,1),weight=1)


    def frametitle_creation(self):
        self.title_label = ct.CTkLabel(self.frameTitle,text_color="#fcf9ce",text="Event",font=("Helvetica",50))
        self.title_label.grid(column=0,row=0,sticky="nsew", pady=10, padx =10)

        try:
            self.event_image = ct.CTkImage(
                light_image=Image.open(f"title_event_image.png"),
                dark_image=Image.open(f"title_event_image.png"),
                size=(200,200)
            )
        except FileNotFoundError:
            print("Imagen no encontrada.")
            self.event_image = None

        self.title_event_image = ct.CTkLabel(self.frameTitle, image=self.event_image, text="") if self.event_image else ct.CTkLabel(self, text="Sin imagen")
        self.title_event_image.grid(column=0,row=1,pady=10,padx=10)


    def configurar_grid_widgets(self):
        self.framewidgets.grid_rowconfigure(index=(0,1,2,3,4,5,6,7,8,9),weight=0)
        self.framewidgets.grid_columnconfigure(index=0,weight=1)

    def framewidgets_creation(self):
        self.id_label = ct.CTkLabel(self.framewidgets,text_color="white",text="Id",font=("helvetica",15))
        self.name_label = ct.CTkLabel(self.framewidgets,text_color="white",text="Nombre",font=("helvetica",15))
        self.date_label = ct.CTkLabel(self.framewidgets,text_color="white",text="Fecha",font=("helvetica",15))
        self.place_label = ct.CTkLabel(self.framewidgets,text_color="white",text="Lugar",font=("helvetica",15))

        self.id_entry =ct.CTkEntry(self.framewidgets,placeholder_text_color="texto de prueba",fg_color="#dea37a",text_color="#fcf9ce")
        self.name_entry =ct.CTkEntry(self.framewidgets,placeholder_text_color="texto de prueba",fg_color="#dea37a",text_color="#fcf9ce")
        self.date_entry =ct.CTkEntry(self.framewidgets,placeholder_text_color="Ej: 2024-03-17 14:30:00",fg_color="#dea37a",text_color="#fcf9ce")
        self.place_entry =ct.CTkEntry(self.framewidgets,placeholder_text_color="texto de prueba",fg_color="#dea37a",text_color="#fcf9ce")

        self.label_register = ct.CTkLabel(self.framewidgets, text_color="#fcf9ce", text="Register",
                                          font=("Helvetica", 15))

        self.label_message = ct.CTkLabel(self, text=" ", font=("Helvetica", 15), corner_radius=20)


        #Grid
        self.id_label.grid(column=0,row=0,sticky="w", padx=10,pady=10)
        self.name_label.grid(column=0,row=2,sticky="w", padx=10,pady=10)
        self.date_label.grid(column=0,row=4,sticky="w", padx=10,pady=10)
        self.place_label.grid(column=0,row=6,sticky="w", padx=10,pady=10)

        self.id_entry.grid(column=0,row=1,sticky="ew",padx=10)
        self.name_entry.grid(column=0,row=3,sticky="ew",padx=10)
        self.date_entry.grid(column=0,row=5,sticky="ew",padx=10)
        self.place_entry.grid(column=0,row=7,sticky="ew",padx=10,pady=10)

        self.label_register.grid(column=0, row=8, sticky="nsew", pady=10, padx=10)
        self.label_message.grid(column=0,row=3,columnspan=2,sticky="nsew",padx=10,pady=10)

    def in_focus_id_event_auto_define(self,event=None):
        self.id_consult = Event_consult()
        last_id = self.id_consult.consult_last_id()
        if last_id is None:
            self.label_message.configure(text="Ningun dato en la base de datos")
            print("ningun dato en base de datos")
            last_id = 1
        else:
            last_id = last_id + 1

        self.id_entry.delete(0, "end")  # Elimina texto anterior
        self.id_entry.insert(0, last_id)  # Inserta la fecha y hora actual
        self.id_entry.configure(text_color="white",state="disabled")
        self.label_message.configure(text="Test de prueba id", fg_color="#9197a1", text_color="black")
        self.after(1500, self.hide_label)

    def out_focus_id_event_auto_define(self,event):
        self.id_entry.configure(state="disabled",placeholder_text="0001")

    def progress_bar_creation(self):
        # Barra de progreso (oculta al inicio)
        self.progress = ct.CTkProgressBar(self)
        self.progress.grid(row=1, column=0, padx=10,columnspan=2, pady=10, sticky="ew")
        self.progress.set(0)  # Iniciar en 0

    def start_loading(self):
        """Inicia la simulación de carga al iniciar sesión"""
        #self.label_register.configure(state="disabled")  # Deshabilitar botón
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


    def bind_creation(self):
        # Eventos bind

        self.id_entry.bind("<FocusIn>",self.in_focus_id_event_auto_define)
        self.id_entry.bind("<FocusOut>",self.out_focus_id_event_auto_define)

        """self.id_entry.bind("<FocusIn>", lambda e: self.on_focus_in(self.id_entry, " Id asignado "))
        self.id_entry.bind("<FocusOut>", lambda e: self.on_focus_out(self.id_entry))"""

        self.name_entry.bind("<FocusIn>", lambda e: self.on_focus_in(self.name_entry, " Nombre del evento "))
        self.name_entry.bind("<FocusOut>", lambda e: self.on_focus_out(self.name_entry))

        self.date_entry.bind("<FocusIn>", lambda e: self.on_focus_in(self.date_entry,
                                                                                " Fecha asignada para el evento"))
        self.date_entry.bind("<FocusOut>", lambda e: self.on_focus_out(self.date_entry))

        self.place_entry.bind("<FocusIn>", lambda e: self.on_focus_in(self.place_entry, " Lugar del evento "))
        self.place_entry.bind("<FocusOut>", lambda e: self.on_focus_out(self.place_entry))

        self.label_register.bind("<Enter>",self.on_focus_in_register)
        self.label_register.bind("<Leave>",self.on_focus_out_register)
        self.label_register.bind("<Button-1>",self.register_user)
        self.bind("<Return>", self.register_user)

    def on_focus_in_register(self,event):
        self.label_register.configure(text_color="green")

    def on_focus_out_register(self,event):
        self.label_register.configure(text_color="#fcf9ce")

    def on_log_error_entry(self, text_color="#d1cdcd", message="Todos los campos son obligatorios.",
                           ):
        self.label_message.configure(text=message, text_color=text_color, corner_radius=20)

    def hide_label(self):
        self.label_message.configure(text="", fg_color="transparent")  # Oculta el Label

    def on_focus_in(self, entry, message):
        entry.configure(text_color="white")
        self.label_message.configure(text=message, fg_color="#9197a1", text_color="black")
        self.after(1500, self.hide_label)

    def on_focus_out(self, entry):
        entry.configure(text_color="gray")

    def validate_user(self, event):
        # Verificar en tiempo real si el usuario existe.

        # usuarios = self.db.obtain_user()
        """if any(user == u[0] for u in usuarios):
            self.label_message.configure(text="Usuario ya registrado", text_color="white", fg_color="#f04735")
        else:
            self.label_message.configure(text="Disponible para registrar", text_color="white", fg_color="green")
"""
        print("Validar usuario")




    def register_user(self, event=None):
        name = self.name_entry.get()
        date = self.date_entry.get()
        place = self.place_entry.get()

        self.Session = sessionmaker(bind=engine)
        self.sesion = self.Session()

        # Validaciones
        if not name or not date or not place:
            self.on_log_error_entry()
            return

        try:
            # Convertir la cadena ingresada a un objeto datetime
            fecha_formateada = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")

            # Crear y guardar el registro en la base de datos
            nuevo_registro = Event(name,fecha_formateada,place)
            self.sesion.add(nuevo_registro)
            self.sesion.commit()
            self.on_log_error_entry(message=f" usuario {name} registrado correctamente.")
            self.start_loading()  # Cierra la ventana de registro
        except ValueError:
            self.label_message.configure(text="Formato incorrecto. Usa: YYYY-MM-DD HH:MM:SS", text_color="red")

        # Agregar usuario a la base de datos
        # Insertando registro
