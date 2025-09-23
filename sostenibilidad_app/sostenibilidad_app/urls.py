"""
URL configuration for sostenibilidad_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

"""
✅ Comentarios sobre los cambios:
Añadimos from django.shortcuts import render para poder mostrar el HTML.
Creamos la función index(request) que carga tu index.html.
Agregamos las rutas para /agenda/ y /diagnostico/, que usaremos más adelante.
"""

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from agenda import views as agenda_views
from diagnostico.views import bienvenida

# Vista principal
def index(request):
    return render(request, 'index.html')

urlpatterns = [
    path('', agenda_views.inicio, name='inicio'),  # Página de inicio
    path('home/', bienvenida, name='home'),
    path('admin/', admin.site.urls),
    path('agenda/', include('agenda.urls')),  # App de tareas
    path('diagnostico/', include('diagnostico.urls')),  # App de sostenibilidad
]

