from django.urls import path
from . import views
from .views import exportar_pdf
from .views import exportar_pdf_simple
from django.contrib.auth import views as auth_views
from . import views
from diagnostico.views import home



urlpatterns = [
    # path('', views.inicio, name='diagnostico_inicio'),
    # Vista de bienvenida (pantalla con los dos botones)
path('', views.bienvenida, name='diagnostico_inicio'),

    path('diagnostico/<int:diagnostico_id>/pdf/', exportar_pdf, name='exportar_pdf'),
    path('diagnostico/<int:diagnostico_id>/pdf_simple/', exportar_pdf_simple, name='exportar_pdf_simple'),
    path('login/', auth_views.LoginView.as_view(template_name='diagnostico/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/', views.registro_empresa, name='registro'),
    # Vista del formulario de sostenibilidad (protegida)
    path('formulario/', views.formulario_sostenibilidad, name='formulario'),
]


