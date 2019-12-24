from tasks import app
from flask import render_template, request, url_for, redirect

import csv


@app.route("/")
def index():
    fdatos = open('./data/tareas.dat','r')
    csvreader = csv.reader(fdatos, delimiter=',')
    tareas = []
    for campo in csvreader:
        tareas.append(campo)
    fdatos.close()
    return render_template("index.html", registros=tareas)

@app.route("/newtask", methods=['GET', 'POST'])
def newtask():
    if request.method == 'GET':
        return render_template('tasks.html')

    fdatos = open('./data/tareas.dat', 'a')
    csvwriter = csv.writer(fdatos, delimiter=",", quotechar='"')

    
    title = request.values.get('title')
    desc = request.values.get('desc')
    date = request.values.get('date')

    if title!="" and desc!="" and date!="":
        csvwriter.writerow([title, desc, date])

    fdatos.close()
    return redirect(url_for("index"))
