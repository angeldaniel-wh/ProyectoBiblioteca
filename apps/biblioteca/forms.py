from django import forms

from apps.biblioteca.models import Libro, Editor, Autor


class FormularioEditor(forms.ModelForm):
    class Meta:
        model = Editor

        fields = {
            'nombre',
            'domicilio',
            'ciudad',
            'estado',
            'pais',
            'website',
        }

        labels = {
            'nombre': 'Nombre',
            'domicilio': 'Domicilio',
            'ciudad': 'Ciudad',
            'estado': 'Estado',
            'pais': 'Pais',
            'website': 'Website',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'domicilio': forms.TextInput(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'pais': forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
        }


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = {
            'nombre',
            'apellidos',
            'email',
        }

        labels = {
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'email': 'Email',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro

        fields = [
            'titulo',
            'autores',
            'editor',
            'fecha_publicacion',
            'portada',
        ]

        labels = {
            'titulo': 'Titulo',
            'autores': 'Autores',
            'editor': 'Editor',
            'fecha_publicacion': 'Fecha Publicacion',
            'portada': 'Portada',
        }

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autores': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'editor': forms.Select(attrs={'class': 'form-control'}),
            'fecha_publicacion': forms.TextInput(attrs={'class': 'form-control'}),
            'portada': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
