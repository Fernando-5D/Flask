from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/animalesExoticos')
def animales():
    return render_template("main.html")

@app.route('/vehiculosAntiguos')
def vehiculos():
    return render_template("main.html")

@app.route('/maravillasMundo')
def maravillas():
    return render_template("main.html")

@app.route('/acercaDe')
def acerca():
    return render_template("main.html")

if __name__ == '__main__':
    app.run(debug=True)
