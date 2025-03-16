#Importamos desde el paquete, la columna y los tipos de clases con los datos que queremos.
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine

#Hacemos un objeto de clase Base
Base = declarative_base()


#Realizando clase Post, teniendo Herencia de Base
#Como Base es parte de Alchemy, por tanto estamos heredando todo de Alchemy
class Event(Base):
    __tablename__ = "event" #Nombre de la tabla
    #Cramos las columnas de la tabla
    #Aqui estamos creando la tabla y los atributos del objeto a la vez
    id_event=Column(Integer,primary_key=True)
    name_event=Column(String(100))
    date_event=Column(Date) # de datetime.date => se pasa atributo como =date(##,##,##)
    place_event=Column(String)

    #Para fecha actual se usa objeto datetime.now ===>  =datetime.now()

    #Creando el cosntructor para el objeto
    def __init__(self,id_event, name_event, date_event, place_event):
        self.id_event = id_event
        self.name_event = name_event
        self.date_event = date_event
        self.place_event = place_event

    #Metodo ___repr__
    #A diferencia dell __str__ que devuelve una cadena
    #INVESTIGAR: ¿Qué es __repr__?
    def __repr__(self):
        return (f"Post(id_event: {self.id_event!r}, name: {self.name_event!r}",
                f"date_event: {self.date_event}",
                f"place_event: {self.place_event}")

#Aqui creamos el motor, indicamos el tipo de base de datos, y el nombre
#echo funciona para devolver respuestas desde la base de datos
#INVESTIGAR : ¿Qué es future?
engine=create_engine("sqlite:///db_assistance.db", echo=True, future=True)

#Arrancamos el motor
Base.metadata.create_all(engine)

#TAREA: Estar indagando como hacer ORM´s más complejos.
#TENER LISTO EL FORMULARIO para agregarlo el ORM al final.