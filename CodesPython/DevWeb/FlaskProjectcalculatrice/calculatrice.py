from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("calculatrice.html")

@app.route("/calculate", methods=["GET", "POST"])

def calculate():
    number1 = float(request.form["num1"])
    number2 = float(request.form["num2"])
    operation = request.form["operation"]
    result= None
    if operation == "add":
        result = number1 + number2
    elif operation == "subtract":
        result = number1 - number2
    elif operation == "multiply":
        result = number1 * number2
    elif operation == "divide":
        if number2 != 0:
            result = number1 / number2
        else:
            result = "Error: Division by zero"
    elif operation == "power":
        result = number1 ** number2
    return render_template("calculatrice.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

