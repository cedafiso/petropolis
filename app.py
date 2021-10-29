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
    USER = db.Column(db.String(30), unique=True)
    PASSWORD = db.Column(db.String(30), unique=True)
    ADMIN = db.Column(db.Integer, unique=False)


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
        username = USUARIOS.query.filter_by(USER=user, PASSWORD=password).first()
        login_user(username)
        if current_user.is_authenticated:
            flash('You have successfully logged in')
            if (current_user.ADMIN == 1):
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
def retroalimentacion():
    return render_template("./Retroalimentacion/retroalimentacion.html")
    
if __name__=='__main__':
    app.run(port=8080, debug=True)
