from tasks import app
from flask import render_template, request, url_for, redirect
from tasks.forms import TaskForm, ProccesTaskForm

import csv, sqlite3
from datetime import date

DATOS = './data/tareas.dat'
COPIA = './data/copia.txt'
BASE_DATOS = './data/task.db'

@app.route("/")
def index():
    fdatos = open(DATOS,'r')
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
        fdatos = open(DATOS, 'a')
        csvwriter = csv.writer(fdatos, delimiter=",", quotechar='"')

        title = request.values.get('title')
        desc = request.values.get('description')
        date = request.values.get('date')

        csvwriter.writerow([title, desc, date])

        fdatos.close()
        return redirect(url_for("index"))
    else:
        return render_template("tasks.html", form=form)

@app.route("/processtask", methods=['GET', 'POST'])
def processtask():
    form = ProccesTaskForm(request.form)

    if request.method == 'GET':

        fdatos = open(DATOS,'r')
        csvreader = csv.reader(fdatos, delimiter=',', quotechar='"')

        registroAct = None
        ilinea = 1
        ix = int(request.values.get('ix'))
        for linea in csvreader:
            if ilinea == ix:
                registroAct = linea
                break
            ilinea += 1

        if registroAct:
            if registroAct[2]:
                fechaTarea = date(int(registroAct[2][:4]), int(registroAct[2][5:7]), int(registroAct[2][8:]))
            else:
                fechaTarea: None
            
            accion = " "
            if 'btnModificar' in request.values:
                accion = 'M'
            
            if 'btnBorrar' in request.values:
                accion = 'B'
            form = ProccesTaskForm(data={'ix': ix, 'title': registroAct[0], 'description': registroAct[1], 'date': fechaTarea, 'btn': accion})

        return render_template('processtask.html', form=form)

    if form.btn.data == 'B':
        print('Borrar registro')
        return redirect(url_for('index'))

    if form.btn.data == 'M':
        if form.validate():
            print("Modificar el fichero")
            '''
            Crear fichero copia vacio en escritura
            leer y copiar todos los registros desde tareas.txt a copia.txt hasta el anterior al que vamos a modificar
            grabar el nuevo registro con los datos del formulario
            leer y copiar el resto de los registros hasta el final
            cerrar los dos ficheros
            borrar tareas.txt
            renombrar copia.txt a tareas.txt
            '''
            return redirect(url_for('index'))

        return render_template("processtask.html", form=form)