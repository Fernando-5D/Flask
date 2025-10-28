from datetime import datetime, date
from flask import Flask, render_template, request, flash, session
app = Flask(__name__)

app.config['SECRET_KEY'] = "janedoelamejorfemmefatalytodaunapioneradelosanomalosymiesposa"
usuarios[email or telefono] = [
    {
        'nombre': "ADMIN1",
        'password': "admin1_123"
    },
    {
        'nombre': "ADMIN2",
        'password': "admin2_456"
    }
]

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
def inicioSesion():
    if session.get('sesion'):
        nombre = session.get('usuario', 'Usuario')
        session.clear()
        flash(f'Sesion cerrada. Hasta luego, {nombre}!', 'success')
        return redirect(url_for('inicio'))
    return render_template("sesion.html")

sesion = False
@app.route('/iniciandoSesion', methods = ("GET", "POST"))
def iniciandoSesion():
    if request.method == "POST":
        email = request.form("email")
        telefono = request.form("telefono")
        password = request.form["password"]
        
        if email in usuarios or telefono in usuarios:
            usuario = usuarios[email or telefono]
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
        apellidoM = request.form("apellidoM")
        fechaNac = datetime.strptime(request.form["fechaNac"], '%Y-%m-%d').date()
        genero = request.form["genero"]
        pronombre = request.form["pronombre"]
        email = request.form("email")
        telefono = request.form("telefono")
        password = request.form["password"]
        passwordC = request.form["passwordC"]
        
        if fechaNac > date.today():
            error.append("Fecha de nacimiento invalida")
            
        if pronombre == None:
            error.append("Pronombre invalido")
            
        if passwordC != password:
            error.append("La contraseña no coincide")
        
        if error:
            for err in error:
                flash(err)                        
            return render_template("registro.html")
        else:
            print(str(nombre), str(apellidoP), str(apellidoM), str(fechaNac), str(genero), str(pronombre), str(email), str(telefono), str(password), str(passwordC))
            return render_template("inicio.html")

if __name__ == '__main__':
    app.run(debug=True)
