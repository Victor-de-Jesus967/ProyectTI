"""
Este archivo sirve como punto de entrada para la aplicación.
Ejecuta Main.py desde la carpeta src/
"""
import sys
import os
from pathlib import Path

# Agregar carpeta src al path
sys.path.insert(0, str(Path(__file__).parent / "src"))
sys.path.insert(0, str(Path(__file__).parent / "config"))

# Importar y ejecutar Main
if __name__ == "__main__":
    from src.Main import LoginDialog, iniciar_interfaz_principal, inicializar_base_datos
    from PyQt5 import QtWidgets
    
    app = QtWidgets.QApplication(sys.argv)
    
    # Inicializa la base de datos antes de arrancar la interfaz
    inicializar_base_datos()
    
    # Crear y mostrar el login
    login = LoginDialog()
    if login.exec_() == QtWidgets.QDialog.Accepted:
        # Si el login es correcto, abrir la interfaz principal
        MainWindow, ui = iniciar_interfaz_principal()
        sys.exit(app.exec_())
    else:
        sys.exit(0)
