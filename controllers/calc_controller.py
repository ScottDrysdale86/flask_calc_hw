from app import app
from flask import render_template
from models.calculator import *


@app.route("/add/<int:num1>/<int:num2>")
def index(num1, num2):
    return render_template(
        "index.html",
        title="Addition Calculator",
        num1=num1,
        num2=num2,
        operator="+",
        result=Calculator.add(num1, num2),
    )


@app.route("/subtract/<int:num1>/<int:num2>")
def index2(num1, num2):
    return render_template(
        "index.html",
        title="Subtraction Calculator",
        num1=num1,
        num2=num2,
        operator="-",
        result=Calculator.subtract(num1, num2),
    )


@app.route("/multiply/<int:num1>/<int:num2>")
def index3(num1, num2):
    return render_template(
        "index.html",
        title="Multiplication Calculator",
        num1=num1,
        num2=num2,
        operator="*",
        result=Calculator.multiply(num1, num2),
    )


@app.route("/divide/<int:num1>/<int:num2>")
def index4(num1, num2):
    return render_template(
        "index.html",
        title="Division Calculator",
        num1=num1,
        num2=num2,
        operator="/",
        result=Calculator.divide(num1, num2),
    )
