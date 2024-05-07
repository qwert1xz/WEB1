from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def calculator():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    equation = request.form['equation']
    try:
        result = eval(equation)
    except:
        result = "Error"
    return render_template('calculator.html', result=result, equation=equation)

if __name__ == '__main__':
    app.run(debug=True)