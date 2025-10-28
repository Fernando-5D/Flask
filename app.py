from datetime import datetime, date
from flask import Flask, render_template, request, flash, session, redirect, url_for
app = Flask(__name__)

app.config['SECRET_KEY'] = "janedoelamejorfemmefatalytodaunapioneradelosanomalosymiesposa"
usuarios = {}

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
    if session.get('login'):
        nombre = session.get('nombre', "Usuario")
        session.clear()
        return redirect(url_for('inicio'))
    return render_template("sesion.html")

@app.route('/iniciandoSesion', methods = ("GET", "POST"))
def iniciandoSesion():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        
        if email in usuarios:
            usuario = usuarios[email]
            if usuario['password'] == password:
                session['email'] = email
                session['nombre'] = usuario['nombre']
                session['login'] = True
                return redirect(url_for('inicio'))
            else:
                flash("Contraseña incorrecta", "error")
        else:
            flash("Usuario no encontrado", "error")
            
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
        apellidoM = request.form.get("apellidoM")
        fechaNac = datetime.strptime(request.form["fechaNac"], '%Y-%m-%d').date()
        genero = request.form["genero"]
        email = request.form["email"]
        password = request.form["password"]
        passwordC = request.form["passwordC"]
        
        if fechaNac > date.today():
            error.append("Fecha de nacimiento invalida")
               
        if passwordC != password:
            error.append("La contraseña no coincide")
        
        if error:
            for err in error:
                flash(err)                        
            return render_template("registro.html")
        else:
            usuarios[email] = {
                'nombre': nombre,
                'apellidoP': apellidoP,
                'apellidoM': apellidoM,
                'fechaNac': fechaNac,
                'genero': genero,
                'password': password
            }
            
            return redirect(url_for('sesion'))

if __name__ == '__main__':
    app.run(debug=True)
