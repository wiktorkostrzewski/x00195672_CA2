from flask import Flask, request, render_template_string
from calculator_app.calculator import Calculator

app = Flask(__name__)
calculator = Calculator()

TEMPLATE = """
<!doctype html>
<title>Calculator</title>
<h1>Simple Calculator</h1>
<form method="post">
  <input name="first" placeholder="First number" required>
  <select name="operation">
    <option value="add">+</option>
    <option value="subtract">-</option>
    <option value="multiply">*</option>
    <option value="divide">/</option>
  </select>
  <input name="second" placeholder="Second number" required>
  <button type="submit">Calculate</button>
</form>
{% if result is not none %}
  <p id="result">Result: {{ result }}</p>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        first = float(request.form["first"])
        second = float(request.form["second"])
        operation = request.form["operation"]

        if operation == "add":
            result = calculator.add(first, second)
        elif operation == "subtract":
            result = calculator.subtract(first, second)
        elif operation == "multiply":
            result = calculator.multiply(first, second)
        elif operation == "divide":
            result = calculator.divide(first, second)

    return render_template_string(TEMPLATE, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1234)