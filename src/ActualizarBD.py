import sqlite3
import os
import pandas as pd
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QTimer, Qt
import time
from Db_manager import DB_PATH  # Agregar import para usar la ruta centralizada de la BD

class ActualizarBD:
    def __init__(self):
        self.Interfaz = None
        self.conn = sqlite3.connect(DB_PATH)  # Usar la ruta centralizada
        self.cursor = self.conn.cursor()
        self.progress_dialog = None
        self.current_progress = 0
        self.timer = None

    def iniciar_barra_progreso(self, mensaje):
        """Crea y muestra una barra de progreso animada"""
        self.progress_dialog = QtWidgets.QProgressDialog(
            mensaje,
            "Cancelar",
            0,
            100,
            None
        )
        self.progress_dialog.setWindowTitle("Procesando")
        self.progress_dialog.setWindowModality(QtCore.Qt.WindowModal)
        self.progress_dialog.setMinimumDuration(0)
        self.progress_dialog.setWindowFlags(
            self.progress_dialog.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint
        )
        # Estilo personalizado para la barra de progreso
        style = """  
        QProgressBar {  
            border: 2px solid grey;  
            border-radius: 5px;  
            text-align: center;  
            height: 25px;  
        }  
        QProgressBar::chunk {  
            background-color: #4CAF50;  
            width: 10px;  
            margin: 0.5px;  
        }  
        """
        self.progress_dialog.setStyleSheet(style)

        # Configurar el temporizador para la animación
        self.current_progress = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.actualizar_progreso)
        self.timer.start(50)  # Actualizar cada 50ms

        self.progress_dialog.show()
        QtWidgets.QApplication.processEvents()

    def actualizar_progreso(self):
        """Actualiza el valor de la barra de progreso"""
        if self.progress_dialog and self.progress_dialog.isVisible():
            self.current_progress += 1
            if self.current_progress > 100:
                self.current_progress = 0
            self.progress_dialog.setValue(self.current_progress)

    def finalizar_barra_progreso(self):
        """Finaliza la barra de progreso"""
        if self.timer:
            self.timer.stop()
        if self.progress_dialog:
            self.progress_dialog.setValue(100)
            self.progress_dialog.close()

    def cargar_datos_excelEquiposReasignados(self, ruta_excel, nombre_hoja, nombre_tabla, columnas_df, columnas_bd):
        if not os.path.exists(ruta_excel):
            print(f"Archivo no encontrado: {ruta_excel}")
            return

        try:
            self.iniciar_barra_progreso(f"Cargando datos de {nombre_hoja}...")

            # Simular proceso de carga con delay
            time.sleep(2)  # Tiempo para ver la animación

            # Leer la hoja específica del archivo Excel con verificación
            df = pd.read_excel(
                ruta_excel,
                sheet_name=nombre_hoja,
                usecols=columnas_df,
                skiprows=1,
                na_filter=True
            )

            # Verificar datos faltantes
            missing_data = df.isnull().sum()
            if missing_data.any():
                print(f"Advertencia: Datos faltantes en {nombre_hoja}:")
                print(missing_data[missing_data > 0])

                # Limpiar datos
            df = df.fillna('')
            df = df.replace({pd.NA: '', None: ''})

            # Renombrar columnas
            df.columns = columnas_bd

            # Limpieza de la tabla antes de insertar nuevos datos
            self.cursor.execute(f'DELETE FROM {nombre_tabla}')
            self.conn.commit()  # Confirmar la eliminación

            # Insertar datos
            datos = df.to_records(index=False).tolist()
            placeholders = ', '.join(['?' for _ in columnas_bd])
            consulta = f'INSERT INTO {nombre_tabla} ({", ".join(columnas_bd)}) VALUES ({placeholders})'

            self.cursor.executemany(consulta, datos)
            self.conn.commit()

            print(f"Datos insertados correctamente en {nombre_tabla}. Registros: {len(datos)}")

            self.finalizar_barra_progreso()

        except Exception as e:
            print(f"Error en {nombre_tabla}: {str(e)}")
            self.conn.rollback()
            self.finalizar_barra_progreso()
            raise

    def cargar_datos_excelEstatusRetiro(self, ruta_excel, nombre_hoja, nombre_tabla, columnas_df, columnas_bd):
        if not os.path.exists(ruta_excel):
            print(f"Archivo no encontrado: {ruta_excel}")
            return

        try:
            self.iniciar_barra_progreso(f"Cargando datos de {nombre_hoja}...")

            # Simular proceso de carga con delay
            time.sleep(2)  # Tiempo para ver la animación

            # Leer la hoja específica del archivo Excel con verificación
            df = pd.read_excel(
                ruta_excel,
                sheet_name=nombre_hoja,
                usecols=columnas_df,
                skiprows=1,
                na_filter=True
            )

            # Verificar datos faltantes
            missing_data = df.isnull().sum()
            if missing_data.any():
                print(f"Advertencia: Datos faltantes en {nombre_hoja}:")
                print(missing_data[missing_data > 0])

                # Limpiar datos
            df = df.fillna('')
            df = df.replace({pd.NA: '', None: ''})

            # Renombrar columnas
            df.columns = columnas_bd

            # Limpieza de la tabla antes de insertar nuevos datos
            self.cursor.execute(f'DELETE FROM {nombre_tabla}')
            self.conn.commit()  # Confirmar la eliminación

            # Insertar datos
            datos = df.to_records(index=False).tolist()
            placeholders = ', '.join(['?' for _ in columnas_bd])
            consulta = f'INSERT INTO {nombre_tabla} ({", ".join(columnas_bd)}) VALUES ({placeholders})'

            self.cursor.executemany(consulta, datos)
            self.conn.commit()

            print(f"Datos insertados correctamente en {nombre_tabla}. Registros: {len(datos)}")

            self.finalizar_barra_progreso()

        except Exception as e:
            print(f"Error en {nombre_tabla}: {str(e)}")
            self.conn.rollback()
            self.finalizar_barra_progreso()
            raise

    def cargar_datos_excelEquipoNuevo(self, ruta_excel, nombre_hoja, nombre_tabla, columnas_df, columnas_bd):
        if not os.path.exists(ruta_excel):
            print(f"Archivo no encontrado: {ruta_excel}")
            return

        try:
            self.iniciar_barra_progreso(f"Cargando datos de {nombre_hoja}...")

            # Simular proceso de carga con delay
            time.sleep(2)  # Tiempo para ver la animación

            # Leer la hoja específica del archivo Excel con verificación
            df = pd.read_excel(
                ruta_excel,
                sheet_name=nombre_hoja,
                usecols=columnas_df,
                skiprows=1,
                na_filter=True
            )

            # Verificar datos faltantes
            missing_data = df.isnull().sum()
            if missing_data.any():
                print(f"Advertencia: Datos faltantes en {nombre_hoja}:")
                print(missing_data[missing_data > 0])

                # Limpiar datos
            df = df.fillna('')
            df = df.replace({pd.NA: '', None: ''})

            # Renombrar columnas
            df.columns = columnas_bd

            # Limpieza de la tabla antes de insertar nuevos datos
            self.cursor.execute(f'DELETE FROM {nombre_tabla}')
            self.conn.commit()  # Confirmar la eliminación

            # Insertar datos
            datos = df.to_records(index=False).tolist()
            placeholders = ', '.join(['?' for _ in columnas_bd])
            consulta = f'INSERT INTO {nombre_tabla} ({", ".join(columnas_bd)}) VALUES ({placeholders})'

            self.cursor.executemany(consulta, datos)
            self.conn.commit()

            print(f"Datos insertados correctamente en {nombre_tabla}. Registros: {len(datos)}")

            self.finalizar_barra_progreso()

        except Exception as e:
            print(f"Error en {nombre_tabla}: {str(e)}")
            self.conn.rollback()
            self.finalizar_barra_progreso()
            raise

    def cargar_datos_excelArrendadoRetirar(self, ruta_excel, nombre_hoja, nombre_tabla, columnas_df, columnas_bd):
        if not os.path.exists(ruta_excel):
            print(f"Archivo no encontrado: {ruta_excel}")
            return

        try:
            self.iniciar_barra_progreso(f"Cargando datos de {nombre_hoja}...")

            # Simular proceso de carga con delay
            time.sleep(2)  # Tiempo para ver la animación

            # Leer la hoja específica del archivo Excel con verificación
            df = pd.read_excel(
                ruta_excel,
                sheet_name=nombre_hoja,
                usecols=columnas_df,
                skiprows=1,
                na_filter=True
            )

            # Verificar datos faltantes
            missing_data = df.isnull().sum()
            if missing_data.any():
                print(f"Advertencia: Datos faltantes en {nombre_hoja}:")
                print(missing_data[missing_data > 0])

                # Limpiar datos
            df = df.fillna('')
            df = df.replace({pd.NA: '', None: ''})

            # Renombrar columnas
            df.columns = columnas_bd

            # Limpieza de la tabla antes de insertar nuevos datos
            self.cursor.execute(f'DELETE FROM {nombre_tabla}')
            self.conn.commit()  # Confirmar la eliminación

            # Insertar datos
            datos = df.to_records(index=False).tolist()
            placeholders = ', '.join(['?' for _ in columnas_bd])
            consulta = f'INSERT INTO {nombre_tabla} ({", ".join(columnas_bd)}) VALUES ({placeholders})'

            self.cursor.executemany(consulta, datos)
            self.conn.commit()

            print(f"Datos insertados correctamente en {nombre_tabla}. Registros: {len(datos)}")

            self.finalizar_barra_progreso()

        except Exception as e:
            print(f"Error en {nombre_tabla}: {str(e)}")
            self.conn.rollback()
            self.finalizar_barra_progreso()
            raise
    def cargar_datos_excelEquipoEntregadoAdquisicion(self, ruta_excel, nombre_hoja, nombre_tabla, columnas_df, columnas_bd):
        if not os.path.exists(ruta_excel):
            print(f"Archivo no encontrado: {ruta_excel}")
            return

        try:
            self.iniciar_barra_progreso(f"Cargando datos de {nombre_hoja}...")

            # Simular proceso de carga con delay
            time.sleep(2)  # Tiempo para ver la animación

            # Leer la hoja específica del archivo Excel con verificación
            df = pd.read_excel(
                ruta_excel,
                sheet_name=nombre_hoja,
                usecols=columnas_df,
                skiprows=1,
                na_filter=True
            )

            # Verificar datos faltantes
            missing_data = df.isnull().sum()
            if missing_data.any():
                print(f"Advertencia: Datos faltantes en {nombre_hoja}:")
                print(missing_data[missing_data > 0])

                # Limpiar datos
            df = df.fillna('')
            df = df.replace({pd.NA: '', None: ''})

            # Limpieza de la tabla antes de insertar nuevos datos
            self.cursor.execute(f'DELETE FROM {nombre_tabla}')
            self.conn.commit()  # Confirmar la eliminación

            # Renombrar columnas
            df.columns = columnas_bd

            # Procesamiento específico por tipo de datos
            if 'FechaEntrega' in df.columns:
                df['FechaEntrega'] = pd.to_datetime(
                    df['FechaEntrega'],
                    errors='coerce'
                ).dt.strftime('%Y-%m-%d')
                df = df.dropna(subset=['FechaEntrega'])

            if 'Ficha' in df.columns:
                # Detectar valores no numéricos en la columna Ficha
                non_numeric_ficha = df[~df['Ficha'].apply(lambda x: str(x).strip().isdigit())]
                if not non_numeric_ficha.empty:
                    print("Advertencia: Se encontraron valores no numéricos en la columna Ficha:")
                    print(non_numeric_ficha)

                    # Convertir la columna Ficha a numérica, reemplazar valores no válidos por NaN, y luego por 0
                df['Ficha'] = pd.to_numeric(
                    df['Ficha'],
                    errors='coerce'  # Convierte valores no numéricos a NaN
                ).fillna(0).astype(int)

            # Limpiar datos duplicados
            #df = df.drop_duplicates(subset=['Ficha'])

            # Insertar datos
            datos = df.to_records(index=False).tolist()
            placeholders = ', '.join(['?' for _ in columnas_bd])
            consulta = f'INSERT INTO {nombre_tabla} ({", ".join(columnas_bd)}) VALUES ({placeholders})'
            self.cursor.executemany(consulta, datos)
            self.conn.commit()

            print(f"Datos insertados correctamente en {nombre_tabla}. Registros: {len(datos)}")

            self.finalizar_barra_progreso()

        except Exception as e:
            print(f"Error en {nombre_tabla}: {str(e)}")
            self.conn.rollback()
            self.finalizar_barra_progreso()
            raise

    def actualizar_base_de_datos(self, archivo):
        try:
            # EquipoEntregadoAdquisicion
            self.cargar_datos_excelEquipoEntregadoAdquisicion(
                archivo,
                'EquipoEntregado',
                'EquipoEntregadoAdquisicion',
                [
                    'FECHA\nENTREGA', 'SERIE CPU', 'HOSTNAME', 'ORGANISMO', 'COMPONENTE', 'PEMP',
                    'IP EQUIPO', 'SERIE REPLICADOR', 'SERIE TECLADO', 'SERIE MONITOR', 'FICHA',
                    'NOMBRE DE USUARIO', 'ESTATUS', 'UBICACIÓN', 'PISO', 'AREA \\ DEPARTAMENTO',
                    'SUBDIRECCION', 'EXT. USUARIO'
                ],
                [
                    'FechaEntrega', 'SerieCPU', 'Hostname', 'Organismo', 'Componente', 'PEMP',
                    'IPEquipo', 'SerieReplicador', 'SerieTeclado', 'SerieMonitor', 'Ficha',
                    'NombreUsuario', 'Estatus', 'Ubicacion', 'Piso', 'AreaDepartamento',
                    'Subdireccion', 'ExtUsuario'
                ]
            )

            # ArrendadoRetirar
            self.cargar_datos_excelArrendadoRetirar(
                archivo,
                'ArrendadoRetirar',
                'ArrendadoRetirar',
                [
                    'CENTRO DE TRABAJO', 'SERIE CPU', 'MARCA', 'MODELO', 'SERIE MONITOR',
                    'SERIE MONITOR ADICIONAL', 'SERIE REPLICADOR', 'CONTRATO',
                    'FOLIO REMEDY DE RETIRO', 'TAS REMEDY', 'MAC PC / LAP', 'MAC REPLICADOR',
                    'MAC WIFI', 'HOSTNAME'
                ],
                [
                    'CentroTrabajo', 'SerieCPU', 'Marca', 'Modelo', 'SerieMonitor',
                    'SerieMonitorAdicional', 'SerieReplicador', 'Contrato', 'FolioRemedyRetiro',
                    'TasRemedy', 'MACPC_LAPTOP', 'MacReplicador', 'MACWIFI', 'Hostname'
                ]
            )

            # EquipoNuevo
            self.cargar_datos_excelEquipoNuevo(
                archivo,
                'EquipoNuevo',
                'EquipoNuevo',
                [
                    'MODELO IMPRESORA', 'IP IMPRESORA', 'MAC PC/LAPTOP', 'MAC REPLICADOR',
                    'MAC WIFI', 'FICHA DE JEFE', 'NOMBRE DE JEFE', 'EXT JEFE'
                ],
                [
                    'ModeloImpresora', 'IPImpresora', 'MACPC_LAPTOP', 'MacReplicador',
                    'MACWifi', 'FichaJefe', 'NombreJefe', 'EXTJefe'
                ]
            )

            # EquiposReasignados
            self.cargar_datos_excelEquiposReasignados(
                archivo,
                'EquiposReasignados',
                'EquiposReasignados',
                [
                    'CORREO DEL USUARIO/QUERICIBIO', 'SID', 'SI/NO', 'FICHA', 'NOMBRE',
                    'COMENTARIOS DEL ENLACE'
                ],
                [
                    'CorreoUsuarioQueRecibio', 'SID', 'Si_No', 'Ficha', 'Nombre',
                    'ComentariosEnlace'
                ]
            )

            # RetiroEquipo
            self.cargar_datos_excelEstatusRetiro(
                archivo,
                'RetiroEquipo',
                'RetiroEquipo',
                [
                    'ESTATUS RETIRO', 'OBSERVACIONES RETIRO', 'RETIRO FISICO', 'ESTATUS WOO', 'ESTATUS TAS'


                ],
                [
                    'EstatusRetiro', 'ObservacionesRetiro', 'RetiroFisico', 'EstatusWoo', 'EstatusTas'
                ]
            )

            # Cerrar el diálogo de progreso
            if self.progress_dialog:
                self.progress_dialog.close()
                self.actualizar_interfaz_principal()

                # Mostrar mensaje de éxito
            QtWidgets.QMessageBox.information(
                None,
                "Actualización Completada",
                "Se actualizó la base de datos correctamente"

            )

            # Actualizar la tabla en la interfaz principal
            self.actualizar_interfaz_principal()

        except Exception as e:
            if self.progress_dialog:
                self.progress_dialog.close()
            QtWidgets.QMessageBox.critical(
                None,
                "Error",
                f"Error durante la actualización: {str(e)}"
            )

    def actualizar_interfaz_principal(self):
        """Actualiza la tabla en la interfaz principal"""
        try:
            # Buscar la ventana principal
            for widget in QtWidgets.QApplication.topLevelWidgets():
                if isinstance(widget, QtWidgets.QMainWindow):
                    main_window = widget
                    break

                    # Actualizar la tabla
            if hasattr(main_window, 'ui'):
                if hasattr(main_window.ui, 'tabla_EquipoEntregadoAdquisicion'):
                    main_window.ui.cargar_datos_en_tabla_EquipoEntregadoAdquisicion(
                        main_window.ui.tabla_EquipoEntregadoAdquisicion
                    )
        except Exception as e:
            print(f"Error al actualizar la interfaz: {str(e)}")

    def cargar_archivo_excel(self):
        options = QtWidgets.QFileDialog.Options()
        archivo, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "Seleccionar Archivo Excel",
            "",
            "Archivos Excel (*.xlsx);;Todos los Archivos (*)",
            options=options
        )

        if archivo:
            self.actualizar_base_de_datos(archivo)

    def cerrar_conexion(self):
        if self.conn:
            self.conn.close()

    def __del__(self):
        self.cerrar_conexion()