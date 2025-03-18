import ORM_classes
from ORM_classes import Assistance
from ORM_classes import Assistant
from ORM_classes import Event
from sqlalchemy.orm import sessionmaker

class Assistant_consult:
    def __init__(self):
        self.Session = sessionmaker(bind=ORM_classes.engine)
        self.session = self.Session()

    # Equivalente a SELECT from * fROM demo
    def consult_all_table(self):
        try:
            resultado = self.session.query(Assistant).all()
            for s in resultado:
                print(s)
        except Exception as e:
            print(f"Error en consult_all_table: {e}")
        finally:
            self.session.close()

    def get_all_assistants(self):
        try:
            resultado = self.session.query(Assistant).all()
            # Retornar solo los nombres o datos relevantes
            return [s.name_assistant for s in resultado]  # Asegúrate de cambiar 'nombre' por el campo adecuado
        except Exception as e:
            print(f"Error en get_all_assistants: {e}")
        finally:
            self.session.close()

    # Equivalente a consultar por filtrado WHERE
    # En este caso consultamos donde el registro sea igual 20
    def consult_by_filter(self):
        try:
            res = self.session.query(Assistant).filter_by(id=20)
            for s in res:
                print(s.id, s.mensaje, s.autor)
        except Exception as e:
            print(f"Error en consult_by_filter: {e}")
        finally:
            self.session.close()

    # Consultar ultimo Id de la base de datos
    def consult_last_id(self):
        try:
            ultimo_id = self.session.query(Assistant.id_assistant).order_by(Assistant.id_assistant.desc()).first()
            print("Ultmo Id ", ultimo_id[0])
            return ultimo_id[0]
        except Exception as e:
            print(f"Error en consult_last_id: {e}")
            return None
        finally:
            self.session.close()

    def consult_by_name_for_id(self, name):
        try:
            asistente = self.session.query(Assistant.id_assistant).filter_by(name_assistant=name).first()
            if asistente:
                print(f"ID encontrado para '{name}': {asistente[0]}")
                return asistente[0]
            else:
                print(f"Error: No se encontró un asistente con el nombre '{name}'")
                return None
        except Exception as e:
            print(f"Error en consult_by_name_for_id: {e}")
            return None
        finally:
            self.session.close()

class Event_consult:
    def __init__(self):
        self.Session = sessionmaker(bind=ORM_classes.engine)
        self.session = self.Session()

    # Consultar todos los eventos
    def consult_all_events(self):
        try:
            resultado = self.session.query(Event).all()
            return resultado
        except Exception as e:
            print(f"Error en consult_all_events: {e}")
            return []
        finally:
            self.session.close()

    # Consultar un evento por su ID
    def consult_by_id(self, event_id):
        try:
            event = self.session.query(Event).filter_by(id_event=event_id).first()
            if event:
                print(event)
                return event
            else:
                print(f"No se encontró un evento con ID {event_id}")
                return None
        except Exception as e:
            print(f"Error en consult_by_id: {e}")
            return None
        finally:
            self.session.close()

    # Consultar el último ID de evento registrado
    def consult_last_id(self):
        try:
            ultimo_id = self.session.query(Event.id_event).order_by(Event.id_event.desc()).first()
            print("Último ID de evento: ", ultimo_id[0] if ultimo_id else "No se encontraron registros.")
            return ultimo_id[0] if ultimo_id else None
        except Exception as e:
            print(f"Error en consult_last_id: {e}")
            return None
        finally:
            self.session.close()

    # Obtener todos los nombres de los eventos registrados
    def get_all_events(self):
        try:
            resultado = self.session.query(Event).all()
            return [event.name_event for event in resultado]
        except Exception as e:
            print(f"Error en get_all_events: {e}")
        finally:
            self.session.close()

    # Consultar un evento por su nombre y devolver su ID
    def consult_by_name_for_id(self, name):
        try:
            event = self.session.query(Event.id_event).filter_by(name_event=name).first()
            if event:
                print(f"ID encontrado para '{name}': {event[0]}")
                return event[0]
            else:
                print(f"Error: No se encontró un evento con el nombre '{name}'")
                return None
        except Exception as e:
            print(f"Error en consult_by_name_for_id: {e}")
            return None
        finally:
            self.session.close()

class Assistance_consult:
    def __init__(self):
        self.Session = sessionmaker(bind=ORM_classes.engine)  # Asegúrate de que 'Assistance' esté correctamente configurado
        self.session = self.Session()

    # Equivalente a SELECT * FROM assistance
    def consult_all_table(self):
        try:
            resultado = self.session.query(Assistance).all()  # Asegúrate de que 'Assistance' sea el nombre de la clase ORM
            return resultado # Aquí puedes personalizar para mostrar los campos de la asistencia
        except Exception as e:
            print(f"Error en consult_all_table: {e}")
            return []
        finally:
            self.session.close()

    def count_by_event(self, id_event):
        try:
            # Utilizamos filter_by para filtrar por el id_event y luego contamos el número de registros
            count = self.session.query(Assistance).filter_by(id_event=id_event).count()
            print(f"Número de asistencias para el evento {id_event}: {count}")
            return count
        except Exception as e:
            print(f"Error en count_by_event: {e}")
            return 0  # Devuelve 0 en caso de error
        finally:
            self.session.close()

app = Event_consult()
eventos = app.consult_all_events()
for evento in eventos:
    print(evento.id_event)
