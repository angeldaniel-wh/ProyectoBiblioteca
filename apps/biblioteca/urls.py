from django.conf.urls import url
from django.views.generic import detail
from django.conf import settings
from django.conf.urls.static import static


from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),

    #URLs para list
    url(r'^autor/function/list$', autor_list, name='function_autor_listar'),
    url(r'^autor/class/list$', AutorView.as_view(), name='class_autor_listar'),

    url(r'^editor/function/list$', editor_list, name='function_editor_listar'),
    url(r'^editor/class/list$', EditorView.as_view(), name='class_editor_listar'),

    url(r'^libro/function/list$', libro_list, name='function_libro_listar'),
    url(r'^libro/class/list$', LibroView.as_view(), name='class_libro_listar'),

    #URLs para nuevo
    url(r'^autor/function/nuevo$', autor_create, name='function_autor_crear'),
    url(r'^autor/class/nuevo$', AutorCreateView.as_view(), name='class_autor_crear'),

    url(r'^editor/function/nuevo$', editor_create, name='function_editor_crear'),
    url(r'^editor/class/nuevo$', EditorCreateView.as_view(), name='class_editor_crear'),

    url(r'^libro/function/nuevo$', libro_create, name='function_libro_crear'),
    url(r'^libro/class/nuevo$', LibroCreateView.as_view(), name='class_libro_crear'),

    #URLs para editar
    url(r'^autor/function/editar/(?P<id_autor>\d+)/', autor_edit, name='function_autor_editar'),
    url(r'^autor/class/editar/(?P<pk>\d+)/', AutorUpdateView.as_view(), name='class_autor_editar'),

    url(r'^editor/function/editar/(?P<id_autor>\d+)/', editor_edit, name='function_editor_editar'),
    url(r'^editor/class/editar/(?P<pk>\d+)/', EditorUpdateView.as_view(), name='class_editor_editar'),

    url(r'^libro/function/editar/(?P<id_autor>\d+)/', libro_edit, name='function_libro_editar'),
    url(r'^libro/class/editar/(?P<pk>\d+)/', LibroUpdateView.as_view(), name='class_libro_editar'),

    #URLs para eliminar
    url(r'^autor/function/eliminar/(?P<id_autor>\d+)/', autor_delete, name='function_autor_eliminar'),
    url(r'^autor/class/eliminar/(?P<pk>\d+)/', AutorDeleteView.as_view(), name='class_autor_eliminar'),

    url(r'^editor/function/eliminar/(?P<id_autor>\d+)/', editor_delete, name='function_editor_eliminar'),
    url(r'^editor/class/eliminar/(?P<pk>\d+)/', EditorDeleteView.as_view(), name='class_editor_eliminar'),

    url(r'^libro/function/eliminar/(?P<id_autor>\d+)/', libro_delete, name='function_libro_eliminar'),
    url(r'^libro/class/eliminar/(?P<pk>\d+)/', LibroDeleteView.as_view(), name='class_libro_eliminar'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)