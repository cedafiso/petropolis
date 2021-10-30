from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user

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
    Depedencia= db.Column(db.String(30), unique=False)
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
    
if __name__=='__main__':
    app.run(port=8080, debug=True)
