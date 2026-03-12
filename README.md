# Sistema de Gestión de Equipos de Cómputo

Aplicación de escritorio para la gestión integral de equipos de cómputo, con capacidades de almacenamiento en base de datos, control de inventario y generación de reportes.

## Descripción General

Este proyecto es una solución desktop desarrollada en **Python** utilizando **PyQt5** como framework de interfaz gráfica. La aplicación permite gestionar un inventario completo de equipos informáticos, incluyendo datos de equipos entregados, equipos arrendados y componentes asociados. Proporciona funcionalidades de búsqueda, filtrado, importación/exportación de datos y generación de reportes en múltiples formatos.

## Stack Tecnológico

- **Lenguaje**: Python 3.x
- **Interfaz Gráfica**: PyQt5 (>=5.15.11)
- **Base de Datos**: SQLite
- **Procesamiento de Datos**: Pandas (>=2.0.3), NumPy (>=1.24.4)
- **Generación de Reportes**: ReportLab (>=4.2.5)
- **Manipulación de Excel**: OpenPyXL (>=3.1.5)
- **Procesamiento de PDF**: PyPDF2 (>=3.0.1)
- **Procesamiento de Imágenes**: Pillow (>=10.4.0)

## Estructura del Proyecto

```
ProyectTI_Original/
├── Main.py                 # Punto de entrada de la aplicación
├── Login.py               # Interfaz de autenticación
├── Interfaz.py            # Interfaz gráfica principal
├── Acciones.py            # Lógica de operaciones y datos
├── Db_manager.py          # Gestor de base de datos
├── ActualizarBD.py        # Actualización de base de datos
├── credentials.py         # Credenciales de acceso
├── requirements.txt       # Dependencias del proyecto
├── README.md              # Este archivo
└── build/                 # Carpeta de compilación (PyInstaller)
```

## Instalación

### Requisitos Previos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar o descargar el repositorio**
   ```bash
   cd ProyectTI_Original
   ```

2. **Crear un entorno virtual** (opcional pero recomendado)
   ```bash
   python -m venv .venv
   ```

3. **Activar el entorno virtual**
   - En Windows:
     ```bash
     .\.venv\Scripts\Activate.ps1
     ```
   - En macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Instalar las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución

Para ejecutar la aplicación:

```bash
python Main.py
```

La aplicación abrirá primero una ventana de login donde deberá ingresar las credenciales configuradas en `credentials.py`.

## Funcionalidades Principales

### 1. Sistema de Autenticación
- Login con usuario y contraseña
- Credenciales configurables
- Interfaz de acceso seguro

### 2. Gestión de Inventario
- Registro de equipos entregados en adquisición
- Registro de equipos arrendados para retirar
- Seguimiento de componentes (teclados, monitores, replicadores, etc.)

### 3. Base de Datos
- Almacenamiento en SQLite
- Tablas para diferentes categorías de equipos:
  - `EquipoEntregadoAdquisicion`: Equipos comprados
  - `ArrendadoRetirar`: Equipos en arrendamiento

### 4. Búsqueda y Filtrado
- Búsqueda avanzada de equipos
- Filtrado de datos por múltiples criterios
- Visualización en tablas interactivas

### 5. Generación de Reportes
- Exportación a Excel (formato .xlsx)
- Generación de reportes en PDF
- Fusión y manipulación de documentos PDF

### 6. Importación/Exportación
- Importación de datos desde archivos
- Exportación de inventario completo
- Soporte para múltiples formatos

## Configuración

### Credenciales
Las credenciales de acceso se configuran en el archivo `credentials.py`. Modifique los valores de `USUARIO` y `CONTRASENA` para cambiar las credenciales de acceso.

```python
# credentials.py
USUARIO = "su_usuario"
CONTRASENA = "su_contraseña"
```

## Estructura de la Base de Datos

### Tabla: EquipoEntregadoAdquisicion
Registra equipos comprados y sus componentes asociados:
- FechaEntrega, SerieCPU, Hostname, Organismo
- Componentes (teclado, monitor, replicador)
- Datos de usuario y ubicación
- Estado del equipo

### Tabla: ArrendadoRetirar
Registra equipos en arrendamiento:
- CentroTrabajo, SerieCPU, Marca, Modelo
- Información de contrato
- Datos de red (IP, MAC, WiFi)

## Dependencias

Ver `requirements.txt` para la lista completa de dependencias y versiones:

- **PyQt5**: Framework GUI
- **pandas**: Análisis y manipulación de datos
- **openpyxl**: Lectura/escritura de Excel
- **reportlab**: Generación de PDF
- **PyPDF2**: Manipulación PDF avanzada
- **Pillow**: Procesamiento de imágenes
- **numpy**: Operaciones numéricas

## Documentación Completa

Este proyecto incluye documentación detallada en los siguientes archivos:

- **[README.md](README.md)** - Guía principal del proyecto (este archivo)
- **[PRESENTACION.md](PRESENTACION.md)** - Presentación del proyecto con 13 diapositivas
- **[DESPLIEGUE.md](DESPLIEGUE.md)** - Guía completa de opciones de despliegue
- **[GITHUB.md](GITHUB.md)** - Instrucciones para crear repositorio en GitHub
- **[Requisitos.md](Requisitos.md)** - Requisitos del TFM según especificaciones

## Despliegue

### Generación de Ejecutable

El proyecto puede compilarse en un ejecutable standalone usando PyInstaller:

```bash
# Instalar PyInstaller si no está disponible
pip install pyinstaller

# Crear el ejecutable
pyinstaller --onefile --windowed --icon=icono.ico Main.py
```

El ejecutable se generará en la carpeta `dist/` con el nombre `Main.exe`.

**Requisitos del sistema para ejecutar:**
- Windows 7 o superior
- Mínimo 2GB de RAM
- Espacio en disco: ~500MB
- Permisos de lectura/escritura en el directorio de instalación

## Notas de Desarrollo

- La base de datos SQLite se crea automáticamente al ejecutar la aplicación
- Los archivos de datos se almacenan localmente en la máquina
- Se recomienda hacer backups periódicos de la base de datos `equipo_computo.db`
- El proyecto está optimizado para Windows, pero puede adaptarse a otras plataformas
- Los datos sensibles (credenciales) están configurados en `credentials.py` - modificar según sea necesario

## Contribuciones y Mejoras

Para sugerencias o mejoras en el proyecto, considere:
- Validación adicional de datos
- Implementación de sincronización con bases de datos remotas
- Mejora de la interfaz gráfica
- Optimización del rendimiento

## Licencia

Este proyecto fue desarrollado como Trabajo de Fin de Máster.

## Repositorio y Control de Versiones

Este proyecto está bajo control de versiones con Git. Para clonar el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
cd ProyectTI_Original
```

Es recomendable trabajar con ramas (`branches`) para desarrollo de nuevas funcionalidades:

```bash
git checkout -b feature/nueva-funcionalidad
```

## Presentación del Proyecto

Ver el documento de presentación: [PRESENTACION.md](PRESENTACION.md)

La presentación incluye:
- Descripción del problema resuelto
- Solución implementada
- Tecnologías utilizadas
- Resultados y conclusiones

## Contacto

Para más información sobre el proyecto, consulte la documentación incluida o los comentarios en el código fuente.

---

**Última actualización**: Marzo 2026
