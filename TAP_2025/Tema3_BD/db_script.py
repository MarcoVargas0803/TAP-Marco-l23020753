import sqlite3

class DataBase:
    db_name = "UsersDB.db"
    # Inicializando tabla
    def __init__(self):
        conexion = sqlite3.connect(self.db_name)
        conexion.close()
        # Crear una tabla
        sqlintruction = "CREATE TABLE if NOT EXISTS " \
                        "users(Id INTEGER PRIMARY KEY," \
                        "name varchar(30))"

        conexion = sqlite3.connect(self.db_name)
        conexion.execute(sqlintruction)
        conexion.close()

    def get_tables(self):
        self.obtieneTablas = " SELECT * FROM sqlite_master"
        conecta = sqlite3.connect(self.db_name)
        cursor = conecta.cursor()
        cursor.execute(self.obtieneTablas)
        print(cursor.fetchall())
        conecta.close()

    def insert(self):
        # Insertar registro
        registro = "INSERT INTO users(Id,name) VALUES(1,'Pedro Navajas')"
        reconecta = sqlite3.connect(self.db_name)
        try:
            reconecta.execute(registro)
            reconecta.commit()
        except Exception as e:
            if type(e).__name__ == "Intregity Error":
                print("Posible llave duplicada")
            else:
                print(type(e).__name__)
        reconecta.close()

    def consult_table(self):
        # Consultar en una tabla
        query = "SELECT * FROM users"
        con = sqlite3.connect(self.db_name)
        cursor = con.cursor()
        resultado = cursor.execute(query).fetchall()
        con.close()

        for item in resultado:
            print(item)

    def refresh_table(self):
        # Para actualizar un registro
        sentencia = "UPDATE users SET name = 'Juanito Alimaña' WHERE Id = 1"
        reconecta = sqlite3.connect(self.db_name)
        reconecta.execute(sentencia)
        reconecta.commit()
        reconecta.close()

db1 = DataBase()
db1.get_tables()
db1.insert()
db1.consult_table()
db1.refresh_table()