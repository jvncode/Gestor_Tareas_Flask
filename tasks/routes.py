from tasks import app
from flask import render_template, request, url_for, redirect
from tasks.forms import TaskForm

import csv


@app.route("/")
def index():
    fdatos = open('./data/tareas.dat','r')
    csvreader = csv.reader(fdatos, delimiter=',', quotechar='"')
    tareas = []
    for campo in csvreader:
        tareas.append(campo)
    fdatos.close()
    return render_template("index.html", registros=tareas)

@app.route("/newtask", methods=['GET', 'POST'])
def newtask():
    form = TaskForm(request.form)

    if request.method == 'GET':
        return render_template('tasks.html', form=form)

    if form.validate():
        fdatos = open('./data/tareas.dat', 'a')
        csvwriter = csv.writer(fdatos, delimiter=",", quotechar='"')

        title = request.values.get('title')
        desc = request.values.get('description')
        date = request.values.get('date')

        csvwriter.writerow([title, desc, date])

        fdatos.close()
        return redirect(url_for("index"))
    else:
        return render_template("tasks.html", form=form)
