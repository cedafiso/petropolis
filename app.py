from flask import Flask, render_template, request
import dbConexion

#Se crea el objeto que manejara la aplicacion
app = Flask(__name__)

class isUserLog:

    def __init__(self):
        self.isUserLog = False

    def checkAuth(self, user, password):
        db = dbConexion.init_app(app);
        query = "SELECT USER, PASSWORD FROM Usuarios WHERE USER = \'{}\' AND PASSWORD = \'{}\';".format(user, password)
        result = []
        for i in db.execute(query):
            result.append(i) if type(i) == list else result.append(0)
            
        if len(result) != 0:
            self.isUserLog = True
            return True
        else:
            self.isUserLog = False

    def logOut(self):
        self.isUserLog = False

loginUser = isUserLog();

@app.route('/')
def index():
    return render_template('/Index/index.html')

@app.route('/login/<string:ruta>/')
@app.route('/login/', methods=["GET", "POST"])
def login(ruta=""):
    if request.method == "GET":
        if(loginUser.isUserLog and ruta == "Actividades"):
            return loginActividades()
        elif(loginUser.isUserLog and ruta == "Retroalimentacion"):
            return retroalimentacion()
        elif(loginUser.isUserLog and ruta == "Informacion"):
            return loginDashboard()
        else:
            return render_template('./Ingresar/ingresar.html')
    elif request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        if (loginUser.checkAuth(user, password) and ruta == ""):
            return loginDashboard()
        else:
            return render_template('./Ingresar/ingresar.html')
    elif request.method == 'PUT':
        loginUser.isUserLog()
        return render_template('./Ingresar/ingresar.html')
          


@app.route('/nosotros')
def nosotros():
    return render_template('./Nosotros/nosotros.html')

@app.route('/productos')
def productos():
    return render_template('./Productos/productos.html')
    

def loginDashboard():
    return render_template('./Dashboard/dashboard.html')

@app.route('/dashboard_admi')
def loginDashboardAdmi():
    return render_template('./Dashboard/dashboard_admi.html')


def loginActividades():
    return render_template('./Actividades/actividades.html')


def retroalimentacion():
    return render_template("./Retroalimentacion/retroalimentacion.html")
    
if __name__=='__main__':
    app.run(port=8080, debug=True)
