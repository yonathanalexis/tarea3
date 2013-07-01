#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
import controller 
from ui_formulario import Ui_Form

class Form(QtGui.QDialog):
	def __init__(self,parent=None,codigo=None):
		QtGui.QDialog.__init__(self,parent)
		self.ui=Ui_Form()
		self.ui.setupUi(self)
		if codigo is None:
            		self.ui.agregar.clicked.connect(self.editar_prod)
       		else:
		    self.codigo =codigo
		    datos_produc = controller.obtener_productos(codigo)
		    self.ui.Nombre_prod.setText(datos_produc["nombre"])
		    self.ui.Descripcion_prod.setText(datos_produc["descripcion"])
		    self.ui.Color_prod.setText(datos_produc["color"])
		    self.ui.Precio_prod.setText(datos_produc["precio"])
		    self.ui.Nombre_marca.setText(datos_produc["nombre_marca"])
            
		#self.ui.agregar.clicked.connect(self.edit)
		self.ui.cancelar.clicked.connect(self.cancel)
	
	
	
	def editar_prod(self):
		nombre = self.ui.Nombre_prod.text()
		descripcion = self.ui.Descripcion_prod.text()
		color = self.ui.Color_prod.text()
		precio = self.ui.Precio_prod.text()
		marca = self.ui.Nombre_marca.text()

		result = controller.crear_producto(nombre,descripcion, color, precio,marca)

		if result:
			self.reject() #Cerramos y esto cargara nuevamente la grilla
		#else:
			#self.ui.mensajes.setText("Hubo un problema al intentar crear el alumno")
	def cancel(self):
		self.reject()
