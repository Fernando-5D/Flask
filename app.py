from flask import Flask, render_template, request, flash
app = Flask(__name__)

app.config['SECRET_KEY'] = "janedoelamejorfemmefatalytodaunapioneradelosanomalosymiesposa"

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

@app.route('/sesion')
def sesion():
    return render_template("sesion.html")

@app.route('/registro')
def registro():
    return render_template("registro.html")

@app.route('/registrando', methods = ("GET", "POST"))
def registrando():
    error = None
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellidoP = request.form["apellidoP"]
        apellidoM = request.form["apellidoM"]
        day = request.form["day"]
        month = request.form["month"]
        year = request.form["year"]
        genero = request.form["genero"]
        email = request.form["email"]
        password = request.form["password"]
        passwordC = request.form["passwordC"]
        
        if passwordC != password:
            error = "La contraseña no coincide"
        
        if error != None:
            flash(error)
            render_template("registro.html")
        else:
            flash("Cuenta \"{nombre}\" registrada")
            return render_template

if __name__ == '__main__':
    app.run(debug=True)
