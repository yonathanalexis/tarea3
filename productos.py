# -*- coding: utf-8 -*-
import sqlite3
import csv

def tabla():
	conn = sqlite3.connect('data.db')
	c = conn.cursor()
	c.execute("""CREATE TABLE productos (id_producto integer primary key AUTOINCREMENT,codigo text,nombre text,descripcion text,marca text,color text)""")

	prod = []
	
	with open('data.csv','rb') as csvfile:
		f = csv.reader(csvfile,delimiter=';')
		for row in f:
			prod.append([unicode(row[0]),unicode(row[1]),unicode(row[2]),unicode(row[3]),unicode(row[4])])		
	c.executemany('INSERT INTO productos (codigo, nombre, descripcion, marca, color) values(?,?,?,?,?)',prod)
	conn.commit()	

if __name__=="__main__":
	tabla()
	
