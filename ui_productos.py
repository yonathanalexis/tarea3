# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_productos.ui'
#
# Created: Wed Jun  5 22:13:25 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 400)
        self.combo_marcas = QtGui.QComboBox(MainWindow)
        self.combo_marcas.setGeometry(QtCore.QRect(70, 60, 101, 25))
        self.combo_marcas.setObjectName("combo_marcas")
        self.label = QtGui.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(20, 60, 51, 16))
        self.label.setObjectName("label")
        self.line_buscar = QtGui.QLineEdit(MainWindow)
        self.line_buscar.setGeometry(QtCore.QRect(230, 60, 371, 25))
        self.line_buscar.setObjectName("line_buscar")
        self.boton_buscar = QtGui.QPushButton(MainWindow)
        self.boton_buscar.setGeometry(QtCore.QRect(610, 60, 87, 27))
        self.boton_buscar.setObjectName("boton_buscar")
        self.tabla_productos = QtGui.QTableView(MainWindow)
        self.tabla_productos.setGeometry(QtCore.QRect(20, 93, 661, 301))
        self.tabla_productos.setObjectName("tabla_productos")
        self.boton_eliminar = QtGui.QPushButton(MainWindow)
        self.boton_eliminar.setGeometry(QtCore.QRect(590, 10, 98, 27))
        self.boton_eliminar.setObjectName("boton_eliminar")
        self.boton_editar = QtGui.QPushButton(MainWindow)
        self.boton_editar.setGeometry(QtCore.QRect(470, 10, 98, 27))
        self.boton_editar.setObjectName("boton_editar")
        self.boton_agregar = QtGui.QPushButton(MainWindow)
        self.boton_agregar.setGeometry(QtCore.QRect(350, 10, 98, 27))
        self.boton_agregar.setObjectName("boton_agregar")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "productos", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Marca:", None, QtGui.QApplication.UnicodeUTF8))
        self.line_buscar.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "Busque películas aquí", None, QtGui.QApplication.UnicodeUTF8))
        self.boton_buscar.setText(QtGui.QApplication.translate("MainWindow", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.boton_eliminar.setText(QtGui.QApplication.translate("MainWindow", "eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.boton_editar.setText(QtGui.QApplication.translate("MainWindow", "editar", None, QtGui.QApplication.UnicodeUTF8))
        self.boton_agregar.setText(QtGui.QApplication.translate("MainWindow", "agregar", None, QtGui.QApplication.UnicodeUTF8))

