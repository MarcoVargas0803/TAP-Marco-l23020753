import sqlite3
from datetime import datetime

class DataBase:
    db_name = "Users.db"

    # Inicializando la base de datos y tabla
    def __init__(self):
        try:
            conexion = sqlite3.connect(self.db_name)
            sqlintruction = """
            CREATE TABLE IF NOT EXISTS users (
                No INTEGER PRIMARY KEY,
                Nombre TEXT,
                Fecha TEXT,
                Clave TEXT,
                Pago REAL
            )
            """
            conexion.execute(sqlintruction)
            conexion.commit()
            conexion.close()
        except Exception as e:
            print(f"Error al inicializar la base de datos: {e}")

    def get_tables(self):
        # Obtener todas las tablas
        try:
            obtieneTablas = "SELECT name FROM sqlite_master WHERE type='table';"
            conecta = sqlite3.connect(self.db_name)
            cursor = conecta.cursor()
            cursor.execute(obtieneTablas)
            print(cursor.fetchall())
            conecta.close()
        except Exception as e:
            print(f"Error al obtener las tablas: {e}")

    def obtain_users(self):
        # Obtener todos los usuarios
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("SELECT Nombre, Fecha, Clave , Pago FROM users")  # Asegúrate de que la tabla y columnas sean correctas
            usuarios = cursor.fetchall()
            conn.close()
            return usuarios
        except Exception as e:
            print(f"Error al obtener usuarios: {e}")
            return []

    def insert(self, nombre, clave, pago):
        # Insertar un registro con valores para nombre, clave y pago
        try:
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Fecha actual
            registro = "INSERT INTO users (Nombre, Fecha, Clave, Pago) VALUES (?, ?, ?, ?)"
            reconecta = sqlite3.connect(self.db_name)
            reconecta.execute(registro, (nombre, fecha, clave, pago))
            reconecta.commit()
            reconecta.close()
        except Exception as e:
            print(f"Error al insertar registro: {e}")

    def consult_table(self):
        # Consultar todos los registros de la tabla
        try:
            query = "SELECT * FROM users"
            con = sqlite3.connect(self.db_name)
            cursor = con.cursor()
            resultado = cursor.execute(query).fetchall()
            con.close()
            for item in resultado:
                print(item)
        except Exception as e:
            print(f"Error al consultar la tabla: {e}")

    def refresh_table(self, id, nombre):
        # Actualizar un registro de acuerdo con el ID
        try:
            sentencia = "UPDATE users SET Nombre = ? WHERE No = ?"
            reconecta = sqlite3.connect(self.db_name)
            reconecta.execute(sentencia, (nombre, id))
            reconecta.commit()
            reconecta.close()
        except Exception as e:
            print(f"Error al actualizar registro: {e}")

    def user_exists(self, usuario):
        try:
            conexion = sqlite3.connect(self.db_name)
            cursor = conexion.cursor()
            cursor.execute("SELECT usuario FROM users WHERE usuario = ?", (usuario,))
            result = cursor.fetchone()
            conexion.close()
            return result is not None
        except Exception as e:
            print(f"Error al verificar usuario: {e}")
            return False
