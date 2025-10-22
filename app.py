from datetime import datetime, date
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
    error = []
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellidoP = request.form["apellidoP"]
        apellidoM = request.form["apellidoM"]
        fecha = datetime.strptime(request.form["fecha"], '%Y-%m-%d').date()
        genero = request.form.get("genero")
        pronombre = request.form.get("pronombre")
        email = request.form["email"]
        telefono = request.form["telefono"]
        password = request.form["password"]
        passwordC = request.form["passwordC"]
        
        if fecha > date.today():
            error.append("Fecha de nacimiento invalida")
            
        if pronombre == None:
            error.append("Pronombre invalido")
            
        if passwordC != password:
            error.append("La contraseña no coincide")
        
        if error:
            for e in error:
                flash(e)                         
            return render_template("registro.html")
        else:
            print(str(nombre), str(apellidoP), str(apellidoM), str(fecha), str(genero), str(pronombre), str(email), str(password), str(passwordC))
            return render_template("inicio.html")

if __name__ == '__main__':
    app.run(debug=True)
