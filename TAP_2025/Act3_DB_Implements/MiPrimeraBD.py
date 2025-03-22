import sqlite3

#Crear la base de datos
name_db = "MiPrimera.db"
conexion=sqlite3.connect(name_db)
conexion.close()

#Crear una tabla
sqlintruction = "CREATE TABLE if NOT EXISTS " \
                "demo(Id INTEGER PRIMARY KEY," \
                "name varchar(30))"


conexion=sqlite3.connect(name_db)
conexion.execute(sqlintruction)
conexion.close()

obtieneTablas = " SELECT * FROM sqlite_master"
conecta=sqlite3.connect(name_db)
cursor = conecta.cursor()
cursor.execute(obtieneTablas)
print(cursor.fetchall())
conecta.close()

#Insertar registro
registro = "INSERT INTO demo(Id,name) VALUES(2,'Pedro Navajas')"
reconecta = sqlite3.connect(name_db)
try:
    reconecta.execute(registro)
    reconecta.commit()
except Exception as e:
    if type(e).__name__ == "Intregity Error":
        print("Posible llave duplicada")
    else:
        print(type(e).__name__)
reconecta.close()

#Consultar en una tabla
query = "SELECT * FROM demo"
con = sqlite3.connect(name_db)
cursor = con.cursor()
resultado = cursor.execute(query).fetchall()
con.close()

for item in resultado:
    print(item)

#Para actualizar un registro
sentencia = "UPDATE demo SET name = 'Juanito Alimaña' WHERE Id = 1"
reconecta = sqlite3.connect(name_db)
reconecta.execute(sentencia)
reconecta.commit()
reconecta.close()

#Borrar registro

"""
TAREA: 
Ya con lo aprendido, lo implementamos en el login, tenemos que agregar, eliminar y consultar en la BD
Hay que investigar como cifrar contraseñas en python para los registros de la BD
Hay algo que se llama OneWayFunction , el cual hace que no haya retorno, por lo cual si nos dan la 
contraseña, y si es correcta con el cifrado, si se logro. 

"""
