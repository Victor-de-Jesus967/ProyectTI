# Guía de Despliegue

## Opciones de Despliegue

Este proyecto puede ser desplegado de múltiples formas según tus necesidades.

---

## Opción 1: Aplicación de Escritorio (Recomendado)

### Despliegue Local con Python

**Requisitos:**
- Python 3.7+
- pip

**Instalación para usuarios finales:**

```bash
# 1. Descargar el proyecto
git clone https://github.com/usuario/ProyectTI_Original.git
cd ProyectTI_Original

# 2. Crear entorno virtual
python -m venv venv
source venv/bin/activate  # macOS/Linux
# o
venv\Scripts\activate  # Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar
python Main.py
```

### Despliegue como Ejecutable (.exe)

**Ventajas:**
- No requiere Python instalado
- Distribución simple
- Interfaz nativa del SO

**Pasos:**

```bash
# 1. Instalar PyInstaller
pip install pyinstaller

# 2. Crear ejecutable
pyinstaller --onefile --windowed --icon=icono.ico --add-data "icono.ico;." Main.py

# 3. El ejecutable estará en dist/
# Distribuir: dist/Main.exe
```

**Configuración avanzada de PyInstaller:**

```bash
# Para una aplicación más optimizada
pyinstaller ^
  --onefile ^
  --windowed ^
  --icon=icono.ico ^
  --add-data "icono.ico;." ^
  --hidden-import=PyQt5.sip ^
  --name "Sistema-Gestion-Equipos" ^
  Main.py
```

**Distribución:**
- Crear carpeta `Sistema-Gestion-Equipos/`
- Incluir:
  - `Sistema-Gestion-Equipos.exe` (ejecutable)
  - `README.txt` (instrucciones básicas)
  - `requirements.txt` (referencia)
  - `icono.ico` (si es necesario)

---

## Opción 2: Aplicación Portátil (USB)

Para transportar la aplicación en USB sin instalación:

**Estructura:**
```
USB:/
├── Sistema-Gestion/
│   ├── Main.exe
│   ├── runtime/
│   ├── equipo_computo.db (generada en primera ejecución)
│   └── README.txt
```

**Instrucciones para usuario:**
1. Conectar USB
2. Ejecutar `Main.exe`
3. La BD se crea automáticamente

**Ventaja:** Portabilidad máxima, sin instalación requerida

---

## Opción 3: Instalador MSI (Profesional)

Para crear un instalador Windows profesional:

```bash
# Instalar herramienta
pip install cx_Freeze

# Crear setup.py
# (Ver configuración abajo)

# Generar instalador
python setup.py bdist_msi
```

**setup.py de ejemplo:**

```python
from cx_Freeze import setup, Executable

setup(
    name="Sistema Gestión Equipos",
    version="1.0.0",
    description="Sistema de Gestión de Equipos de Cómputo",
    executables=[Executable("Main.py")],
    options={
        "bdist_msi": {
            "add_to_path": False,
            "all_users": True,
            "directory_table_base_folder": "ProgramFilesFolder",
        }
    }
)
```

---

## Opción 4: Base de Datos Remota (Escalable)

Para múltiples usuarios accediendo a un servidor central:

### Con PostgreSQL

```python
# Modificar Db_manager.py
import psycopg2

def conectar_db_remota():
    conn = psycopg2.connect(
        host="servidor.ejemplo.com",
        database="gestion_equipos",
        user="usuario",
        password="contraseña"
    )
    return conn
```

### Con MySQL

```python
import mysql.connector

def conectar_db_remota():
    conn = mysql.connector.connect(
        host="servidor.ejemplo.com",
        user="usuario",
        password="contraseña",
        database="gestion_equipos"
    )
    return conn
```

**Ventajas:**
- Datos centralizados
- Acceso multiusuario
- Backups automáticos
- Escalabilidad

**Requisitos:**
- Servidor de BD remota configurado
- Conexión de red estable
- Modificación del código de conexión

---

## Opción 5: Aplicación Web (Futuro)

Para acceso desde cualquier navegador:

### Con Flask

```python
from flask import Flask, render_template
import Db_manager
import Acciones

app = Flask(__name__)

@app.route('/')
def inicio():
    equipos = Acciones().cargar_datos()
    return render_template('index.html', equipos=equipos)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
```

**Ventajas:**
- Acceso remoto
- No requiere instalación cliente
- Interfaz web responsive
- Multiplataforma

**Requisitos:**
- Servidor web (Linux recomendado)
- Framework web (Flask, Django)
- HTML/CSS/JavaScript para interfaz

---

## Monitoreo y Mantenimiento

### Backups Regular

```bash
# Script de backup automático
@echo off
set fecha=%date:/=-%
copy equipo_computo.db backups\backup_%fecha%.db
echo Backup realizado: %fecha%
```

### Logs

```python
import logging

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Aplicación iniciada")
```

### Monitoreo de Performance

```python
import time

def medir_tiempo_consulta(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        duracion = time.time() - inicio
        print(f"Consulta tardó: {duracion:.2f}s")
        return resultado
    return wrapper
```

---

## Problemas Comunes y Soluciones

### Problema: "No se encuentra módulo PyQt5"

**Solución:**
```bash
# Reinstalar dependencias
pip install -r requirements.txt
```

### Problema: Base de datos corrupta

**Solución:**
```bash
# Restaurar desde backup
copy backups\backup_anterior.db equipo_computo.db

# O recrear BD
del equipo_computo.db
python -c "from Db_manager import crear_base_datos; crear_base_datos()"
```

### Problema: Aplicación lenta

**Solución:**
```python
# Agregar índices a BD
CREATE INDEX idx_hostname ON EquipoEntregadoAdquisicion(Hostname);
CREATE INDEX idx_serie_cpu ON EquipoEntregadoAdquisicion(SerieCPU);
```

---

## Checklist de Despliegue

Antes de desplegar, verificar:

- ✅ Todas las dependencias en `requirements.txt`
- ✅ Credenciales NO incluidas en el código
- ✅ Base de datos inicializa automáticamente
- ✅ Archivos de configuración están presentes
- ✅ Icono y recursos están incluidos
- ✅ README actualizado con instrucciones
- ✅ Tested en máquina limpia
- ✅ Backups automáticos funcionales
- ✅ Documentación de administrador incluida
- ✅ Versión documentada en requirements.txt

---

## Requisitos Mínimos del Sistema

| Componente | Mínimo | Recomendado |
|-----------|---------|------------|
| RAM | 2 GB | 4 GB |
| Espacio disco | 500 MB | 1 GB |
| Procesador | Dual Core | Quad Core |
| SO | Windows 7 | Windows 10+ |
| Python | 3.7 | 3.10+ |

---

## Recursos Útiles

- [PyInstaller Docs](https://pyinstaller.readthedocs.io/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [PostgreSQL Setup](https://www.postgresql.org/docs/)
- [Git Best Practices](https://git-scm.com/doc)

---

**Última actualización**: Marzo 2026
