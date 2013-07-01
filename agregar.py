#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
import controller 
import productos_marca
from ui_formulario import Ui_Form

class Form(QtGui.QDialog):
	def __init__(self,parent=None):
		QtGui.QDialog.__init__(self,parent)
		self.ui=Ui_Form()
		self.ui.setupUi(self)
		self.ui.cancelar.clicked.connect(self.cancel)
		self.ui.agregar.clicked.connect(self.agregar_prod)
	def agregar_prod(self):
		nombre = self.ui.Nombre_prod.text()
		descripcion = self.ui.Descripcion_prod.text()
		color = self.ui.Color_prod.text()
		precio = self.ui.Precio_prod.text()
		marca = self.ui.Nombre_marca.text()

		result = controller.agregar_producto(nombre,descripcion, color, precio,marca)

		if result:
			self.reject() #Cerramos y esto cargara nuevamente la grilla
		#else:
			#self.ui.mensajes.setText("Hubo un problema al intentar crear el alumno")
	def cancel(self):
		self.reject()
