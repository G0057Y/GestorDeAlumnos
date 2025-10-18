
# Gestor de Alumnos - Proyecto Django

Este proyecto fue desarrollado como parte del curso de Python con Django en CoderHouse. La aplicación permite gestionar alumnos, docentes, asistencias y trabajos prácticos en un entorno educativo.

## 🧠 Descripción

La plataforma simula un sistema de gestión académica donde los docentes pueden registrar alumnos, cargar asistencias y trabajos prácticos, mientras que los alumnos pueden acceder a su perfil y visualizar sus datos.

## Video Explicativo:
https://youtu.be/i3xK2HoHmLc

## ⚙️ Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/G0057Y/GestorDeAlumnos.git
cd proyecto-gestor-alumnos
```

2. Crear entorno virtual y activarlo:
```bash
python -m venv env
source env/bin/activate  # En Linux/macOS
env\Scriptsctivate    # En Windows
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Migrar la base de datos:
```bash
python manage.py migrate
```

5. Crear superusuario:
```bash
python manage.py createsuperuser
```

6. Ejecutar el servidor:
```bash
python manage.py runserver
```

## 👥 Roles de usuario

- **Docente**: puede registrar alumnos, cargar asistencias y trabajos prácticos, y ver listados.
- **Alumno**: accede a su perfil, visualiza sus datos y entregas.

## 🔐 Autenticación

La aplicación incluye registro, login, logout y edición de perfil. Se utiliza `UsuarioExtendido` para diferenciar roles.

## 📋 Funcionalidades principales

- Registro y login de usuarios
- Diferenciación entre docentes y alumnos
- CRUD de alumnos (con CBV y mixins)
- Registro de asistencias y trabajos prácticos
- Listado general de asistencias (solo para docentes)
- Perfil de usuario con datos personales

## ✅ Requisitos técnicos cumplidos

- Uso de decorador `@login_required` en vistas comunes
- Uso de `LoginRequiredMixin` en CBV
- Uso de relaciones entre modelos (`Alumno`, `UsuarioExtendido`, `Asistencia`, `TrabajoPractico`)
- Formularios con validaciones
- Panel de administración habilitado

## 📝 Observaciones

- Los alumnos se vinculan automáticamente al registrarse como no docentes.
- Las asistencias se pueden visualizar desde una vista exclusiva para docentes.
- La contraseña por defecto para alumnos creados automáticamente es `1234`.
- El diseño se mantuvo simple para priorizar funcionalidad.

## 📂 Accesos útiles

- Panel de administración: `http://127.0.0.1:8000/admin/`
- Registro: `http://127.0.0.1:8000/accounts/registro/`
- Listado de asistencias: `http://127.0.0.1:8000/asistencias/`


## Estructura del código
GestorDeAlumnos/
│
├── manage.py
├── requirements.txt
├── README.md
│
├── GestorDeAlumnos/               # Configuración principal del proyecto Django
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py                    # URLs globales del proyecto
│   └── wsgi.py
│
├── AppGestor/                     # App principal: gestión de alumnos, asistencias y trabajos prácticos
│   ├── __init__.py
│   ├── admin.py                   # Registro de modelos en el panel de administración
│   ├── apps.py (opcional)
│   ├── models.py                  # Modelos: Alumno, Asistencia, TrabajoPractico
│   ├── views.py                   # Vistas FBV y CBV para CRUD y formularios
│   ├── forms.py                   # Formularios personalizados
│   ├── urls.py                    # URLs específicas de AppGestor
│   └── templates/
│       └── AppGestor/
│           ├── inicio.html
│           ├── formulario.html
│           ├── exito.html
│           ├── alumno_list.html
│           ├── alumno_form.html
│           ├── alumno_detail.html
│           ├── alumno_confirm_delete.html
│           ├── listado_asistencias.html
│           └── buscar.html
│
├── accounts/                      # App secundaria: autenticación y perfiles
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py                  # Modelo UsuarioExtendido
│   ├── views.py                   # Registro, login, perfil, edición
│   ├── forms.py                   # RegistroForm, PerfilForm
│   ├── urls.py                    # URLs específicas de accounts
│   ├── signals.py (opcional)     # Lógica para vincular UsuarioExtendido con Alumno
│   └── templates/
│       └── accounts/
│           ├── registro.html
│           ├── login.html
│           ├── perfil.html
│           └── editar_perfil.html
│
└── media/                         # Carpeta para imágenes de alumnos y avatares
    ├── alumnos/
    └── avatars/
---

Este proyecto fue desarrollado con fines educativos y puede ser extendido para incluir funcionalidades como cambio de contraseña, exportación de datos y visualización de estadísticas.

16/10/2025
El proyecto se basó en un trabajo práctico anterior del curso y para evitar reescribir algunas funcionalidades todavía hay algunos elementos que no se comportan como deberían o funcionan "raro". La vinculación entre UsuariosExtendidos y los objetos básicos de django creados a partir de forms todavía está incompleta. La entrega de trabajos prácticos
