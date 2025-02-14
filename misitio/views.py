from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail
import datetime


from apps.biblioteca.models import *

from misitio.forms import FormularioContactos

HTML="""
<!DOCTYPE html>
<html lang="es">
<head>
<meta http-equiv="content-type" content="text/html" charset="utf-8">
<meta name="robots" content="NONE, NOARCHIVE">
<titel> Hola mundo </titel>
<style type="text/css">
html * {padding: 0; margin: 0;}
body * {padding: 10px 20px;}
body ** {padding: 0;}
body {font:small sans-serif;}
body>div {border-bottom: 1px solid #ddd;}
h1 {font-weight:normal}
#summary {background-color: #e0ebff;}
</style>
</head>
<body>
<div id="summary">
<h1> ¡Hola mundo! </h1>
</div>  
</body>
</html>
"""

def hola(request):
    return HttpResponse(HTML)

#def fecha_actual(request):
    #ahora = datetime.datetime.now()
    #html = "<hml><body><h1> Fecha: </h1> <h3> %s </h3></body></html>" % ahora
    #return HttpResponse(html)

def horas_adelante(request : HttpResponse, offset : int) -> HttpResponse:
    try:
        offset = int(offset)
    except ValueError:
        raise Http404
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)

    assert True
    html = "<html><body><h1>En %s hora(s), seran </h1><h3>%s</h3></body></html>" % (offset, dt)
    return HttpResponse(html)

def fecha_actual(request : HttpResponse) -> HttpResponse:
    ahora = datetime.datetime.now()
    #t = get_template('fecha_actual.html')
    #html = t.render(Context({"fecha_actual": ahora}))
    #return HttpResponse(html)
    return render(request, 'fecha_actual.html', {"fecha_actual": ahora})

def horas_adelante(request : HttpResponse, horas : int) -> HttpResponse:
    try:
        horas = int(horas)
    except ValueError:
        raise Http404
    dt = datetime.datetime.now() + datetime.timedelta(hours=horas)
    return render(request, 'horas_adelante.html', {"hora_siguiente": dt, 'horas': horas})

def encabezados_http(request : HttpResponse) -> HttpResponse:
    atributos_meta = sorted(request.META.items())
    print(atributos_meta)

    return render(request, 'encabezados.html', {'atributos_meta': atributos_meta})

def formulario_buscar(request : HttpResponse) -> HttpResponse:
    return render(request, "formulario_buscar.html")

def buscar(request : HttpResponse) -> HttpResponse:
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Por favor introduce un termino de busqueda')
        elif len(q) > 20:
            errors.append('Por favor introduce un termino de busqueda menos a 20 caracteres')
        else:
            libros = Libro.objects.filter(titulo__icontains=q)
            print(libros)
            return render(request, 'resultados.html', {'libros': libros, 'query':q})
    return render(request, "formulario_buscar.html", {'errors': errors})

def contactos1(request : HttpResponse) -> HttpResponse:
    errors = []
    if request.method == 'POST':
        if not request.POST.get('asunto', ''):
            errors.append('Por favor introduce un asunto')
        if not request.POST.get('mensaje', ''):
            errors.append('Por favor introduce un mensaje')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Por favor introduce un email valido')
        if not errors:
            send_mail(
                request.POST['asunto'],
                request.POST['mensaje'],
                request.POST.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contactos/gracias/')
        return render(request, 'contactos_formulario.html', {'errors': errors,
                      'asunto': request.POST.get('asunto', ''),
                      'mensaje': request.POST.get('mensaje', ''),
                      'email': request.POST.get('email', ''),}
                      )

def contactos(request : HttpResponse) -> HttpResponse:
    if request.method == 'POST':
        form = FormularioContactos(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['asunto'],
            cd['mensaje'],
            cd.get('email', 'noreply@example.com'),
            ['siteowner@example.com'],)
            return HttpResponseRedirect('/contactos/gracias/')
    else:
        form = FormularioContactos(initial={'asunto': 'Adoro tu sitio'})
    return render(request, 'formulario-contactos.html', {'form': form})

def contactos_gracias(request : HttpResponse) -> HttpResponse:
    return render(request, 'gracias.html')