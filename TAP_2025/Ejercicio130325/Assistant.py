#Importamos desde el paquete, la columna y los tipos de clases con los datos que queremos.
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine

#Hacemos un objeto de clase Base
Base = declarative_base()


#Realizando clase Post, teniendo Herencia de Base
#Como Base es parte de Alchemy, por tanto estamos heredando todo de Alchemy
class Assistant(Base):
    __tablename__ = "assistant" #Nombre de la tabla
    #Cramos las columnas de la tabla
    #Aqui estamos creando la tabla y los atributos del objeto a la vez
    id_assistant=Column(Integer,primary_key=True)
    name_assistant=Column(String(100))
    first_lastname_assistant=Column(String)
    second_lastname_assistant=Column(String)
    curp_assistant=Column(String)
    phone_assistant=Column(Integer)

    #Creando el cosntructor para el objeto
    def __init__(self,id_assistant, name, first_lastname, second_lastname, CURP, Phone):
        self.id_assistant = id_assistant
        self.name_assistant = name
        self.first_lastname_assistant = first_lastname
        self.second_lastname_assistant = second_lastname
        self.curp_assistant = CURP
        self.phone_assistant = Phone

    #Metodo ___repr__
    #A diferencia dell __str__ que devuelve una cadena
    #INVESTIGAR: ¿Qué es __repr__?
    def __repr__(self):
        return (f"Post(id: {self.id!r}, name: {self.name_assistant!r}",
                f"First_lastname: {self.first_lastname_assistant}",
                f"Second_lastname: {self.second_lastname_assistant}",
                f"CURP: {self.CURP_assistant}"
                f"Phone: {self.phone_assistant})")

#Aqui creamos el motor, indicamos el tipo de base de datos, y el nombre
#echo funciona para devolver respuestas desde la base de datos
#INVESTIGAR : ¿Qué es future?
engine=create_engine("sqlite:///db_assistance.db", echo=True, future=True)

#Arrancamos el motor
Base.metadata.create_all(engine)

#TAREA: Estar indagando como hacer ORM´s más complejos.
#TENER LISTO EL FORMULARIO para agregarlo el ORM al final.