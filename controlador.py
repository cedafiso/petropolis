from dbConexion import get_db

def insertar (id,Codigo_Empleado,Fecha_Ingreso,Fecha_Salida,Cargo,Dependencia,Salario,Desenpeno,Puntaje,Retroalimentacion,Nombre,Apellido,Edad,Fecha_Nacimiento,Telefono,Correo,Direccion,User,Password,Admin,authenticated):
    Conexion = get_db()
    with Conexion.cursor() as cursor:
        cursor.execute("INSERT INTO USUARIOS (id,Codigo_Empleado,Fecha_Ingreso,Fecha_Salida,Cargo,Dependencia,Salario,Desenpeno,Puntaje,Retroalimentacion,Nombre,Apellido,Edad,Fecha_Nacimiento,Telefono,Correo,Direccion,User,Password,Admin,authenticated) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"), 
        (id,Codigo_Empleado,Fecha_Ingreso,Fecha_Salida,Cargo,Dependencia,Salario,Desenpeno,Puntaje,Retroalimentacion,Nombre,Apellido,Edad,Fecha_Nacimiento,Telefono,Correo,Direccion,User,Password,Admin,authenticated)

        Conexion.commit()
        Conexion.close

def obtener():
    Conexion = get_db()
    usuarios = []
    with Conexion.cursor() as cursor:
        cursor.execute("SELECT id,Codigo_Empleado,Fecha_Ingreso,Fecha_Salida,Cargo,Dependencia,Salario,Desenpeno,Puntaje,Retroalimentacion,Nombre,Apellido,Edad,Fecha_Nacimiento,Telefono,Correo,Direccion,User,Password,Admin,authenticated FROM USUARIOS")
        usuarios = cursor.fetchall()
    Conexion.close()
    return usuarios

def eliminar(id):
    Conexion = get_db()
    with Conexion.cursor() as cursor:
        cursor.execute("DELETE FROM USUARIOS WHERE id = ?", (id,))
    Conexion.commit()
    Conexion.close()

def obtener_usuario_por_id(id):
    Conexion = get_db()
    usuarios = None
    with Conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id,Codigo_Empleado,Fecha_Ingreso,Fecha_Salida,Cargo,Dependencia,Salario,Desenpeno,Puntaje,Retroalimentacion,Nombre,Apellido,Edad,Fecha_Nacimiento,Telefono,Correo,Direccion,User,Password,Admin,authenticated FROM USUARIOS WHERE id = ?", (id,))
        usuarios = cursor.fetchone()
    Conexion.close()
    return usuarios

def actualizar_usuario(id,Codigo_Empleado,Fecha_Ingreso,Fecha_Salida,Cargo,Dependencia,Salario,Desenpeno,Puntaje,Retroalimentacion,Nombre,Apellido,Edad,Fecha_Nacimiento,Telefono,Correo,Direccion,User,Password,Admin,authenticated):
    Conexion = get_db()
    with Conexion.cursor() as cursor:
        cursor.execute("UPDATE USUARIOS SET Codigo_Empleado = ?, Fecha_Ingreso = ?, Fecha_Salida = ?, Cargo = ?, Dependencia = ?, Salario = ?, Desenpeno = ?, Puntaje = ?, Retroalimentacion = ?, Nombre = ?, Apellido = ?, Edad = ?, Fecha_Nacimiento = ?, Telefono = ?, Correo = ?, Direccion = ?, User = ?, Password = ?, Admin = ?, authenticated = ? WHERE id = ?",
                       (Codigo_Empleado,Fecha_Ingreso,Fecha_Salida,Cargo,Dependencia,Salario,Desenpeno,Puntaje,Retroalimentacion,Nombre,Apellido,Edad,Fecha_Nacimiento,Telefono,Correo,Direccion,User,Password,Admin,authenticated, id))
    Conexion.commit()
    Conexion.close()
