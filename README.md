# 🌱 Sostenibilidad App

¡Hola! Soy Sandra, y te doy la bienvenida a mi perfil de GitHub. Aquí comparto soluciones web pensadas para ofrecer experiencias funcionales, estéticas y con propósito.

Hoy te presento **Sostenibilidad App**, una aplicación web desarrollada con Django que integra dos módulos complementarios:

- **Agenda de Tareas**: una herramienta práctica para añadir, editar y eliminar tareas personales, pensada para fomentar la organización y el seguimiento de hábitos sostenibles.
- **Diagnóstico de Sostenibilidad**: un sistema interactivo que permite a los usuarios evaluar sus prácticas cotidianas, recibir recomendaciones personalizadas y generar informes en PDF.

Este proyecto combina diseño limpio, navegación intuitiva y funcionalidades robustas para brindar valor real tanto a usuarios como a empresas comprometidas con la sostenibilidad. Cada módulo está diseñado para promover la conciencia ambiental, la acción responsable y la gestión eficiente de la información.

---

## 👤 Funcionalidades del proyecto

🗓️ **Agenda de Tareas**  
- Registro e inicio de sesión seguro.
- Añadir nuevas tareas personales.
- Editar tareas existentes.
- Eliminar tareas completadas o innecesarias.  

🌿 **Diagnóstico de Sostenibilidad**  
- Registro e inicio de sesión seguro.
- Evaluación personalizada de prácticas sostenibles para empresas mediante un cuestionario estructurado.
- Visualización de resultados y recomendaciones.
- Generación de informes en PDF.

---

## 🧩 Tecnologías utilizadas

- **Python 3.12**
- **Django 5.2**
- **HTML5, CSS3**
- **SQLite (desarrollo) / PostgreSQL (producción)**
- **Gunicorn** (servidor de producción)
- **WhiteNoise** (gestión de archivos estáticos)
- **dj-database-url** (configuración dinámica de base de datos)
- **Pillow** (manejo de imágenes)
- **psycopg2-binary** (conector PostgreSQL)
- **Render** (despliegue en la nube)

---

## 📁 Estructura del proyecto

- `sostenibilidad_app/` → Lógica principal de la aplicación  
- `templates/` → Vistas HTML organizadas por módulo  
- `static/` y `staticfiles/` → Archivos estáticos como CSS e imágenes  
- `requirements.txt` → Dependencias del proyecto  
- `Procfile` → Configuración para despliegue en Render  
- `.gitignore` → Exclusión de archivos sensibles  

---

## 🚀 Despliegue en Render

Este proyecto está preparado para producción con configuración optimizada para Render, incluyendo:

- Servidor Gunicorn  
- Archivos estáticos servidos con WhiteNoise  
- Base de datos PostgreSQL gestionada por `dj-database-url`  

---

## 🖥️ Demo del Proyecto

⚠️ Este proyecto está en fase de despliegue. Pronto estará disponible la demo funcional.

---

🪄 Este proyecto ha sido construido con enfoque meticuloso, integrando una arquitectura backend eficiente y una interfaz intuitiva que facilita la navegación. Cada módulo está diseñado para impulsar la sostenibilidad desde la funcionalidad, la claridad y el propósito.
