from flask import Flask, render_template, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user
import controlador



#Se crea el objeto que manejara la aplicacion
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Petropolis.db"
app.config['SECRET_KEY'] = 'jo3n2o23noi42'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.init_app(app)

class USUARIOS(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    User = db.Column(db.String(30), unique=True)
    Password = db.Column(db.String(30), unique=False)
    Admin = db.Column(db.Integer, unique=False)
    Nombre = db.Column(db.String(30), unique=False)
    Codigo_Empleado = db.Column(db.Integer, unique=True)
    Fecha_Ingreso = db.Column(db.String(30), unique=False)
    Fecha_Salida = db.Column(db.String(30), unique=False)
    Cargo = db.Column(db.String(30), unique=False)
    Dependencia= db.Column(db.String(30), unique=False)
    Salario = db.Column(db.Float(30), unique=False)
    Desempeno= db.Column(db.Integer, unique=False)
    Puntaje= db.Column(db.Integer, unique=False) 
    Retroalimentacion = db.Column(db.String(30), unique=False)
    Apellido = db.Column(db.String(30), unique=False)
    Edad = db.Column(db.Integer, unique=False)
    Fecha_Nacimiento = db.Column(db.String(30), unique=False)
    Telefono = db.Column(db.Integer, unique=False)
    Correo = db.Column(db.String(30), unique=False)
    Direccion = db.Column(db.String(30), unique=False)


login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return USUARIOS.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('/Index/index.html')

@app.route('/login/', methods=["GET", "POST"])
def login(ruta=""):
    if request.method == "GET":
        return render_template('./Ingresar/ingresar.html')
    elif request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        username = USUARIOS.query.filter_by(User=user, Password=password).first()
        if username is None:
            return render_template('./Ingresar/ingresar.html') 
        else:
            login_user(username)
        if current_user.is_authenticated:
            if (current_user.Admin == 1):
                return render_template('./Dashboard/dashboard_admi.html')
            else:
                return render_template('./Dashboard/dashboard.html')
        else:
            return render_template('./Ingresar/ingresar.html') 


@app.route('/nosotros')
def nosotros():
    return render_template('./Nosotros/nosotros.html')

@app.route('/productos')
def productos():
    return render_template('./Productos/productos.html')

@app.route('/contactos')
def contactos():
    return render_template("./Contactos/contactos.html")
    
@app.route('/Dashboard')
@login_required
def loginDashboard():
    return render_template('./Dashboard/dashboard.html')

@app.route('/dashboard_admi')
@login_required
def loginDashboardAdmi():
    return render_template('./Dashboard/dashboard_admi.html')

@app.route('/Actividades')
@login_required
def loginActividades():
    return render_template('./Actividades/actividades.html')

@app.route('/Retroalimentacion')
@login_required
def retroalimentacion():
    return render_template("./Retroalimentacion/retroalimentacion.html")

#Desde aquí comienza el crud

@app.route('/agregar_usuario')
def formulario_agregar():
    return render_template('agregar_usuario.html')

@app.route("/guardar_usuario", methods=["POST"])
def guardar_usuario():
    id = request.form["id"]
    Codigo_Empleado = request.form["Codigo_Empleado"]
    Fecha_Ingreso = request.form["Fecha_Ingreso"]
    Fecha_Salida = request.form["Fecha_Salida"]
    Cargo = request.form["Cargo"]
    Dependencia = request.form["Dependencia"]
    Salario = request.form["Salario"]
    Desenpeno = request.form["Desenpeno"]
    Puntaje = request.form["Puntaje"]
    Retroalimentacion = request.form["Retroalimentacion"]
    Nombre = request.form["Nombre"]
    Apellido = request.form["Apellido"]
    Edad = request.form["Edad"]
    Fecha_Nacimiento = request.form["Fecha_Nacimiento"]
    Telefono = request.form["Telefono"]
    Correo = request.form["Correo"]
    Direccion = request.form["Direccion"]
    User = request.form["User"]
    Password = request.form["Password"]
    Admin = request.form["Fecha_Salida"]
    authenticated = request.form["authenticated"]


    controlador.insertar(id,Codigo_Empleado,Fecha_Ingreso,Fecha_Salida,Cargo,Dependencia,Salario,Desenpeno,Puntaje,Retroalimentacion,Nombre,Apellido,Edad,Fecha_Nacimiento,Telefono,Correo,Direccion,User,Password,Admin,authenticated)
    return redirect("/usuarios")

    
@app.route("/usuarios")
def usuarios():
    usuarios = controlador.obtener()
    return render_template("usuarios.html", usuarios=usuarios)


@app.route("/eliminar_usuario", methods=["POST"])
def eliminar_usuario():
    controlador.eliminar(request.form["id"])
    return redirect("/usuarios")

@app.route("/formulario_editar_usuario/<Integer:id>")
def editar_usuario(id):
    
    usuarios = controlador.obtener_usuario_por_id(id)
    return render_template("editar_usuario.html", usuarios=usuarios)

@app.route("/actualizar_usuario", methods=["POST"])
def actualizar_usuario():
    id = request.form["id"]
    Codigo_Empleado = request.form["Codigo_Empleado"]
    Fecha_Ingreso = request.form["Fecha_Ingreso"]
    Fecha_Salida = request.form["Fecha_Salida"]
    Cargo = request.form["Cargo"]
    Dependencia = request.form["Dependencia"]
    Salario = request.form["Salario"]
    Desenpeno = request.form["Desenpeno"]
    Puntaje = request.form["Puntaje"]
    Retroalimentacion = request.form["Retroalimentacion"]
    Nombre = request.form["Nombre"]
    Apellido = request.form["Apellido"]
    Edad = request.form["Edad"]
    Fecha_Nacimiento = request.form["Fecha_Nacimiento"]
    Telefono = request.form["Telefono"]
    Correo = request.form["Correo"]
    Direccion = request.form["Direccion"]
    User = request.form["User"]
    Password = request.form["Password"]
    Admin = request.form["Fecha_Salida"]
    authenticated = request.form["authenticated"]
    controlador.actualizar_usuario(id,Codigo_Empleado,Fecha_Ingreso,Fecha_Salida,Cargo,Dependencia,Salario,Desenpeno,Puntaje,Retroalimentacion,Nombre,Apellido,Edad,Fecha_Nacimiento,Telefono,Correo,Direccion,User,Password,Admin,authenticated)
    return redirect("/usuarios")
    

    
if __name__=='__main__':
    app.run(host='0.0.0.0', port=port, debug=True)

