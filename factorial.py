from flask import Flask
app = Flask(__name__)

@app.route('/fact/<int:num>')
def Factorial(num = 1):
    if type(num) == int:
        factorial = 1
        for x in range(1, num + 1):
            factorial *= x
        
        return (format(str(num) + "! = " + str(factorial)))
    
if __name__ == '__main__':
    app.run(debug=True)
