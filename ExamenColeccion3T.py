##Para trabajar con base de datos
import sqlite3 as lite
import sys

##Nos conectamos a una base de datos llamada coleccionCds
conexion = lite.connect("coleccionCds.sqlite")

##Establezco un cursor para saber en que punto de la base de datos voy a trabajar
cursor = conexion.cursor()

##Le pido algo a la base de datos en lenguaje SQL
cursor.execute("INSERT  INTO discos VALUES(NULL,'El cd de Paco','Paco','2021','Rock');")

conexion.commit()
