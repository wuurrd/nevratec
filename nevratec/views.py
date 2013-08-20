from nevratec.app import app
from nevratec.solar_query import query
from flask import render_template, request
import traceback


@app.route("/")
def index():
    return render_template('index.template')


@app.route('/solar_calc', methods=["POST"])
def calculate_solar():
    try:
        value = query(request.form['address'])
    except Exception, e:
        value = traceback.format_exc(e)
    return render_template('solar.template', value=value)
