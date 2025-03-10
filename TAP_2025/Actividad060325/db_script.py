import sqlite3

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
            obtiene_tablas = "SELECT name FROM sqlite_master WHERE type='table';"
            conecta = sqlite3.connect(self.db_name)
            cursor = conecta.cursor()
            cursor.execute(obtiene_tablas)
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

    def insert(self, nombre, fecha, clave, pago):
        # Insertar un registro con valores para nombre, clave y pago
        try:
            registro = "INSERT INTO users (Nombre, Fecha, Clave, Pago) VALUES (?, ?, ?, ?)"
            reconecta = sqlite3.connect(self.db_name)
            reconecta.execute(registro, (nombre, fecha, clave, pago))
            reconecta.commit()
            reconecta.close()
            return True
        except Exception as e:
            print(f"Error al insertar registro: {e}")
            return False

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

    def refresh_table(self,user_id, nombre):
        """Actualiza el nombre de un usuario en la base de datos según su ID"""
        try:
            conexion = sqlite3.connect(self.db_name)
            cursor = conexion.cursor()
            sentencia = "UPDATE users SET Nombre = ? WHERE ID = ?"

            cursor.execute(sentencia, (nombre, user_id))  # Ejecutar la actualización
            conexion.commit()  # Guardar cambios

            if cursor.rowcount == 0:
                print(f"No se encontró un usuario con el ID {user_id}. No se realizó ninguna actualización.")
            else:
                print(f"Usuario con ID {user_id} actualizado correctamente.")

            cursor.close()
            conexion.close()
        except Exception as e:
            print(f"Error al actualizar registro: {e}")

    def user_exists(self, nombre):
        try:
            conexion = sqlite3.connect(self.db_name)
            cursor = conexion.cursor()
            cursor.execute("SELECT Nombre FROM users WHERE Nombre = ?", (nombre,))
            result = cursor.fetchone()
            conexion.close()
            return result is not None
        except Exception as e:
            print(f"Error al verificar usuario: {e}")
            return False

    def obtain_user(self):
        # Obtener todos los usuarios
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute(
                "SELECT Nombre FROM users")  # Asegúrate de que la tabla y columnas sean correctas
            usuarios = cursor.fetchall()
            conn.close()
            return usuarios
        except Exception as e:
            print(f"Error al obtener usuarios: {e}")
            return []

    def eliminar_usuario(self, id_usuario):
        """Elimina un usuario por su ID"""
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM users WHERE ID = ?", (id_usuario,))
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"Error al eliminar usuario: {e}")
