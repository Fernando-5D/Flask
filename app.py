from flask import Flask
app = Flask(__name__)

@app.route('/')
def ruta():
    return '<h1>Hola Fer</h1>'

@app.route('/fact/<int:num>')
def Factorial(num = 1):
    if type(num) == int:
        factorial = 1
        for x in range(1, num + 1):
            factorial *= x
        
        return (format(str(num) + "! = " + str(factorial)))

@app.route('/calc')
def calcInstrucciones():
    return '''<h1>Calculadora</h1>
                <p>Agregar a la URL si es...</p>
                <h2>Suma: /sum</h2>
                <h2>Resta: /res</h2>
                <h2>Multiplicacion: /multi</h2>
                <h2>Division: /div</h2>
                <h2>Mayor: /max</h2>
                <h2>Menor: /min</h2>
                <p>Seguido de...
                <h3>/num1/num2</h3>'''

@app.route('/calc/<op>/<int:n1>/<int:n2>')
def Calculadora(op, n1, n2):
    resultado = 0
    if op == 'sum':
        resultado = n1 + n2
    elif op == 'res':
        resultado = n1 - n2
    elif op == 'multi':
        resultado = n1 * n2
    elif op == 'div':
        resultado = n1 / n2
    elif op == 'max':
        resultado = max(n1, n2)
    elif op == 'min':
        resultado = min(n1, n2)
    
    return (format(str(resultado)))

if __name__ == '__main__':
    app.run(debug=True)
