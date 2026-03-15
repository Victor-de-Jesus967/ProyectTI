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
├── config/                # Configuración (sin credenciales)
│   └── __init__.py
│
├── docs/                  # Documentación del proyecto
│   ├── README.md
│   ├── PRESENTACION.md
│   ├── DESPLIEGUE.md
│   ├── GITHUB.md
│   ├── CHECKLIST_TFM.md
│   ├── Requisitos.md
│   ├── Documentacion-TFM.pdf
│   └── Encabezado.pdf
│
├── assets/                # Recursos (iconos, imágenes)
│   └── icono.ico
│
├── data/                  # Datos locales (NO se suben a Git)
│   └── equipo_computo.db   # Base de datos SQLite (generada)
│
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

```bash
source .venv/bin/activate
```

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

Las credenciales se definen en `config/credentials.py`. Este archivo **no se sube al repositorio**.

```python
# config/credentials.py
USUARIO = "su_usuario"
CONTRASENA = "su_contraseña"
```

---

## 🧩 Recursos adicionales (Drive)

Se anexará un enlace a un Drive donde se otorgan permisos al correo **mouredev@gmail.com**.

El usuario con ese acceso podrá descargar:

- Base de datos
- Excel adaptado
- Ejecutable

---

## 📌 Notas importantes

- El proyecto está orientado a Windows, pero puede adaptarse a otras plataformas.
- Se recomienda hacer copias de seguridad del archivo `data/equipo_computo.db`.
- Mantener `config/credentials.py` fuera de control de versiones.

---

## 🧑‍💻 Desarrollo

- La base de datos se crea al iniciar la aplicación.
- Las dependencias principales están en `requirements.txt`.

---

**Última actualización**: Marzo 2026
