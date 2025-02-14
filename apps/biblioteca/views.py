from urllib import request

from django.contrib import messages
from urllib.request import Request

from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest

# Create your views here.


from apps.biblioteca.forms import AutorForm, LibroForm, FormularioEditor
from apps.biblioteca.models import Autor, Libro, Editor

##############################################################################
#############              Vistas Autor                 ######################
##############################################################################
# Vista index
def index(request : HttpRequest) -> HttpResponse:
    return render(request, 'biblioteca/index.html')

# Listado de autores ordenados por id
def autor_list(request: HttpRequest) -> HttpResponse:
    autores = Autor.objects.all().order_by('id')
    contexto = {'autores': autores}
    return render(request, 'biblioteca/autor/autor_list.html', contexto)

# VIsta para crear un autor usando el formulario
def autor_create(request : HttpRequest) -> HttpResponse:
    if request.method == "POST":
         form = AutorForm(request.POST)
         if form.is_valid():
            form.save()
            messages.success(request, 'Autor registrado correctamente')
            return redirect('biblioteca:function_autor_listar')
         else:
             messages.error(request, 'Ocurrio un error al guardar el autor')
    else:
        form = AutorForm()
        print(form)
    return render(request, "biblioteca/autor/autor_form.html", {'form': form})

#Vista para editar la informacion existente de un autor
def autor_edit(request: HttpRequest, id_autor: int) -> HttpResponse:
    autor = Autor.objects.get(id=id_autor)
    if request.method == "GET":
        form = AutorForm(instance=autor)
        print(form)
    else:
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Autor registrado correctamente')
            return redirect('biblioteca:function_autor_listar')
        else:
            messages.error(request, 'Ocurrio un error al guardar el autor')
    return render(request, 'biblioteca/autor/autor_form.html', {'form': form})

def autor_delete(request: HttpRequest, id_autor: int) -> HttpResponse:
    autor = Autor.objects.get(id=id_autor)
    if request.method == "POST":
        autor.delete()
        messages.success(request, 'Autor eliminado correctamente')
        return redirect('biblioteca:function_autor_listar')
    return render(request, 'biblioteca/autor/autor_delete.html', {'autor': autor})

class AutorView(ListView):
    model = Autor
    template_name = 'biblioteca/autor/autor_list.html'

class AutorCreateView(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'biblioteca/autor/autor_form.html'
    success_url = reverse_lazy('biblioteca:class_autor_listar')

    def form_valid(self, form):
        messages.success(self.request, 'Autor registrado exitosamente!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Ocurrio un error al registrar el Autor')
        return super().form_invalid(form)


class AutorUpdateView(UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'biblioteca/autor/autor_form.html'
    success_url = reverse_lazy('biblioteca:class_autor_listar')

    def form_valid(self, form):
        messages.success(self.request, 'Autor actualizado exitosamente!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Ocurrio un error al actualizar el Autor')
        return super().form_invalid(form)


class AutorDeleteView(DeleteView):
    model = Autor
    template_name = 'biblioteca/autor/autor_delete.html'
    success_url = reverse_lazy('biblioteca:class_autor_listar')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Solicitud eliminada correctamente')
        return super(AutorDeleteView, self).delete(request, *args, **kwargs)


##############################################################################
#############              Vistas Editor                ######################
##############################################################################

def editor_list(request : HttpRequest) -> HttpResponse:
    editores = Editor.objects.all().order_by('id')
    contexto = {'editores': editores}
    return render(request, 'biblioteca/editor/editor_list.html', contexto)

def editor_create(request : HttpRequest) -> HttpResponse:
    if request.method == "POST":
         form = FormularioEditor(request.POST)
         if form.is_valid():
            form.save()
            messages.success(request, 'Editor registrado correctamente')
            return redirect('biblioteca:function_editor_listar')
         else:
             messages.error(request, 'Ocurrio un error al guardar el editor')
    else:
        form = FormularioEditor()
        print(form)
    return render(request, "biblioteca/editor/editor_form.html", {'form': form})

def editor_edit(request: HttpRequest, id_editor: int) -> HttpResponse:
    editor = Editor.objects.get(id=id_editor)
    if request.method == "GET":
        form = AutorForm(instance=editor)
    else:
        form = AutorForm(request.POST, instance=editor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Editor actualizado correctamente')
            return redirect('biblioteca:function_autor_listar')
        else:
            messages.error(request, 'Ocurrio un error al actualizar el editor')
    return render(request, 'biblioteca/editor/editor_form.html', {'form': form})

def editor_delete(request: HttpRequest, id_editor: int) -> HttpResponse:
    editor = Editor.objects.get(id=id_editor)
    if request.method == "POST":
        editor.delete()
        messages.success(request, 'Editor eliminado correctamente')
        return redirect('biblioteca:function_editor_listar')
    return render(request, 'biblioteca/editor/libro_delete.html', {'editor': editor})

class EditorView(ListView):
    model = Editor
    template_name = 'biblioteca/editor/editor_list.html'

class EditorCreateView(CreateView):
    model = Editor
    form_class = FormularioEditor
    template_name = 'biblioteca/editor/editor_form.html'
    success_url = reverse_lazy('biblioteca:class_editor_listar')

    def form_valid(self, form):
        messages.success(self.request, 'Autor creado exitosamente!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Ocurrio un error al crear el Editor')
        return super().form_invalid(form)


class EditorUpdateView(UpdateView):
    model = Editor
    form_class = FormularioEditor
    template_name = 'biblioteca/editor/editor_form.html'
    success_url = reverse_lazy('biblioteca:class_editor_listar')

    def form_valid(self, form):
        messages.success(self.request, 'Editor actualizado exitosamente!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Ocurrio un error al actualizar el Editor')
        return super().form_invalid(form)


class EditorDeleteView(DeleteView):
    model = Editor
    template_name = 'biblioteca/editor/editor_delete.html'
    success_url = reverse_lazy('biblioteca:class_editor_listar')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Solicitud eliminada correctamente')
        return super(EditorDeleteView, self).delete(request, *args, **kwargs)

##############################################################################
#############              Vistas Libro                 ######################
##############################################################################

def libro_list(request : HttpRequest) -> HttpResponse:
    libros = Libro.objects.all().order_by('id')
    contexto = {'libros': libros}
    for libro in libros:
        print(libro.autores)
    return render(request, 'biblioteca/libro/libro_list.html', contexto)

def libro_create(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
         form = LibroForm(request.POST, request.FILES)
         if form.is_valid():
            form.save()
            messages.success(request, 'Libro creado exitosamente!')
            return redirect('biblioteca:function_libro_listar')
         else:
             messages.error(request, 'OCurrió un error al crear el libro')
    else:
        form = LibroForm()
    return render(request, "biblioteca/libro/libro_form.html", {'form': form})

def libro_edit(request: HttpRequest, id_libro: int) -> HttpResponse:
    libro = Libro.objects.get(id=id_libro)
    if request.method == "GET":
        form = Libro(instance=libro)
        print(form)
    else:
        form = LibroForm(request.POST, request.FILES, instance=libro)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro actualizado exitosamente!')
            return redirect('biblioteca:function_libro_listar')
        else:
            messages.error(request, 'OCurrió un error al actualizar el libro')
    return render(request, 'biblioteca/libro/libro_form.html', {'form': form})

def libro_delete(request: HttpRequest, id_libro: int) -> HttpResponse:
    libro = Libro.objects.get(id=id_libro)
    if request.method == "POST":
        libro.delete()
        messages.success(request, 'Libro eliminado exitosamente!')
        return redirect('biblioteca:function_libro_listar')
    return render(request, 'biblioteca/libro/libro_delete.html', {'libro': libro})

class LibroView(ListView):
    model = Libro
    template_name = 'biblioteca/libro/libro_list.html'

class LibroCreateView(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'biblioteca/libro/libro_form.html'
    success_url = reverse_lazy('biblioteca:class_libro_listar')

    def form_valid(self, form):
        messages.success(self.request, 'Libro creado exitosamente!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Ocurrio un error al crear el libro')
        return super().form_invalid(form)

class LibroUpdateView(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'biblioteca/libro/libro_form.html'
    success_url = reverse_lazy('biblioteca:class_libro_listar')

    def form_valid(self, form):
        messages.success(self.request, 'Libro actualizado exitosamente!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Ocurrio un error al actualizar el libro')
        return super().form_invalid(form)


class LibroDeleteView(DeleteView):
    model = Libro
    template_name = 'biblioteca/libro/libro_delete.html'
    success_url = reverse_lazy('biblioteca:class_libro_listar')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Libro eliminado exitosamente!')
        return super(LibroDeleteView, self).delete(request, *args, **kwargs)

