from flask import Flask, render_template

#Se crea el objeto que manejara la aplicacion
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('ingresar.html')

if __name__=='__main__':
    app.run(port=8080, debug=True)
