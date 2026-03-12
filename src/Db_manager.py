import sqlite3
import os
from pathlib import Path

# Ruta de la base de datos
DB_PATH = os.path.join(Path(__file__).parent.parent, "data", "equipo_computo.db")

def crear_base_datos():
    # Crear carpeta data si no existe
    os.makedirs(Path(DB_PATH).parent, exist_ok=True)
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''  
        CREATE TABLE IF NOT EXISTS EquipoEntregadoAdquisicion (  
            FechaEntrega TEXT,   
            SerieCPU TEXT,   
            Hostname TEXT,   
            Organismo TEXT,   
            Componente TEXT,   
            PEMP TEXT,  
            IPEquipo TEXT,   
            SerieReplicador TEXT,   
            SerieTeclado TEXT,   
            SerieMonitor TEXT,   
            Ficha TEXT,  
            NombreUsuario TEXT,   
            Estatus TEXT,   
            Ubicacion TEXT,   
            Piso TEXT,   
            AreaDepartamento TEXT,  
            Subdireccion TEXT,   
            ExtUsuario TEXT
        )  
    ''')

    cursor.execute('''  
        CREATE TABLE IF NOT EXISTS ArrendadoRetirar (  
            CentroTrabajo TEXT,  
            SerieCPU TEXT, 
            Marca TEXT,   
            Modelo TEXT,   
            SerieMonitor TEXT,   
            SerieMonitorAdicional TEXT,  
            SerieReplicador TEXT,   
            Contrato TEXT,   
            FolioRemedyRetiro TEXT,  
            TasRemedy TEXT,   
            MACPC_LAPTOP TEXT,   
            MACReplicador TEXT,   
            MACWIFI TEXT,   
            Hostname TEXT  
        )  
    ''')

    cursor.execute('''  
        CREATE TABLE IF NOT EXISTS EquipoNuevo (  
            ModeloImpresora TEXT,  
            IPImpresora TEXT,   
            MACPC_LAPTOP TEXT, 
            MacReplicador TEXT,   
            MACWifi TEXT,   
            FichaJefe INTEGER,   
            NombreJefe TEXT,   
            EXTJefe TEXT  
        )  
    ''')

    cursor.execute('''  
        CREATE TABLE IF NOT EXISTS EquiposReasignados (  
            CorreoUsuarioQueRecibio TEXT,  
            SID TEXT,   
            Si_No TEXT,   
            Ficha INTEGER,   
            Nombre TEXT,   
            ComentariosEnlace TEXT  
        )  
    ''')

    cursor.execute('''  
        CREATE TABLE IF NOT EXISTS RetiroEquipo (  
            EstatusRetiro,  
            ObservacionesRetiro TEXT,  
            RetiroFisico TEXT,  
            EstatusWoo TEXT,  
            EstatusTas TEXT  
        )  
    ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS ArchivosGuardados (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                ruta TEXT,
                extension TEXT,
                tamaño INTEGER
        )''')

    conn.commit()
    conn.close()
    print("Base de datos y tablas creadas correctamente.")