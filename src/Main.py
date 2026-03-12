import sys
import os
from pathlib import Path

from config.credentials import CONTRASENA, USUARIO

# Agregar directorio padre al path para importar módulos
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent.parent / "config"))

from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets
import Interfaz
from Acciones import Acciones
from Db_manager import crear_base_datos
from Login import Ui_Dialog

# Función para inicializar la base de datos
def inicializar_base_datos():
    crear_base_datos()

# Clase para manejar el login
class LoginDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        # Ruta al icono en la carpeta assets
        icon_path = os.path.join(Path(__file__).parent.parent, "assets", "icono.ico")
        self.setWindowIcon(QIcon(icon_path))
        self.setupUi(self)  # Configurar la UI del login
        # Conectar el botón 'Entrar' a la función de validación
        self.Bentrar.clicked.connect(self.validar_usuario)
        # Conectar el botón 'Salir' a la función de cerrar
        self.Bsalir.clicked.connect(self.close)

    def validar_usuario(self):
        # Validación de usuario usando credenciales del archivo de configuración
        usuario = self.Lusuario.text()
        contrasena = self.Lcontra.text()
        if usuario == USUARIO and contrasena == CONTRASENA:
            self.accept()  # Cierra el diálogo y permite abrir la interfaz principal
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos")


# Función para iniciar la interfaz principal
def iniciar_interfaz_principal():
    MainWindow = QtWidgets.QMainWindow()
    ui = Interfaz.Ui_MainWindow()
    ui.setupUi(MainWindow)
    # Cargar los datos en la tabla
    ui.acciones = Acciones()
    ui.acciones.cargar_datos_en_tabla_EquipoEntregadoAdquisicion(ui.Tabla)
    MainWindow.show()
    return MainWindow, ui

# Función principal
if __name__ == "__main__":
    # Inicializa la base de datos antes de arrancar la interfaz
    inicializar_base_datos()
    # Iniciar la aplicación
    app = QtWidgets.QApplication(sys.argv)
    # Crear el diálogo de login
    login = LoginDialog()
    # Si el login es exitoso, mostramos la interfaz principal
    if login.exec_() == QtWidgets.QDialog.Accepted:
        main_window, ui = iniciar_interfaz_principal()
        sys.exit(app.exec_())
    else:
        sys.exit(0)  # Cierra la aplicación si no pasa el login
