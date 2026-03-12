# Estructura del Proyecto

Este documento describe la organización de carpetas y archivos del proyecto.

## Descripción General

El proyecto está organizado siguiendo una estructura modular y profesional para mejor mantenimiento y escalabilidad.

## Directorio Raíz

```
ProyectTI_Original/
├── main.py                  # Script de entrada principal
├── requirements.txt         # Dependencias Python
├── .gitignore              # Configuración de Git
└── README.md               # Enlace al README en docs/
```

## Carpetas Principales

### `src/` - Código Fuente

Contiene toda la lógica de la aplicación Python.

```
src/
├── __init__.py             # Inicialización del paquete
├── Main.py                 # Punto de entrada de la aplicación
├── Login.py                # Interfaz de autenticación (Qt)
├── Interfaz.py             # Interfaz gráfica principal (Qt)
├── Acciones.py             # Lógica de negocio y operaciones de datos
├── Db_manager.py           # Gestor de base de datos SQLite
└── ActualizarBD.py         # Script para actualizar base de datos
```

**Cómo funciona:**
- `Main.py` es ejecutado por `main.py` en la raíz
- Los módulos importan entre sí (Login, Interfaz, Acciones, etc.)
- Todas las rutas se calculan relativamente desde el módulo

### `config/` - Configuración

Archivos de configuración y credenciales.

```
config/
├── __init__.py             # Inicialización del paquete
└── credentials.py          # ⚠️ NO se sube a Git - Credenciales locales
```

**Importante:**
- `credentials.py` está en `.gitignore` - cada usuario debe crear el suyo
- Contiene `USUARIO` y `CONTRASENA` para acceso a la aplicación

### `docs/` - Documentación

Documentación completa del proyecto.

```
docs/
├── README.md               # Guía principal (copiado aquí desde raíz)
├── PRESENTACION.md         # Presentación del proyecto (13 diapositivas)
├── DESPLIEGUE.md          # Guía de despliegue (5 opciones)
├── GITHUB.md              # Instrucciones para GitHub
├── CHECKLIST_TFM.md       # Checklist de requisitos del TFM
├── Requisitos.md          # Requisitos originales
├── Documentacion-TFM.pdf  # PDF con especificaciones
└── Encabezado.pdf         # Portada oficial
```

### `assets/` - Recursos

Archivos multimedia y recursos de la aplicación.

```
assets/
└── icono.ico              # Icono de la aplicación (ventana principal)
```

### `data/` - Datos

Base de datos y archivos de datos generados por la aplicación.

```
data/
├── equipo_computo.db      # ⚠️ Base de datos SQLite (generada automáticamente)
└── *.xlsx                 # ⚠️ Archivos Excel exportados (generados, NO se suben)
```

**Importante:**
- Se crea automáticamente al ejecutar la aplicación
- Los archivos `.db` y `.xlsx` están en `.gitignore`

### `build/` - Compilación

Archivos generados por herramientas de compilación.

```
build/
├── Main/                  # Archivos PyInstaller temp
├── warn-Main.txt         # Warnings de compilación
└── ... (archivos temporales)
```

## Archivos Especiales

### `.gitignore`

Define qué archivos NO se suben a Git:

```
# Base de datos (se generan localmente)
data/equipo_computo.db
*.db

# Credenciales (cada usuario tiene las suyas)
config/credentials.py

# Entorno virtual (cada usuario lo crea)
.venv/
venv/

# Otros archivos generados
__pycache__/
*.xlsx
build/
dist/
```

### `requirements.txt`

Dependencias Python necesarias:

```
PyQt5>=5.15.11
openpyxl>=3.1.5
pandas>=2.0.3
numpy>=1.24.4
reportlab>=4.2.5
PyPDF2>=3.0.1
Pillow>=10.4.0
```

## Flujo de Importaciones

### Ejecución

```
1. Ejecutar: python main.py (en raíz)
           ↓
2. main.py configura sys.path y ejecuta src/Main.py
           ↓
3. Main.py importa módulos desde src/
           ↓
4. Interfaz.py, Acciones.py, etc. se cargan
           ↓
5. Base de datos se inicializa en data/equipo_computo.db
```

### Rutas Relativas

Los módulos en `src/` usan rutas relativas calculadas con `Path`:

```python
# En src/Main.py
from pathlib import Path

# Ruta a assets/icono.ico
icon_path = Path(__file__).parent.parent / "assets" / "icono.ico"

# Ruta a config/credentials.py
sys.path.insert(0, str(Path(__file__).parent.parent / "config"))
from credentials import USUARIO, CONTRASENA

# Ruta a data/equipo_computo.db
DB_PATH = Path(__file__).parent.parent / "data" / "equipo_computo.db"
```

## Convenciones

- **Python files** (`*.py`): En `src/` y subdirectories
- **Configuration** (`*.py`): En `config/`
- **Documentation** (`*.md`, `*.pdf`): En `docs/`
- **Assets** (`*.ico`, `*.png`): En `assets/`
- **Data** (`*.db`, `*.xlsx`): En `data/`
- **Build outputs** (compilados): En `build/` y `dist/`

## Agregar Nuevos Módulos

Si necesitas agregar nuevo código:

1. **Código general**: Agregar archivo en `src/`
2. **Configuración**: Agregar archivo en `config/`
3. **Recursos**: Agregar archivo en `assets/`
4. **Documentación**: Agregar archivo en `docs/`

## Despliegue

Cuando se compila a ejecutable (`.exe`), la estructura se mantiene:

```bash
python -m PyInstaller --onefile --windowed main.py
# Genera: dist/main.exe
```

El ejecutable empaqueta todo y mantiene las rutas relativas.

## Ventajas de esta Estructura

✅ **Modular**: Fácil de mantener y escalar
✅ **Profesional**: Sigue convenciones de proyectos grandes
✅ **Seguro**: Credenciales en `.gitignore`
✅ **Organizado**: Cada tipo de archivo en su lugar
✅ **Portable**: Funciona en cualquier ruta
✅ **Documentado**: Código y docs claramente separados

---

**Última actualización**: 12 de marzo de 2026
