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
class Post(Base):
    __tablename__ = "demo" #Nombre de la tabla
    #Cramos las columnas de la tabla
    #Aqui estamos creando la tabla y los atributos del objeto a la vez
    id=Column(Integer,primary_key=True)
    mensaje=Column(String(100))
    autor=Column(String)

    #Creando el cosntructor para el objeto
    def __init__(self,id,mensaje,autor):
        self.id = id
        self.mensaje = mensaje
        self.autor = autor

    #Metodo ___repr__
    #A diferencia dell __str__ que devuelve una cadena
    #INVESTIGAR: ¿Qué es __repr__?
    def __repr__(self):
        return f"Post(id: {self.id!r}, mensaje: {self.mensaje!r}, autor: {self.autor!r} )"

#Aqui creamos el motor, indicamos el tipo de base de datos, y el nombre
#echo funciona para devolver respuestas desde la base de datos
#INVESTIGAR : ¿Qué es future?
engine=create_engine("sqlite:///misdatos.db", echo=True, future=True)

#Arrancamos el motor
Base.metadata.create_all(engine)

#TAREA: Estar indagando como hacer ORM´s más complejos.
#TENER LISTO EL FORMULARIO para agregarlo el ORM al final.