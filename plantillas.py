from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def ruta():
    nombre = "Fer"
    pasatiempos = ["Programacion", "Fotografia", "Rally"]
    return render_template("plantillas_Test/template.html", usuario = nombre, hobbies = pasatiempos)

@app.route('/bienvenida/<nombre>')
def ruta1(nombre = "Usuario"):
    return render_template("plantillas_Test/bienvenida.html", name = nombre)

@app.route('/edad/<int:edad>')
def ruta2(edad = 18):
    return render_template("plantillas_Test/edad.html", age = edad)

@app.route('/altura/<int:altura>')
def ruta3(altura = 170):
    return render_template("plantillas_Test/altura.html", height = altura)

if __name__ == '__main__':
    app.run(debug=True)
