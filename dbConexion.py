import sqlite3
from flask import current_app, g
from flask.cli import with_appcontext

DATABASE = "Petropolis.db"


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def close_connection(exception=None):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def finish_app(app):
    app.teardown_appcontext(close_connection)

def init_app(app):
    with app.app_context():
        db = get_db()
        return db

def guardar (id,Codigo_Empleado,Fecha_Ingreso,Fecha_Salida,Cargo,Dependencia,Salario,Desenpeno,Puntaje,Retroalimentacion,Nombre,Apellido,Edad,Fecha_Nacimiento,Telefono,Correo,Direccion,User,Password,Admin,authenticated):
    Conexion = get_db()
    with Conexion.cursor() as cursor:
        cursor.execute("INSERT INTO USUARIOS (id,Codigo_Empleado,Fecha_Ingreso,Fecha_Salida,Cargo,Dependencia,Salario,Desenpeno,Puntaje,Retroalimentacion,Nombre,Apellido,Edad,Fecha_Nacimiento,Telefono,Correo,Direccion,User,Password,Admin,authenticated) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"), 
        (id,Codigo_Empleado,Fecha_Ingreso,Fecha_Salida,Cargo,Dependencia,Salario,Desenpeno,Puntaje,Retroalimentacion,Nombre,Apellido,Edad,Fecha_Nacimiento,Telefono,Correo,Direccion,User,Password,Admin,authenticated)

        Conexion.commit()
        Conexion.close


