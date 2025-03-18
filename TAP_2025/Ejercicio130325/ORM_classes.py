from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import create_engine
from sqlalchemy import Date


Base = declarative_base()

class Assistant(Base):
    __tablename__ = "assistant" #Nombre de la tabla
    #Cramos las columnas de la tabla
    #Aqui estamos creando la tabla y los atributos del objeto a la vez
    id_assistant=Column(Integer,primary_key=True, autoincrement=True)
    assistances = relationship("Assistance", back_populates="assistant")

    name_assistant=Column(String(100))
    first_lastname_assistant=Column(String)
    second_lastname_assistant=Column(String)
    curp_assistant=Column(String)
    phone_assistant=Column(Integer)

    #Creando el cosntructor para el objeto
    def __init__(self, name, first_lastname, second_lastname, CURP, Phone):
        self.name_assistant = name
        self.first_lastname_assistant = first_lastname
        self.second_lastname_assistant = second_lastname
        self.curp_assistant = CURP
        self.phone_assistant = Phone

    def __repr__(self):
        return (f"First_lastname: {self.first_lastname_assistant}",
                f"Second_lastname: {self.second_lastname_assistant}",
                f"CURP: {self.CURP_assistant}"
                f"Phone: {self.phone_assistant})")


class Event(Base):
    __tablename__ = "event"

    id_event=Column(Integer,primary_key=True, autoincrement=True)
    assistances = relationship("Assistance",back_populates="event")


    name_event=Column(String(100))
    date_event=Column(Date) # de datetime.date => se pasa atributo como =date(##,##,##)
    place_event=Column(String)

    def __init__(self, name_event, date_event, place_event):
        self.name_event = name_event
        self.date_event = date_event
        self.place_event = place_event


class Assistance(Base):
    def __init__(self,id_event,id_assistant):
        self.id_event = id_event
        self.id_assistant = id_assistant

    __tablename__ = "assistance" #Nombre de la tabla
    id_assistance=Column(Integer,primary_key=True, autoincrement=True)
    # Claves foráneas
    id_assistant = Column(Integer, ForeignKey("assistant.id_assistant"),nullable=False)
    id_event = Column(Integer, ForeignKey("event.id_event"),nullable=False)

    assistant = relationship("Assistant",back_populates="assistances")
    event = relationship("Event",back_populates="assistances")



engine=create_engine("sqlite:///db_assistance.db", echo=True, future=True)

#Arrancamos el motor
Base.metadata.create_all(engine)