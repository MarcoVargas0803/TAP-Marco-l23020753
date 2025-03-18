import customtkinter as ct
from ORM_classes import Assistant, Event
from sqlalchemy.orm import sessionmaker
from ORM_classes import Assistance

# Clases de consulta
class Assistant_consult:
    def __init__(self):
        self.Session = sessionmaker(bind=Assistance.engine)
        self.session = self.Session()

    def get_all_assistants(self):
        try:
            resultado = self.session.query(Assistant).all()
            # Retornar solo los nombres o datos relevantes
            return [s.nombre for s in resultado]  # Asegúrate de cambiar 'nombre' por el campo adecuado
        except Exception as e:
            print(f"Error en get_all_assistants: {e}")
        finally:
            self.session.close()

class Event_Consult:
    def __init__(self):
        self.Session = sessionmaker(bind=Assistance.engine)
        self.session = self.Session()

    def get_all_events(self):
        try:
            resultado = self.session.query(Event).all()
            # Retornar solo los nombres o datos relevantes
            return [s.nombre_evento for s in resultado]  # Asegúrate de cambiar 'nombre_evento' por el campo adecuado
        except Exception as e:
            print(f"Error en get_all_events: {e}")
        finally:
            self.session.close()

# Clase de la interfaz gráfica
class EventApp(ct.CTk):
    def __init__(self):
        super().__init__()

        self.title("Consulta de Eventos y Asistentes")
        self.geometry("850x400")
        self.resizable(False, False)

        self.configurar_grid_main()
        self.frame_main_creation()
        self.configure_grid_frameMain()
        self.frametitle_creation()

        # Crear instancia de las clases de consulta
        self.assistant_consult = Assistant_consult()
        self.event_consult = Event_Consult()

        # Consultar todos los asistentes y eventos
        self.assistants = self.assistant_consult.get_all_assistants()
        self.events = self.event_consult.get_all_events()

        # Crear los Comboboxes
        self.combobox_event = ct.CTkComboBox(self, values=self.events, width=200)
        self.combobox_event.grid(row=0, column=1, padx=10, pady=10)

        self.combobox_assistant = ct.CTkComboBox(self, values=self.assistants, width=200)
        self.combobox_assistant.grid(row=1, column=1, padx=10, pady=10)

        self.button_display = ct.CTkButton(self, text="Mostrar", command=self.display_selected)
        self.button_display.grid(row=2, column=1, padx=10, pady=10)

    def display_selected(self):
        selected_event = self.combobox_event.get()
        selected_assistant = self.combobox_assistant.get()

        print(f"Evento seleccionado: {selected_event}")
        print(f"Asistente seleccionado: {selected_assistant}")

    def configurar_grid_main(self):
        # Configurar la grilla principal
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def frame_main_creation(self):
        # Crear frame principal
        self.frame = ct.CTkFrame(self)
        self.frame.grid(row=0, column=0, sticky="nsew")

    def configure_grid_frameMain(self):
        # Configurar la grilla dentro del frame
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)

    def frametitle_creation(self):
        # Titulo de la ventana
        self.label_title = ct.CTkLabel(self.frame, text="Seleccione un Evento y Asistente", font=("Arial", 16))
        self.label_title.grid(row=0, column=0, padx=10, pady=10)

# Ejecutar la app
if __name__ == "__main__":
    app = EventApp()
    app.mainloop()