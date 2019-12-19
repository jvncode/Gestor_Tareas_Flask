from tasks import app
from flask import render_template, request

import csv

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("tasks.html")

print("method:", request.method)
print('parametros', request.values)


'''
@app.route("/salvarTarea")
def salvartarea():
    recuperar paramentros
    abrir fichero
    añadir registros
    devovler respuesta todo correcto
'''
