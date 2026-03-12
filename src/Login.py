from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(374, 223)

        # Crear un layout vertical principal
        self.mainLayout = QtWidgets.QVBoxLayout(Dialog)

        # Etiqueta del título
        self.label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Sitka Subheading Semibold")
        font.setPointSize(14)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.mainLayout.addWidget(self.label_3)

        # Crear un layout de formulario para usuario y contraseña
        self.formLayout = QtWidgets.QFormLayout()

        # Campo Usuario
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Lusuario = QtWidgets.QLineEdit(Dialog)
        self.Lusuario.setObjectName("Lusuario")
        self.formLayout.addRow(self.label, self.Lusuario)

        # Campo Contraseña
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Lcontra = QtWidgets.QLineEdit(Dialog)
        self.Lcontra.setObjectName("Lcontra")
        self.Lcontra.setEchoMode(QtWidgets.QLineEdit.Password)
        self.formLayout.addRow(self.label_2, self.Lcontra)

        # Añadir el layout de formulario al layout principal
        self.mainLayout.addLayout(self.formLayout)

        # Crear un layout horizontal para los botones
        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.Bentrar = QtWidgets.QPushButton(Dialog)
        self.Bentrar.setObjectName("Bentrar")
        self.buttonLayout.addWidget(self.Bentrar)
        self.Bsalir = QtWidgets.QPushButton(Dialog)
        self.Bsalir.setObjectName("Bsalir")
        self.buttonLayout.addWidget(self.Bsalir)

        # Añadir el layout de botones al layout principal
        self.mainLayout.addLayout(self.buttonLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Control de Acceso"))
        self.label.setText(_translate("Dialog", "Usuario:"))
        self.label_2.setText(_translate("Dialog", "Contraseña:"))
        self.Bentrar.setText(_translate("Dialog", "Entrar"))
        self.Bsalir.setText(_translate("Dialog", "Salir"))
        self.label_3.setText(_translate("Dialog", "Login"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
