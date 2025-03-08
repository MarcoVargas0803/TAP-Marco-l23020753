import sqlite3
from datetime import datetime

class DataBase:
    db_name = "Users.db"

    def __init__(self):
        try:
            conexion = sqlite3.connect(self.db_name)
            sqlintruction = """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                usuario TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                fecha_registro TEXT NOT NULL
            )
            """
            conexion.execute(sqlintruction)
            conexion.commit()
            conexion.close()
        except Exception as e:
            print(f"Error al inicializar la base de datos: {e}")

    def insert_user(self, nombre, apellido, email, usuario, password):
        try:
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            query = "INSERT INTO users (nombre, apellido, email, usuario, password, fecha_registro) VALUES (?, ?, ?, ?, ?, ?)"
            conexion = sqlite3.connect(self.db_name)
            cursor = conexion.cursor()
            cursor.execute(query, (nombre, apellido, email, usuario, password, fecha))
            conexion.commit()
            conexion.close()
            return True
        except sqlite3.IntegrityError:
            print("Error: El usuario o email ya existe.")
            return False
        except Exception as e:
            print(f"Error al insertar usuario: {e}")
            return False

    def get_users(self):
        try:
            conexion = sqlite3.connect(self.db_name)
            cursor = conexion.cursor()
            cursor.execute("SELECT id, nombre, apellido, email, usuario, fecha_registro FROM users")
            usuarios = cursor.fetchall()
            conexion.close()
            return usuarios
        except Exception as e:
            print(f"Error al obtener usuarios: {e}")
            return []

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

    def validate_user(self, usuario, password):
        try:
            conexion = sqlite3.connect(self.db_name)
            cursor = conexion.cursor()
            cursor.execute("SELECT usuario FROM users WHERE usuario = ? AND password = ?", (usuario, password))
            result = cursor.fetchone()
            conexion.close()
            return result is not None
        except Exception as e:
            print(f"Error al validar usuario: {e}")
            return False
