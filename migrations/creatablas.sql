DROP TABLE IF EXISTS tareas;

CREATE TABLE "tareas" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"titulo"	TEXT NOT NULL,
	"descripcion"	TEXT,
	"fecha"	TEXT NOT NULL
	"id_empleado"	INTEGER,
	FOREIGN KEY("id_empleado") REFERENCES "empleados"("id")
);

DROP TABLE IF EXISTS empleados;

CREATE TABLE "empleados" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"name"	TEXT NOT NULL,
	"apellidos"	TEXT NOT NULL,
	"email"	TEXT NOT NULL
)