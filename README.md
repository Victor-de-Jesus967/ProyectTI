# ProyectTI

Sistema de gestión de equipos de cómputo (desktop) desarrollado en **Python + PyQt5**.

---

## 📁 Estructura del proyecto (solo archivos permitidos en el repositorio)

```
ProyectTI/
├── src/                   # Código fuente
│   ├── __init__.py
│   ├── Main.py            # Punto de entrada
│   ├── Login.py
│   ├── Interfaz.py
│   ├── Acciones.py
│   ├── Db_manager.py
│   └── ActualizarBD.py
│
├── config/                
│   ├── credentials.py    # Credenciales
│   └── __init__.py
│
├── docs/                  # Documentación del proyecto
│   ├── DESPLIEGUE.md
│   └── Encabezado.pdf
│
├── assets/                # Recursos (iconos, imágenes)
│   └── icono.ico
│
├── data/                  # Datos locales (NO se suben a Git)
│   └── equipo_computo.db   # Base de datos SQLite (generada)
│
├── Diapositivas.pdf       # Presentacion del proyecto
├── Mnaul de usuario 2026  # Manual
├── main.py                # Script wrapper para ejecutar la app
├── requirements.txt       # Dependencias del proyecto
└── .gitignore             # Archivos ignorados por Git
```

> **Nota**: `data/equipo_computo.db` es generada automáticamente al ejecutar la aplicación y **no se incluye en el repositorio**.

---

## 🚀 Instalación rápida

1. Clonar el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
cd ProyectTI
```

2. Crear y activar entorno virtual (recomendado):

```bash
python -m venv .venv
```

- Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

- macOS/Linux:

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

4. Ejecutar la aplicación:

```bash
python main.py
```

---

## 🔐 Configuración de credenciales

Las credenciales se definen en `config/credentials.py`. Este archivo 

```python
# config/credentials.py
USUARIO = "su_usuario"
CONTRASENA = "su_contraseña"
```

---

## 🧩 Recursos adicionales (Drive)

Enlace: https://drive.google.com/drive/folders/1Lltc0UDTylEcJ2NjM123moIP_YFxPsjN?usp=sharing

Contenido:
- Base de datos
- Excel adaptado
- Ejecutable

---

## 📌 Notas importantes para BRAIS

- El proyecto está orientado a Windows, pero puede adaptarse a otras plataformas.
- Las credenciales se encuentran en :`config/credentials.py`
- La base de datos se encuentra en el enlace proprocionado en Drive 
- Excel adaptado este archivo es para cargar la base de datos, se adapto para carga masicva de informacion al proyecto
- Brais para que la base datos se muestre en pantalla debes de moverla a la carpeta `data` y una vez cargada presiona el boton atras y se mostrara
- O tambien puedes cargar el excel y el programa creara la base de datos para su correcto funcionamiento
---

## 🧑‍💻 Desarrollo

- La base de datos se crea al iniciar la aplicación.
- Las dependencias principales están en `requirements.txt`.

---

**Última actualización**: Marzo 2026 

Un abrazo Brais creci y aprendi mucho con esta maestria, me abriste un mundo de posibilidades para futuros proyectos. 
