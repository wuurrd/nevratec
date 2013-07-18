from nevratec.app import app
from nevratec.solar_query import query
from flask import render_template, request


@app.route("/")
def index():
    return render_template('index.template')


@app.route('/solar_calc', methods=["POST"])
def calculate_solar():
    value = query(request.form['address'])
    return render_template('solar.template', value=value)
