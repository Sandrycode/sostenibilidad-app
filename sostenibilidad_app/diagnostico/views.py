from django.shortcuts import render
from .forms import DiagnosticoForm
from .models import Diagnostico
from django.template.loader import get_template
from django.http import HttpResponse
# from weasyprint import HTML
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from datetime import datetime
import matplotlib.pyplot as plt
from io import BytesIO
from reportlab.lib.utils import ImageReader

from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from .forms import RegistroForm





def home(request):
    return render(request, 'diagnostico/home.html')

  #@login_required
def inicio(request):
    if request.method == 'POST':
        form = DiagnosticoForm(request.POST)
        if form.is_valid():
            diagnostico = form.save()
            return render(request, 'diagnostico/resultados.html', {
                'diagnostico': diagnostico,
                'puntaje14001': diagnostico.puntaje_iso_14001(),
                'puntaje26000': diagnostico.puntaje_iso_26000(),
                'dictamen': diagnostico.dictamen_tecnico()
            })
        else:
            print("❌ Formulario inválido:")
            print(form.errors)
    else:
        form = DiagnosticoForm()
    return render(request, 'diagnostico/inicio.html', {'form': form})

def bienvenida(request):
    return render(request, 'agenda/inicio.html', {'ocultar_menu': True})


def exportar_pdf(request, diagnostico_id):
    diagnostico = Diagnostico.objects.get(id=diagnostico_id)
    dictamen = diagnostico.dictamen_tecnico()

    template = get_template('agenda/resultados_pdf.html')
    html_string = template.render({
        'diagnostico': diagnostico,
        'dictamen': dictamen
    })

    pdf_file = HTML(string=html_string).write_pdf()

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'filename="informe_{diagnostico.nombre_empresa}.pdf"'
    return response


def exportar_pdf_simple(request, diagnostico_id):
    diagnostico = Diagnostico.objects.get(id=diagnostico_id)
    dictamen = diagnostico.dictamen_tecnico()

    # Crear gráfico de barras
    fig, ax = plt.subplots()
    ax.bar(['ISO 14001', 'ISO 26000'],
           [dictamen['ISO_14001']['puntaje'], dictamen['ISO_26000']['puntaje']],
           color=['#00bfa5', '#00796b'])
    ax.set_ylim(0, 7)
    ax.set_ylabel('Puntaje')
    ax.set_title('Comparativa de cumplimiento')
    plt.tight_layout()

    # Guardar imagen en memoria
    img_buffer = BytesIO()
    plt.savefig(img_buffer, format='PNG')
    plt.close(fig)
    img_buffer.seek(0)

    # Crear PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="informe_{diagnostico.nombre_empresa}.pdf"'

    p = canvas.Canvas(response, pagesize=A4)
    width, height = A4
    margen_izquierdo = 2.5 * cm
    margen_derecho = width - 2.5 * cm
    margen_superior = height - 3 * cm
    margen_inferior = 2 * cm
    y = height - 3 * cm

    # Encabezado
    p.setFont("Helvetica-Bold", 18)
    p.drawString(2 * cm, y, "📋 Informe Técnico de Sostenibilidad")
    y -= 0.8 * cm

    p.setFont("Helvetica", 10)
    fecha_emision = datetime.now().strftime("%d/%m/%Y")
    p.drawString(2 * cm, y, f"Fecha de emisión: {fecha_emision}")
    y -= 0.5 * cm

    p.setStrokeColorRGB(0, 0.8, 0.6)
    p.setLineWidth(1)
    p.line(2 * cm, y, width - 2 * cm, y)
    y -= 1 * cm

    # Datos generales
    p.setFont("Helvetica", 12)
    p.drawString(2 * cm, y, f"Empresa: {diagnostico.nombre_empresa}")
    y -= 0.5 * cm
    p.drawString(2 * cm, y, f"Sector: {diagnostico.sector}")
    y -= 0.5 * cm


    # Insertar gráfico
    p.drawImage(ImageReader(img_buffer), x=2 * cm, y=y - 8 * cm, width=10 * cm, height=6 * cm)
    y -= 9 * cm  # Ajustar espacio después del gráfico

    # Dictamen técnico
    for norma, datos in dictamen.items():
        p.setFont("Helvetica-Bold", 14)
        p.drawString(2 * cm, y, f"{norma}")
        y -= 0.5 * cm

        p.setFont("Helvetica", 12)
        p.drawString(2.5 * cm, y, f"Puntaje: {datos['puntaje']}")
        y -= 0.6 * cm
        p.drawString(2.5 * cm, y, f"Nivel: {datos['nivel']}")
        y -= 0.35 * cm

        y -= 0.3 * cm

        for linea in datos['recomendacion'].split('. '):
            p.drawString(2.5 * cm, y, f"- {linea.strip()}.")
            y -= 0.55 * cm

        y -= 0.5 * cm

    # Observaciones
    if diagnostico.observaciones:
        p.setFont("Helvetica-Bold", 14)
        p.drawString(2 * cm, y, "📝 Observaciones adicionales:")
        y -= 0.7 * cm
        p.setFont("Helvetica", 12)
        for linea in diagnostico.observaciones.split('. '):
            p.drawString(2.5 * cm, y, f"- {linea.strip()}.")
            y -= 0.35 * cm

    # Pie de página
    p.setFont("Helvetica-Oblique", 9)
    p.setFillColorRGB(0.4, 0.4, 0.4)
    p.drawString(2 * cm, 1.5 * cm, f"Informe generado por Diagnóstico Sostenible · {fecha_emision}")
    p.drawRightString(width - 2 * cm, 1.5 * cm, f"Página 1")

    p.showPage()
    p.save()
    return response



def registro_empresa(request):
    next_url = request.GET.get('next', '/diagnostico/formulario/')  # ← valor por defecto

    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            messages.success(request, "Registro completado correctamente.")
            return redirect(next_url)
    else:
        form = RegistroForm()

    return render(request, 'diagnostico/registro.html', {'form': form})





@login_required
def formulario_sostenibilidad(request):
    if request.method == 'POST':
        form = DiagnosticoForm(request.POST)
        if form.is_valid():
            diagnostico = form.save()
            return render(request, 'diagnostico/resultados.html', {
                'diagnostico': diagnostico,
                'puntaje14001': diagnostico.puntaje_iso_14001(),
                'puntaje26000': diagnostico.puntaje_iso_26000(),
                'dictamen': diagnostico.dictamen_tecnico()
            })
        else:
            print("❌ Formulario inválido:")
            print(form.errors)
    else:
        form = DiagnosticoForm()
    return render(request, 'diagnostico/inicio.html', {'form': form})





