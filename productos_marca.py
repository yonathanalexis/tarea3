#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from PySide import QtGui, QtCore
import controller
import agregar
import editar
from ui_productos import Ui_MainWindow


class ProductosApp(QtGui.QWidget):

    def __init__(self):
        super(ProductosApp, self).__init__()
        self.ui =  Ui_MainWindow()
        self.ui.setupUi(self)
        self.cargar_marcas()
        self.cargar_productos()
        self.show()
        self.set_listeners()

    def delete(self):
        	model = self.ui.tabla_productos.model()
        	index = self.ui.tabla_productos.currentIndex()
        	if index.row() == -1: 
            		self.errorMessageDialog = QtGui.QErrorMessage(self)
            		self.errorMessageDialog.showMessage("Debe seleccionar una fila")
            		return False
        	else:
            		codigo = model.index(index.row(),0, QtCore.QModelIndex()).data()
            	if (controller.delete(codigo)):
                	self.cargar_productos()
                	msgBox = QtGui.QMessageBox()
                	msgBox.setText("EL registro fue eliminado.")
                	msgBox.exec_()
                	return True
            	else:
                	self.ui.errorMessageDialog = QtGui.QErrorMessage(self)
                	self.ui.errorMessageDialog.showMessage("Error al eliminar el registro")
                	return False
    def set_listeners(self):
        self.ui.combo_marcas.activated[int].connect(self.cargar_productos_por_marca)
        self.ui.boton_buscar.clicked.connect(self.cargar_buscar)
	self.ui.boton_eliminar.clicked.connect(self.delete)
	self.ui.boton_agregar.clicked.connect(self.agregar_dato)
	#self.boton_editar.clicked.connect(self.editar_dato)
    
    def agregar_dato(self):
		form=agregar.Form(self)
		form.rejected.connect(self.dato_nuevo)
		form.exec_()
    def dato_nuevo(self):
		self.cargar_productos()    
    def cargar_marcas(self):
        marcas = controller.get_marcas()
        self.ui.combo_marcas.addItem("Todos", -1)
        for marc in marcas:
            self.ui.combo_marcas.addItem(marc["nombre"],marc["id_marca"])


    def cargar_productos_por_marca(self, index):
        id_marca = self.ui.combo_marcas.itemData(self.ui.combo_marcas.currentIndex())
        if id_marca == -1:
             produc= controller.get_productos()
        else:
             produc = controller.get_produc_marca(id_marca)
        self.cargar_productos(produc)

    def cargar_buscar(self):
        dato = self.ui.line_buscar.text()
        prod = controller.buscar_producto(dato)
        self.cargar_productos(prod)

    def cargar_productos(self, producto=None):
        if producto is None:
            producto = controller.get_productos()

        
        self.model = QtGui.QStandardItemModel(len(producto), 6)
        self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"Codigo"))
        self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Nombre"))
        self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Descripcion"))
        self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Color"))
	self.model.setHorizontalHeaderItem(4, QtGui.QStandardItem(u"Precio"))
	self.model.setHorizontalHeaderItem(5, QtGui.QStandardItem(u"Marca"))

        r = 0
        for row in producto:
            index = self.model.index(r, 0, QtCore.QModelIndex()); 
            self.model.setData(index, row['codigo'])
            index = self.model.index(r, 1, QtCore.QModelIndex()); 
            self.model.setData(index, row['nombre'])
            index = self.model.index(r, 2, QtCore.QModelIndex()); 
            self.model.setData(index, row['descripcion'])
            index = self.model.index(r, 3, QtCore.QModelIndex()); 
            self.model.setData(index, row['color'])
	    index = self.model.index(r, 4, QtCore.QModelIndex()); 
            self.model.setData(index, row['precio'])
	    index = self.model.index(r, 5, QtCore.QModelIndex()); 
            self.model.setData(index, row['nombre_marca'])
            r = r+1

        self.ui.tabla_productos.setModel(self.model)
        self.ui.tabla_productos.setColumnWidth(0, 90)
        self.ui.tabla_productos.setColumnWidth(1, 150)
        self.ui.tabla_productos.setColumnWidth(2, 150)
        self.ui.tabla_productos.setColumnWidth(3, 150)
	self.ui.tabla_productos.setColumnWidth(4, 150)
	self.ui.tabla_productos.setColumnWidth(5, 150)



def run():
    app = QtGui.QApplication(sys.argv)
    main = ProductosApp()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()
