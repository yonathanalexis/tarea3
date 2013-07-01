# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_formulario.ui'
#
# Created: Thu Jun  6 02:30:38 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(385, 325)
        Form.setToolTip("")
        Form.setWhatsThis("")
        Form.setAccessibleName("")
        self.agregar = QtGui.QPushButton(Form)
        self.agregar.setGeometry(QtCore.QRect(80, 260, 98, 27))
        self.agregar.setObjectName("agregar")
        self.cancelar = QtGui.QPushButton(Form)
        self.cancelar.setGeometry(QtCore.QRect(220, 260, 98, 27))
        self.cancelar.setObjectName("cancelar")
        self.Nombre_prod = QtGui.QLineEdit(Form)
        self.Nombre_prod.setGeometry(QtCore.QRect(210, 30, 151, 27))
        self.Nombre_prod.setStatusTip("")
        self.Nombre_prod.setWhatsThis("")
        self.Nombre_prod.setAccessibleName("")
        self.Nombre_prod.setInputMask("")
        self.Nombre_prod.setText("")
        self.Nombre_prod.setObjectName("Nombre_prod")
        self.Descripcion_prod = QtGui.QLineEdit(Form)
        self.Descripcion_prod.setGeometry(QtCore.QRect(210, 70, 151, 27))
        self.Descripcion_prod.setObjectName("Descripcion_prod")
        self.Color_prod = QtGui.QLineEdit(Form)
        self.Color_prod.setGeometry(QtCore.QRect(210, 110, 151, 27))
        self.Color_prod.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.Color_prod.setObjectName("Color_prod")
        self.Precio_prod = QtGui.QLineEdit(Form)
        self.Precio_prod.setGeometry(QtCore.QRect(210, 150, 151, 27))
        self.Precio_prod.setObjectName("Precio_prod")
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 30, 66, 17))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(90, 70, 81, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(90, 110, 66, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(90, 150, 66, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 81, 17))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(90, 200, 66, 17))
        self.label_7.setObjectName("label_7")
        self.Nombre_marca = QtGui.QLineEdit(Form)
        self.Nombre_marca.setGeometry(QtCore.QRect(210, 200, 151, 27))
        self.Nombre_marca.setObjectName("Nombre_marca")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Producto", None, QtGui.QApplication.UnicodeUTF8))
        self.agregar.setText(QtGui.QApplication.translate("Form", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelar.setText(QtGui.QApplication.translate("Form", "cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.Nombre_prod.setPlaceholderText(QtGui.QApplication.translate("Form", "Ingresar nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.Descripcion_prod.setPlaceholderText(QtGui.QApplication.translate("Form", "Ingresar Descripción", None, QtGui.QApplication.UnicodeUTF8))
        self.Color_prod.setPlaceholderText(QtGui.QApplication.translate("Form", "Ingresar Color", None, QtGui.QApplication.UnicodeUTF8))
        self.Precio_prod.setPlaceholderText(QtGui.QApplication.translate("Form", "Ingresar Precio", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Descripcion:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Color:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Precio:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "Producto", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Form", "Marca:", None, QtGui.QApplication.UnicodeUTF8))
        self.Nombre_marca.setPlaceholderText(QtGui.QApplication.translate("Form", "Ingresar marca ", None, QtGui.QApplication.UnicodeUTF8))

