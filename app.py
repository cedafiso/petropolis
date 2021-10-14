from flask import Flask, render_template

#Se crea el objeto que manejara la aplicacion
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('./Ingresar/ingresar.html')

@app.route('/nosotros')
def nosotros():
    return render_template('./Nosotros/nosotros.html')

@app.route('/productos')
def productos():
    return render_template('./Productos/productos.html')
    
@app.route('/dashboard')
def loginDashboard():
    return render_template('./Dashboard/dashboard.html')

@app.route('/dashboard_admi')
def loginDashboardAdmi():
    return render_template('./Dashboard/dashboard_admi.html')

@app.route('/dashboard/actividades')
def loginActividades():
    return render_template('./Actividades/actividades.html')

@app.route('/dashboard/retroalimentacion')
def retroalimentacion():
    return render_template("./Retroalimentacion/retroalimentacion.html")
    
if __name__=='__main__':
    app.run(port=8080, debug=True)
