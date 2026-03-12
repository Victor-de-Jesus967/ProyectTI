import sqlite3
import os
from pathlib import Path
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox, QTableWidget

# Ruta de la base de datos
DB_PATH = os.path.join(Path(__file__).parent.parent, "data", "equipo_computo.db")

# Clase CustomProxyModel separada
class CustomProxyModel(QtCore.QSortFilterProxyModel):
    def filterAcceptsRow(self, source_row, source_parent):
        model = self.sourceModel()

        # Verifica si hay datos en alguna columna de la fila
        row_has_data = False
        for column in range(model.columnCount()):
            index = model.index(source_row, column, source_parent)
            data = model.data(index)
            if data and str(data).strip():  # Verifica si hay datos y no está vacío
                row_has_data = True
                break

        return row_has_data
class Acciones:
    def __init__(self):
        # Inicializar la conexión a la base de datos al crear la instancia de Acciones
        self.db_manager = sqlite3.connect(DB_PATH)

    def filterAcceptsRow(self, source_row, source_parent):
        model = self.sourceModel()

        # Verifica si hay datos en alguna columna de la fila
        row_has_data = False
        for column in range(model.columnCount()):
            index = model.index(source_row, column, source_parent)
            data = model.data(index)
            if data and str(data).strip():  # Verifica si hay datos y no está vacío
                row_has_data = True
                break

        return row_has_data

    def obtener_archivos(self, carpeta_path):
        archivos = []
        for nombre_archivo in os.listdir(carpeta_path):
            ruta_archivo = os.path.join(carpeta_path, nombre_archivo)
            if os.path.isfile(ruta_archivo):  # Solo archivos
                extension = os.path.splitext(nombre_archivo)[1]
                tamaño = os.path.getsize(ruta_archivo)
                archivos.append({
                    "nombre": nombre_archivo,
                    "ruta": ruta_archivo,
                    "extension": extension,
                    "tamaño": tamaño
                })
        return archivos

    def mostrar_archivos_en_tabla(self, tableView, archivos):
        # Mostrar los archivos en la tabla
        model = QTableWidget()
        model.setHorizontalHeaderLabels(['Nombre de archivo'])

        for archivo in archivos:
            item = QtGui.QStandardItem(archivo)
            model.appendRow(item)

        tableView.setModel(model)

    def agregar_registro(self, datos):
        cursor = self.db_manager.cursor()
        query = '''INSERT INTO EquipoEntregadoAdquisicion 
                   (FechaEntrega, SerieCPU, Hostname, Organismo, Componente, PEMP, IPEquipo, SerieReplicador, SerieTeclado,
                    SerieMonitor, Ficha, NombreUsuario, Estatus, Ubicacion, Piso, AreaDepartamento, Subdireccion, ExtUsuario) 
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        cursor.execute(query, datos)
        self.db_manager.commit()
        print(f"Registro agregado: {datos}")

    def modificar_registro(self, id_registro, nuevos_datos):
        cursor = self.db_manager.cursor()
        query = '''UPDATE EquipoEntregadoAdquisicion SET 
                   FechaEntrega=?, SerieCPU=?, Hostname=?, Organismo=?, Componente=?, PEMP=?, IPEquipo=?, SerieReplicador=?, SerieTeclado=?, 
                   SerieMonitor=?, Ficha=?, NombreUsuario=?, Estatus=?, Ubicacion=?, Piso=?, AreaDepartamento=?, Subdireccion=?, ExtUsuario=? 
                   WHERE SerieCPU=?'''
        cursor.execute(query, nuevos_datos + (id_registro,))
        self.db_manager.commit()
        print(f"Registro con ID {id_registro} modificado")

    def eliminar_por_ficha(self, ficha):
        if not ficha:
            QMessageBox.warning(None, "Advertencia", "Por favor, ingrese un número de ficha.")
            return

        cursor = self.db_manager.cursor()

        try:
            # Ejecutar la eliminación
            cursor.execute("DELETE FROM EquipoEntregadoAdquisicion WHERE Ficha = ?", (ficha,))
            self.db_manager.commit()

            if cursor.rowcount > 0:
                QMessageBox.information(None, "Éxito", f"Se eliminó el registro con ficha {ficha}.")
            else:
                QMessageBox.warning(None, "Advertencia", f"No se encontró ningún registro con ficha {ficha}.")
        except sqlite3.Error as e:
            QMessageBox.critical(None, "Error", f"Error al eliminar el registro: {str(e)}")

    def buscar_registro(self, criterio_busqueda):
        cursor = self.db_manager.cursor()
        query = 'SELECT * FROM EquipoEntregadoAdquisicion WHERE Ficha=? OR NombreUsuario=? OR SerieCPU=?'
        cursor.execute(query, (criterio_busqueda, criterio_busqueda, criterio_busqueda))
        resultado = cursor.fetchall()
        return resultado

    def buscar_(self, criterio_busqueda):
        cursor = self.db_manager.cursor()
        query = 'SELECT * FROM EquipoEntregadoAdquisicion WHERE Ficha=? OR NombreUsuario=?'
        cursor.execute(query, (criterio_busqueda, criterio_busqueda))
        resultado = cursor.fetchall()
        return resultado

    def guardar_archivos(self, archivos):
        try:
            cursor = self.db_manager.cursor()

            # Limpiar la tabla de archivos guardados antes de insertar nuevos
            cursor.execute("DELETE FROM ArchivosGuardados")
            #print("Archivos anteriores eliminados")

            for archivo in archivos:
                cursor.execute(
                    "INSERT INTO ArchivosGuardados (nombre, ruta, extension, tamaño) VALUES (?, ?, ?, ?)",
                    (archivo["nombre"], archivo["ruta"], archivo["extension"], archivo["tamaño"])
                )

            self.db_manager.commit()
            print("Archivos guardados correctamente")
        except Exception as e:
            print(f"Error al guardar archivos: {e}")

    def obtener_archivos_guardados(self):
        try:
            cursor = self.db_manager.cursor()
            cursor.execute("SELECT nombre, ruta, extension, tamaño FROM ArchivosGuardados")
            archivos = [{"nombre": row[0], "ruta": row[1], "extension": row[2], "tamaño": row[3]} for row in cursor.fetchall()]
            print(f"Archivos guardados recuperados: {archivos}")
            return archivos
        except Exception as e:
            print(f"Error al recuperar archivos guardados: {e}")
            return []

    def cargar_datos_en_tabla_EquipoEntregadoAdquisicion(self, tabla_widget, datos=None):
        cursor = self.db_manager.cursor()

        if datos is None:
            cursor.execute('''  
                SELECT FechaEntrega, Ficha, SerieCPU, Hostname, Organismo,   
                       Componente, PEMP, IPEquipo, SerieReplicador, SerieTeclado,   
                       SerieMonitor, NombreUsuario, Estatus, Ubicacion, Piso,   
                       AreaDepartamento, Subdireccion, ExtUsuario   
                FROM EquipoEntregadoAdquisicion
                ORDER BY FechaEntrega ASC  -- Orden ascendente por fecha            ''')
            datos = cursor.fetchall()

            # Crear el modelo base
        base_model = QtGui.QStandardItemModel()
        headers = [
            "FechaEntrega", "Ficha", "SerieCPU", "Hostname", "Organismo",
            "Componente", "PEMP", "IPEquipo", "SerieReplicador", "SerieTeclado",
            "SerieMonitor", "NombreUsuario", "Estatus", "Ubicacion", "Piso",
            "AreaDepartamento", "Subdireccion", "ExtUsuario"
        ]
        base_model.setHorizontalHeaderLabels(headers)

        for fila in datos:
            items = [QtGui.QStandardItem(str(campo)) for campo in fila]
            base_model.appendRow(items)

            # Crear y configurar el proxy model
        proxy_model = CustomProxyModel()
        proxy_model.setSourceModel(base_model)

        # Aplicar el modelo a la tabla
        tabla_widget.setModel(proxy_model)
        tabla_widget.resizeColumnsToContents()

    def cargar_datos_en_tabla_ArrendadoRetirar(self, tabla_widget, datos=None):
        cursor = self.db_manager.cursor()

        if datos is None:
            cursor.execute('SELECT * FROM ArrendadoRetirar')
            datos = cursor.fetchall()

            # Crear el modelo base
        base_model = QtGui.QStandardItemModel()
        headers = [
            'CentroTrabajo', 'SerieCPU', 'Marca', 'Modelo', 'SerieMonitor',
            'SerieMonitorAdicional', 'SerieReplicador', 'Contrato', 'FolioRemedyRetiro',
            'TasRemedy', 'MACPC_LAPTOP', 'MacReplicador', 'MACWIFI', 'Hostname'
        ]
        base_model.setHorizontalHeaderLabels(headers)

        for fila in datos:
            items = [QtGui.QStandardItem(str(campo)) for campo in fila]
            base_model.appendRow(items)

            # Crear y configurar el proxy model
        proxy_model = CustomProxyModel()
        proxy_model.setSourceModel(base_model)

        # Aplicar el modelo a la tabla
        tabla_widget.setModel(proxy_model)
        tabla_widget.resizeColumnsToContents()

    def cargar_datos_en_tabla_EquipoNuevo(self, tabla_widget, datos=None):
        cursor = self.db_manager.cursor()

        if datos is None:
            cursor.execute('SELECT * FROM EquipoNuevo')
            datos = cursor.fetchall()

            # Crear el modelo base
        base_model = QtGui.QStandardItemModel()
        headers = [
            'ModeloImpresora', 'IPImpresora', 'MACPC_LAPTOP', 'MacReplicador', 'MACWifi',
            'FichaJefe', 'NombreJefe', 'EXTJefe'
        ]
        base_model.setHorizontalHeaderLabels(headers)

        for fila in datos:
            items = [QtGui.QStandardItem(str(campo)) for campo in fila]
            base_model.appendRow(items)

            # Crear y configurar el proxy model
        proxy_model = CustomProxyModel()
        proxy_model.setSourceModel(base_model)

        # Aplicar el modelo a la tabla
        tabla_widget.setModel(proxy_model)
        tabla_widget.resizeColumnsToContents()

    def cargar_datos_en_tabla_RetiroEquipo(self, tabla_widget, datos=None):
        cursor = self.db_manager.cursor()

        if datos is None:
            cursor.execute('SELECT * FROM RetiroEquipo')
            datos = cursor.fetchall()

            # Crear el modelo base
        base_model = QtGui.QStandardItemModel()
        headers = [
            'EstatusRetiro', 'ObservacionesRetiro', 'RetiroFisico', 'EstatusWoo', 'TasRemedy'
        ]
        base_model.setHorizontalHeaderLabels(headers)

        for fila in datos:
            items = [QtGui.QStandardItem(str(campo)) for campo in fila]
            base_model.appendRow(items)

            # Crear y configurar el proxy model
        proxy_model = CustomProxyModel()
        proxy_model.setSourceModel(base_model)

        # Aplicar el modelo a la tabla
        tabla_widget.setModel(proxy_model)
        tabla_widget.resizeColumnsToContents()

    def cargar_datos_en_tabla_EquiposReasignados(self, tabla_widget, datos=None):
        cursor = self.db_manager.cursor()

        if datos is None:
            cursor.execute('SELECT * FROM EquiposReasignados')
            datos = cursor.fetchall()

            # Crear el modelo base
        base_model = QtGui.QStandardItemModel()
        headers = [
            'CorreoUsuarioQueRecibio', 'SID', 'Si_No', 'Ficha', 'Nombre', 'ComentariosEnlace'
        ]
        base_model.setHorizontalHeaderLabels(headers)

        for fila in datos:
            items = [QtGui.QStandardItem(str(campo)) for campo in fila]
            base_model.appendRow(items)

            # Crear y configurar el proxy model
        proxy_model = CustomProxyModel()
        proxy_model.setSourceModel(base_model)

        # Aplicar el modelo a la tabla
        tabla_widget.setModel(proxy_model)
        tabla_widget.resizeColumnsToContents()

    def cargar_datos_por_tabla_comboBox(self, tabla_nombre):
        cursor = self.db_manager.cursor()
        try:
            query = f'SELECT * FROM {tabla_nombre}'
            cursor.execute(query)
            datos = cursor.fetchall()
            return datos
        except sqlite3.Error as e:
            print(f"Error al cargar datos de {tabla_nombre}: {e}")
            return []

    def buscar_registro(self, criterio_busqueda):
        cursor = self.db_manager.cursor()
        query = '''
            SELECT * FROM EquipoEntregadoAdquisicion 
            WHERE Ficha=? OR FechaEntrega=? OR SerieCPU=?
        '''
        cursor.execute(query, (criterio_busqueda, criterio_busqueda, criterio_busqueda))
        resultado = cursor.fetchall()
        return resultado  # Retorna todos los registros que coinciden con el criterio

    def buscar_registro1(self, criterio_busqueda):
        try:
            cursor = self.db_manager.cursor()
            query = 'SELECT * FROM ArchivosGuardados'
            cursor.execute(query)
            resultados = cursor.fetchall()

            print(f"Total de registros en la base de datos: {len(resultados)}")
            registros_filtrados = []

            for registro in resultados:
                nombre_archivo = registro[1]  # Índice 1 para 'nombre'
                print(f"\nAnalizando archivo: {nombre_archivo}")

                # Quitamos la extensión .pdf
                base_name = os.path.splitext(nombre_archivo)[0]

                # Separamos la fecha, ficha y número de serie correctamente
                fecha = base_name[:10]  # Los primeros 10 caracteres (YYYY-MM-DD)
                ficha = base_name[11:17]  # Los siguientes 6 caracteres después del primer guión
                numero_serie = base_name[18:]  # El resto después del segundo guión

                print(f"Fecha: {fecha}, Ficha: {ficha}, Serie: {numero_serie}")
                print(f"Comparando con criterio: '{criterio_busqueda}'")

                # Búsqueda más flexible
                if (criterio_busqueda in fecha or
                        criterio_busqueda in ficha or
                        criterio_busqueda in numero_serie or
                        criterio_busqueda in nombre_archivo):
                    print("¡Coincidencia encontrada!")
                    registros_filtrados.append({
                        'registro': registro,
                        'fecha': fecha,
                        'ficha': ficha,
                        'numero_serie': numero_serie
                    })

            cursor.close()

            print(f"Total de coincidencias encontradas: {len(registros_filtrados)}")
            return registros_filtrados

        except Exception as e:
            print(f"Error al buscar registros: {e}")
            print(f"Detalles del error: {str(e.__class__.__name__)}")
            import traceback
            print(traceback.format_exc())
            return []