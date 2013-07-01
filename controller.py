#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

def connect():
    con = sqlite3.connect('marprod.db')
    con.row_factory = sqlite3.Row
    return con


def get_marcas():
    con = connect()
    c = con.cursor()
    query = """SELECT id_marca,nombre FROM marcas"""
    result = c.execute(query)
    marca = result.fetchall()
    con.close()
    return marca 


def get_productos():
    con = connect()
    c = con.cursor()
    query = """SELECT a.codigo, a.nombre, a.descripcion, a.color,a.precio, b.nombre as 'nombre_marca'
            FROM productos a, marcas b WHERE a.fk_id_marca = b.id_marca"""
    result = c.execute(query)
    prod = result.fetchall()
    con.close()
    return prod

def delete(dato):
    exito = False
    con = connect()
    c = con.cursor()
    query = "DELETE FROM productos WHERE codigo = ?"
    try:
        resultado = c.execute(query, [dato])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito

def agregar_producto(nombre,descripcion, color, precio,marca_):
    exito = False
    con = connect()
    c = con.cursor()
    query_ = "SELECT id_marca FROM marcas WHERE nombre = ?"
    c.execute(query_, [marca_])
    id_marcas = c.fetchone()
    id_ = id_marcas[0]
    values = [nombre,descripcion, color, precio, id_]
    query = "INSERT INTO productos (nombre,descripcion, color, precio, fk_id_marca) VALUES (?,?,?,?,?)"
    try:
        resultado1 = c.execute(query, values)
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito

def get_produc_marca(id_marca):
    con = connect()
    c = con.cursor()
    query = """SELECT a.codigo, a.nombre, a.descripcion, a.color,a.precio, b.nombre as 'nombre_marca'
            FROM productos a, marcas b WHERE a.fk_id_marca = b.id_marca
            AND a.fk_id_marca = ?"""
    result = c.execute(query, [id_marca])
    prod = result.fetchall()
    con.close()
    return prod

def buscar_producto(word):
    con = connect()
    c = con.cursor()
    query = """SELECT a.codigo, a.nombre, a.descripcion, a.color,a.precio, b.nombre as 'nombre_marca'
            FROM productos a, marcas b WHERE a.fk_id_marca = b.id_marca
            AND (a.codigo LIKE '%'||?||'%' OR a.nombre LIKE '%'||?||'%' OR b.nombre LIKE '%'||?||'%' )"""

    result = c.execute(query, [word, word, word])
    seleccion= result.fetchall()
    con.close()
    return seleccion
