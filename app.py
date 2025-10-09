from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/animalesExoticos')
def animales():
    return render_template("animales.html")

@app.route('/vehiculosAntiguos')
def vehiculos():
    return render_template("vehiculos.html")

@app.route('/maravillasMundo')
def maravillas():
    return render_template("maravillas.html")

@app.route('/acercaDe')
def acerca():
    return render_template("acerca.html")

if __name__ == '__main__':
    app.run(debug=True)
